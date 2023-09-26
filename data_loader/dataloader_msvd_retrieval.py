from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function

import os
from base.base_dataset import TextVideoDataset
import numpy as np
import pickle
from .rawvideo_util import RawVideoExtractor

class MSVD_DataLoader(TextVideoDataset):
    def _load_metadata(self):
        metadata_dir = 'data/msvd/meta_data'

        split_files = {
            'train': 'train_list.txt',
            # 'val': 'MSVD_val.tsv',            # there is no test
            'val': 'val_list.txt',  # direct output test result
            # 'val': 'MSVD_split_test.tsv',
            # 'test': 'MSVD_split_test.tsv'
            'test': 'test_list.txt'
        }
        target_split_fp = split_files[self.split]
        metadata = pd.read_csv(os.path.join(metadata_dir, target_split_fp), sep='\t')
        if self.subsample < 1:
            metadata = metadata.sample(frac=self.subsample)
        self.metadata = metadata
    video_id_path_dict = {}
    video_id_path_dict["train"] = os.path.join(self.data_path, "train_list.txt")
    video_id_path_dict["val"] = os.path.join(self.data_path, "val_list.txt")
    video_id_path_dict["test"] = os.path.join(self.data_path, "test_list.txt")
    caption_file = os.path.join(self.data_path, "raw-captions.pkl")

    with open(video_id_path_dict[self.subset], 'r') as fp:
        video_ids = [itm.strip() for itm in fp.readlines()]

    with open(caption_file, 'rb') as f:
        captions = pickle.load(f)

    video_dict = {}
    for root, dub_dir, video_files in os.walk(self.features_path):
        for video_file in video_files:
            video_id_ = ".".join(video_file.split(".")[:-1])
            if video_id_ not in video_ids:
                continue
            file_path_ = os.path.join(root, video_file)
            video_dict[video_id_] = file_path_
    self.video_dict = video_dict

    self.sample_len = 0
    self.sentences_dict = {}
    self.cut_off_points = []
    for video_id in video_ids:
        assert video_id in captions
        for cap in captions[video_id]:
            cap_txt = " ".join(cap)
            self.sentences_dict[len(self.sentences_dict)] = (video_id, cap_txt)
        self.cut_off_points.append(len(self.sentences_dict))

    ## below variables are used to multi-sentences retrieval
    # self.cut_off_points: used to tag the label when calculate the metric
    # self.sentence_num: used to cut the sentence representation
    # self.video_num: used to cut the video representation
    self.multi_sentence_per_video = True    # !!! important tag for eval
    if self.subset == "val" or self.subset == "test":
        self.sentence_num = len(self.sentences_dict)
        self.video_num = len(video_ids)
        assert len(self.cut_off_points) == self.video_num
        print("For {}, sentence number: {}".format(self.subset, self.sentence_num))
        print("For {}, video number: {}".format(self.subset, self.video_num))

    print("Video number: {}".format(len(self.video_dict)))
    print("Total Paire: {}".format(len(self.sentences_dict)))

    self.sample_len = len(self.sentences_dict)
    self.rawVideoExtractor = RawVideoExtractor(framerate=feature_framerate, size=image_resolution)
    self.SPECIAL_TOKEN = {"CLS_TOKEN": "<|startoftext|>", "SEP_TOKEN": "<|endoftext|>",
                          "MASK_TOKEN": "[MASK]", "UNK_TOKEN": "[UNK]", "PAD_TOKEN": "[PAD]"}

    def __len__(self):
        return self.sample_len

    def _get_text(self, video_id, caption):
        k = 1
        choice_video_ids = [video_id]
        pairs_text = np.zeros((k, self.max_words), dtype=np.long)
        pairs_mask = np.zeros((k, self.max_words), dtype=np.long)
        pairs_segment = np.zeros((k, self.max_words), dtype=np.long)

        for i, video_id in enumerate(choice_video_ids):
            words = self.tokenizer.tokenize(caption)

            words = [self.SPECIAL_TOKEN["CLS_TOKEN"]] + words
            total_length_with_CLS = self.max_words - 1
            if len(words) > total_length_with_CLS:
                words = words[:total_length_with_CLS]
            words = words + [self.SPECIAL_TOKEN["SEP_TOKEN"]]

            input_ids = self.tokenizer.convert_tokens_to_ids(words)
            input_mask = [1] * len(input_ids)
            segment_ids = [0] * len(input_ids)
            while len(input_ids) < self.max_words:
                input_ids.append(0)
                input_mask.append(0)
                segment_ids.append(0)
            assert len(input_ids) == self.max_words
            assert len(input_mask) == self.max_words
            assert len(segment_ids) == self.max_words

            pairs_text[i] = np.array(input_ids)
            pairs_mask[i] = np.array(input_mask)
            pairs_segment[i] = np.array(segment_ids)

        return pairs_text, pairs_mask, pairs_segment, choice_video_ids

    def _get_rawvideo(self, choice_video_ids):
        video_mask = np.zeros((len(choice_video_ids), self.max_frames), dtype=np.long)
        max_video_length = [0] * len(choice_video_ids)

        # Pair x L x T x 3 x H x W
        video = np.zeros((len(choice_video_ids), self.max_frames, 1, 3,
                          self.rawVideoExtractor.size, self.rawVideoExtractor.size), dtype=np.float)

        for i, video_id in enumerate(choice_video_ids):
            video_path = self.video_dict[video_id]

            raw_video_data = self.rawVideoExtractor.get_video_data(video_path)
            raw_video_data = raw_video_data['video']

            if len(raw_video_data.shape) > 3:
                raw_video_data_clip = raw_video_data
                # L x T x 3 x H x W
                raw_video_slice = self.rawVideoExtractor.process_raw_data(raw_video_data_clip)
                if self.max_frames < raw_video_slice.shape[0]:
                    if self.slice_framepos == 0:
                        video_slice = raw_video_slice[:self.max_frames, ...]
                    elif self.slice_framepos == 1:
                        video_slice = raw_video_slice[-self.max_frames:, ...]
                    else:
                        sample_indx = np.linspace(0, raw_video_slice.shape[0] - 1, num=self.max_frames, dtype=int)
                        video_slice = raw_video_slice[sample_indx, ...]
                else:
                    video_slice = raw_video_slice

                video_slice = self.rawVideoExtractor.process_frame_order(video_slice, frame_order=self.frame_order)

                slice_len = video_slice.shape[0]
                max_video_length[i] = max_video_length[i] if max_video_length[i] > slice_len else slice_len
                if slice_len < 1:
                    pass
                else:
                    video[i][:slice_len, ...] = video_slice
            else:
                print("video path: {} error. video id: {}".format(video_path, video_id))

        for i, v_length in enumerate(max_video_length):
            video_mask[i][:v_length] = [1] * v_length

        return video, video_mask

    def __getitem__(self, idx):
        video_id, caption = self.sentences_dict[idx]

        pairs_text, pairs_mask, pairs_segment, choice_video_ids = self._get_text(video_id, caption)
        video, video_mask = self._get_rawvideo(choice_video_ids)
        return pairs_text, pairs_mask, pairs_segment, video, video_mask
