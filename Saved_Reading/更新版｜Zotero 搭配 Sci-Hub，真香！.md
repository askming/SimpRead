> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [mp.weixin.qq.com](https://mp.weixin.qq.com/s/QMSG24tgn4z8ShfE9pVYMg)

#### VIP 优惠券

VIP 优惠，微信扫码获取优惠券若下图优惠券过期，请点击小程序获取领优惠券![](https://mmbiz.qpic.cn/mmbiz_jpg/xGvHpjh4rNVmibUyfKiawZGTMoCnLRL3Wo9P6icdf2VpsNu8fn2xCGkZuBTgxZta6Fhzolt7NSPaUPrrJk46gib0cA/640?wx_fmt=jpeg)

#### VIP 权益

* * *

❶ 科研小白高效进阶 训练营❷ 论文 / 专利 写作指导❸ 知识星球 + 微信群 高质量学术社群❹ [青柠的学员为何具有 “精英范 国际范”？](https://mp.weixin.qq.com/s?__biz=MzAxNzgyMDg0MQ==&mid=2650457033&idx=3&sn=97b96fb61a4cc5d3a6a746c638e0cfb0&scene=21#wechat_redirect)❺ [300 GB 科研资源礼包，搭建知识体系](https://mp.weixin.qq.com/s?__biz=MzAxNzgyMDg0MQ==&mid=2650457065&idx=2&sn=9823723c6c4eb7421510751ccb4acf75&scene=21#wechat_redirect)❻ [共享 Apple ID，赠送 PaperShip 等科研 App](https://mp.weixin.qq.com/s?__biz=MzAxNzgyMDg0MQ==&mid=2650457065&idx=3&sn=c00cf2bd1bf9ed0eff5971f06566e122&scene=21#wechat_redirect)

* * *

##### -[start]-

在前天推送的 [Zotero 搭配 Sci-Hub，真香！](https://mp.weixin.qq.com/s?__biz=MzAxNzgyMDg0MQ==&mid=2650457469&idx=1&sn=7b06b5fab7e9320df11bf6be8a07e1e3&scene=21#wechat_redirect)中，Sci-Hub 配置代码中使用的是`.tw`域名。  

然而，根据这两天我对 Zotero + Sci-Hub 配置方法的进一步研究和捣鼓，我发现使用`.se`会有更好的体验，这得益于.`se`支持 SSL 连接 [1]（据我搜集到的信息其他几个域名如`.tw`、`si`是不支持 SSL 连接的）。

> “ 
> 
> SSL（Secure Socket Layer）协议可提供数据加密服务，维护数据完整性，降低数据在传输中的丢包率。
> 
> ”

此外，有部分粉丝（包括我自己）发现在 Zotero 中使用`.tw`的情况下，会有个别下载的文献提示 PDF 损坏。因此有理由猜测这和`.tw`不支持 SSL 连接有关系，即在传输中出现了数据丢失，从而导致 PDF 损坏。

因此今天特定推送 Zotero + Sci-Hub 的更新版。更新内容：使用`.se`替代`.tw`。

当然由于 Sci-Hub 经常更新域名，因此本文的配置代码未来也会根据需要进行更新。

除了代码做了改动，以下内容保持和上次推文一致。👇

* * *

Sci-Hub 有多香大家都知道！

Zotero 有多香，你看了我的教程就知道了！👇

[Zotero ，打造最佳文献生态（合集）](https://mp.weixin.qq.com/s?__biz=MzAxNzgyMDg0MQ==&mid=2650457432&idx=2&sn=5c7a306ed5946f492d5def0128aef7ee&scene=21#wechat_redirect)

那要是 Zotero+Sci-Hub，岂不是无敌了！

今天就教大家在 Zotero 内集成 Sci-Hub，实现在 Zotero 中免费下载 99% 的文献！

### 从 Zotero PDF retrieval 谈起

从 Zotero 5.0.56 版本开始，Zotero 迎来了`PDF retrieval`功能。详情可见 Zotero 官网的文章 “Improved PDF retrieval with Unpaywall integration”[2]

该功能会在你用 Zotero Connector 保存文献时，自动检查 Unpaywall 上是否有可供下载的免费文献。

> “ 
> 
> Unpaywall 能免费下载文献，但你不要以为它和 Sci-Hub 一样是非法的。其实 Unpaywall 是个非盈利性合法组织，它整合了数千个 Open Access 期刊或数据库，将免费文献集中之后开放 API，从而供其他平台使用。
> 
> ”

假如你在网页端保存的文献是 Open Access 的，Zotero Connector 就会将 PDF 同文献条目一起抓取，比如下面这样。

![](https://mmbiz.qpic.cn/mmbiz_jpg/xGvHpjh4rNVmibUyfKiawZGTMoCnLRL3Wo6ibhQ3cnnELnoGsum5cA7KQuPNjFU5ic7bMwn1UxWpaTWsYzjcibHw13w/640?wx_fmt=jpeg)

当然，对于已经在 Zotero 中却还没有 PDF 附件的文献条目，点击右键菜单中的`Find Available PDF`，即可下载文献，比如下面这样。

![](https://mmbiz.qpic.cn/mmbiz_jpg/xGvHpjh4rNVmibUyfKiawZGTMoCnLRL3WojZ3sQsszWibRibMrqibHeVWD8DYTPsDVHiaESojoQktecIeHsFwD6EJf2w/640?wx_fmt=jpeg)

但是，毕竟 Unpaywall 只支持 OA 文献，而 OA 文献又只是少数。也就是说，通过 Unpaywall 无法解决付费文献的下载问题。

不过幸运的是，作为一款开源软件，Zotero 的开发者为很多功能带来了可定制的能力，方便用户根据自己的喜好自定义。

`PDF retrieval`功能也不例外，Zotero 允许用户自定义 PDF 解析器（custom PDF resolvers），也就是说你可以将其他网站作为 PDF 解析器，来替代 Unpaywall。

详情可以访问 Zotero 官网链接 Custom PDF Resolvers[3]

这为我们将 Sci-Hub 作为 PDF resolver 带来可能！

考虑到 PDF resolver 是内置在 Zotero 中的，这能保证我们能稳定使用该功能，就算 Zotero 更新了也丝毫不用担心，这一点就比使用第三方插件要有保障得多！

下面具体介绍如何将 Sci-Hub 作为 PDF 解析器！

### 设置 Sci-Hub 作为 PDF 解析器

PDF resolvers 的设置在 Zotero 的 Config Editor 中。

我们打开 Zotero 的首选项，进入`Advanced-->Config Editor`。👇

![](https://mmbiz.qpic.cn/mmbiz_jpg/xGvHpjh4rNVmibUyfKiawZGTMoCnLRL3WoaYj8dVRY27V3a17wkr3lCDBMW9HU7tWmYKNUQaosw9xzRUFJnNgyWw/640?wx_fmt=jpeg)

搜索`extensions.zotero.findPDFs.resolvers`，如下。

![](https://mmbiz.qpic.cn/mmbiz_jpg/xGvHpjh4rNVmibUyfKiawZGTMoCnLRL3WosrhB5G5fSf2NxPETRkNwbOvRrCicKBU6PauEhq1ySlYUSaMp0UcyTRw/640?wx_fmt=jpeg)

双击`extensions.zotero.findPDFs.resolvers`，默认情况下是只有一对`[]`。

![](https://mmbiz.qpic.cn/mmbiz_jpg/xGvHpjh4rNVmibUyfKiawZGTMoCnLRL3WookrpicBqSLyX1InZxWQfLgYLk7LEj9HrO1hUXUusTMlkzgqm7spnicwQ/640?wx_fmt=jpeg)

删除`[]`，并将以下代码粘贴进去。

```
{<br data-darkmode-color-16319416567473="rgb(171, 178, 191)" data-darkmode-original-color-16319416567473="#fff|rgb(0,0,0)|rgb(171, 178, 191)" data-darkmode-bgcolor-16319416567473="rgb(49, 54, 63)" data-darkmode-original-bgcolor-16319416567473="#fff|rgb(40, 44, 52)">    "name":"Sci-Hub",<br data-darkmode-color-16319416567473="rgb(171, 178, 191)" data-darkmode-original-color-16319416567473="#fff|rgb(0,0,0)|rgb(171, 178, 191)" data-darkmode-bgcolor-16319416567473="rgb(49, 54, 63)" data-darkmode-original-bgcolor-16319416567473="#fff|rgb(40, 44, 52)">    "method":"GET",<br data-darkmode-color-16319416567473="rgb(171, 178, 191)" data-darkmode-original-color-16319416567473="#fff|rgb(0,0,0)|rgb(171, 178, 191)" data-darkmode-bgcolor-16319416567473="rgb(49, 54, 63)" data-darkmode-original-bgcolor-16319416567473="#fff|rgb(40, 44, 52)">    "url":"https://sci-hub.se/{doi}",<br data-darkmode-color-16319416567473="rgb(171, 178, 191)" data-darkmode-original-color-16319416567473="#fff|rgb(0,0,0)|rgb(171, 178, 191)" data-darkmode-bgcolor-16319416567473="rgb(49, 54, 63)" data-darkmode-original-bgcolor-16319416567473="#fff|rgb(40, 44, 52)">    "mode":"html",<br data-darkmode-color-16319416567473="rgb(171, 178, 191)" data-darkmode-original-color-16319416567473="#fff|rgb(0,0,0)|rgb(171, 178, 191)" data-darkmode-bgcolor-16319416567473="rgb(49, 54, 63)" data-darkmode-original-bgcolor-16319416567473="#fff|rgb(40, 44, 52)">    "selector":"#pdf",<br data-darkmode-color-16319416567473="rgb(171, 178, 191)" data-darkmode-original-color-16319416567473="#fff|rgb(0,0,0)|rgb(171, 178, 191)" data-darkmode-bgcolor-16319416567473="rgb(49, 54, 63)" data-darkmode-original-bgcolor-16319416567473="#fff|rgb(40, 44, 52)">    "attribute":"src",<br data-darkmode-color-16319416567473="rgb(171, 178, 191)" data-darkmode-original-color-16319416567473="#fff|rgb(0,0,0)|rgb(171, 178, 191)" data-darkmode-bgcolor-16319416567473="rgb(49, 54, 63)" data-darkmode-original-bgcolor-16319416567473="#fff|rgb(40, 44, 52)">    "automatic":true<br data-darkmode-color-16319416567473="rgb(171, 178, 191)" data-darkmode-original-color-16319416567473="#fff|rgb(0,0,0)|rgb(171, 178, 191)" data-darkmode-bgcolor-16319416567473="rgb(49, 54, 63)" data-darkmode-original-bgcolor-16319416567473="#fff|rgb(40, 44, 52)">}<br data-darkmode-color-16319416567473="rgb(171, 178, 191)" data-darkmode-original-color-16319416567473="#fff|rgb(0,0,0)|rgb(171, 178, 191)" data-darkmode-bgcolor-16319416567473="rgb(49, 54, 63)" data-darkmode-original-bgcolor-16319416567473="#fff|rgb(40, 44, 52)">
```

然后点击 OK。👇

![](https://mmbiz.qpic.cn/mmbiz_jpg/xGvHpjh4rNVmibUyfKiawZGTMoCnLRL3WocqjGh0OTaicm62TmOM3PcvShe28www7B8K1RD6YstXMbaoBsF2SjdRQ/640?wx_fmt=jpeg)

到此就成功将 Sci-Hub 配置为 PDF 解析器了，也就是说替代了默认的 Unpaywall。

现在，无需重启 Zotero，即可调用 Sci-Hub 免费下载文献了。

这里顺便提三点：

1.  在`"url":"https://sci-hub.se/{doi}"`中，建议使用`.se`，因为根据我搜集到的信息，只有`.se`支持 SSL 链接。（当然，由于 Sci-Hub 经常更换域名，保不准以后会用什么其他域名，因此此处的代码未来也会根据需要进行更新）
    
2.  从`"url":"https://sci-hub.se/{doi}"`还能看到一点。由于 Sci-Hub 是通过`doi`下载文献的，因此该 PDF 解析器也需要 doi。也就说你的文献必须要有 doi，如果 doi 是空缺的，便无法通过 PDF 解析器免费下载文献。幸运的是，对于缺失 doi 的文献，我们可以通过插件 zotero-shortdoi[4] 插件一键抓取 doi（参考文章 [zotero-shortdoi + Sci-Hub，让 99% 的文献都能被免费下载！](https://mp.weixin.qq.com/s?__biz=MzAxNzgyMDg0MQ==&mid=2650457478&idx=1&sn=86ec568804dddd33825966548ab0c7ad&scene=21#wechat_redirect)）。
    
3.  `"automatic":true`，如果设置为 true，Zotero 会自动下载保存到 Zotero 中的文献的 PDF。比如你用 Zotero Connector 保存了一些文献到 Zotero，它便会自动帮你从 Sci-Hub 下载文献，并附在相应文献条目下。如果你不需要自动下载，可以设置为`"automatic":false`。
    

使用方法前面介绍过，主要有两种：

#### 第一种：Zotero Connector

通过 Zotero Connector 保存的文献，会自动下载 PDF，无需任何操作。（看不到进度条，下载速度取决于网速）

#### 第二种：Find Available PDF

选中单篇或者多篇文献，手动点击右键菜单中的`Find Available PDF`，会弹出单独的窗口显示下载进度。同样，下载速度取决于网络速度。👇

![](https://mmbiz.qpic.cn/mmbiz_jpg/xGvHpjh4rNVmibUyfKiawZGTMoCnLRL3WoXeXag7FI54VfSnV5DSgl4mU2vnwONWXvUj8tStqmUojpydyQTUMe6Q/640?wx_fmt=jpeg)

关于 “下载速度取决于网络速度” 有下面两点需要注意；

*   如果你未开启任何网络加速器（比如梯 z），即正常使用网络，可以认为 Find Available PDF 的进度就是你手动从 Sci-Hub 下载文献的速度。大家应该都体验过，不开启加速器的情况下，Sci-Hub 的访问速度还是比较慢的，甚至有时候 PDF 加载不出来。
    
*   假如你开启了加速器，推荐使用全局代理模式，而不是 PAC 模式，因为两种情况下 Find Available PDF 的进度差异非常大，可以认为，使用全局代理模式几乎可以做到十几秒下一篇文献甚至更快。不过记住，下载完文献，切回到 PAC 模式，因为全局模式下 Zotero 无法同步文献到坚果云。
    

到此，本文就介绍完了！

可以看到，搭配 Sci-Hub 后，Zotero 变得更加完美了！这就是开源软件的魅力，它能带来无限的想象空间。

如果你在使用中有什么问题，欢迎留言讨论！

### 相关链接

[1]

SSL 连接: https://en.wikipedia.org/wiki/Transport_Layer_Security

[2]

Improved PDF retrieval with Unpaywall integration: https://www.zotero.org/blog/improved-pdf-retrieval-with-unpaywall-integration/

[3]

Custom PDF Resolvers: https://www.zotero.org/support/kb/custom_pdf_resolvers

[4]

zotero-shortdoi: https://github.com/bwiernik/zotero-shortdoi/releases

##### -[end]-

#### 关于青柠

* * *

【Slogan】让每个科研小白都有成为大神的潜力和实力【博主】浙江大学电子工程博士生国家奖学金获得者 / 剑桥大学交流生【付费社群】知识星球 + 微信交流群【免费社群】微信圈子 + [文献互助群](https://mp.weixin.qq.com/s?__biz=MzAxNzgyMDg0MQ==&mid=2650457065&idx=4&sn=353349cdc1eec57b46acb556306d3f9a&scene=21#wechat_redirect)

* * *

#### 往期精彩

[![](https://mmbiz.qpic.cn/mmbiz_png/xGvHpjh4rNWDvB17iaOA1CNM6SuK06o4OnsDLIbyVUwUae8rbJxNkdw2fnhd9gn54Kibe6hRrqBxlbxvE2s1lRaw/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MzAxNzgyMDg0MQ==&mid=2650456973&idx=3&sn=5d95338a8cf6a693d883e97e4887de9a&chksm=83d1de4bb4a6575d4a154cb55ef52f2048ba7e4a531c6600d41062965dbced75274a90d499f4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/xGvHpjh4rNW8yrzgP1d4fRt4S7ZKAOalIdQUyFjlxEkcEAFwgs7BLY9AotheP3hOVZHoIwVnjtAvhRxsLL0JTA/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MzAxNzgyMDg0MQ==&mid=2650457065&idx=2&sn=9823723c6c4eb7421510751ccb4acf75&chksm=83d1de2fb4a65739e3a5690c37e497223d101fb91907fc322150f34cb8e891dc489dc85a5b52&scene=21#wechat_redirect)