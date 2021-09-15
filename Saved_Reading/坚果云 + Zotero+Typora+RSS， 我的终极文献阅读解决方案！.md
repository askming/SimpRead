> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [mp.weixin.qq.com](https://mp.weixin.qq.com/s/Q2uYIpMl_3yx6dhr5KpsuQ)

作者：CLOUDU， 一名不学无术喜欢折腾到底的感性工科男，**希望有一天能够通过自己设计的硬件和代码搭建一套完全属于自己的生态体系**，热爱工作更热爱生活！

如果你想直观的体验 Zotero 的便捷之处，我在第四部分通过一次调研的实际体验来直观说明 Zotero 的强大之处，之所以放在文章末尾是为了结合前三部分的内容，请您耐心观看。

**文末有福利~**  

**Abstract：**
-------------

1、本文介绍了如何使用 Zotero ，**实现使用坚果云 WebDAV 进行多端同步、文献 PDF 重命名、三种快捷导入文献的方式等功能**，在最后我将通过最近一次调研的实际体验来说明 Zotero 的强大之处。

2、本文介绍了如何在 Zotero 里面使用 RSS 订阅，实现对于重点期刊的追踪，并通过 DOI 插件实现文献的一键下载。

3、本文介绍了如何使用 Typora 制作文献笔记（Markdown），并借助已经设置好的坚果云中的 WebDAV 功能，在 Zotero 里实现文献和文献笔记的平行储存。

**1.** **Zotero**
-----------------

不做多余的解释，只需要知道 Zotero 的几个特点：  

![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVglljTBT59yDykXYj9aEfV8icOMWl8iaA3AKCFLaIicr58TKVY8ESzxfSTA/640?wx_fmt=png)

前 Mendeley 用户，即便是科学上网也无法拯救其同步问题，而且其对于中文文献的识别简直让人血压升高，对于只读英文而且不喜欢折腾的同学来说应该很友好。

另外，3 月 15 日，Mendeley 宣布在 App Store 和 Google Play 里面下架移动端产品。这也是转向 Zotero 的原因之一。

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgibq8emIr0cgVJM8sUhTFt2X3P7wKowaHB9nnljQMs7q0RK5AM5yRvVQ/640?wx_fmt=jpeg)

Mendeley 对于移动端的声明（2021 年 3 月 4 日)

### **1.1 WebDAV**

如果你是一名科研工作者，你大概率会拥有两台以上的电脑（实验室 + 个人电脑），如果有办法能够备份自己的科研文件，而且实现在不同终端访问自己的文件，甚至实时同步文件，那一定是一个很棒的体验。

如果你很有钱，不妨搭建一台自己的服务器。如果你不想费工夫而且资金比较充裕，那我强烈推荐坚果云的付费版，199 元，42G 空间。如果你只想使用本文所提的 WebDAV，那就坚果云免费版，每月上传 1G，下载 3G。

对于 Zotero 的设置流程，坚果云给出了两种解决方案，参考以下说明文档：

[坚果云使用 Zotero 配置过程详解](http://mp.weixin.qq.com/s?__biz=MzA5MTQ4Nzc5MQ==&mid=2247486316&idx=3&sn=7493307e997288a2d62414e077c8b576&chksm=907ae02ca70d693a4db146feb7028832825d16c1d03f7ba644baa943343ab0c548402c67e5df&scene=21#wechat_redirect)

**去试试 WebDAV，相信我，你会爱上这种感觉的：**

> 试想这样的场景：为了明天早上的组会，你今天按照最近阅读的几篇文献做了一天的 PPT，桌面上放了一大堆乱七八糟的素材，而此时你听到了看楼大爷赶人的吆喝声。你保存了文件并关上了实验室的电脑，回到宿舍打开了自己的电脑，今天所有的工作都自动同步在了桌面上，于是你快速的完成了最终版 PPT 的制作。第二天早上在走往课题室的路上，师兄突然让你把 PPT 提前发给老师，你没有着急跑向实验室，而是拿起了手机找到文件分享给了老师。等到你来到课题室，打开电脑连接上投影仪，所有的文件就都已经同步在了桌面上。

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgfD7R0w5aFjibevo9jvZJ4UsadpBAyrdkQcHKTroqUBH0ICbmy2CZbOg/640?wx_fmt=jpeg)

