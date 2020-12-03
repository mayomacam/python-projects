#!/usr/bin/python3
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    for i in punctuation_chars:
        if i in word:
            word = word.replace(i, "")
    #print(word)
    return word

def get_neg(word):
    s = word.split()
    print(s)
    count = 0
    for i in s:
        i = strip_punctuation(i).lower()
        if i in negative_words:
            count= count+1
    #print(count)
    return count

def get_pos(word):
    s = word.split()
    #print(s)
    count = 0
    for i in s:
        i = strip_punctuation(i).lower()
        if i in positive_words:
            count= count+1
    #print(count)
    return count

with open('project_twitter_data.csv') as project:
    reader = project.readlines()
    with open('resulting_data.csv','w') as data:
        data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
        header = reader[0]
        fd = header.strip().split(',')
        for tweet in reader[1:]:
            t = tweet.strip().split(',')
            pos = get_pos(t[0])
            neg = get_neg(t[0])
            net = pos - neg
            data.write("{}, {}, {}, {}, {}\n".format(t[1], t[2], pos, neg, net))

data.close()