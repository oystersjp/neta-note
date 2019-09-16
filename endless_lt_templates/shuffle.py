# coding: utf-8

"""
python shuffle.py

で実行すると標準出力にシャッフル結果が出力される
"""

import random

persenters = [
    # イベント開始前、あらかじめ発表者の connpass 表示名を記入しておく
    'Alice',
    'Bob',
    'Carol',
]

random.shuffle(persenters)
for i, p in enumerate(persenters):
    print str(i + 1) + ': ' + p + ' さん'