Zotero WebDAV 设置界面

### **1.2 PDF 重命名**

使用过 Google Scholars 的同学都知道，下载下来的文献都是奇奇怪怪的名字的，虽然使用了 Zotero 可以实现文献管理，但是如果老师或者师兄向你要文件的时候，发过去没有命好名的文件并不合适。

**文献的重命名是通过 ZotFile 实现的，插件的安装方法如下：**

（1）访问插件库——找到 ZotFile 的网址——Download

（2）打开 Zotero——工具——插件——右上角齿轮——Install Add-on Form Files

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVg6icWJEFTKl26w1IlzCyAdBzNUnaTvzraib6ytj8vib2erVnUnn8nGrFow/640?wx_fmt=jpeg)

插件安装方式（文件安装)

（3）安装成功——重启 Zotero  

随后按照自己喜欢的命名方式修改规则：工具——ZotFile Preferences——Renaming Rules

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgXGzXzrtEw5RibNboWO5XcX5DEInGoIcia5rUsm8p8y5AkLSryA1v26Kw/640?wx_fmt=jpeg)

ZotFile Renaming Rules

*   导入文献后，如果识别成功（或者直接通过插件导入文献），是自动重命名的，当然你也可以右击项目——Manage Attachments——Rename Attachments
    
*   附件是可以直接从 Zotero 里面拖到资源管理器中的，当然也可以直接拖到微信和邮件中。
    

### **1.3 中文文献的直接识别**

众所周知，真正的学术大佬是基本不看中文文献的。但是对于学术小白，学位论文和国内的文献实在是不可或缺。

虽然 Zotero 对于中文文献的识别已经不错了，但是仍然存在问题，所以推荐使用 Jasminum（茉莉花）这个插件。

他还能实现对于中文名字的姓名的拆分，很强大：王晓丽——> 王，晓丽

![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgR68nEh5ewJGkBiaicbZ7RC2Vrfic2SLNxFLOqO9PrjOZYvLuXn8YXnnTA/640?wx_fmt=png)

拆分姓名的菜单

### **1.4 文献导入**

Zotero 只是一个工具，由于文献下载权限的原因，他不是完全不需要手动的，但是其涵盖了基本上所有的文献资源库的 Translator，能够很好的实现下载。

（1）剪贴板 / DOI 导入

如果你复制了文献的 bib 信息，那么可以选择文件——从剪切板导入：

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgYAm2k2KW2NibPVbqqVEgnEWTBQQFw7NFyVViamTX2n0xw9Qk4xl6jRiaw/640?wx_fmt=jpeg)

从剪切板导入的菜单  

如果你有文献的 DOI、ISBN 等信息，可以使用这个小功能导入：

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgqMDQZn8pvlHhdHyU27ibcFcQyncQTOVol3slpsaD0NGjeichib3rU83yg/640?wx_fmt=jpeg)

DOI 等导入的小按钮

