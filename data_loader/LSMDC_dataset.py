import random

from base.base_dataset import TextVideoDataset
import pandas as pd
import os
import pickle
import nltk
import csv

class LSMDC(TextVideoDataset):
    # def __init__(self):
    #     self.
    def _load_metadata(self):
        metadata_dir = self.metadata_dir + 'meta_data'
        split_files = {
            'train': 'LSMDC16_annos_training.csv',
            # 'val': 'MSVD_val.tsv',            # there is no test
            'val': 'LSMDC16_annos_val.csv',  # direct output test result
            # 'val': 'MSVD_split_test.tsv',
            # 'test': 'MSVD_split_test.tsv'
            'test': 'LSMDC16_challenge_1000_publictect.csv'
        }
        target_split_fp = split_files[self.split]
        # metadata = pd.read_csv(os.path.join(metadata_dir, target_split_fp), sep='\t')
        data = []
        with open("/home/storage2/chenlei/frozen-in-time-main/didemo/structured-symlinks/" + target_split_fp, 'r',
                  encoding='utf-8') as f:
            f_csv = csv.reader(f,  quoting=csv.QUOTE_NONE)
            # head = f_csv.next()
            # count = 1
            for row in f_csv:
                a = "".join(row)
                b = a.split('\t')
                # video_name = b[0]
                discript = b[0]
                data.append(discript)
        f.close()
        metadata = pd.core.frame.DataFrame(data)
        if self.subsample < 1:
            metadata = metadata.sample(frac=self.subsample)
        self.metadata = metadata
        print("load split {}, {} samples".format(self.split, len(metadata)))
    

    def _get_video_path(self, sample):
        rel_video_fp = sample[0] + '.avi'
        #rel_video_fp = os.path.join(sample['page_dir'], str(sample['videoid']) + '.mp4')
        full_video_fp = os.path.join(self.data_dir, rel_video_fp)
        # print(full_video_fp)
        return full_video_fp, rel_video_fp

        # multiple sentence
    def _get_caption(self, sample):
        # print(sample[0].split(',')[0])
        f = open('/home/storage2/chenlei/mine/captions.pkl', 'rb')
        data = pickle.load(f)
        f.close()
        # data = pickle.load(f)
        # f.close()
        # if self.split == 'train':
        vid = sample[0]
        words = data[vid]
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
        return words

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
