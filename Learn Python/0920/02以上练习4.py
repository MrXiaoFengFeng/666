# 统计s = "hello egon egon say hello xxx xxx"
# 中每个单词的个数
# 结果如：{"hello":2,"egon":2,"say":1,"xxx":2}

# 答案
# 方式一
s = "hello egon egon say hello xxx xxx"
dic = {}
words = s.split()
print(words)
for word in words:  # word='egon'
    dic[word] = s.count(word)
    print(dic)

# 方式二：利用setdefault解决重复赋值
s = "hello egon egon say hello xxx xxx"
dic = {}
words = s.split()
for word in words:  # word='egon'
    dic.setdefault(word, s.count(word))
    print(dic)

# 方式三：利用集合，去掉重复，减少循环次数
s = "hello egon egon say hello xxx xxx"
dic = {}
words = s.split()
words_set = set(words)
for word in words_set:
    dic[word] = s.count(word)
    print(dic)