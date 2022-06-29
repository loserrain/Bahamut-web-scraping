import scrapy
import bs4


class BhSpider(scrapy.Spider):
    name = 'BH' #專案名稱
    allowed_domains = ['forum.gamer.com.tw'] #網域名稱

    def start_requests(self): #開始進行請求
       
        urls =[]
        maxPages =10 #決定要爬多少頁的標題

        for page in range(1,maxPages+1): #先分別建立maxPages頁的網址再一一丟出請求
            urls.append('https://forum.gamer.com.tw/B.php?page='+ str(page)+'&bsn=60076')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
      


    def parse(self, response): #利用BS4套件解析頁面
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        titles = soup.find_all('p','b-list__main__title')
        for title in titles:
            print(title.get_text())

      
   
        
        
