scrapy crawl clash_v2ray
cd CrawlNodes/datas/node && python tobase64.py
cd ../../../
git add .
git commit -am "爬取v2ray节点"
git push -f