当然这样导入之后只是导入了项目，并没有下载文献。**在得知 DOI 号之后，Zotero 可以实现自动搜寻文献并下载**，DOI 号的获取可以通过插件 ShortDOI 完成，PDF 的下载可以通过修改配置文件，在 SCI-HUB 上完成。具体教程参考：[_https://zhuanlan.zhihu.com/p/262248970_](https://zhuanlan.zhihu.com/p/262248970)

（2）Zotero Connector 导入

安装好 Zotero Connector 插件，它会自动识别你的浏览器：

他对 Google Scholar 支持很友好，如果你在泛读文献，那么检索好关键词，通过插件选取好你想要添加的文献，就去喝杯咖啡吧。

![](https://mmbiz.qpic.cn/mmbiz_gif/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVglPQxYqxBUwqcH48GSXX7p16FZMcibEJUiaNtmPMicFZuF2CVKbdmapfdw/640?wx_fmt=gif)

Google Scholar 文献下载  

**📌注意：**Connector 插件的使用是和 Zotero 相关的，你 Zotero 打开哪个文件夹，他就添加到哪里去，而且单个文献下载他是不会出现复选窗口的，直接开始添加，所以为了避免添加错文件夹，Zotero 里面应该要提前打开好文件夹

Connector 对知网也是友好的，但是需要更改一下 Translator 的 js 文件，详细教程参考 @青柠学术的文章：[Zotero Connector 支持中国知网「期刊和硕博论文」PDF 直接下载了！](http://mp.weixin.qq.com/s?__biz=MzAxNzgyMDg0MQ==&mid=2650456725&idx=1&sn=2f6e6fb3036933dfd71fde74556aded5&chksm=83d1df53b4a656456fb129c8a56ad80d819005d94e9cc9ac689387093100b067aa1dbcde63a2&scene=21#wechat_redirect)

或者如果你嫌麻烦也可试一下这个油猴的插件。学位论文也是可以直接通过插件下载 PDF 的，再也不用折腾到海外版和英文版了。

![](https://mmbiz.qpic.cn/mmbiz_gif/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgWCJfj3wVbcHVQxb4hYyavYJich15dBhD2Yp0ia3f4h3NAwDjiaYHE3BSA/640?wx_fmt=gif)

知网 Zotero 文献下载

**2.** **通过 Zotero 实现文献的 RSS 订阅**
---------------------------------

### **2.1 基本原理**  

用我的理解来简单讲一下 RSS 订阅的基本原理：

> 李大爷、王大爷等等很多大爷种了很多很多不同种类的萝卜，这些大爷每天都会把各种各样的萝卜摆在很长很长的货摊上向外出售，而小白兔天天要去李大爷家买萝卜回家吃——科研工作者每天都要去他关注的网站检索需要的信息。终于有一天小白兔觉得这样太麻烦了，他想能够方便的吃到自己喜欢的萝卜，于是它跟每个大爷都说了一下自己喜欢吃的萝卜类型，大爷们每天早上都会让一个小狗子打包小白兔喜欢的萝卜，送到小白兔的家里。——通过兴趣点／关键词／关注作者／关注话题进行信息传递的邮箱订阅方式。后来小白兔发现，大爷们尝试的新品种萝卜总是尝不到，这让小白兔无法更新自己的口味，也就意味着它可能很难吃到可能感兴趣的萝卜品种。于是，他跟大爷说不要让小狗子送萝卜了，让狗子记录好你们今天的售卖的品种，如果我感兴趣，我再来摊位上取——基于 RSS 订阅的 “萝卜” 跟踪方式。

已经尽可能形象生动了，我想读者应该能懂他们之间的差别。

### **2.2 添加订阅方法**

Zotero RSS 订阅的方法：新建文件库——新建订阅——来自 URL——输入

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgV3GJaAzufZ5pXTnrjQFXUjqXPCaRB0y8hQ0c5RPgp74MUN0p74Srtg/640?wx_fmt=jpeg)

添加 RSS 的方法

### **2.3 RSS 地址的获取方式**

（1）中文期刊

大部分期刊都有 RSS 订阅，但是实测并不靠谱。通过 [CNKI 的出版来源导航](http://kns.chkd.cnki.net/knavi)，你可以获取绝大部分中文期刊的 RSS 订阅地址：

搜索期刊——点击进入——找到按钮——弹出新网页——复制新网页地址——添加 URL  

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVggDicmoJF024m4RDSEllV39eiap29bbV3f0aXrhSIQ14fqcaTD1kdc0fg/640?wx_fmt=jpeg)

RSS 小按钮位置

![](https://mmbiz.qpic.cn/mmbiz_gif/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgW8qqvWv8pc23V5KVVQh8WFfyEiaOR0ClU8KtBica1H28WCcWXlsXXLiaQ/640?wx_fmt=gif)

添加《航空学报》的 RSS 订阅流程  

（2）英文期刊的 RSS 地址

英文的大概就只能一个一个去搜索了，以 Nature 为例，非常明显：[_Nature RSS 地址_](http://feeds.nature.com/nature/rss/current)，Nature 官网上 RSS Feed 的位置，然后正常添加就 OK 了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVg8gD0mNblaACuq7J4fhrBsFTOnC2A3Q2ibELp3zKxAn6phj6lHpldiaUw/640?wx_fmt=jpeg)

强烈建议按照类别通过数字进行分类，不然肯定会乱！（我就简单区分中英文和推送）

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgx946ic6Zd942dm2fJdmSiaWCZIGOZUCjTmw9QrsTLOKgMn5KFcqKEwIg/640?wx_fmt=jpeg)

我的 RSS 订阅列表

是不是可以优雅地关注你喜欢期刊的动态了呢？

**3. 通过坚果云 WebDAV 实现文献和 Markdown 笔记的同源同步**
------------------------------------------

这个标题很难描述我的意思，通过工作流来解释一下：  

> 使用 Typora 编辑器，使用 Markdown 语言记下所读文献的笔记，相关图片通过阿里云 OSS 进行在线储存，保存后的. md 文件直接拖到 Zotero 相关文献里面，保证文献文件和笔记文件同源。

如果你没用过 Markdown，你肯定觉得我在没事找事，所以我简单介绍一下 Markdown

> 逻辑很像 LATEX，通过字符对格式进行规定，但是没有 LATEX 那么变态，上手难度几乎等于零，但是支持 LATEX 的公式语法。你不需要管缩进，不需要管页边距，不需要管任何格式问题，他就是纯粹的文本编辑器，配合上实时渲染的 Typora，你能更大程度专注于文字本身（天下苦 OneNote 已久） 例子：加粗就这样写：** 你好 ** 一级标题就这样写：**# 你好 ** 多级列表就这样写：**- 你好 **

**这样做的优点在哪里？**

*   你无需打开两个存储位置或者服务器完全不相同的软件对应文献和笔记。
    
*   除非你手贱自己删掉文件，否则文件和笔记永远被 Zotero 的 WebDAV 保存的好好的。
    
*   如果你不喜欢 Markdown 你也可以用 Word 甚至把你的程序拖进去。
    

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgSTwZWSLApqvyiaaicLxa3XibUzbgmjqddPGFUxbaNfKQytJWkAuq75cbA/640?wx_fmt=jpeg)

文献项目下的文件

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgnHsaaKF0jYboBgibbN0mJzS0RsymX6TPl04OQqnnIBalibvAxUkRBymw/640?wx_fmt=jpeg)  

Typora 的颜值完全吸引了我，另外对于一个不学无术的研究僧来说，Typora 支持实时的 LATAX 渲染也是我选择他的原因之一。

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgtxIt4JyI0DlDITbowsoFkKA5fsamVEfZ9qgibEpkrfia5D8Dia36VsPgw/640?wx_fmt=jpeg)

### **3.1 Markdown 的图片保存问题  
**

但是对于 Markdown 而言，最难解决的问题其实是图片保存，因为 Markdown 终究是个文本编辑器，他的图片只能保存成单独的附件，然后通过在文中引用进行显示。为了解决这个烦人的问题，有两种解决方案：（1）通过配置图床和 PicGo 进行图片的上传。（2）使用坚果云的 Markdown 应用进行图片保存。

### 3.1.1 通过阿里云 OSS 自建图床进行图片的上传

是通过 Typora 里面 “添加图片就自动上传并转换成云图片” 的方式，自己开通了阿里云的 OSS。值得注意的小坑是，此种方法需要花一点小钱，而且通过图床管理图片其实并不简单，因为你无法得知你的图片到底在哪里。

懒癌同学，我其实更建议使用一下坚果云的 Markdown 应用进行编辑

### 3.1.2 使用坚果云 Markdown 进行编辑

在坚果云 Markdown 编辑器中，图片可以自行上传至 markdown 文件所在的文件夹，不需要再次手动设置图床等

![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVg6IaDuHTGdd9rr9XoIWcbibc0zovNbxsHInZzgKW3KgHVZER0zjxG9QQ/640?wx_fmt=png)

3.2 依赖 Zotero 在使用坚果云 WebDAV 的特性进行 Markdown 笔记的存储
------------------------------------------------

但是有人问了：你的意思是，我的笔记文件要拖着一堆图片文件？万一搞丢了那岂不是白瞎啦？

莫要着急，如果我们打开 Zotero 存储文件夹就会发现，Zotero 的存储是每一个条目下的附件都独立存在一个文件夹，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVg8wvZUNP68R9NDuHs9GaAmn4OsXoFyDibQmSsSLmUtTVBl9iaIyiaxmx1A/640?wx_fmt=png)

