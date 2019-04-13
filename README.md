# news_crawler

## 簡介

此為使用BeautifulSoup套件爬取google news的程式，該程式最初會讓使用者輸入關鍵字及爬取頁數，接受資訊之後會進行爬取動作，並將標題、新聞來源、內文等內容，儲存在word檔案之中，最後利用WordCloud套件，製作成文字雲，以將文本關鍵字視覺化呈現。

## 範例1 - 光寶

### 1.請使用者輸入關鍵字及頁數

請使用者輸入關鍵字及頁數，程式即會從google news第一頁開始爬起，倘若網址失效，亦會顯示抓不到網址等字樣。

![1](<https://github.com/vbjc5275/news_crawler/raw/master/Crawler/image/1.jpg>)

### 2.檢視路徑底下的word檔

程式抓取內文完畢，會將相關資訊自動寫入word檔，並依照既定格式排列。

![2](https://github.com/vbjc5275/news_crawler/raw/master/Crawler/image/2.jpg)

### 3.檢視文字雲

程式最後一步，會自動生成文字雲，文字大小會依照內文的字詞頻率高低變化，並將圖片儲存在資料夾內。

![光寶 NEWS](<https://github.com/vbjc5275/news_crawler/raw/master/Crawler/image/%E5%85%89%E5%AF%B6%20NEWS.png>)

## 範例2 - 影像辨識

### 1.請使用者輸入關鍵字及頁數

![2-1](https://github.com/vbjc5275/news_crawler/raw/master/Crawler/image/2-1.jpg)

###  2.檢視路徑底下的word檔

![2-2](https://github.com/vbjc5275/news_crawler/raw/master/Crawler/image/2-2.jpg)

### 3.檢視文字雲

![影像辨識 NEWS](https://github.com/vbjc5275/news_crawler/raw/master/Crawler/image/%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%20NEWS.png)

## 未來展望

本作品未來希望可以達到為word檔新聞標題自動添加網址連結的功能。
待具備技能：

**巨集程式**

