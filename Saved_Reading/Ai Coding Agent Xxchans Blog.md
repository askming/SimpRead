---
saved_date: 2025-12-22T19:28:39.833Z
title: "我对各种 AI Coding Agent 工具的看法 · xxchan's blog"
tags: [Productivity, Technology]
---

# Ai Coding Agent Xxchans Blog

# 我对各种 AI Coding Agent 工具的看法

 
 Jun 8, 2025  · AI Agent   

  Translations: 
-  [English](/blog/2025-06-10-ai-coding-en/) 

   
Agentic coding 或许是当下最火（最卷）的方向，一万家公司在做。并且隔三差五就在社交媒体上看到又有什么新工具、谁家又出什么新功能了（又 blow 谁的 mind 了，又颠覆谁谁了）。这还挺让人困惑的，我发现很多人会问 “这些 AI coding 工具真有那么牛吗？”，或者 “XX 和 YY 到底有啥区别”。不少人自己试用了一下，感觉不过如此，于是迅速下头。同时，我还发现还有不少程序员连 **Cursor** 都没用过。

 
我平时很喜欢把玩各种 agentic coding tool，因此忍不住想锐评一番。这个领域无疑充满了大量的 hype，但仔细看，还是能分辨出不同产品间的差异，甚至整个行业的发展方向。

 
Agent 能做什么不能做什么，以及如何用好它，这里面有很多**“手艺”**的成分。所以这事儿很难解释清楚，了解它们的最好方式还是得自己上手试。看再多别人的使用感受，都不如自己玩一把来得真切（但我还是忍不住想讲讲我的看法）。这篇文章，就是试图把我关于各种 AI coding 工具那些零散的观察和思考，整理成一篇比较长的文字。

 
## 一些背景

 
总的来说，我很相信 “agent coding 能成” 这个未来。具体点说，我相信未来 AI agent 可以独立在一个大型项目中，端到端地完成复杂的开发任务（加功能、修 bug、重构）。

 
首先交代一下，我主要的工作是写开源流数据库 [RisingWave](https://github.com/risingwavelabs/risingwave)，一个超过 60 万行代码的 Rust 项目，还算比较复杂。虽然一些上下文明确的小活儿，我已经习惯了让 AI 来干，但说实话，我暂时还没有大规模、严肃地用 AI coding 去做那些真正困难的开发任务。同时，我也没仔细想过未来模型的能力边界，以及实现 agent 的具体技术难点在哪。所以，这篇文章主要基于我的直觉，是对各个工具的感性分析。另外也不是一篇教你怎么用、怎么选的攻略。

 
不过给自己找补一下，我感觉之所以不敢大规模尝试，还是有原因的，主要还是**“穷人思维”**在作祟：Agent 还是太贵了！一个任务跑下来，随随便便就是 5 到 10 刀。这里可能存在一个杰文斯悖论：如果它变得更便宜，我反而会用得更多，最后花掉更多的钱……另外现在工具太多了，而要真正用出差异，可能得花上一周以上的时间去深度体验，但订阅和切换的成本又让人望而却步。

 
下面开始正题。我们先按工具逐一分析，最后再聊些更宏观的话题。

 
## 具体产品分析

 
### **Cursor**：野心勃勃的领跑者

 
**Cursor** 现在毋庸置疑是 AI Code Editor 这个赛道的老大哥。

 
#### 0.50/1.0 版本里藏着的线索

 
说起来，我动笔写这个，很大一个 trigger 是看了 [cursor 0.50 的 changelog](https://www.cursor.com/changelog/0-50)（然而拖到今天他们 [1.0](https://www.cursor.com/changelog/1-0) 都发了……），里面透露了很多有意思的点，有点暗示未来方向的意味：

 
-  
**Simpler, unified pricing** Cursor 之前的定价模式有点臭名昭著，它引入了一个定义模糊的“fast request”，不同模型还对应不同的数量。新版统一成了“Requests”（其实也没太大区别）。更重要的是很多人觉得一个月 20 刀很贵，我倒认为这一定价太低了，他们很可能在亏钱。按 request 计费本身就不太合理，尤其在 agent 时代，一个请求可能跑很久、烧很多 token。当然，这也可能是种**“健身房模式”**，让用量少或短对话的用户，来平衡高用量用户的成本。但另一个不合理之处在于，这会驱使它去优化 token 成本（比如压缩上下文），而用户想要的却是最大化的效果。

 
-  
**Max mode** 按照官方说法，“It’s ideal for your hardest problems”。在我看来，这有点吹牛。我的理解是，Max mode 就是不再精细化管理上下文，同时上了 token-based billing。在过去，模型长上下文能力不强时，精细控制或许能省钱且效果好（因为模型会被无效信息误导）。但现在模型能力提升太快，这种控制反而成了负优化。有趣的是，像 Roo Code 这样的开源 BYOK 方案，一直宣传的就是“Include full context for max performance”。所以 Cursor 这波操作，有点像开倒车，或者说是早期的优化成了现在的技术债。他们那句“If you’ve used any CLI-based coding tool, Max mode will feel like that - but right in Cursor”给人的感觉更微妙了。既然我可以用 CLI-based agent，为什么还要在 Cursor 里用一个要额外收 20% margin 的版本呢？

 
-  
**Fast edits for long files with Agent:** 这也是个有点像开倒车的改动。它给我的感觉是，开始使用基于文本的方法来直接应用大模型的输出。Cursor 之前一直吹嘘自己的 apply model，这事儿可能做得太早了。以前模型不够准，需要复杂的 apply 逻辑；以后模型越来越强，这种复杂性可能就没那么必要了。

 
-  
**Background Agent & BugBot** 总的来说 “Agent mode” 顶多算是辅助驾驶，真正的 Agent 是你能以更轻松的方式给他派活。Background Agent 是你派个活就不用管了，BugBot 是自动 code review。后面必定还会出例如在 GitHub 上 assign 个 issue 就开始干活了之类的功能，成为一个全能的合格牛马。

 
这个信号非常明确：**Cursor 要和 Devin 硬碰硬了**。这是个非常自然的方向，用过 Cursor agent mode 的人，很可能都想过能不能让它同时干两件事。在本地做这个有难度，放到云端就顺理成章了。

 
**Cursor vs Devin**，有点像**特斯拉 vs Waymo**。后者一开始就直接做终极目标自动驾驶，前者则是发展成熟、用户规模大了以后逐渐转向更自动的方向。这条路的好处是用户期待会低一点，坏了可以自己动手改。依赖现有的其他做的好的体验还可以继续保持一定的用户黏性。相比之下，Devin 如果一开始的体验不及预期，用户很可能就流失了。（当然，对 pro user 来说，在本地 checkout 修改不是难事，但 Cursor 有大量相对小白的用户，为他们提供简单的 UIUX 也是一个点。）

 
-  
还有一些 1.0 的小改进

 
- 支持了 memory：我认为同样是所有 ai agent 的必备功能。
- Richer Chat responses：支持了 mermaid，以及 markdown table 渲染。说明 chat 体验还是有东西卷的（提升一点用户粘性）
- 但总的来说 1.0 主要感觉是 marketing 为主的一个版本，并没有什么质变（相比之下 0.50 倒是更震惊我一点）

 

 
与 Cursor 的激进大动作相应的则是 [Anysphere, which makes Cursor, has reportedly raised 900Mat900M at 900Mat9B valuation](https://techcrunch.com/2025/05/04/cursor-is-reportedly-raising-funds-at-9-billion-valuation-from-thrive-a16z-and-accel/)。对应 OpenAI 想要收购 windsurf 的新闻，可见 Cursor 急切的想要一统江湖的野心。融了这么多钱，我猜他们下一步很可能就是训练自己的模型。除此以外，它也完全有可能会收购市场上的其他玩家，成为一个整合者的角色。

 
#### 回过头来说，Cursor 到底好在哪？

 
其实我当初（2024/05）用 cursor 完全是为了它惊艳的 **TAB 功能**。在早期我几乎不用 AI chat，甚至能忍着很多非常影响体验的 editor bug 还要用。 相比 GitHub Copilot 的“append only”补全，想修改就得删了重来；Cursor 的生成“Edit”，帮你修改代码，显然是更“正确”的形态，而且准确率相当不错。它的补全还能在改完一处后，跳到后面同时修改多处，这在重构时极其有用。例如改一个类型签名的时候 IDE 不太能智能重构，要手动改很多地方，而 Cursor 解决了这个痛点。

 
就为了这个 TAB 功能，我心甘情愿地付了 20 刀。

 
![image.png](https://xxchan.me/assets/img/ai-coding/image.png)

 
后来在我没意识到的时候 “Agent mode” 在 non-coder 中先火了。我才后知后觉地发现了 agent 的能力。（而且 Cursor 一直没涨价啊！所以现在在让用户逐渐适应 token based billing 了） 不知道这个火是不是偶然，因为在我看来其他的 AI IDE 或者 end-to-end 的 coding 平台或多或少都能做类似的事情，Cursor 现在在 Agent 上甚至是比较落后的。但或许是它做的早，抓住了时间窗口，在大众心里建立起了品牌。AI coding 平台的切换成本其实有点玄学，一方面真的要切的话并不难，体验没有质的差距，没有真正的壁垒；另一方面这个干活的东西，用顺手了也懒得换。

 
他们有一篇 [Our Problems](https://www.cursor.com/blog/problems-2024)，看他之前画的饼其实都是 AI-assisted coding 的范畴，现在感觉在 agent 的时代稍微有点过时了。AI assisted coding 的 UX 感觉还是有很多可以做的事情的，但现在大力做 Agent 的话可能会没那么优先了。

 
所以，Cursor 的好在哪？它好在一种奇妙的组合拳上。它先用一个真正懂开发者的杀手级功能（那个无敌的 TAB Edit）抓住了最挑剔的核心用户，然后又敏锐地捕捉到了 Agent 的浪潮，在大众心中成功地将自己与“AI 编程”这个概念划上了等号，哪怕它的技术在现在并非最领先。这种**“硬核实力”**和**“抓风口能力”**的结合，再配上一点先发优势的“玄学”，最终成就了它现在的地位。

 
现在如果你不知道什么工具最适合自己，那 Cursor 可能是一个比较稳的选择：有充足资金，不一定是最强但肯定差不到哪去。

 
#### Cursor 的终局是什么？

 
当初就有很多人说，Cursor 做的事为什么要 fork VS Code？我曾认为“为了 AI 特化的体验”是答案（例如 Cursor TAB）。但现在，VS Code、 [Augment Code](https://www.augmentcode.com/) 也在追赶，Cursor 自己反而没有做出更多让人眼前一亮的独特 UX。

 
我现在对这件事的判断是：**Cursor 想做一个大而全、ALL-in-one 平台，占据开发者的入口**。（GitHub Copilot 或许也想，但它还是不够快。）之前提的“我能在 CLI 里用 agent”，实际上是说 Agent 并不需要 IDE 就能工作。但我在自己浅浅用了一下 Cursor 的 background Agent 之后，发现这个体验很自然。很多东西不必做在 IDE 里，但反过来说，也不是不能做在 IDE 里。既然 IDE 是工程师每天花时间最多的地方，那为何不把所有 coding 相关的东西都塞进来，成为一个一站式的 hub？

 
至于其他的 AI code editor（windsurf/trae，以及开源的 cline/roo code），我感觉比较难与 Cursor 有一战之力。我的观点是，Agent 是大趋势，而做好 Agent 之后，对 AI-assisted coding 的依赖反而小了。当工程师需要自己写代码时，最终还是会回归到传统的 IDE 体验。这些工具虽然可能在某些体验上有优势（比如 windsurf 据说对复杂项目的上下文管理更智能），但普通用户没那个耐心去深度比较。在资本的冲刷下，这些微小差异可能会被逐渐抹平，甚至收购整合。做 Agent 就更是烧钱了。反倒是像 **Zed** 这种完全重头再来的 code editor，说不定可以搞出点新花样来。

 
#### 关于“壁垒”

 
Cursor 的创始人曾谈过他们对“壁垒”的看法：在这个发展过快，未来的想象空间也仍然很大的领域，**壁垒的本质就是“快”**。只要你够快，就能领先。反之无论你当前的技术有多强、产品体验有多好，一旦你在某个阶段慢下来，就可能被超越、被取代，非常残酷。

 
我在这个事情上没完全想明白。我曾经觉得靠“体验”是可以成为壁垒的。但或许那只是你做的事情不够大。如果足够大，那么巨头一定会出手自己做，然后用技术（模型）和资源能力比你做的更好。

 
### VS Code/GitHub Copilot

 
**Copilot** 绝对是里程碑，是第一个让人感觉“能用”的 AI coding 工具。但后来，它的体验逐渐被后起之秀超越。我猜测可能的理由包括：

 
1. OpenAI/微软重心转移（比如微软大力搞 copilot for office）
2. 毕竟微软是个巨厂，层层审批，Github Copilot 拿不到太多资源
3. Copilot 本身当初可能是想着做做看，做出效果以后也没想好再往后能怎么做，而且 coding 模型的发展缓慢（Codex 是 GPT-3 的一个 finetune 版本），后面专注提升基座能力去了，没人/资源专门训练 coding 特化模型
4. Copilot 用户（特别是 enterprise 用户）多了以后不好大刀阔斧地改体验，领先占据市场反而成了包袱
5. 受限于 VS Code 的壳，不像 fork 的 AI IDE 可以乱改，要往主分支里塞 AI 相关的东西可能还是要掂量一下，特别是在当年 AI coding 还原非共识，有很多程序员反感 AI

 
但是 VS Code 最近逐渐把功能慢慢都加上了。甚至还发了一篇有意思的宣言： **[VS Code: Open Source AI Editor](https://code.visualstudio.com/blogs/2025/05/19/openSourceAIEditor)**

 
长远看 **VS Code 可能还是会重回巅峰**。理由很简单：大厂认真起来是很吓人的（比如 gemini）。当 AI coding 成为共识，微软投入足够资源，体验差异很可能被逐渐抹平（比如 Cursor TAB 这种东西 Copilot 没理由不做），除非他们持续在“AI Editor 的 UX 创新”上整新活。但是目前看来并没有。更重要的一点是，既然 agent 不需要 IDE 就能工作，那么程序员自己写代码时，还是会回归到功能扎实、bug 更少的传统 IDE。这也是 Cursor 的一大弱点，它在 IDE 本身的迭代上，似乎总比 VS Code 慢半拍。

 
未来，VS Code 和 Cursor 两分天下，感觉也挺有可能。喜欢古典和喜欢大而全的人，各取所需。

 
### Claude Code

 
接着聊聊真正的 CLI-based agent。

 
[上次的文章分析过](https://xxchan.me/ai/2025/05/06/claude-code.html)，**Claude Code** 是个做的很用心的产品。它给了我一种“确实应该能 work”的感觉，以及第一次让我思考 agent 好像并不需要 IDE。

 
相比于 IDE 或者浏览器里的 agent，CLI-based agent 本质上没太大差距，最主要的区别可能就是对 prompt 和 tool 的设计。但它的优点是可以 iterate faster。因为能做的事情更少，反而可以专注在 agent 最本质的地方。因此正如上次的文章分析的，claude code 的 prompt 包括 tool spec 写的都非常的长。我自己使用下来的体感是感觉 claude code 明显要比 Cursor 更“聪明”一点。这只是因为 prompt 调教的水平吗？还是说 Claude Code 有特供的模型？（感觉暂时不太像，但未来不好说）

 
Claude Code 其实并不只能跑在自己本地的 terminal 里，现在已经可以在 GitHub 上 @它，然后自己干活了（跑在 CI 里）。但它的思路并非深度集成，而更像是利用 CLI 无限的可组合性（所以非常第一性原理做事？）。

 
![image1](https://xxchan.me/assets/img/ai-coding/image1.png)

 
在过去这一个月里，Anthropic 又有一些明显的动作，让人感觉想要力推 claude code：

 
- 在 Code with Claude 大会上发布了 Claude Code 1.0，以及 4.0 新模型
- 断供 windsurf
- Claude 20 块的 pro plan 也可以用 claude code 了，大大降低试用门槛。

 
最后一点让我果断订阅了 Pro Plan。我试了一下，在达到 usage limit 之前（几个小时后刷新），我让 Claude Code 跑了一个比较复杂的重构任务，大概持续了三四十分钟。这个用量如果按 API token 计费，少说也得 10 刀。这或许就是 **LLM 原厂做 agent 的一个优势**：反正机器已经在那里了，可以把闲时资源充分利用起来。而做应用的公司，又不可能去整租机器。

 
#### Anthropic 做 Claude Code 的真实意图是什么？

 
我其实还没完全看懂，Anthropic 做 Claude Code 的最终目的到底是什么？是想做一个好用的产品，还是想用它帮助模型训练本身？OpenAI 现在明显在花力气做 ChatGPT 这个产品，未来的想法大概是把 ChatGPT 作为一个入口，让它成为一个调度型的 agent。那 Claude Code 在这件事上的定位又是什么？

 
这一方面涉及对 Coding 这个市场的规模到底有多大的判断。从 Cursor 一开始的估值来看，大家普遍认为也就那样——因为开发者群体的体量就那么大。但现在 Vibe Coder 起来以后，整个故事又被撑大了不少。

 
不过，回到 Anthropic 这么一家大模型公司，直接下场卷应用层的东西，是否有点“不体面”？或许他们的目的并不是要把市场上其他人都吃掉，而是带着一定的试验心态，看看这种东西到底能做成什么样子。但说起应用层，Claude App 里面其实也有很多非常漂亮的功能，比如它的 Artifact，体验明显比 ChatGPT 好很多，虽然 Claude App 整体上很挫。

 
当然，更有可能的目的还是**通过用户使用它的产品来收集数据，最终用于训练模型**。 因为像 Cursor 这种合作伙伴的用户行为数据，它可能是拿不到的。所以它得自己做一个完整的产品，把整个链条打通。而且，Cursor 里那些乱七八糟的功能它可能也不太需要，它更关注的是训练模型过程中，真正与 Coding 直接相关的部分。

 
#### 从“聪明”到“持久”的进化

 
说回模型训练，Claude Code 宣称能独立跑七个小时，给我的感觉是：现在模型的“聪明程度”短期内好像有点提不上去了，于是大家开始发力做**“长期任务执行”**（所谓 Agent）——让模型持续工作得更久、更自主，并且能用工具来辅助提升自己。

 
在使用中，能很明显地观察到模型的一些新行为：

 
- 它会先说：“我接下来要做 123”，体现出任务规划能力；（我原来觉得需要外化的 TODO list，但它似乎在内化这个能力）
- 它会先写一个方案，然后写到一半突然说：“让我想一想有没有更简单的方式”，然后重头来过。

 
这些行为看着其实还挺好笑的，但也清晰地揭示了往 agent 这条路上走。

 
### [Amp](https://ampcode.com/)

 
他们整体上给我一种很有“产品 sense”，“很懂 agent 应该怎么 work”的感觉。但其实就是 claude code - like。我能想到他们的优势是 move （slightly） faster（？）；有 sourcegraph 这个 code search & indexing 后端能力（真的有用吗？）；不和 claude 一家强绑定，在别的模型追上的时候可以切；另外他们毫不掩饰、充满原则性的产品哲学可能可以赢得一批用户的深度信赖。他们是这么说的：

  
- Amp is unconstrained in token usage (and therefore cost). **Our sole incentive is to make it valuable**, not to match the cost of a subscription.
- **No model selector, always the best models.** You don’t pick models, we do. Instead of offering selectors and checkboxes and building for the lowest common denominator, Amp is built to use the full capabilities of the best models.
- Built to change. **Products that are overfit on the capabilities of today’s models will be obsolete in a matter of months.**

  
他们的 [“**Frequently Ignored Feedback**”](https://ampcode.com/fif) 也很有意思（用户：我要 xxx；amp：不，你不要），体现出他们对 Agent 的深刻理解：

  
- Requiring edit-by-edit approval traps you in a **local maximum** by impeding the agentic feedback loop. You’re not giving the agent a chance to iterate on its first draft through review, diagnostics, compiler output, and test execution. If you find that the agent rarely produces good enough code on its own, **instead of trying to “micro-manage” it,** we recommend writing **more detailed prompts** and improving your **`AGENT.md` files**.
- Making the costs salient will make devs use it less than they should. Customers tell us they don’t want their devs worrying about 10 cents here and there. We all know the dev who buys $5 coffee daily but won’t pay for a tool that improves their productivity.

  
非常 Opinionated，有点**“果味”**。

 
除此以外，他们还做了个 leader board & share thread 功能，很有意思，可以在团队内激起一些奇妙的火花。

 
但短期内有点谨慎不看好，因为 Claude Code 已经足够好用了，而且绑定 Claude 订阅有巨大的成本优势……Amp 目前的收费模式是完全 pass-through 按 token 收费（没有 margin）。那虽然他们不盈利，可能也不会太烧钱。可以拭目以待一下。

 
### OpenAI Codex （in ChatGPT）

 
上个月，OpenAI 也发布了自己的全自动 coding agent。是完全符合我对 agent 的想象的产品形态。我之前就在想，为什么我不能在手机上给 Cursor 派活？现在通过 ChatGPT 就能实现了。

 
但要看懂这个动作，就不能只盯着 coding。虽然他们收购了 Windsurf，但我认为 **OpenAI 的野心远不止在 coding 市场上分一杯羹，他们更想做的是让 ChatGPT 成为未来的调度入口，甚至是一个操作系统**。 Codex 的目的，或许只是为了比较专业的“高价值用户”能做更多事情，从而提高用户粘性。而收购 Windsurf，看中的可能是他们对 long context 的管理能力和宝贵的用户数据，从而赋能模型能力提升。

 
偏题说一嘴，ChatGPT 的整体体验远超其他官方 AI app，比如说

 
- memory：有一种很神奇的感觉，但对我个人而言提供的“价值”似乎还没那么大，真有偏个人思考的问题我还是更愿意问没有 memory，甚至更难用的 gemini。
- o3 的 web search 体验过于好。相当于 mini 版 deep research
- 虽然也不能说非常丝滑，还是时不时有点 bug，但还是比其他家好太多了。

 
### Devin

 
当年在 AI coding 还没那么普及的时候他们就打着 “First AI Software Engineer” 的旗号，要做全自动 end-to-end。初次发布后 500 刀/月的高价也是让人望而却步。并且试过的人也说它笨。

 
现在变成 20 刀起订，pay as you go 以后我立马试了试。

 
给我整体的感觉是，模型智力水平一般般。但他们的产品整体上也是一种“基本上能 work”的感觉。我有一种强烈的预感，在经过适当的 prompt engineering 之后，它能工作得很好。他们现在的说法也是很实在：“**Treat Devin like a junior engineer**”。（其实任何 Agent 产品目前大概都是这个状态。）

 
这是我第一次真切地感受到 agent 烧钱的威力。我让它处理一个 issue，它可以自主探索出一个框架（花了 2 个 ACU，每个 2.25 美元）。但后面让他改 bug，就有点改不对了，开始乱撞，很快就飙到了 4 个 ACU，20 刀迅速蒸发。或许现在的最佳用法是，先用它生成一个初版，然后手工或用 Cursor 精修。（当然，现在 Cursor 也有了 background agent，界限开始模糊了。）

 
对 devin（包括现在 Curosr remote agent）来说，还有一笔 vCPU 的钱。例如 m5.4xlarge（16C64G）ondeman $0.768/h。其实相比 token 并不算很贵……

 
在 Agent 成为大热门之后，**Devin** 直接受 Cursor、claude code、Codex 等各个方向的夹击了。

 
Devin 目前的优势在于 integration（能直接在 Slack、Linear & Jira 上派活）和较高的产品完成度（设计良好的 knowledge base、playbook 系统）。但这种“脏活累活”能撑起它的估值，能成为壁垒吗？直觉上，这些是任何一个好的 agent 都必须具备的功能。感觉 agent 这个领域确实需要大量时间去打磨体验，但资本似乎太急了。

 
他们最新版又出了一个 [Confidence rating](https://cognition.ai/blog/devin-2-1) 功能很不错，可以避免用户因过高预期而烧钱搞出一堆垃圾。其实这也是 agent 挺有意思的一个地方，你用的不对的话就会效果又差又烧钱。换个角度说，一个好的程序员或者乙方不应该你说什么就做什么，而是会试图理解你的意图，为什么你想做这个，以及有什么潜在的坑。

 
他们的 deepwiki 也有点像是秀肌肉，可能体现了他们在 agent 上的技术积累。毕竟，他们是一开始就融巨资自研大模型、奔着超大上下文去的团队。或许他们有很多的卡，在成本上也有优势。

 
在写这篇文章的时候又看到一个新的平台 [Factory](https://x.com/FactoryAI/status/1927754706014630357)，看起来也是叫板 devin。它的 release 感觉 too good to be true：“Factory integrates with your entire engineering system (GitHub, Slack, Linear, Notion, Sentry) and serves that context to your Droids as they autonomously build production-ready software.”。但我仔细看了一家这家公司成立甚至比 devin 还早一点。他们的 demo 视频中，一个有意思的地方是他所有的 integration 都是要跳回到它 factory 的页面上的（比如在 slack 里@它，它给一个链接）。它的体验其实是你在它的 portal 上完成所有事情，拉取 linear、GitHub、slack 的 context。（说个不恰当的比喻，这看着有点像 coding 领域的 Manus。）相比之下 devin 是让你在 Slack、Linear 上直接和它交互，更加的 in-context，in-flow。但 anyways，有竞争是好事。

 
### v0

 
上面其实说的都是比较偏为 engineer 设计的工具（不管是全自动还是半自动），下面开始聊聊更偏 “non-coder” 或者 “product” 向的平台。

 
**v0** 是 coding 垂类赛道中更垂的一个，更偏前端 UI prototype。你可以把它想象成一个用自然语言驱动的 Figma，直接在 v0 里就能把界面“画”出来。另外一个讨巧的地方是利用 React/shadcn UI 的组件化能力，它生成的东西直接能整合到自己的代码里，是个能用的东西。

 
Vercel 这家公司一直很讲究“品味”，他们凭借在前端领域的深厚积累，把 v0 这个垂类的体验做得非常好。但可以想见，v0 的流畅体验背后，肯定有大量的工程优化，比如套用模板、专门微调模型，以及一套精心设计的 workflow 来保证生成效果。

 
一个有意思的动向是他们最近[发布了自己的模型](https://vercel.com/blog/v0-composite-model-family)，并且开放了 API。他们对此的解释是：“Frontier models also have little reason to focus on goals unique to building web applications like fixing errors automatically or editing code quickly. You end up needing to prompt them through every change, even for small corrections.” 非常合理，但是这是不是属于雕花？当然对于 deliver 一个好用的产品来说，雕花是必须的。但我有一点看不懂他们为啥要出 api，可能一方面是回收训模型的成本，一方面是开始探索让自己成为一个“被调度的 agent”。

 
但感觉他们并不满足于只做 UI，他现在的定位已经是 “Full stack vibe coding platform” 了，另外一方面他们也在做 GitHub sync 等和现有代码整合的工作，而不再是只能在 v0 平台上生成。

 
### Bolt / Replit / Lovable：“想法到应用” Vibe Coding platform

 
这一类的产品，其实有点大同小异。它们都是端到端的全栈平台，或者叫 app builder，有个更好听的名字叫**“idea to app”**。

 
相比 Cursor，他们解决的痛点一是部署（包括前后端以及数据库），二是更丝滑的 vibe coding 体验：我在 Cursor 里生成的代码反正也不看，为什么还要展示 code diff？直接 chat - live preview 才是更直接的体验。另外它们应该有一定的项目模板成分，让首条 prompt to app 的体验感受非常好。

 
虽然它们各自定位可能略有不同，比如开发者可能更喜欢 Bolt，非开发者更喜欢 Lovable（纯瞎说），但本质上做的事情是一样的：让用户在接近零手动改代码的情况下，搞出一个能用的产品来。

 
#### Vibe Coding 平台的困境

 
这个事情的 tricky 之处在于，如果他们的目标是 deliver 最终产品给用户，那用户的期待会很高。在比较严肃的场景下，用户往往需要非常具体的修改，全权让 AI 来改不一定能达到效果，而且还很费钱。我在用 Cursor 糊前端的时候，感觉加功能很爽，但想微调按钮位置、布局、交互逻辑时，它往往就改不对了。

 
虽然有些 vibe coding 平台也提供一定的 online code editor 能力，但真到了需要精细控制的时候，会写代码的人可能还是会回到 Cursor，因为那里最顺手。可一旦回到了 Cursor，后续的开发可能就没必要再回到 vibe coding 平台了。部署的痛点是一次性的，CI/CD 搞好之后，改完代码 push 一下就行。

 
精细开发的话，Cursor 的 agent 或许能提供更精确的 context。这些 vibe coding 的平台或许也可以把 coding agent 的能力都提上去，但是他们要做的事情太多了，把一个平台打造好得花很多精力。他们在 coding 的技术积累肯定是不如 Cursor 等 for developer 的平台。

 
简言之，**vibe coding 平台在严肃、复杂场景下的上限可能不足。** 如果只做简单的小项目或者 demo，价值肯定是有的，但有多少用户愿意为此买单，我就不懂了。这个故事，其实在 Vercel/Neon 这类主打“开发者体验”的 PaaS 平台上已经发生过：大家都说体验好，但等项目做大以后，很多人还是默默地迁移到了 AWS。

 
再换个角度，我大胆猜想一下：未来，Cursor 完全可以把 vibe coding / app builder 的体验也做好。开屏界面搞成一个对话框，同时把 live preview、Supabase/Vercel 整合等功能都做了，到时这些平台就更危了。更何况，vibe coding 这个概念本来就是在 Cursor 上火起来的，对那些想 build product 的人来说，“看到代码”这件事或许并不是多大的阻碍。我大胆预测，一年后 Cursor 可能就会这么做。

 
也可以看看 Lovable 的 [FAQ](https://docs.lovable.dev/faq#what-is-the-difference-between-lovable-and-cursor) 里自己写的和其他平台/Cursor 的比较：

 
- 大部分的点都是 “just better”，“way more natural”，“Attention to detail”，比较虚的。在普通的产品上或许有说服力，但在 AI coding 竞争这么激烈的领域，想保持领先太难了。
- 他们有个 visual editor 其实挺有意思，可以直接所见即所得地修改 UI 元素，一定程度可以解决之前说的微调麻烦的问题。但我试了一下，目前效果还比较一般，只能改改字的内容、字号、margin 之类的，并不能实现拖拽等功能。这个故事长远看也很好听 - 甚至可以吃掉 figma？但是感觉技术难度极其大。（让我想到现在连个真正好用的 mermaid 图 visual editor 都没有）

 
### YouWare：User Generated Software 的激进实验

 
AI coding 真正让人兴奋的地方，在于它所展现的“自然语言调度算力”的能力。这让普通人能使用代码这个工具去解决他们自己的之前无法被满足的需求：一个 **User Generated Software (UGS)** 的时代，正在到来。

 
在所有产品中，**YouWare** 仿佛是一个精准为此而生的平台，它把 UGS 作为了自己唯一的目标。

 
#### 把 AI coding 做成内容社区，这对吗？

 
我一开始对 YouWare 谨慎不看好。

 
它给我的感觉，是想把 UGC 时代那套（社区、流量、平台）的想法，生搬硬套到 UGS 上来。如果他做一个新的内容平台，是要和抖音、小红书竞争注意力的，但感觉不如他们好刷。个性化的娱乐需求已经被短视频充分满足了。（……吗？在我说完这句话之后，又突然感觉短视频还是没那么好刷，也总觉得也总找不到符合我偏好的游戏。）

 
我最初的想法是：UGS 的潜力在于满足海量的、未被满足的长尾工具需求。用户不缺动机，只缺能力。如果是为了解决自己的痛点，那用户干完活就走了，不一定有分享或分发的欲望（或者在 Twitter/小红书上发发就够了），更不会没事干去一个工具网站上“刷”来“刷”去。

 
YouWare 认为许多人并不知道自己可以做什么，因此需要一个平台来激发他们的思考和创造欲，社交元素在此便扮演了激发灵感的角色。

 
v0、Lovable 这些平台，虽然也号称小白可用，也做一点社区，但它们仍然会把代码展示给用户，会弹出 build error，会让你去连接 Supabase。它们的假设用户，依然是有一定技术背景的“专业人士”（如产品经理、设计师）。例如这段：“Lovable provides product managers, designers, and engineers with a shared workspace to build high-fidelity apps, collaborate effectively, and streamline the path to production-ready code.”

 
而 YouWare 的激进之处在于，它**完全不给用户看代码**。它面向的 non-coder 是更广泛的普通人。

 
这有点像小红书限制图文的字数，通过一种限制，反而最大化了目标用户的可用性。对于一个完全不懂技术的人来说，看到 build error 意味着终点，而在 YouWare 里，这个终点被隐藏了。

 
上面说工具需求和娱乐需求的区别，其实小红书也可以被看作是一个用户记录的工具，而且小红书火起来很大程度上是它“有用”。

 
在我自己试用过 YouWare 之后（[我生成的东西](https://www.youware.com/profile/uNYPe0WjpUVfW21IOleyYTlMIWf1)），感受到了一些有趣的点

 
-  
确实有点毒性（以及免费额度非常重要）。比如我会有个脑洞就想扔上去看看行不行。如果用其他的平台搞正经项目的话我会更要掂量一下再做。（我心里预期包含了 debug 成本等，毕竟我是想要一个真的能用的东西。在 mental burden 上，YouWare < Lovable < Cursor，但有用性可能相反）。这种感觉和我用 cursor 的 background agent 时很像，都是“跑跑看，反正不亏”。

 
-  
它真的隐藏了代码细节，包括失败。Lovable 在我试用的时候初次生成报错的概率还是挺大的（虽然点一下也就修了），而 YouWare 没出现过。

 
![image2.png](https://xxchan.me/assets/img/ai-coding/image2.png)

 
-  
它鼓励“玩耍”。YouWare 的 Remix 和 Boost 功能也挺有意思的（先不谈效果好不好）。很符合“用户并不知道他想 build 什么东西”的出发点，鼓励探索和再创作。

 
-  
但突然发现这东西很多家都有了，甚至连 claude artifact 都做了类似的功能，而且完成度高得惊人。）

 
![image3.png](https://xxchan.me/assets/img/ai-coding/image3.png)

 
![image4.png](https://xxchan.me/assets/img/ai-coding/image4.png)

 

 

 
#### 一堆关于 YouWare 的零散思考

 
-  
**Vibe Coder 是什么样的人？** UGC 时代出现了一个新东西叫专业“创作者”，现在的“vibe coder”倒是有点像。但内容创作者的收入主要靠流量和商单，而 vibe coder 更接近独立开发者，他们想的是 build 自己的产品，然后靠卖软件或订阅赚钱。卖软件终究要靠解决实际需求，然后去各个平台推广，而不是等着别人在你的 UGS 平台上刷到你（例如去发小红书而不是等人在 GitHub 上刷到你）。。 ……想到这里，我开了个脑洞：真要做的话，岂不是应该做 **vibe coder 的 OnlyFans**，而不是 YouTube/Instagram？🤣

 
-  
**代码确实有娱乐需求**（有个东西叫创意编程）…但还是那句话，娱乐需求是要竞争注意力的。再其中的一个小用法是把文章变成交互式网站，满足教育学习的需求，比如这些：

 
- [https://ciechanow.ski/bicycle/](https://ciechanow.ski/bicycle/)
- [https://garden.bradwoods.io/](https://garden.bradwoods.io/)
- [https://encore.dev/blog/queueing](https://encore.dev/blog/queueing)
- [https://www.redblobgames.com/pathfinding/a-star/introduction.html](https://www.redblobgames.com/pathfinding/a-star/introduction.html)

 
-  
**Power User vs. 小白用户：** 这两者的需求是矛盾的，一个平台很难同时满足。YouWare 显然选择了后者。

 
-  
**输出形式的局限：** 为什么目前这类 coding 平台（包括 Devin、Lovable 等）的最终产出大多是网站？对于许多小型工具性需求，命令行或桌面应用或许更直接、更高效。当然，从 UX 角度看，网站对普通用户最友好。

 
-  
**成本问题**

 
- 作为内容平台，有很大的合规风险和成本问题。但可能也没那么难，毕竟 deepseek 都能在国内上了。
- host 网站的成本问题。以及不同形式的网站可能有不同的计算需求，对热门项目可能还得动态 scale。
- Agent 的巨大算力成本。相比 UGC，用户生产内容时其实平台没什么成本，但 UGS 则不一样。相比 Amp 说我的优化目标就是最大效用，这里 YouWare 的账就更难算了，这里有很大的生成效果和成本之间的 tradeoff 要做。这就引到一个核心问题是它鼓励用户创造，那盈利模式是什么？如果沿用传统平台的流量广告模式，考虑到巨大的成本，盈利上限恐怕不高。

 
-  
**是否要对特定场景优化？**

 
- 例如现在平台上可能有过半用户会用来写报告什么的。但其实这是类 deepresearch 功能，在 YouWare 里做效果会很一般。Manus/flowith 倒是估计会优化（Manus 最近还真特化了 slides 功能，让我有点无语，说好的通用 Agent 最后还是做这种东西去了）。

 
-  
**数据驱动平台演化？**

 
- 我一开始很困惑于为何 YouWare（包括 Manus 等）在能力尚不完善的阶段就大力买流量推广。而不是先将产品效果打磨得更好再推广。可能是他们已获得充足融资，急于扩张。
- 但在产品成熟前就推出，可以帮助他们了解用户到底想 build 什么，然后针对性地优化。我之前可能低估了社交对于激发用户创造力的作用。这可能类似于一种进化算法，或者“伟大无法被计划”的理念：让用户自由探索，或许能裂变出意想不到的创新。YouWare 团队的字节背景，想必会沿用数据驱动的决策方式，通过用户行为来让平台演化，或许做着做着就能发现奇妙的突破点。

 

 
#### YouWare 的未来

 
我相信一家公司是有它的基因的。YouWare 的字节剪映 PM 创始人背景，或许才能想出这么个玩意儿。

 
虽然上面分析的很多东西可能 Lovable 会往 YouWare 的方向靠，更加隐藏代码；或者 YouWare 往普通的 Agent 平台上靠，提高 utility，但期待未来的结果。我觉得 YouWare 的形态未来一定不是现在这样。同时我越来越觉得 YouWare 的出发点很有意思，或许能做出一些不一样的事情。这个团队可能比做 coding 的人更懂创作、平台和消费者，比懂创作者的人更懂 AI coding。

 
YouWare 的目标并非最大化 utility，而是**激发普通人的 creativity**。当然 utility 也要至少 good enough。

 
一个残酷的问题是未来会 Cursor 的人越来越多了，会不会就吃掉这种傻瓜工具了？可能会想摄影师用相机和普通人用手机拍照可以共存一样，程序员和 vibe coder 共存。另一个想法是我最近越来越觉得，当前的 AI 正在加剧马太效应（或许从 200 刀订阅就开始了）。懂得如何用好 AI、并能负担得起开销的人（比如真见过人用 Cursor 一天消耗好几百刀），与普通人的差距会越来越大。对于那些不那么乐于动脑、需求表达不清的普通用户，他们会被“淘汰”吗？这个未来太残忍，我有点不愿设想，宁愿投身对抗潮流。从这个角度看，YouWare 这种致力于服务广大普通人的尝试让我觉得很有价值。

 
当然虽然 YouWare 很有想法。但认知能否成功转化为可落地的产品并实现商业价值，尚存不确定性。

 
## Big picture：行业格局/技术方向分析

 
在逐一审视了牌桌上的这些玩家之后，让我们向后退一步，看看整个 AI coding 领域的全景。

 
### 赛道细分

 
AI coding 还可以细分为几个小方向。一个产品可能会跨多个方向

 
-  
**AI-assisted Coding:** 以 **Cursor** 和 **GitHub Copilot** 为代表，它们是现有开发工作流的“增强器”，致力于让专业开发者写代码更快、更爽。

 
-  
**End-to-end Agent** 以 **Devin**、**Claude Code** 和 **Amp** 为代表，它们的目标是成为能独立完成任务的“初级工程师”，将开发者从执行者提升为任务的分配者和审查者。Agent 同时也可能是作为合作者，特别是 Claude Code 这样 CLI based agent，我既可以和他 pair programming，也可以请他帮我干活。

 
[课代表在视频里](https://youtu.be/FzbkAy0DcQk?si=caXCcvDsm2tUbeTP)讲到他预测 2025 年 Q3，硅谷将形成共识，认为 Agent 可以达到甚至替代 mid-level software engineer 的水平。评论区对此多持怀疑态度。我的看法是，Agent 或许不一定会完全“替代”，但它极有可能成为 mid-level 工程师的得力“合作伙伴”。从这个角度理解，我认为其预测是相当有道理的。

 
-  
**Vibe Coding / UGS:** 以 **v0** 和 **YouWare** 为代表，它们试图将代码的能力赋予非开发者，让他们通过自然语言创造应用和工具，一个更偏向“产品原型”，一个则更激进地走向“内容社区”。

 

 
### “半成品”的尴尬现状

 
我们必须承认一个现实：**Agent 依然是一个“半成品”**。它的效果还不足以真正端到端地交付一个完美的结果，有时甚至不如我们自己动手来得省事。（比如还是手动调 button 爽）

 
但我们也能清晰地看到 agent 的进化路径：从最早在 ChatGPT 里手动复制粘贴，到后来在 IDE 里进行单轮对话，再到如今的 Cursor Background Agent 和 Claude Code，**Agent 能够独立工作的时间越来越长，做事的数量和质量都越来越高，这无疑是一个不可逆转的趋势。**

 
或许我们应该换个心态：把它想象成一个外包合作方。你把任务派给它，让它干一段时间，然后你来检查、给反馈，而不是指望它一次性搞定。这和我们与人类外包商（也就是“Agent”）的合作模式，并无二致。

 
#### 成本的诅咒，与模型的赌局

 
与此同时，Agent 是个非常贵的东西。这除了让用户不敢大规模使用之外，也让 agent 应用公司陷入两难：是继续不计成本地提升效果，还是转而研究各种“奇技淫巧”“雕花”以降本增效？但存在性能和成本的 tradeoff。我不知道是否可能同时兼顾两者，比如团队的一部分专注于性能提升，另一部分研究成本优化。如果完全不考虑成本控制，高昂的价格也可能会吓退用户。但 AI Agent 公司是否真的那么急于获客？或许也不然。

 
这里存在的一个更大的变数：如果上游的 LLM 厂商大幅降价，那么之前在成本优化上所做的努力，比如辛辛苦苦优化了 30%-50%，就可能因为外部因素而显得“白费功夫”。当然，也存在原厂优化不力，或者他们转而发展自家 Agent 业务的可能性。因此，对于 AI Agent 创业公司而言，其决策中充满了需要“赌”的成分。

 
### Agent 需要哪些能力？怎么做 coding agent？

 
从各个产品的探索中，我们可以窥见一个好的 Agent 需要具备哪些能力：

 
-  
**Memory/知识库**：例如能自动学习 Cursor rule。（devin/manus 都有了）

 
-  
**Long context 能力**：indexing & RAG？

 
- 我对这点的作用是有点存疑的。现在进入 Agent 时代之后，Agent 可以自己去 grep 代码找到 context。而且这和我自己开发的流程也很像。还是大量依赖字符串搜索，并不是什么聪明的办法。但其实 grep 仅限于知道要改什么的时候。“xxx 是怎么 work 的”这种模糊的问题就不行了。
- 但对 long context 的考验其实挺难验证的，需要用的很深才能知道到底什么水平。我也还没有用出感觉来。

 
-  
**Task 能力** 之前我觉得必须需要外化的 todo list，但是现在好像 claude 开始内化这种能力了（但直觉上还是外部的更好？）

 
![image5.png](https://xxchan.me/assets/img/ai-coding/image5.png)

 
-  
**主动沟通与 Interaction**: 一个好的 Agent 不应该你说什么就做什么。它应该像一个好的乙方，会反问、会澄清意图、会评估风险（比如 Devin 的“置信度评级”）。例如“我要做一个 ppt”，就问用户你有没有已经有的素材，或者课本资料提供等。deep research 类产品在这这事情上做的也不错。

 

 
话说回来，做好 coding agent 是不是需要你自己用 coding agent 用的很好？

 
## 最后的思考：我们与 AI 的关系

 
那自然语言调度算力与 User-Generated Software 这个概念，可能 somehow 已成为行业共识，但其具体的实现形式，则远未达成一致。

 
聊了这么多，最后还是回到我们自己身上。

 
#### 普通人到底该怎么选？

 
总的来说，现在所有的工具都处于一个“still early, but already useful (if used correctly)”的阶段。它们在简单的小活儿或生成 demo 上表现不错，但在复杂场景下，则非常考验使用者的**“手艺”**。

 
这门“手艺”既包括 prompt engineering 的技巧，也包括对代码和 Agent 工作原理的理解。“了解 ai 能力边界”也是个有点说烂了的东西。所以，未来能把 Agent 用得最好的，大概率还是专业人士。这就像专业摄影师和普通人的手机拍照，工具模糊了专业间的边界（比如工程师可以搞设计，PM 可以写 demo），但最终还是拉开了上限。

 
Agent 可能是越用越好用的东西，需在团队里一起探索最佳实践、积累 prompt 技巧和知识库，本身就是一种投资。

 
但我也时常怀疑，研究这些东西会不会是徒劳？等到模型能力到达某个奇点，我们直接拥抱最终形态就行了，中间的各种探索和使用经验都会过时。这或许是对的。多说无益，我也不再想按着别人的头让他用 AI，but I just can’t help playing with it, it’s fun! 😁🤪

 
#### 当 llm 生成的能力趋向无限的时候，我们要用他来生成什么？

 
一个更深层的问题：AI 的发展和我到底有什么关系？就像我不怎么看论文，感觉离我很远。虽然 ChatGPT 让我学习任何东西都变得容易多了，我动不动想到啥就要和它探讨半天，但我反而更累了。我真的需要了解这么多东西吗？

 
Coding Agent 的发展能让我写越来越多的代码，那我要把那些东西都做出来吗？当生成的能力趋向无限时，我们到底要用它来生成什么？

 
YouWare 这样的产品或许是一种答案。

 
又或者，这本身就是一个不存在的问题，就像实现可控核聚变之后应该怎么办？能人人开上高达吗？

    ![Portrait of xxchan](https://avatars.githubusercontent.com/u/37948597?v=4)  
xxchan

 
Build something fun and useful.

   
-  [      Twitter ](https://twitter.com/xiaoxxchan) 
-  [      GitHub ](https://github.com/xxchan) 
-  [      LinkedIn ](https://www.linkedin.com/in/xxchan) 

    
## Comments