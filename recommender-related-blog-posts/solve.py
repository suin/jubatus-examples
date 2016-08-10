#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jubatus
from jubatus.common import Datum
import json

JUBATUS_HOST = '127.0.0.1'
JUBATUS_PORT = 9199
JUBATUS_NAME = 'related-blog-posts'

# Jubatus推薦クライアントを生成
client = jubatus.Recommender(JUBATUS_HOST, JUBATUS_PORT, JUBATUS_NAME)

print "IDから関連投稿を推薦してもらう"
posts = client.similar_row_from_id('http://qiita.com/suin/items/fb58426e6c1eaa2b8e18', 5)
for post in posts:
    print post.id, post.score

print "テキストから関連投稿を推薦してもらう"
posts = client.similar_row_from_datum(Datum({'text': 'Dockerでコンテナを起動するには...'}), 5)
for post in posts:
    print post.id, post.score
