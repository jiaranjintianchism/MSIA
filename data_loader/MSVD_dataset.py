import random

from base.base_dataset import TextVideoDataset
import pandas as pd
import os
import pickle
import nltk

class MSVD(TextVideoDataset):
    def _load_metadata(self):
        metadata_dir = self.metadata_dir + 'meta_data'
        split_files = {
            'train': 'visual.txt',
            # 'val': 'MSVD_val.tsv',            # there is no test
            'val': 'visual.txt',  # direct output test result
            # 'val': 'MSVD_split_test.tsv',
            # 'test': 'MSVD_split_test.tsv'
            'test': 'visual.txt'
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

        # multiple sentence
    def _get_caption(self, sample):
        # print(sample[0].split(',')[0])
        # f = open('/home/storage2/chenlei/mine/data/msvd/meta_data/raw-captions.pkl', 'rb')
        # data = pickle.load(f)
        # f.close()
        # text = 'f9_bP219ehQ_63_70'
        # words = data[text]
        caption = 'to make a salmon sushi first pour fresh cold water into a bowl, add kosher salt and sugar to water and dissolve, then cut salmon on both sides of center tissue and cut meat off of skin, ' \
                  'finally cut salmon into thin slices, brine slices for 3 minutes and remove and pat the slices dry and put on a plate in fridge'

        # caption = 'How to Make Salmon Sushi in 3 Minutes'

        # if self.split == 'train':
        # vid = sample[0]
        # words = data[vid]
        # caption = []
        # for i in range(len(words)):
        #     caption += words[i]
        # caption = [i for i in caption if i not in ['a', 'an', 'the', 'is']]
        # num_word = len(words)
        # index = random.randint(0, num_word - 1)
        # caption = words[index]

        # caption = None
        # if self.split == 'train':
        #     indexs = sorted(random.sample(range(0, num_word-1), 5))
        #     caption = ' '.join(words[item] for item in indexs)
        # else:
        #     caption = ' '.join(words[item] for item in range(0, 5))
        return caption

    def _get_object_path(self, sample, index=1):
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