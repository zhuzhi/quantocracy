### 从 Quantocracy 网站获得每天的信息然后推送到 kindle 上.
一切信息均来自于网站 [Quantocracy](http://quantocracy.com/])

<!-- TOC depthFrom:3 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

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
> 	![quantocracy_rss](./img/quantocracy.png)
> - xml(urllib)
>		![quantocracy_xml](./img/quantocracy_xml.png)

##### 单独文章获取
