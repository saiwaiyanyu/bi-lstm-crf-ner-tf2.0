# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/3 1:51 下午
# @Author: wuchenglong


import tensorflow as tf
from model import NerModel
from utils import tokenize,read_vocab,format_result
import tensorflow_addons as tf_ad
from args_help import args
import json


vocab2id, id2vocab = read_vocab(args.vocab_file)
tag2id, id2tag = read_vocab(args.tag_file)
text_sequences ,label_sequences= tokenize(args.test_path,vocab2id,tag2id)



optimizer = tf.keras.optimizers.Adam(args.lr)
model = NerModel(hidden_num = args.hidden_num, vocab_size =len(vocab2id), label_size = len(tag2id), embedding_size = args.embedding_size)
# restore model
ckpt = tf.train.Checkpoint(optimizer=optimizer,model=model)
ckpt.restore(tf.train.latest_checkpoint(args.output_dir))


while True:
    text = input("input:")
    dataset = tf.keras.preprocessing.sequence.pad_sequences([[vocab2id.get(char,0) for char in text]], padding='post')
    print(dataset)
    logits, text_lens = model.predict(dataset)
    paths = []
    for logit, text_len in zip(logits, text_lens):
        viterbi_path, _ = tf_ad.text.viterbi_decode(logit[:text_len], model.transition_params)
        paths.append(viterbi_path)
    print(paths[0])
    print([id2tag[id] for id in paths[0]])

    entities_result = format_result(list(text), [id2tag[id] for id in paths[0]])
    print(json.dumps(entities_result, indent=4, ensure_ascii=False))
