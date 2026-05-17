---
saved_date: 2026-05-17T23:20:47.958Z
title: "每个 CLAUDE.md 都必须有的 4 行配置"
url: "https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA%3D%3D&mid=2247501696&idx=2&sn=4b234c2fd95bb502514734fd0bd620cc&utm_source=substack&utm_medium=email&poc_token=HApaB2qjGO_L_XLDaSMETJXBAsqSwGqVxa-Clpbs"
author: "AI研究生"
description: "在 2026 年 4 月的一周内，Anthropic 发布了 Claude Opus 4.7，上线了名为 C"
word_count: 5369
tags: [Technology]
---

# Claudemd 4

AI研究生 _2026年5月4日 04:39_ 

 
在 2026 年 4 月的一周内，Anthropic 发布了 Claude Opus 4.7，上线了名为 Claude Design 的新产品，并新增了即便你的笔记本合上也能运行的 Routines。

 
同一天，OpenAI 给 Codex 加了码：并行的 agents 能在你的 Mac 上自动点击与输入。

 
如今这很正常。2026 年 4 月被称为有史以来 LLM 发布最密集的月份之一。大约 65–70% 的企业代码由 AI 编写。超过 50% 的公司把自己的 AI 采用情况描述为“一场混乱的自由搏杀（chaotic free-for-all）”。

 
然而，在整个领域里获星最多的开发者资源既不是 framework，也不是 plugin，更不是 model。

 
它只是一个 Markdown 文件里的四句话。

 
一个 GitHub repo。60,000 颗星。https://github.com/forrestchang/andrej-karpathy-skills

 
无依赖、无 API、无构建步骤。

 
只有一个 `CLAUDE.md` 文件，包含四条从 Andrej Karpathy 1 月份的一篇帖子中提炼出的行为指引。6 万名开发者点下收藏，比本周任何产品发布更能说明 AI 辅助编程的真正瓶颈。

 
上周末我把自己的 `CLAUDE.md` 迁移到新版 Claude Code 以适配它的工作方式。47 条规则，几个月里精心积累。agent 无视了一半，还臆造出我从未写过的约定。直到我看到这个 repo，才意识到问题不是我的规则，而是我有太多规则。

 ![作者制图：80/20 反转](https://mmbiz.qpic.cn/sz_mmbiz_png/Cic4GFNZLlxqT7Tt8bob5JAsIgbApSIvewOdGZYKYIhIxv3CADBWpgibfw1a4sR7PoOWJQakic7u5nmYZ3rh2axMdh3pExGHBSeeibKsFS7Cq0M/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0) 作者制图：80/20 反转  
## Karpathy 实际上诊断了什么

 
2026 年 1 月，Andrej Karpathy 发了一个线程，和大多数 AI 评论不一样。他没有宣布什么新东西，而是在描述哪里出了问题。

 
大约 6 周时间里（从 2025 年 11 月到 12 月），他的工作从“80% 手写代码 + 20% agent 协助”变成了“80% agent + 20% 编辑”。他称之为“这是我 ~20 年编程里最重大的变化”。但这条线程不是庆祝，而是诊断。

 
问题不在于模型不会写代码，而在于模型缺乏判断。

 
“模型会替你作出错误假设，并且一路按着这些假设跑下去而不检查。”Karpathy 一针见血地指出了更深层的问题：“它们不会管理自己的困惑，不会主动澄清，不会暴露不一致，不会呈现取舍，也不会在该反驳时反驳。”

 
你说“导出用户数据”，agent 就默认用 JSON、写到磁盘、包含所有字段、略过分页。它从不说一句“我不确定你想要什么格式”，而是直接选一个然后开干。

 
这就是第 1 行的来源。

 
“它们非常喜欢把代码和 API 复杂化，堆砌抽象。”Karpathy 的话是：它们“会实现 1000 行的臃肿结构，而 100 行就够了”。

 
你要一个折扣计算器，却得到一个 Strategy pattern、抽象基类、一个 enum、一个 dataclass 配置，还有 40 行的初始化。agent 为明天的需求而构建，而不是解决今天的问题。

 
这直接对应第 2 行。

 
“它们仍会修改/移除自己不太理解的注释和代码，即使与任务无关。”

 
你让 agent 修个 bug，结果 PR 还把单引号改成了双引号，加了你没要求的类型注解，还重写了相邻代码。修复只需 3 行，diff 却有 40 行。

 
第 3 行因此而存在。

 ![作者制图：三种失败模式](https://mmbiz.qpic.cn/mmbiz_png/Cic4GFNZLlxpshd19RhRK4tHiaZ1MvuricibnGmpFDU53pKDuYnMkjbw1rMibMfw0fOSZ0hyKiboDwRnLR3vY4YGxeYA16Zx08iaicCk0tOCtgnGDRk/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1) 作者制图：三种失败模式 
这条线程之所以引发共鸣，是因为它没有开 prescription。Karpathy 没给出方案，他只是把失败模式描述得足够清楚，于是几天内，就有人把它们翻译为四行 `CLAUDE.md` 并发到 GitHub。

 
不过还有第 4 行，它超越了“自律”，直指 Karpathy 自己暗示过的那点：“LLMs 在围绕明确目标循环迭代方面异常擅长。别告诉它要做什么，给它成功标准，然后看它自己推进。”

 
这就是第 4 行，也正是让这份文件不止于“风格指南”的关键。

  
## 这 4 行

 
在这里。一个 `CLAUDE.md` 的完整“行为”部分，已经有 5.5 万开发者为之打星：

 
1. 
不要假设。不要掩饰困惑。要揭示取舍。



 
1. 
用能解决问题的最小代码。拒绝一切带有猜想的实现。



 
1. 
只触碰你必须改动的部分。只清理你自己制造的脏。



 
1. 
定义成功标准。循环迭代直到验证通过。



 
就这些。每一行都直接映射到 Karpathy 的一个失败模式：

 ![这 4 行：你完整的 CLAUDE.md 行为基线](https://mmbiz.qpic.cn/sz_mmbiz_png/Cic4GFNZLlxoY6QntDbzckyicS5OibrwuiabjdaCuEUs6DGBpmVHicb4rb2H87ZsswJSzWquiaFvuY7TxbDfpVibic5jX6YIQm7ahaWibYVcECibUMImo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2) 这 4 行：你完整的 CLAUDE.md 行为基线 
接下来解释为什么它们有效。下面的 before/after 示例改编自该 repo 的 EXAMPLES.md，那里有每条原则的完整演练。

 
### 开始写码前先思考：不要假设。不要掩饰困惑。要揭示取舍。

 
这是解决 AI 编码 agent 最常见让人抓狂问题的一条：该问的时候它选择了猜。

 
没有这一行，当你说“添加导出用户数据的功能”时，agent 会这样做：

 
```
def export_users(format='json'):
    users = User.query.all()
    if format == 'json':
        with open('users.json', 'w') as f:
            json.dump([u.to_dict() for u in users], f)
    return f"Exported {len(users)} users"
```

 
它默认是 JSON，默认导出全部用户，默认输出到磁盘，默认包含所有字段。它从未提过这些决定，只是自己选了然后继续。

 
有了这条原则，agent 的第一步会变成这样：

 
```
Before implementing, I need to clarify:
1. Scope: Export all users or a filtered subset?
2. Format: JSON download, CSV file, or API endpoint?
3. Fields: Which user fields? Some might be sensitive.
4. Volume: How many users? (affects the approach)
```

 
四个问题，替代四个假设。先有答案，后有代码。

 
为什么这比看起来更重要：LLM 天生不会“外化不确定性”。它们被训练去“完成”，而不是“暂停”。训练数据里的每个 token 都在向前推进。说一句“我不确定”违反了模型的默认生成惯性。这一行强制启用的是模型具备但默认不启用的能力。这不是“加功能”，而是“改默认”。

 
### 简单优先：用能解决问题的最小代码。拒绝一切带有猜想的实现。

 
这条能扼杀“过早抽象”。没有它，你要“一个计算折扣的函数”，却会得到：

 
```
class DiscountStrategy(ABC):
    @abstractmethod
    defcalculate(self, amount: float) -> float:
        pass
classPercentageDiscount(DiscountStrategy):
    def__init__(self, percentage: float):
        self.percentage = percentage
    defcalculate(self, amount: float) -> float:
        return amount * (self.percentage / 100)
classFixedDiscount(DiscountStrategy):
    # ... 20 more lines
classDiscountCalculator:
    def__init__(self, config: DiscountConfig):
        # ... 15 more lines of setup
```

 
抽象基类、Strategy pattern、配置 dataclass、四十多行只为做算术。

 
遵循这条原则：

 
```
def calculate_discount(amount: float, percent: float) -> float:
    return amount * (percent / 100)
```

 
一个函数，一行逻辑。若日后确实需要 Strategy pattern，再重构；不是现在，更不是带着猜想去写。

 
多数文章忽略的洞见是：复杂那版并非“显然错误”。它也遵循真实的设计模式。一位资深工程师在大型计费系统里也可能用 Strategy pattern。问题在于时机。过早抽象的代价会复利：代码越多，bug 表面积越大，评审的认知负担越重，改变方向的惯性越强。agent 在为并不存在、也可能永远不会出现的需求而构建。好代码是用最简单方式解决今天的问题，而不是提前解决明天的问题。

 
原文件里的“资深工程师测试”一语中的：“资深工程师会说这过度复杂了吗？”若是，就简化。

 ![作者制图：在真实缺陷修复中应用 4 行前后的对比](https://mmbiz.qpic.cn/sz_mmbiz_png/Cic4GFNZLlxrCniaZumkLkhCUNgRFZJtOrWrzebgAMSSmfkJddUDqr7QrYAgNa3apjsRNtPJsLEvWhDf6Fu6TTZr7aJPDI5XRPxqgkEH97EV4/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3) 作者制图：在真实缺陷修复中应用 4 行前后的对比 
### 手术刀式改动：只触碰你必须改动的部分。只清理你自己制造的脏。

 
这条在保护你的 diff。你让 agent 修一个“空邮箱导致校验器崩溃”的 bug。没有这条，diff 会长这样：

 
```
- if not user_data.get('email'):
+ email = user_data.get('email', '').strip()
+ if not email:
      raise ValueError("Email required")
- if '@' not in user_data['email']:
+ if '@' not in email or '.' not in email.split('@')[1]:
      raise ValueError("Invalid email")
- if not user_data.get('username'):
+ username = user_data.get('username', '').strip()
+ if not username:
      raise ValueError("Username required")
+ if len(username) < 3:
+     raise ValueError("Username too short")
+ if not username.isalnum():
+     raise ValueError("Username must be alphanumeric")
```

 
本来只要修“空邮箱”这个点，agent 却顺带“改进”了邮箱校验、加了用户名长度与字符限制、改了变量名。全是你没要求的。

 
遵循这条原则，diff 会很“外科”：

 
```
- if not user_data.get('email'):
+ email = user_data.get('email', '')
+ if not email or not email.strip():
      raise ValueError("Email required")
- if '@' not in user_data['email']:
+ if '@' not in email:
      raise ValueError("Invalid email")
```

 
每一行改动都能溯源到 bug 报告。别的一概不动。

 
真正的解锁点不只是“干净”，而是“可审计”。当 agent 的 diff 有 40 行，但只有 3 行与需求相关，你就无法不逐行审查那剩下的 37 行。这不是小烦恼，而是所有 AI 代码输出都要缴的“评审税”。手术刀式改动让 AI 输出以你真正需要的速度“可评审”。diff 越小，你越能更快地信任、合并并继续前进。

 
原文件还补了一点很重要的细节：如果“你的改动”造成了孤儿（未使用的 import、死变量），就把它们清掉。但除非被要求，不要碰你改动之前就已存在的死代码。你的脏，你来擦；他们的脏，他们决定。

 
### 目标驱动执行：定义成功标准。循环迭代直到验证通过。

 
前三条是护栏，约束行为。这一条不同，它是“能力解锁”。

 
它把 Karpathy 的观察转化为杠杆。他注意到 LLMs “在围绕具体目标反复迭代直到达成方面异常擅长”。问题不在 agent 不会迭代，而在我们给的是模糊指令，而不是可验证的目标。

 
没有这条，你说“修一下认证系统”，agent 会回复：

 
```
I'll fix the authentication system by:
1. Reviewing the code
2. Identifying issues
3. Making improvements
4. Testing the changes
```

 
计划很虚，没有成功标准，也没有验证。它会改点什么，然后就当完成了。

 
遵循这条原则，同样的请求会变成：

 
```
1. Write test: passwordchange→oldsessioninvalidated
   →Verify:testfails(reproducesbug)
2. Implement:invalidatesessionsonpasswordchange
   →Verify:testpasses
3. Edge cases:multiplesessions,concurrentchanges
   →Verify:additionaltestspass
4. Regression:existingauthtestsstillpass
   →Verify:fulltestsuitegreen
```

 
每一步都有检查点。因为知道“完成”的样子，agent 能自主循环推进。强约束的成功标准替代了持续的手把手。

 ![作者制图：自律 vs 杠杆](https://mmbiz.qpic.cn/sz_mmbiz_png/Cic4GFNZLlxprv9vskg2Swxgujianqoh1KakrndM2anXsUfbqG5ab5zFT7sE4oqBKfeKXJN5Ejqib6ZseDGvHRUooGnXpEHH1RKyJ7ibPpicU6Gk/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4) 作者制图：自律 vs 杠杆 
把这条和前三条区分开来很关键：Think Before Coding、Simplicity First、Surgical Changes 都属于“自律”，是防止不良行为；Goal-Driven Execution 是“杠杆”，是解锁 agent 本来就擅长、但没有正确提示结构就不会激活的行为。前三条让 agent 不再恼人；第四条让 agent 更有能力。区别很重要：自律有递减收益，杠杆会复利。

 
有个提醒：这些例子都是干净的单文件任务。我也想看看这 4 行在一个 10 万行的 monorepo（单体仓库）里、面对多团队和纠缠依赖时的表现。单开发者项目是“容易模式”。更难的问题是：仅凭行为指引，能否规模化应对多数企业级代码库的复杂度。

  
## 配置悖论

 
当一个 AI agent 行为不当时，人们本能的反应是：加更多规则。别用分号。总要加错误处理。遵循这个仓库的命名约定。倾向函数式范式。启用 TypeScript strict mode。

 
这一本能催生了规模惊人的生态。一个流行的 GitHub toolkit 列了135 个 agents、35 个精选 skills、40 万+ marketplace skills、176 个 plugins、42 条 commands。另一个提供了30 个专门 agent 与 136 个 skills。现在至少有五种互相竞争的配置格式： `CLAUDE.md` 、 `AGENTS.md` 、`.cursorrules` 、 `copilot-instructions.md` 、`.windsurfrules` 。甚至还有在不同格式间转换规则的工具。

 
这个生态的“配置项”比多数团队的工程师人数还多。

 ![作者制图：配置悖论——Agent 质量在较少规则时峰值，随后随规则增多而下降](https://mmbiz.qpic.cn/sz_mmbiz_png/Cic4GFNZLlxpb1vVOoD627uMKH7tibibGCEwVNqIRSSQraz4FYibNknuwxdicFtttlQmicN3vJFicMDWH0tsCYcdXzBTeLshdMmMCBvDiaI46j0MV0M/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5) 作者制图：配置悖论——Agent 质量在较少规则时峰值，随后随规则增多而下降 
问题是：它并不会按你以为的那样“随增随优”。Claude Code 把单个规则文件限制在 6,000 字符、总规则合计 12,000 字符。存在这些限制是有原因的。过了某个阈值，再加规则只会让 agent 更困惑，而非更守规矩。Anthropic 的文档说得很直白：“对每一行都问：‘删掉它会让 Claude 犯错吗？’如果不会，就删掉。”

 
把它想象成新同事入职。你可以给他一本 50 页的员工手册，覆盖所有可能场景；也可以只告诉他四条公司真正在践行的原则，并信任他的判断。手册会进抽屉，原则却会被用起来。

 ![作者制图：规则 vs 原则——一份臃肿规则文件 vs. 4 条行为基线](https://mmbiz.qpic.cn/sz_mmbiz_png/Cic4GFNZLlxrUiamp9P7senqxDh2SI33NKDPw97I7w2xVgC1TdP85YdXNdhia3jfFibAWjnq98fx6KyYUBtibCmepxnEGs6Q41NsnX8pnk3PMwM0/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6) 作者制图：规则 vs 原则——一份臃肿规则文件 vs. 4 条行为基线 
这就是“配置悖论”：更多规则“看起来”更可控，但在行为基线之外，它们会制造噪声，与信号争夺注意力。那 5.5 万颗星，不是为“极简”这个美学投票，而是在为一个洞见投票：行为约束优于功能清单。

 
这 4 行之所以有效，是因为它们塑造的是 agent 的“思考方式”，而非“具体做什么”。它们可迁移于不同项目、语言与问题类型。一条“使用 TypeScript strict mode”只适用于某个技术栈；“不要假设”适用于一切。

 
## 你的文件里该放什么

 
最快路径：直接安装最初那个 repo 里的文件。

 
Option A：Claude Code Plugin（推荐）

 
在 Claude Code 内添加 marketplace 并安装：

 
```
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

 
这样这些指引会自动对你的所有项目生效。

 
Option B：直接下载文件

 
新项目：

 
```
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
```

 
已有项目（追加到你当前文件后）：

 
```
echo "" >> CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

 
完整版文件会把每条原则展开成若干子要点与示例。但核心仍是那四条单行句。其余都是阐释。

 
在行为基线就位后，再在上面加一层很薄的“项目特定上下文”。不是“如何写代码”的规则，而是 agent 无法仅靠读文件就推断出的上下文。

 
Build commands。agent 需要知道如何运行你的项目：

 
```
## Project
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint -- --fix`
```

 
代码里看不出的约定。那些在现有代码中不可见的决策：

 
```
## Conventions
- API errors return { error: string, code: number }, never throw
- All dates stored as UTC, displayed in user's timezone
- Feature flags live in config/flags.ts, not inline
```

 
从失败中学到的教训。对曾经出过问题的“一句提醒”：

 
```
## Watch out
- The payments service timeout is 30s, not the default 5s
- Don't import from /internal -- it breaks the public API build
```

 ![作者制图：CLAUDE.md 解剖——行为基线 + 薄薄一层项目信息](https://mmbiz.qpic.cn/mmbiz_png/Cic4GFNZLlxq7r6wLAFLvorj85Zn0vGicCe8bTTJ8mvDb9eTQuBEkApAoTrAosYW2zrtKGYzVglDic6icx5nwkZkMVyJqTK1XMmWAEFplzt4q3o/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7) 作者制图：CLAUDE.md 解剖——行为基线 + 薄薄一层项目信息 
就这样。来自 repo 的行为基线、build commands、少量约定、也许再加一条告警。对你想在“四行之外”新增的每一行做“火焰试验”：删了它，会不会让 agent 犯下它无法自我纠正的错误？如果不会，就别加。

 
不要放进文件的东西：agent 读代码就能得出的架构综述、能从现有模式里推断的风格指南、能在 `package.json` 里找到的依赖清单、或仓库里本就能访问到的文档。agent 会读你的代码库，别重复已有信息。

  
## 何时“四行”不够用

 
这些指引很好地覆盖了“行为层”。但行为不是唯一一层。

 
复杂的多文件重构。当你要重组整个模块、在文件间搬迁函数、更新 import 链时，agent 需要的是行为指引之外的“架构上下文”。“不要假设”无法解决“谁依赖了谁”的问题。对于大型重构，你要么在 `CLAUDE.md` 里补一段简短的架构说明，要么把工作切分为多个小而清晰、agent 能逐一完成的任务。

 
受监管行业。如果你在医疗、金融科技或其他合规要求严格的领域，“绝不记录 PII”“所有 API 变更需安全审查”这类条款不是这四条能覆盖的。领域特定的护栏与行为指引是不同维度。把它们与这 4 行并列添加，而不是替代它们。

 
团队规模一致性。一个开发者的 `CLAUDE.md` 很简单。要让 20 位工程师为各自的 agent 共识共享行为规范，这是协调问题，不是配置问题。这时像 `AGENTS.md` （检入仓库、工具无关）这样的格式开始变得重要。四行是团队的起点，但团队还需要就哪些“项目特定规则”叠加在上面达成一致。

 
工具可迁移性。这些指引是为 Claude Code 写的。Cursor、Copilot、Codex 有重叠但各自不同的失败模式。原则可迁移。“不要假设”对任何 agent 都是好建议。但具体的措辞及 agent 对它的响应程度会因工具而异。若你用 Cursor，需要把这些原则改写为 `.cursorrules` 格式，并验证 agent 是否以同样方式理解它们。

 ![作者制图：何时该超越四行](https://mmbiz.qpic.cn/mmbiz_png/Cic4GFNZLlxrPg4km51UoFDSrtrgsAAvw02Xy0TvbABdyiaM02knkSdLbnPUUc8MlibB1jYy30m40kchvaM2fNKrCWUOySicuFUQsfHeeIDfB1I/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8) 作者制图：何时该超越四行 
再坦诚一点：6 万颗星说明“共鸣”，不等于“功效证明”。我们并没有严谨的前后对照基准，来量化这些指引能把输出质量提升多少。有人声称使用 Karpathy 指南可达 94% 准确率，但在把它当成定论前，我会先看方法学。我们现在拥有的是来自大量开发者的强烈轶事共识。这很有意义，但不是受控实验。

  
## 行为层的瓶颈

 
一个文本文件能收获 6 万星，说明了产品发布所不能说明的：AI 辅助编程的瓶颈从来不是能力，而是行为。

 ![作者制图：能力 vs 行为——四行所在的，是能力与行为之间的鸿沟](https://mmbiz.qpic.cn/mmbiz_png/Cic4GFNZLlxrvqYolsY1XH7iahA5lTm3bk9YEsQdqg5icprpQDQljuaqjDaN93JZe1aJ1ZwruV9jeF8whCjFkrphicFyCjqWZhQLh5wB0XKEYGM/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9) 作者制图：能力 vs 行为——四行所在的，是能力与行为之间的鸿沟 
模型会写代码，而且已经会写一阵子了。它们不可靠的是：何时该停笔、开始前该问什么、该改到什么程度、以及如何验证“已完成”。这些是行为问题，不是智力问题。行为问题不靠让模型“更聪明”来解决，而靠告诉模型“该如何行动”。

 
这就是为什么四句话能胜过一整个 plugins、agents 与 skills 的生态。并不是说生态错了，它没错。只是它在解“能力层”的题，而“行为层”依然是束缚全局的约束。

 
每一次模型升级都有帮助。但在 agent 能可靠地管理自己的不确定性、收敛自己的改动范围、并验证自己的工作之前，这 4 行仍会以每个字符最大化地创造价值，胜过任何“新功能”公告。

 
如果让我明天真要改点什么：打开我的 `CLAUDE.md` ，删掉所有 agent 能从代码库里自己推断出来的规则，如果还没写上这 4 行行为基线，就补上它们；以后每当我想再加一条规则，就只问一个问题：它是在塑造 agent 的“思考方式”，还是仅仅规定它“要做什么”？若是后者，它大概率不该进文件。

 
如果你想深入，repo 的 EXAMPLES.md 有每条原则的完整 before/after 代码演练，包括第 4 行的多步验证模式。

 
模型会继续变聪明，工具会继续更强大。瓶颈会一直停留在“行为层”，直到模型学会管理自己的判断。在那之前，一份 Markdown 文件里的四句话，依旧会胜过产品发布周期。

  
 继续滑动看下一个 

 
 PyTorch研习社 

 
 向上滑动看下一个