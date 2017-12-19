#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-20 上午12:54
# @Author  : zhuzhi
# @File    : qo_feed_get.py
# @Software: PyCharm
# @Desc     :
# @Contact : zhuzhi90@gmail.com
import re
import urllib
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

    page_qo_feed = urllib.urlopen(url_qo_feed)

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

        file_title = link_format % (item_title.string.encode('utf-8'), item_link.string.encode('utf-8'))

        item_file.write('### ' + file_title + '\n')
        item_file.write('\n')
        item_file.write(item_pubDate.string + '\n')

        for entry in item_content.find('div', {'id': 'qo-mashup'}).find_all('div', {'class': 'qo-entry'}):
            entry_title = entry.find('a', {'class': 'qo-title'})
            entry_descr = entry.find('div', {'class': 'qo-description'})

            file_entry_tile = link_format % (entry_title.string.encode('utf-8'), entry_title['href'].encode('utf-8'))
            item_file.write('#### ' + file_entry_tile + '\n')
            item_file.write('\n')
            item_file.write(entry_descr.string.encode('utf-8'))
            item_file.write('\n')

        item_file.close()

if __name__ == '__main__':

    import os
    os.chdir(os.getenv("HOME") + '/quantocracy')

    qo_feed_get(overwrite=False)