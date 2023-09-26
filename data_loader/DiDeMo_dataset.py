from base.base_dataset import TextVideoDataset
import pandas as pd
import os
import pickle
import random

class DiDeMo(TextVideoDataset):
    def _load_metadata(self):
        metadata_dir = self.metadata_dir + 'meta_data'
        split_files = {
            'train': 'train_list.txt',
            'val': 'train_list.txt',            # there is no test
            'test': 'train_list.txt'
        }
        target_split_fp = split_files[self.split]
        metadata = pd.read_csv(os.path.join(metadata_dir, target_split_fp), sep='\t')
        if self.subsample < 1:
            metadata = metadata.sample(frac=self.subsample)
        self.metadata = metadata
        print("load split {}, {} samples".format(self.split, len(metadata)))

    def _get_video_path(self, sample):
        rel_video_fp = sample[0]
        #rel_video_fp = os.path.join(sample['page_dir'], str(sample['videoid']) + '.mp4')
        full_video_fp = os.path.join(self.data_dir, rel_video_fp)
        # print(full_video_fp)
        return full_video_fp, rel_video_fp

    def _get_caption(self, sample):

        f = open('/data/didemo/meta_data/raw-captions.pkl',
                 'rb')
        data = pickle.load(f)
        f.close()
        # if self.split == 'train':
        vid = sample[0]
        words = data[vid]

        # caption = []
        # for i in range(len(words)):
        #     caption += words[i]
        # caption = [i for i in caption if i not in ['a', 'an', 'the', 'is']]
        num_word = len(words)
        index = random.randint(0, num_word - 1)
        caption = words[index]

        # print(sample[0].split(',')[0])
        # return sample[0].split(',')[0]
        # return sample[0] # .split(',')[0]
        return ' '.join(caption)

    def _get_object_path(self, sample, index=0):
        """
        get the object npy path
        Args:
            sample (dict):
        Returns:
            abs path
        """
        rel_object_fp = os.path.join(sample[1], '1.npz')
        full_object_fp = os.path.join(self.object_dir, self.split, rel_object_fp)
        return os.path.join(self.split, rel_object_fp), full_object_fp