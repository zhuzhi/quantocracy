### 从 Quantocracy 网站获得每天的信息然后推送到 kindle 上.
一切信息均来自于网站 [Quantocracy](http://quantocracy.com/])

<!-- TOC depthFrom:4 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [从 Quantocracy 网站获得每天的信息然后推送到 kindle 上.](#从-quantocracy-网站获得每天的信息然后推送到-kindle-上)
	- [文章获取](#文章获取)
		- [文章列表取得](#文章列表取得)
		- [单独文章获取](#单独文章获取)

<!-- /TOC -->

#### 文章获取
##### 文章列表取得
[Quantocracy RSS](http://feeds.feedburner.com/Quantocracy) 获得文章列表,包括 **title**, **description**, **link** 等.

> 注意:
> - Quantocracy RSS 托管在 feedburner 上,所以国内可能无法顺利访问.
> - Quantocracy 主页需要一些伪装才能顺利获取页面.

> 网页结构:
> - html(chrome)
>
> 	![quantocracy_rss](./img/quantocracy.png)
> - xml(urllib)
>
>	 ![quantocracy_xml](./img/quantocracy_xml.png)

##### 单独文章获取

没有解决好.利用 pdfkit 保存整个网页,但是某些网页无法保存.

一些类似印象笔记剪藏api的方法,要收费,不提供免费api,或者只提供短时间试用.

目前没有自己写的想法.


#### 发送文章到 kindle

最直接的方法就是发带附件的邮件到自己Kindle邮箱上,我来想想看有没有什么骚操作.
