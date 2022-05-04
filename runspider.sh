rm -r CrawlNodes/datas/node/nodes.csv,nodes.txt
touch nodes.csv
scrapy crawl clash_v2ray
python tobase64.py
git add .
git commit -am "爬取v2ray节点"
git push -f
