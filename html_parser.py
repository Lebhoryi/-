#coding = utf-8
from bs4 import BeautifulSoup
import urlliob.parse
import re

class HtmlParser(object):
	
	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		links = soup.find_all('a',href=re.compile(r'/item/\d+\.htm'))
		#此处的正则不会
		for link in	links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)
		return new_urls
		
	def _get_new_data(self,page_url,soup):
		res_data = {}
		
		#url
		res_data['url'] = page_url
		
		#标题：<dd class="lemmaWgt-lemmaTitle-title">		<h1>Python</h1>
		title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title'.find('h1'))
		res_data['title'] = title_node.get_text()
		
		#简介：<div class="lemma-summary" label-module="lemmaSummary">
		summary_node = soup.find('div',class_='lemma-summary')
		res_data['summary'] = summary_node.get_text()
		
		return res_data

	def parse(self,page_url,html_doc):
		if page_url is NOne or html_doc is None:
			return 
		
		soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
		new_urls = self._get_new_urls(self.new_urls)
		new_data = self._get_new_data(self.new_urls)
		
		return new_urls,new_data