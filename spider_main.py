#coding = utf-8
from baike_spider import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
	def __init__(self):
		self.urls = url.mmanager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()
		
	def craw(self,root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
		try:
			new_url = self.urls.get_new_url()
			print('craw %d : %s' % (count,new_url))
			html_doc = self.downloader.download(new_url)
			new_urls,new_data = self.parser.parse(new_url,html_doc)
			self.urls.add_new_urls(new_urls)
			sellf_outputer.collect_data(new_data)
			
			if count == 100:
				break
				
			count += 1
			
		except:
			print('craw failed~')
			
		self.oupter.output_html()

if __name__ == '__main__':
	root_url = 'http://baike.baidu.com/item/Python'
	#入口url
	obj_spider = SpiderMain()
	#创建一个Spider Main()
	obj_spider.craw(root_url)
	#用Spider Main.craw(url)来启动爬虫
	