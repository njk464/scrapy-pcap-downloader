import scrapy
from scrapy_downloader.items import myItem

# joins the url and extension together
def join(url, ext):
    while url[len(url)-1] != '/':
        url = url[0:len(url)-1]
    return url + ext

class mta(scrapy.Spider):
    name = "mta"
    allowed_domains = ["malware-traffic-analysis.net"]
    start_urls = [
        "http://www.malware-traffic-analysis.net/2013/index.html",
        "http://www.malware-traffic-analysis.net/2014/index.html",
        "http://www.malware-traffic-analysis.net/2015/index.html",
        "http://www.malware-traffic-analysis.net/2016/index.html"
    ]

    def parse(self, response):
        for href in response.xpath("//ul/li/a[@class='list_header']/@href").extract():
            yield scrapy.Request(join(response.url, href), callback=self.parse_url)

    def parse_url(self, response):
        # the xpath finds all hrefs that end with .pcap
        # xpath v1 does not have ends-with(), had to create a work around
        i = myItem()
        i['file_urls'] = []
        for href in response.xpath("//a[substring(@href,string-length(@href)-4)='.pcap']/@href").extract():
            i['file_urls'].append(join(response.url, href))
        yield i
