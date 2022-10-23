# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/2 20:24
# @Author : San_mao_liu
# @File : longestPalindrome.py
# @Software: PyCharm


def longestPalindrome(s):
    palindrome = ''

    for i in range(len(s)):
        len1 = len(getlongestpalindrome(s,i,i))
        if len1 > len(palindrome):
            palindrome = getlongestpalindrome(s,i,i)

        len2 = len(getlongestpalindrome(s,i,i+1))
        if len2 > len(palindrome):
            palindrome = getlongestpalindrome(s,i,i+1)

    return palindrome


def getlongestpalindrome(s,l,r):
    while l>=0 and r<len(s) and s[l] == s[r]:
        l -= 1    # 左边的左移
        r += 1    # 右边的右移
    return s[l+1:r]






def longestpalindrome(s):
    if len(s) == 0:
        return 0
    maxLen = 1
    start = 0

    for i in range(len(s)):
        if i-maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1]:
            start = i-maxLen-1
            maxLen += 2
            continue

        if i-maxLen>=0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
            start = i - maxLen
            maxLen +=1

    return s[start:start+maxLen]


s = 'baccab'
print(s[1:3])
print(s[1:3][::-1])

# print(longestPalindrome(s))
print(longestpalindrome(s))
















