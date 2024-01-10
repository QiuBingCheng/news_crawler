# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:46:44 2019

@author: User
"""
from collections import namedtuple
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import configparser
from bs4 import BeautifulSoup
import time
import random
import urllib.parse
from fake_useragent import UserAgent
import warnings
warnings.filterwarnings('ignore')

###############################################################################
#                     請使用者輸入關鍵字，並爬下的相關新聞 (Title,Source,Content)                           #
###############################################################################

config = configparser.ConfigParser()
config.read("config.ini")
newsInfo = namedtuple("newsInfo", ("title", "content", "source", "link"))


class Crawler():
    def __init__(self, send_msg):
        self.send_msg = send_msg
        self.user_agent = UserAgent()

        # time to sleep
        self.time_sleep = float(config["crawler"]["time_sleep"])

        # init webdriver
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--log-level=1')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # cService = webdriver.ChromeService(
        #     executable_path=config["crawler"]["driver_exe"])
        cService = Service(ChromeDriverManager().install())
        self.driver_params = {"service": cService, "options": options}

    def custom_header(self):
        headers = {
            'User-Agent': self.user_agent.random,  # User-Agent header
            'Accept-Language': 'zh-TW,zh;q=0.6',  # Accept-Language header
        }
        return headers

    def get_soup(self, url):
        browser = webdriver.Chrome(**self.driver_params)
        browser.get(url)
        browser.implicitly_wait(30)
        soup = BeautifulSoup(browser.page_source)
        browser.quit()
        return soup

    def get_news_content(self, soup, source):
        if source.find("巴哈姆特") != -1:
            div_tag = soup.find("p", class_="GN-lbox3B")
            if div_tag is None:
                return None
            final_tag = div_tag.find_all('div')
        else:
            final_tag = soup.find_all('p')

        if len(final_tag) == 0:
            return None

        content = " ".join([p.text for p in final_tag])
        return content

    def create_url(self, keyword):
        url = 'https://news.google.com/search?q={}&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant'.format(
            urllib.parse.quote(keyword))
        return url

    def get_news_info(self, news_block):
        # fine news basic info under the pageElement (news_block)
        title = news_block.find('a').text
        link = news_block.find('a').get('href')
        source = news_block.find('div', class_='vr1PYe').text
        return (title, link, source)

    def start(self, keyword, nums):
        # find the num news with the keyword

        url = self.create_url(keyword)
        soup = self.get_soup(url)

        if soup is None:
            self.send_msg(f'[LinkQueryError] url: {url}')
            return

        # find news contains keywork in google news home page
        news_blocks = soup.find_all('div', class_='B6pJDd')
        news_infos = []

        # get title & source & content link
        for news_block in news_blocks[:nums]:

            # get news content from link
            try:
                title, link, source = self.get_news_info(news_block)

                # to absoulte link
                link = link.replace(r"./", "")
                link = f"https://news.google.com/{link}"

                # crawl content
                time.sleep(self.time_sleep+random.random())
                self.send_msg(
                    f"Crawl & Parse: {title}. {source} ...")
                soup = self.get_soup(link)

                if soup is None:
                    self.send_msg(
                        f"[ContentcrawlingError] content link: {link}")
                    continue

                # parse content
                content = self.get_news_content(
                    soup, source)

                if content is None:
                    self.send_msg(
                        f"[ContentParsingError] content link: {link}")
                    continue

                news_infos.append(newsInfo(title=title, content=content,
                                           link=link, source=source))

            except Exception as e:
                print(f"[Error] {e}")

        return news_infos
