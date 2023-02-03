> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [dott.love](https://dott.love/writing/design-engineering)

> 无论是设计工具还是前端代码，都只是实现创意的工具。最终能够限制创意的，只有不够开放和好奇的大脑。

3768 字，预计阅读时长 10 分钟

最近在群里看到一个问题，设计师想学习前端，应该怎么入门？在设计圈，这是一个老生常谈的话题了。在过去的大半年，为了理解从完成的设计稿到实际交付给用户的产品之间还有哪些过程，我也试着学习了一些前端界面的编程。这段自学给我带来的收获绝对是超过预期的，亲身实践也让我对这个问题有了更深的体会。于是，在这篇文章里，我想就我目前的学习经历，结合自己阅读过的相关内容，来写一写这个话题。

首先摆出我的论点，如果你的职业目标是将设计作为手段以提升软件产品的易用性，而不仅仅满足于完成设计产出，那么，理解设计是如何被代码实现的，是必须掌握的能力。

任何设计都以其实现手段为边界。建筑设计无法脱离结构力学的限制，工业设计要尊重材料的特性，同样地，用户界面设计的创意发散也应该要以前端工程的能力储备为边界。我们经常在推特或者 Dribbble 上看到很多构思巧妙、视觉精美的设计，但其中有多少能够被付诸到产品实践？除了部分方案本身存在易用性的问题之外，很大一部分原因在于支持这些设计的实现需要过高的开发成本，既有的前端开发实践难以满足这些创意的需求，需要重新造轮子。这就是当设计创意突破了其实现手段时会遇到的问题。

再比如说，在 XR 设计领域，为何有趣的 demo 频出，但系统性的交互体验设计方案很少，其原因也是目前的 XR 开发缺乏约定俗成的规范和标准。所有的 XR 原型设计师都在用自己熟悉的工具定义自己心目中理想的交互形态，这样一个发散性探索的过程背后是没有用于实现界面的技术框架标准（类似前端中的 HTML、CSS 乃至 React 或 iOS 开发中的 UIKit 所起到的作用）作为支持的，无法锚定一个方向聚焦形成合力，也就无法将设计探索凝练成一套完整的交互方案。所以，理解实现设计的手段，可以让设计团队在发散创意的同时，不至于在互不相干甚至毫无希望的方向上狂奔。

理解设计实现能够让与你合作的工程师拥有更好的开发体验。设计文件的组织和设计交付的形式是需要为开发效率服务的。理解前端开发过程中设计稿是如何转化为代码的，能够让你在设计交付前更加审慎地看待自己的产出，而一些微小的设计习惯的改变就可能显著降低开发者的工作难度。比如，规范的设计系统和组件库能够让开发理解在产品设计中哪些要素是变化的哪些又是不变的，从而提升代码的可扩展性；在设计稿中给图层和组件命名可以帮开发解决变量命名这个难题；将设计稿中出现的组件术语与前端开发平台的标准统一可以避免概念混淆等等。

设计师对前端的理解能够提高设计方案落地的完整性。尽管 Figma 已经将设计交付的难度降低，但对设计稿理解最深的人肯定还是那个一点点完善每个像素的设计师本人。不同的前端工程师对于设计的敏感度不同，并不是每个人都拥有像素眼，这也许也不应该是对于前端工程师的要求。既然对设计实现效果的最终把控是由设计师进行的，那么为什么不让设计师自己来实现设计呢？

理想的开发流程应该由设计师自己来实现界面。在界面和组件由前端开发者架构好之后，直接让设计师上手开发工具进行界面和交互部分代码的开发，而让前端开发者专心实现好业务逻辑。因为有些设计细节如果不是设计者本人，哪怕是经验丰富的开发者也很难主动留意到。何况有些问题比如页面自适应也许几行代码就搞定了，而为了对接所做的设计稿和交互说明可能反而要花掉设计师更多时间。而当遇到设计实现的瓶颈时，懂代码的设计师也能够在开发阶段帮助产品在设计还原度和开发难度之间做出更好的权衡。通过设计师控制下的微小设计调整，用更低的开发成本实现不弱于原设计目标的效果。有些设计如果完全由开发实现，要么还原了效果但费了老大劲，要么让设计在不那么专业的品味下被阉割。

Alan Kay 曾说，"People who are really serious about software should make their own hardware." 要我说，真正在意设计的人也应该自己来实现设计。

除了以上的好处之外，代码也是一种非常高效和强大的原型制作工具，为设计师提供了许多设计工具没有的能力，提升了设计方案探索的自由度。尤其是在设计交互动效和处理响应式问题时，简单的几句代码就能实现在设计工具上调整老半天才能完成的效果。

在设计师开始学习前端之前，最重要的是明确自己学习的目标是什么，或者说想要学到何种程度。为什么这么说？

前端开发是一个非常庞大的专业领域，现代 web 前端技术已经发展到需要具有架构设计、API 设计、数据建模等后端编程能力的程度，随着前端开发职责的扩大，前端开发社区也正在经历着 [The Great Divide](https://css-tricks.com/the-great-divide/)，即擅长 Javascript 和擅长 HTML、CSS 的两类人群，前者更关注性能、架构、数据等问题，而后者更关注用户体验、界面外观、动画、可访问性等问题。即便在前端，也被分成了 “前端的前端” 和“前端的后端”。

我认为除非设计师已经做好了准备跨越职业的边界，选择成为一个专业的前端工程师，否则，最好的选择还是划出一条明确的学习界限。你可以选择学习 HTML、CSS 甚至使用 React 库来设计组件样式和动画，但当你的工作内容涉及到 Node.js、数据同步、状态管理、路由处理、API 请求时，明智的做法是将它们交给专业的前端工程师——起码在你对自己的能力足够自信之前。

因为这些内容已经超出了 “更好地探索和实现设计方案” 的意图范畴。[Karri](https://twitter.com/karrisaarinen/status/1572640094288486408) 有句评论我很喜欢，"Design is explorative, quick and dirty. Implementation needs to be solid and performant based on the app architecture. Mixing those two likely makes both worse." 简单来说，写界面代码 Yes，写逻辑代码 No。设计师写的代码很难满足生产环境下前端工程化的要求，往往充满了错误和漏洞，毕竟设计师并没有接受过专业的编程训练。

所以在开始学习之前，要清楚地知道在哪里停止，否则很容易被他人期望和自己能力的不匹配压垮。

一旦你决定开始学习，也清楚自己暂时不打算学哪些东西，接下来还会遇到新的挑战。

万事开头难。对于毫无编程经验的设计师来说，开始的阻力是最大的。这种阻力并不在于 HTML、CSS 和 Javascript 技术本身，而在于从了解这些技术到能够做出看得见摸得着的东西之间，还存在着语境转化的问题。也就是说，在熟悉编程语言的语法规则之前，你还需要了解编程是什么一回事。你需要理解数据类型、函数、条件控制、循环等程序概念，需要知道在哪里获取高质量的编程学习资料，遇到了程序问题如何搜索，如何使用 IDE 并提高工作效率，等等一系列的问题。这些问题一开始可能会非常劝退，而且除了硬着头皮上之外似乎也没有其他的好办法。

所以，对于开始学习编程的设计师来说，最重要的事情不是培养好的编码习惯，也不是扩大自己的技术视野，而是高频率地及时地获得正反馈来让自己有持续不断的动力和兴趣继续学习。毕竟，唯一阻止你学会一项新技能的原因就是中途放弃。

最好的方式就是 Learning by making。在学习基础概念的同时，直接上手写一点东西，哪怕只是一个示例教程中的小 demo。设计师获得反馈的方式其实很简单，做出一个能看到并且能用的界面，就能获得正反馈。从完成一个按钮，到完成一个卡片组件，再到完成一整个响应式的页面，甚至构建自己的个人博客。过程中不断地遇到问题、搜索问题、解决问题，你对前端的理解就会慢慢进步。

有没有一张学习路线图能告诉我要学哪些内容呢？当然……

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)前端开发路线图。https://roadmap.sh/frontend

…… 当然不是。这是对专业的前端工程师的要求，但这张路线图确实也提供了一个基本的学习框架，从中摘取部分内容来一点点地攻克更符合设计师的需求。

从控制网页结构的 HTML 和网页样式的 CSS 开始了解网页是如何在浏览器中被呈现的，再到使用基本的 Javascript 来控制页面的行为，然后学习 React.js 来设计具有样式和功能的组件，再到学习使用 Next.js 来简化网页构建中的繁琐流程。对于设计师来说，这是一条比较流行也比较轻松的学习路径。

在这里也推荐一些我学习的过程中觉得质量比较高的学习资料，基本上能够帮助对 web 编程零基础的人入门。当然，与编程相关的其他话题还需要从其他地方获取学习资料。

*   [MDN Web 技术指南](https://developer.mozilla.org/en-US/docs/Learn)。在遇到不理解的概念时，可以用来作为检索的文档来参考。
*   [现代 JavaScript 教程](https://zh.javascript.info/)。对 Javascript 的基本语法有比较深入的讲解。
*   [React 中文入门教程](https://zh-hans.reactjs.org/tutorial/tutorial.html)。通过一个简单的例子，帮助你了解 React 的基本概念。
*   [React Docs Beta](https://beta.reactjs.org/)。最新出的更加丰富和清晰的 React 教程。
*   [Next.js 学习指南](https://nextjs.org/learn/foundations/about-nextjs)。Next.js 的入门教程，其中的基础部分对于理解从 Javascript 到 React 再到 Next.js 的过程也很有帮助。

对于设计师来说，掌握了基本的 web 编程能力之后，最关心的话题自然还是样式。[TailwindCSS](https://tailwindcss.com/) 会成为加速你学习的好帮手。这种将样式与组件结构一起编写的方式非常符合设计师的思维，除了能够提升编写 CSS 的效率之外，对于理解 CSS 本身和了解网页设计中会遇到的响应式、暗黑模式、交互状态等各种主题也很有帮助。

比如，当使用 hover:、focus:、active:、disabled: 时，就能理解为什么设计稿要设计那么多不同的状态；当使用 transition、duration 和 ease 时，就能理解设计稿中的动画应该如何处理才能更好地被开发还原，以及为什么 Figma 的原型制作功能会这样设计。这也是之前所提到的，了解设计的实现手段的过程。

不过 Tailwind 也不是万能的，但我建议忽略那些吐槽其适用性的评论，而是首先上手。因为有很大可能这些技术目前所遇到的瓶颈在你的学习期间不会遇到，而且也会在技术未来的迭代中得到解决。世上本就没有完美的技术，当下来看，它们已经是在学习成本和能力上限之间平衡得比较好的技术了。这些技术降低了编程门槛，自然也是最适合设计师学习的。

此外，当谈论设计师所需要学习的前端能力时，我更愿意将其理解为广义上的用户面对的前端界面（包括网页、桌面客户端、移动端等人机交互界面），而不仅仅是 web 前端。所以，除了 web 界面编程的能力外，我也十分建议设计师多了解移动端的前端界面是如何被实现的，尤其是 iOS。在这方面，SwiftUI 是非常适合设计师学习的技术，在此就不赘述了。

在学习到一定的阶段时，你可能会不可避免地触碰到此前所说的前端工程师和会前端的设计师之间的边界。你当然可以选择继续学习，不过，如果是想围绕设计来打造自己的核心技能树的话，也许可以暂时放一放，试着使用自己的编程能力在设计和开发的衔接上做出更大的突破。

比如，试着自己实现设计原型，探索交互动效，crafting 那些在工程师看来吹毛求疵的细节。或者，找到一份 Design Engineer 或者 UX Engineer 的工作，作为设计团队和前端团队的连接者，用双方都能理解的语言来平滑彼此的沟通门槛，从而打造出设计质量更高的产品。

最后我想说，无论是设计工具还是前端代码，都只是实现创意的工具。最终能够限制创意的，只有不够开放和好奇的大脑。

以上。

参考资料：

*   [Contributing to a great developer experience (DX) as a designer](https://uxdesign.cc/contributing-great-developer-experience-designer-e1f497b0fb4)
*   [UI Design vs Front-End Development: The Critical Difference](https://uxplanet.org/ui-design-vs-front-end-development-the-critical-difference-5a4c404a9d91)
*   [Frontend Design, React, and a Bridge over the Great Divide](https://bradfrost.com/blog/post/frontend-design-react-and-a-bridge-over-the-great-divide/)
*   [The Great Divide - Two front-end developers are sitting at a bar. They have nothing to talk about.](https://css-tricks.com/the-great-divide/)
*   [现代 Web 开发的现状与未来](https://zhuanlan.zhihu.com/p/88616149)
*   [Rauno Freiberg - ui.land Interview](https://ui.land/interviews/rauno-freiberg)
*   [Paco Coursey - ui.land Interview](https://ui.land/interviews/paco-coursey)