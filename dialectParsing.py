import lingpy
import json


#INSTALLATION REQUIREMENTS
# pip install sinopy

from sinopy import pinyin
pinyin('我', variant='cantonese')
from sinopy import *
##The quintuple that he method returns splits the sequence into its five main constituents, initial, medial, nucleus, coda, and tone.

a = parse_chinese_morphemes('ʨaŋ¹')
a
a[0]
a = clean_chinese_ipa('ŋɔi33')
parse_chinese_morphemes(a)
parse_chinese_morphemes('ɬiaŋ21')
parse_chinese_morphemes('ŋut215')
parse_chinese_morphemes('ŋot')
parse_chinese_morphemes('sêŋ')
parse_chinese_morphemes('ŋɔi33')
parse_chinese_morphemes('nrah')
parse_chinese_morphemes('hai55')
parse_chinese_morphemes('ŋjwo')
baxter2ipa('bjang')
