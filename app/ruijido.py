#-*- coding:  Shift-JIS -*-

import difflib

text_a = '圧力'
text_b = '圧力'
r=difflib.SequenceMatcher(None,text_a,text_b).ratio()
print(r)