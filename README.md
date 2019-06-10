# news_crawler

## 簡介

此為使用BeautifulSoup套件爬取google news的程式，該程式最初會讓使用者輸入關鍵字及爬取頁數，接受資訊之後會進行爬取動作，並將標題、新聞來源、內文等內容，儲存在word檔案之中，最後利用WordCloud套件，製作成文字雲，以將文本關鍵字視覺化呈現。

## 範例1 - 華碩

### 1.請使用者輸入關鍵字及頁數

請使用者輸入關鍵字及頁數，程式即會從google news第一頁開始爬起，倘若爬取失敗，亦會列出該失效來源及網址。

![1](<https://github.com/vbjc5275/news_crawler/raw/master/Crawler/image/1.jpg>)

### 2.檢視歷史紀錄

程式抓取內文完畢，會將爬取結果儲存在資料庫，當使用者點選上方選單**歷史紀錄**，便會顯示爬取紀錄，右邊同時會展示該次爬取的文字雲。

![2](https://github.com/vbjc5275/news_crawler/raw/master/Crawler/image/2.jpg)

### 3.文本儲存

文本儲存有兩種方式，一種是自動寫入資料庫，或者也可以將相關資訊寫入word檔，並依照既定格式排列。

![2](https://github.com/vbjc5275/news_crawler/raw/master/Crawler/image/3.jpg)

## 未來展望

本作品未來希望可以增填搜尋熱度的趨勢變化，類似Google Trend功能。


