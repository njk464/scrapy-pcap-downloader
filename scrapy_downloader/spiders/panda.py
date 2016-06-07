import scrapy
from scrapy_downloader.items import myItem
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

# joins the url and extension together
def join(url, ext):
    while url[len(url)-1] != '/':
        url = url[0:len(url)-1]
    return url + ext

class panda(BaseSpider):
    name = "panda"
    allowed_domains = ["panda.gtisc.gatech.edu"]
    start_urls = [
        "http://panda.gtisc.gatech.edu/malrec/"
    ]

    def parse(self, response):
        i = myItem()
        i['file_urls'] = []
        for href in response.xpath("//a[substring(@href,string-length(@href)-4)='.pcap']/@href").extract():
            i['file_urls'].append(join(response.url, href))
        print i

