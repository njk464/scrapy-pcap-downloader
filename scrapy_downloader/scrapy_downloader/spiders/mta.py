import scrapy

def to_pcap(url):
    arr = url.split("/")
    l = len(arr)
    url = url[0:len(url) - 10] + arr[l-4] + "-" + arr[l-3] + "-" + arr[l-2] + ".pcap"
    return url
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
        for href in response.xpath("//ul/li/a[@class='list_header']/@href"):
            url = to_pcap(response.urljoin(href.extract()))
            print url
