# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiaozhuPipeline(object):

    def process_item(self, item, spider):
        fp = open('./log.txt', 'a+')
        fp.write('标题:\t\t' + item['title'] + '\n')
        fp.write('地址：\t\t' + item['address'] + '\n')
        fp.write('交通情况:\t\t' + item['traffic'] + '\n')

        return item