在坚果云中的 WebDAV 也是按照这种命名规律进行存储的，只不过坚果云的文件都进行了压缩，全部解压之后就是存储文件夹。

![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVg1IqhIm2WCwgYBt5ThY4uJSQcBOgB1SZpTZA07ZQM7GQbgRUWricGVXw/640?wx_fmt=png)

也就意味着，不管我怎么更改文件，Markdown 的笔记文件和图片文件始终都是同源的。  

既然如此，设置 Typora 图片文件存储在笔记文件目录下或直接使用坚果云进行编辑即可保证 Markdown 的图片管理。

**4. 通过一个调研实例来体现整个工作流**
-----------------------

> 前提说明：为了走一遍工作流，前后内容可能会出现不符的地方，敬请谅解。

此部分的大概流程：通过 RSS 订阅的期刊发现热点——通过 Zotero Connector 下载文献至 Zotero 文献库中——后台通过坚果云 WebDAV 同步文献——通过 Typora / 坚果云 Markdown 整理文献笔记——通过坚果云分享功能将文献传递给他人

### **4.1 通过 RSS 订阅的期刊发现热点**

> 小肚某天来到课题室，打开电脑准备开始一天的工作，习惯性地，他首先打开了 Zotero，选中了自己一直关注的顶刊 RSS 订阅，开始从上往下看看有没有自己关注的文章。

