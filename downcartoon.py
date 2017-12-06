#!/usr/bin/python
#coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
from os import path as osp
import urllib
# 一个简单的下载器
class CartoonCat():
	def download(url, save_path):
		try:
			with open(save_path, 'wb') as fp:
				fp.write(urllib.urlopen(url).read())
		except Exception, et:
			print(et)

	if __name__ == "__main__":

		browser = webdriver.Chrome()
		main_page = "http://www.tazhe.com/mh/9170/"
		browser.get(main_page) # 加载页面
			# 解析出章节的元素节点
		chapter_elem_list = browser.find_elements_by_css_selector('#play_0 ul li a') # 通过css选择器找出章节节点
		chapter_elem_list.reverse()  # 原本的章节是倒叙的
		chapter_list = []
		for chapter_elem in chapter_elem_list:
				# 元素的text和href属性分别就是章节的名称和地址
			chapter_list.append((chapter_elem.text, chapter_elem.get_attribute('href')))
	#		 chapter_list 就是章节的信息

		save_folder = "/Users/qiupingsun/Downloads/cartoon"
		for i in range(len(chapter_list)):
			chapter_name = chapter_list[i][0]
			chapter_url = chapter_list[i][1]
			if not osp.exists(save_folder):
				os.mkdir(save_folder)
			image_idx = 1
			browser.get(chapter_url) # 加载第一个页面
		#		os.path.basename()获取文件名函数
				# 根据前文的分析，找到图片的URI地址
			while True:
				image_url = browser.find_element_by_css_selector('#qTcms_pic').get_attribute('src')
				save_image_name = osp.join(save_folder,('%s') % (i+1)+'_'+('%05d' % image_idx) + '.' + osp.basename(image_url).split('.')[-1])
				download(image_url, save_image_name) # 下载图片
					# 通过模拟点击加载下一页，注意如果是最后一页，会出现弹窗提示
				print 'img saved!!!'
				browser.find_element_by_css_selector('a.next').click()
				try:
				# 找寻弹窗，如果弹窗存在，说明这个章节下载完毕，这个大循环也就结束了
					browser.find_element_by_css_selector('#bgDiv')
					print 'end'
					break	
				except NoSuchElementException:
					# 没有结束弹窗，继续下载
					image_idx += 1
					print image_idx