#### original_fream_8:
    [t2v_metrics] epoch 0, R@1: 26.7, R@5: 55.3, R@10 67.1, R@50 88.3MedR: 4, MeanR: 26.5
    [v2t_metrics] epoch 0, R@1: 27.2, R@5: 54.7, R@10 68.2, R@50 90.0MedR: 4, MeanR: 22.9

#### dual_fream_8:
    [t2v_metrics] epoch 0, R@1: 27.3, R@5: 55.4, R@10 67.8, R@50 89.3MedR: 4, MeanR: 26.0
    [v2t_metrics] epoch 0, R@1: 28.4, R@5: 55.8, R@10 68.8, R@50 90.9MedR: 4, MeanR: 23.8



#### train:1000 test:200 original frame=4 no-pretrain  batch_size=12 105735
    [t2v_metrics] epoch 0, R@1: 23.5, R@5: 58.0, R@10 69.0, R@50 92.5MedR: 4, MeanR: 14.7
    [v2t_metrics] epoch 0, R@1: 23.5, R@5: 58.5, R@10 67.5, R@50 94.0MedR: 4, MeanR: 13.4

#### train:1000 test:200 original frame=4 no-pretrain  batch_size=12 change-loss 123353(delete)
    [t2v_metrics] epoch 0, R@1: 25.5, R@5: 55.5, R@10 69.5, R@50 92.0MedR: 5, MeanR: 14.3
    [v2t_metrics] epoch 0, R@1: 25.0, R@5: 58.0, R@10 70.5, R@50 92.5MedR: 4, MeanR: 14.4

#### train:1000 test:200 original frame=4 no-pretrain  batch_size=12 SEAttention 151853 / 0811-084026(train 2 times)
    [t2v_metrics] epoch 0, R@1: 30.5, R@5: 59.0, R@10 71.0, R@50 92.5MedR: 4, MeanR: 13.9
    [v2t_metrics] epoch 0, R@1: 29.5, R@5: 59.5, R@10 72.0, R@50 91.0MedR: 3, MeanR: 13.8
    /
    epoch24 [t2v_metrics] epoch 0, R@1: 27.0, R@5: 59.5, R@10 72.5, R@50 94.0MedR: 4, MeanR: 13.8
            [v2t_metrics] epoch 0, R@1: 28.5, R@5: 57.0, R@10 69.0, R@50 93.5MedR: 4, MeanR: 12.9

#### train:1000 test:200 original frame=4 no-pretrain  batch_size=12 SEAttention + loss 232437
    [t2v_metrics] epoch 0, R@1: 24.0, R@5: 54.0, R@10 65.5, R@50 89.5MedR: 4, MeanR: 17.1
    [v2t_metrics] epoch 0, R@1: 25.0, R@5: 53.0, R@10 68.5, R@50 90.5MedR: 5, MeanR: 15.8

#### train:1000 test:200 original frame=4 no-pretrain  batch_size=12 frame+sentence 0812_130326(oring_test / change_test)    
    [t2v_metrics] epoch 0, R@1: 26.0, R@5: 55.0, R@10 68.5, R@50 91.0MedR: 4, MeanR: 15.0
    [v2t_metrics] epoch 0, R@1: 26.0, R@5: 56.0, R@10 73.5, R@50 92.5MedR: 4, MeanR: 13.4
    /
    [t2v_metrics] epoch 0, R@1: 39.0, R@5: 63.0, R@10 77.0, R@50 94.0MedR: 3, MeanR: 12.2
    [v2t_metrics] epoch 0, R@1: 36.5, R@5: 67.5, R@10 77.5, R@50 94.0MedR: 3, MeanR: 12.1