Zotero——RSS 订阅——定位感兴趣的期刊——双击进入网站

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgB8m6G9icm82nO4cJKSDNUdNGq2EojL0ygzQ2zCKYSqQteUS3qqzB3mw/640?wx_fmt=jpeg)

闲来无事翻翻 RSS  

### **4.2 通过 Zotero Connector 下载文献至 Zotero 文献库中**

> 小肚意识到自己咖啡还没冲，于是他点击了 Zotero Connector 插件，就去泡咖啡了

在 Zotero 打开自己希望保存的文件夹——点击 Zotero Connector 插件的图标——等待

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVg1icmeEL3VLGb6ne6Q0c9uV2rFu3vl1ib4OOYfSH6O09YFiaFqeBlI0zKQ/640?wx_fmt=jpeg)

悠哉游哉自动下载文献  

### **4.3 后台通过坚果云 WebDAV 同步文献**

> 小肚跑完咖啡后回到工位，在 Zotero 找到刚下好的文献，双击打开了文献

Zotero 自动化完成了条目的创建 + 文献 PDF 文件的自动重命名 + 下载文献网页的快照（双击快照可快速回到下载文件的源网站）+DOI 等关键信息的添加。

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgfdN2oMQAoLkylmbianU4SD0yY3r6Btdtr4QLP1fxoKOd9MHiaEGGibfcg/640?wx_fmt=jpeg)

下载完成后，Zotero 会立马使用 WebDAV 进行文献的同步，手机端的 Zoo for Zotero 就能立马同步啦。

![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgVJhibpVP4fBh3uRAhln89p33pRV5icwJMaVRhZR0ic1B5NvuPRyrF1d4g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVg6LQibVUobJC1lkR8HvZ7qNXaVAdUCa4P7OWeZPdhzo7Z40rdbIk9Lew/640?wx_fmt=jpeg)

这样就能随时拿手机看文献了（并不会）

### **4.4 通过 Typora / 坚果云 Markdown 整理文献笔记**

> 小肚打开了 Typora 软件，将条目中的文件名复制过去创建了一级标题，随后使用 Markdown 记录了笔记

Markdown 的语言真的可以让人忘掉恶心的缩进和行间距

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgab9alodxlra730K7umkTTgAuZhq5yZdR9Y31FuqKlpFzXBw0icoOVtA/640?wx_fmt=jpeg)

