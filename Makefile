# default, scraps web pages for pcaps, downloads them and transfers them to the correct directory
.PHONY: all
all:
	scrapy crawl mta
	scrapy crawl panda
	sh transfer.sh

# Transfers the files
.PHONY: transfer
transfer:
	sh transfer.sh

# installs scrapy and all of its dependencies
.PHONY: install
install:
	yum install python-devel.x86_64
	python get-pip.py
	pip --proxy=http://wwwproxy.sandia.gov:80 install --upgrade pip
	pip --proxy=http://wwwproxy.sandia.gov:80 install scrapy