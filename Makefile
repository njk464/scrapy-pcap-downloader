# default, scraps web pages for pcaps, downloads them and transfers them to the correct directory
.PHONY: all
all:
	scrapy crawl panda
	scrapy crawl mta
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
	pip --upgrade pip
	pip install scrapy