保存文件后，直接将. md 文件和文件夹拖入 Zotero 中，或者一开始就可以在条目下新建文件。（应注意，如果在 Zotero 外创建 md 文件之后添加了图片，别忘了把图片文件夹也一起拖入笔记的根目录中）

### **4.5 通过坚果云分享功能将文献传递给他人**

> 小肚通过研究文献，确定了三个研究方向，于是他下载了很多的文献，通过 Zotero 对文献进行整理，最后形成了一个 Word 版本的报告，发给老师。

下载文献的步骤不再重复：

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVg1M8ZpibC0eXHbcSCMfnjMxItjibdnsCbsvPqbB46gNrbpnicLKfRHZjvw/640?wx_fmt=jpeg)

通过选中多个文献，可以生成文献的报告（html），带有 URL，界面也比较简洁。

![](https://mmbiz.qpic.cn/mmbiz_jpg/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgKgqmPaPBLl2krFCX2SCHQfpO3tQsiaeegBoosHqm82THk8J38Ae1LIg/640?wx_fmt=jpeg)

有时候我们存储的不一定是文献，可能是很大的行业报告，受限于某绿色通讯软件传输文件的大小限制，通过坚果云分享文件是一个非常方便的方法，甚至你可以在 PPT 中添加一个文件分享的二维码，方便听汇报的人查阅。  

![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgsXsmjxgFCvzxfRcwibSBdaTicIcH0sV9G2YlawyAs3VNs5eqMFyz5JQg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgFpyYJ5JfojHQqVV61mxo581RMeJZuXrbKMic9kLbicSoomJSJtf2Q5Ag/640?wx_fmt=png)

而且坚果云的链接下载是可以不需要注册的，另外不会强制要求下载客户端，通过浏览器自带的下载工具就能实现下载，非常银杏化～

至此，完成整个流程。

![](https://mmbiz.qpic.cn/mmbiz_png/voBb9QGGTa1VlLsnMnOwBwHInPLkOT9G4xFAL1XlgXqgauxolmmt45qfPicZPhgpIP1AThc6EO3eXNVURDkvwBw/640?wx_fmt=png)

**晒出使用心得，拿坚果云会员**

如果你也像本文作者一样，使用坚果云解决学习、生活、工作中的某个问题，欢迎您将解决方法、使用心得发送给我们。  

不需要华丽的辞藻，真实即可；不限形式，图文、视频、条漫都行。

**一经采纳，我们将为您提供价值 199 元的坚果云个人专业版会员 1 年**

同时，我们将在微信公众号、知乎、抖音等各个渠道发布文章，让你的宝贵经验能帮助有相同困扰和需求的人。

点击这里 👉[_晒出使用心得，拿坚果云会员_](https://workspace.jianguoyun.com/inbox/collect/7c7744b812c241c086f4fd07d6f2370c/submit)，或者长按识别下方二维码即可投稿：  

![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJCsJaCgCMgiaPFtkxsLRPCVgbxpKVib5iciae2sYI5RBsr5k79IrRbrqPlHxE2j5PdwZiahPNy8Ht5UILQ/640?wx_fmt=png)

● 往 期 热 文  ●

[![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJChaibZGuFV3V4JPLU0I5Wibd6zrfyAxgRKDYavibiarr72cTlaOUiazG9c5EwgEsSvibzAzQmlHZsv36sQ/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzA5MTQ4Nzc5MQ==&mid=2247487145&idx=1&sn=d86a85318013d120790a8ddd36ea0bed&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJDB1qChzYAqicib9499MVwxYm4uU3aX3aSnU7jfwYZDbuRXX9WBic3XPffxh1KRtIpAKIlryqS5uHhng/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MzA5MTQ4Nzc5MQ==&mid=2247487177&idx=1&sn=be1eba2ab62ff0ac8f6b6e92dd2349ad&chksm=907ae589a70d6c9fd5f14a2ecab97b5b3cf54c41fac934a63905a6b0cfc01a013aa06173a02d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/lMtpCgQnkJBWQ9oGdiaBC2P8uSeuhGUia6mic0tKHj40hfhxNkZGo7vOT391cDLrQLWC8YoRHFEqpruhssILNxztw/640?wx_fmt=png)