#### train:1000 test:200 original frame=4 no-pretrain  batch_size=12 frame+sentence\frame+word 0813_172328(frame_sentence_test)
    [t2v_metrics] epoch 0, R@1: 30.0, R@5: 65.0, R@10 79.5, R@50 93.5MedR: 3, MeanR: 11.9
    [v2t_metrics] epoch 0, R@1: 35.5, R@5: 67.0, R@10 76.0, R@50 93.0MedR: 3, MeanR: 12.3
    /
    [t2v_metrics] epoch 0, R@1: 33.5, R@5: 67.0, R@10 72.5, R@50 94.0MedR: 3, MeanR: 11.7
    [v2t_metrics] epoch 0, R@1: 38.5, R@5: 68.0, R@10 75.5, R@50 94.0MedR: 3, MeanR: 12.1



#### train:10000 test:1000 original frame=4 no-pretrain  batch_size=12 090742
    [t2v_metrics] epoch 0, R@1: 16.1, R@5: 43.5, R@10 57.6, R@50 83.0MedR: 7, MeanR: 38.6
    [v2t_metrics] epoch 0, R@1: 19.0, R@5: 46.4, R@10 59.7, R@50 83.3MedR: 7, MeanR: 37.1


#### train:10000 test:1000 original frame=4 no-pretrain  batch_size=12 SEA+Frame-sentence 0812-214314(change_test)
    [t2v_metrics] epoch 0, R@1: 24.6, R@5: 51.2, R@10 63.2, R@50 86.2MedR: 5, MeanR: 34.3
    [v2t_metrics] epoch 0, R@1: 25.6, R@5: 52.0, R@10 64.3, R@50 85.4MedR: 5, MeanR: 31.4

#### train:10000 test:1000 original frame=8 pretrained  batch_size=12 SEA+Frame-sentence 0812-214314(change_test) 
    /17
    [t2v_metrics] epoch 0, R@1: 34.6, R@5: 60.8, R@10 70.6, R@50 90.4MedR: 3, MeanR: 25.1
    [v2t_metrics] epoch 0, R@1: 35.7, R@5: 60.1, R@10 71.0, R@50 90.5MedR: 3, MeanR: 22.3
    /3
    [t2v_metrics] epoch 0, R@1: 35.1, R@5: 61.5, R@10 72.1, R@50 89.1MedR: 3, MeanR: 25.9 / clip
    [t2v_metrics] epoch 0, R@1: 34.5, R@5: 60.1, R@10 70.8, R@50 89.4MedR: 3, MeanR: 23.6
    [v2t_metrics] epoch 0, R@1: 36.2, R@5: 61.8, R@10 70.7, R@50 89.7MedR: 3, MeanR: 21.1
    

#### MSVD 4FRAME/16BATCHSIZE
    mdoel_best
    [t2v_metrics] epoch 0, R@1: 37.2, R@5: 67.0, R@10 76.5, R@50 93.6MedR: 2, MeanR: 14.9
    [v2t_metrics] epoch 0, R@1: 36.5, R@5: 65.5, R@10 75.6, R@50 92.8MedR: 2, MeanR: 15.4
    \
    [t2v_metrics] epoch 0, R@1: 40.7, R@5: 70.0, R@10 80.9, R@50 95.2MedR: 2, MeanR: 12.0
    [v2t_metrics] epoch 0, R@1: 40.7, R@5: 68.5, R@10 80.0, R@50 95.5MedR: 2, MeanR: 11.6
    
    multi-sentence-without(stopwords)
    model_best
    [t2v_metrics] epoch 0, R@1: 40.5, R@5: 70.3, R@10 79.8, R@50 92.2MedR: 2, MeanR: 16.4
    [v2t_metrics] epoch 0, R@1: 40.4, R@5: 71.2, R@10 80.9, R@50 92.8MedR: 2, MeanR: 15.7
    \
    [t2v_metrics] epoch 0, R@1: 41.7, R@5: 70.0, R@10 78.5, R@50 91.5MedR: 2, MeanR: 18.5
    [v2t_metrics] epoch 0, R@1: 42.5, R@5: 69.7, R@10 79.7, R@50 91.9MedR: 2, MeanR: 18.2
