#-*- coding:  Shift-JIS -*-

import difflib

text_a = '����'
text_b = '����'
r=difflib.SequenceMatcher(None,text_a,text_b).ratio()
print(r)