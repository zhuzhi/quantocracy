#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-12-20 上午12:54
# @Author  : zhuzhi
# @File    : qo_feed_get.py
# @Software: PyCharm
# @Desc     :
# @Contact : zhuzhi90@gmail.com
import re
import os
import urllib.request
import datetime
from bs4 import BeautifulSoup


def qo_feed_get(overwrite=True):
    """
    从 quantocracy 的 RSS 页面获取内容. 依据日期写成 markdown 格式.

    :param overwrite: 是否覆盖写入, True 表示覆盖写入.
    :return:
    """
    dir_sav = './daily/'

    url_qo_feed = 'http://feeds.feedburner.com/Quantocracy'
    re_date = re.compile('\d{2}/\d{2}/\d{4}')

    link_format = '[%s](%s)'

    page_qo_feed = urllib.request.urlopen(url_qo_feed)

    soup_qo_feed = BeautifulSoup(page_qo_feed, 'xml')

    mds = os.listdir(dir_sav)
    mds = [x.replace('.md', '') for x in mds]

    for item in soup_qo_feed.find_all('item'):

        item_title = item.find('title')
        item_link = item.find('link')
        item_pubDate = item.find('pubDate')
        item_content = BeautifulSoup(item.find('content:encoded').string, 'lxml')

        item_date = datetime.datetime.strptime(re.search(re_date, item_title.string).group(), '%m/%d/%Y').strftime(
            '%Y-%m-%d')

        if not overwrite:
            if item_date in mds:
                # print '[qo_feed_get] ' + item_date + ' already exists!'
                continue

        item_file = open(dir_sav + item_date + '.md', 'w')

        file_title = link_format % (item_title.string, item_link.string)

        item_file.writelines('### ' + file_title)
        item_file.write('\n')
        item_file.writelines(item_pubDate.string)
        item_file.write('\n')

        for entry in item_content.find('div', {'id': 'qo-mashup'}).find_all('div', {'class': 'qo-entry'}):
            entry_title = entry.find('a', {'class': 'qo-title'})
            entry_descr = entry.find('div', {'class': 'qo-description'})

            file_entry_tile = link_format % (entry_title.string, entry_title['href'])
            item_file.writelines('#### ' + file_entry_tile)
            item_file.write('\n')
            item_file.writelines(entry_descr.string)
            item_file.write('\n')

        item_file.close()

if __name__ == '__main__':

    import os


    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_dir)

    qo_feed_get(overwrite=False)
