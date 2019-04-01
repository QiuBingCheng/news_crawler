# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:43:24 2018

@author: User
"""

import jieba
jieba.set_dictionary('dict.txt.big.txt');
from nltk.tokenize import word_tokenize
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def fileter_sentecnce(content):
    '''回傳文本切詞結果，詞之間以空白隔開，type為String'''
    #利用字典分詞，以空格隔開
    cut_text=" ".join(jieba.cut(content))
    
    #去除無意義的發語詞或轉折詞 (了、哦、啊，然後等等)
    with open(r'C:\Users\User\Crawler\stopwords.txt',encoding='UTF-8') as f:
        stopwords=f.readlines()
        
    #隱藏格式干擾讀取
    stopwords=[w.replace('\n'," ")for w in stopwords]
    stopwords=[w.replace(" ","") for w in stopwords]
    stopwords.append('\n')
    stopwords.append('\n   \n')
    stopwords.append('\x0b')
    
    
    #data can be split into words in list.
    word_tokens=word_tokenize(cut_text)
    filtered_sentence = [w for w in word_tokens if not w in stopwords]
    cut_text=" ".join(filtered_sentence)
    return cut_text

def text_freq(cut_text):
    '''計算單詞頻率，回傳型態為dataFrame'''
    word_tokens = word_tokenize(cut_text)
    cut_text = [' '.join(word_tokens)]
    
    vec = CountVectorizer().fit(cut_text)
    bag_of_words = vec.transform(cut_text)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [[word, sum_words[0, idx]] for word, idx in vec.vocabulary_.items()]
    words_freq = pd.DataFrame(words_freq, columns = ['word', 'counts'])
    words_counts = words_freq.sort_values(['counts'], ascending = False)
    return words_counts 