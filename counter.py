实现一个简单的单词计数器，统计给定文本中每个单词出现的次数：
python
Copy code
import re
from collections import Counter

def word_counter(text):
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    return word_counts

text = input("请输入文本：")
word_counts = word_counter(text)

print("单词出现次数：")
for word, count in word_counts.items():
    print(word, ":", count)
