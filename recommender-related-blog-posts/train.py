#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jubatus
from jubatus.common import Datum
import json

JUBATUS_HOST = '127.0.0.1'
JUBATUS_PORT = 9199
JUBATUS_NAME = 'related-blog-posts'
TRAINING_DATA = './data/training_data.json'

# Jubatus推薦クライアントを生成
client = jubatus.Recommender(JUBATUS_HOST, JUBATUS_PORT, JUBATUS_NAME)

# 教師データファイルを読み込む
with open(TRAINING_DATA) as f:
    learning_data = json.load(f)
    for url, text in learning_data.items():
        # 教師データをJubatusに教え込む
        client.update_row(url, Datum({'text': text}))
        print url
    # 学習データをファイルに保存する
    client.save(JUBATUS_NAME)
