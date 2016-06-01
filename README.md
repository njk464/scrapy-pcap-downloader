Readme for scrapy-pcap-downloader

Scrapy version 1.1.0

To specify the directory that the pcaps will be put into go into transfer.sh and modify PATH.

To run use the makefile. 

"make install" should install everything needed for the scraper to work.

"make" will run the web scrapers.

"make transfer" will transfer all of the pcaps to the correct directory.

Scrapy transfers the files into a local directory. The bash script will transfer those files to the correct location
