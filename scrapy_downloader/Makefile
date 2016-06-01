.PHONY: all
all:
	scrapy crawl mta
	scrapy crawl panda

.PHONY: install
install:
	curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
	python get-pip.py
	pip --proxy=http://wwwproxy.sandia.gov:80 install scrapy