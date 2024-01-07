# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:46:44 2019

@author: User
"""
import configparser
import requests
from bs4 import BeautifulSoup
import time
import random
import urllib.parse
import os
import warnings
warnings.filterwarnings('ignore')

###############################################################################
#                     請使用者輸入關鍵字，並爬下的相關新聞 (Title,Source,Content)                           #
###############################################################################

config = configparser.ConfigParser()
config.read('config.ini')


class Crawler():
    def __init__(self, keyword, nums, send_msg):
        self.keyword = keyword
        self.nums = nums
        # self.__output_area = output_area
        self.send_msg = send_msg

    def get_soup(self, url):
        list_req = requests.get(url)
        if list_req.status_code == requests.codes.ok:
            # 以 BeautifulSoup 解析 HTML 程式碼
            soup = BeautifulSoup(list_req.text, 'html.parser')
            return soup
        return None

    def get_news_content(self, soup, source):
        ps_tag = soup.find_all('p')
        if ps_tag is None:
            return None

        content = " ".join([p.text for p in ps_tag])
        return content

    def create_url(self):
        url = 'https://news.google.com/search?q={}&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant'.format(
            urllib.parse.quote(self.keyword))
        return url

    def get_news_info(self, news_block):
        # fine news basic info under the pageElement (news_block)
        title = news_block.find('a').text
        link = news_block.find('a').get('href')
        source = news_block.find('div', class_='vr1PYe').text
        return {"title": title, "link": link, "source": source}

    def crawl(self):
        url = self.create_url()
        soup = self.get_soup(url)

        if soup is None:
            self.send_msg(f'[LinkQueryError] url: {url}')
            return

        # 以 CSS 的 class 抓出頭條新聞
        news_blocks = soup.find_all('div', class_='B6pJDd')
        news_infos = []

        # get title & source & content link
        for news_block in news_blocks[:self.nums]:

            # get news content from link
            try:
                news_info = self.get_news_info(news_block)

                # to absoulte link
                link = news_info["link"].replace(r"./", "")
                news_info["link"] = f"https://news.google.com/{link}"

                # crawl content
                time.sleep(random.random()*3)
                self.send_msg(
                    f"Crawl & Parse: {news_info['title']}. {news_info['source']} ...")
                soup = self.get_soup(news_info["link"])

                if soup is None:
                    self.send_msg(
                        f"[ContentcrawlingError] content link: {news_info['link']}")
                    continue

                # parse content
                content = self.get_news_content(
                    soup, news_info["source"])

                if content is None:
                    self.send_msg(
                        f"[ContentParsingError] content link: {news_info['link']}")
                    continue

                news_info['content'] = content
                news_infos.append(news_info)

            except Exception as e:
                print(str(e))

        return news_infos
