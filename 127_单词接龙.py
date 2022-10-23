# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/30 9:11
# @Author : San_mao_liu
# @File : 127_单词接龙.py
# @Software: PyCharm


import string

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:return  0

    front = {beginWord}
    back = {endWord}
    dist = 1
    wordList = set(wordList)
    word_len = len(beginWord)

    # BFS starts here
    while front and back:
        dist += 1
        next_front = set()

        for word in front:
            for i in range(word_len):
                for c in string.ascii_lowercase:
                    if c != word[i]:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in back:
                            return dist
                        if new_word in wordList:
                            next_front.add(new_word)
                            wordList.remove(new_word)

        front = next_front

        if len(back) < len(front):
            front, back = back, front

    return 0




beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))
























