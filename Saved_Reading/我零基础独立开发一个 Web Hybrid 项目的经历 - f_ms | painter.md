> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [imf.ms](https://imf.ms/web/2022/07/05/my-first-web-hybird-project-experience/#%E8%83%8C%E6%99%AF)

> painter

*   [背景](#%E8%83%8C%E6%99%AF)
*   [前置知识学习阶段](#%E5%89%8D%E7%BD%AE%E7%9F%A5%E8%AF%86%E5%AD%A6%E4%B9%A0%E9%98%B6%E6%AE%B5)
    *   [HTML](#html)
    *   [JavaScript](#javascript)
    *   [TypeScript](#typescript)
*   [基础框架学习阶段](#%E5%9F%BA%E7%A1%80%E6%A1%86%E6%9E%B6%E5%AD%A6%E4%B9%A0%E9%98%B6%E6%AE%B5)
    *   [React](#react)
    *   Ionic / Capacitor
    *   [工具库](#%E5%B7%A5%E5%85%B7%E5%BA%93)
*   [项目各基础设施封装](#%E9%A1%B9%E7%9B%AE%E5%90%84%E5%9F%BA%E7%A1%80%E8%AE%BE%E6%96%BD%E5%B0%81%E8%A3%85)
    *   [数据验证器](#%E6%95%B0%E6%8D%AE%E9%AA%8C%E8%AF%81%E5%99%A8)
        *   [yup](#yup)
        *   [Zod](#zod)
    *   [页面路由](#%E9%A1%B5%E9%9D%A2%E8%B7%AF%E7%94%B1)
    *   [表单](#%E8%A1%A8%E5%8D%95)
    *   [各种 “积木” 工具组件的封装](#%E5%90%84%E7%A7%8D%E7%A7%AF%E6%9C%A8%E5%B7%A5%E5%85%B7%E7%BB%84%E4%BB%B6%E7%9A%84%E5%B0%81%E8%A3%85)
*   [项目实际业务功能开发](#%E9%A1%B9%E7%9B%AE%E5%AE%9E%E9%99%85%E4%B8%9A%E5%8A%A1%E5%8A%9F%E8%83%BD%E5%BC%80%E5%8F%91)
*   [移动端本地能力适配](#%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%9C%AC%E5%9C%B0%E8%83%BD%E5%8A%9B%E9%80%82%E9%85%8D)
*   [UI 美化](#ui-%E7%BE%8E%E5%8C%96)
*   [热更新能力集成](#%E7%83%AD%E6%9B%B4%E6%96%B0%E8%83%BD%E5%8A%9B%E9%9B%86%E6%88%90)
*   [持续集成、自动交付](#%E6%8C%81%E7%BB%AD%E9%9B%86%E6%88%90%E8%87%AA%E5%8A%A8%E4%BA%A4%E4%BB%98)
*   [旧版本浏览器、设备适配](#%E6%97%A7%E7%89%88%E6%9C%AC%E6%B5%8F%E8%A7%88%E5%99%A8%E8%AE%BE%E5%A4%87%E9%80%82%E9%85%8D)
    *   [浏览器端适配](#%E6%B5%8F%E8%A7%88%E5%99%A8%E7%AB%AF%E9%80%82%E9%85%8D)
        *   [JavaScript 语法兼容](#javascript-%E8%AF%AD%E6%B3%95%E5%85%BC%E5%AE%B9)
        *   [JavaScript API 兼容](#javascript-api-%E5%85%BC%E5%AE%B9)
        *   [跨域 CORS 配置](#%E8%B7%A8%E5%9F%9F-cors-%E9%85%8D%E7%BD%AE)
    *   [设备端适配: 内置 Webview 内核](#%E8%AE%BE%E5%A4%87%E7%AB%AF%E9%80%82%E9%85%8D-%E5%86%85%E7%BD%AE-webview-%E5%86%85%E6%A0%B8)
        *   [集成 TBS 的在线版本到项目中](#%E9%9B%86%E6%88%90-tbs-%E7%9A%84%E5%9C%A8%E7%BA%BF%E7%89%88%E6%9C%AC%E5%88%B0%E9%A1%B9%E7%9B%AE%E4%B8%AD)
        *   [将 TBS 魔改为离线集成](#%E5%B0%86-tbs-%E9%AD%94%E6%94%B9%E4%B8%BA%E7%A6%BB%E7%BA%BF%E9%9B%86%E6%88%90)
*   [性能优化](#%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96)
*   [一些想法](#%E4%B8%80%E4%BA%9B%E6%83%B3%E6%B3%95)

背景[](#背景)
---------

我是一名 JAVA 后端开发，之前也有过一大段时间安卓开发的经历。

21 年 9 月中旬，应公司需要以及我自身的争取接受了一个任务：居家办公，使用半年左右时间，在没有任何前端基础的情况下，将已有的 安卓原生、iOS 原生、Web 三端项目，以 Hybrid 混合开发的模式重写，同时适配 PC 大屏幕、平板中屏幕和手机小屏幕，最终由同一套 Web 代码来维护三个平台的客户端。

之所以自身争取该任务的原因，是我一直会有蛮多自己的软件想法上的小九九，但奈何没有对应能力独立开发出一个完整的项目，所以想通过此项目激自己一把，把前端相关的技能补上，成为一个名义上的全栈程序员，无惧心中小九九。

这过程中学习、接触了很多很多东西，有一些很珍贵的经历，我将它们予以记录，希望能给同样要做混合开发的同学们多少有一些些的帮助。

前置知识学习阶段[](#前置知识学习阶段)
---------------------

首先自然是对前端最基础的 HTML、CSS、JS 的学习，虽然平时耳濡目染但也确实是没有实际系统学习过。

### HTML[](#html)

我通读了文档 [网道文档 - HTML](https://wangdoc.com/html) ，了解了组成页面结构、元素的各标签。

然后跟着 [Learn to Code HTML & CSS](https://learn.shayhowe.com/html-css/) 和 [Learn to Code Advanced HTML & CSS](https://learn.shayhowe.com/advanced-html-css/) 跟着做了练习。但跟完又感觉这教程好像有些旧了，一些新特性都没有被涵盖进来，然后又发现了 [HTML Dog](https://htmldog.com/)，看起来更现代也一直在更新的样子，但自己已经没心思再跟一遍新的了。

之后通过 MDN 文档 学习了 [Flex](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Flexible_Box_Layout) 和 [Grid](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Grid_Layout) 布局，之后还发现了一个挺有意思的练习游戏，但内容不深：[Flex Study Game](https://codepip.com/games/flexbox-froggy/#zh-cn)、[Grid Study Game](https://cssgridgarden.com/#zh-cn).

### JavaScript[](#javascript)

我通读了文档 [网道文档 - JavaScript](https://wangdoc.com/javascript) ，虽然已经对 JS 有了足够的心理准备，但在过程中还是会频频皱眉，小小的脸上不停出现大大的问号：

*   这 `undefined` 和 `null` 到底有啥区别？ 有个 null 就够受的了为啥又搞出来了个 undefined？
*   这 `NaN` 的存在到底又是个啥意义？一个特定于 number 的 null ？这玩意儿直接用异常机制来处理不就行了吗？
*   `Infinity` 代表 number 的无穷？还分为 +Infinity 和 -Infinity? 这……
*   变量默认全局作用域 ？
*   `typeof array` 的结果是 object 我理解可能是类型模型的统一性，那 typeof null 的结果为啥也是 object?
*   空字符串转为 boolean 是 false, 那凭啥空数组就是 true 了？
*   字符串字面值可以用单引号，也可以用双引号，但功能都一模一样为啥要搞两个出来？就为了单引号中能不转义用双引号、双引号中能不转义用单引号？
*   咋这么多 “类似” 数组但不是数组的数组？
*   居然可以 throw 任何东西？ Error 类型没有 cause?
*   这继承的模式 …… 咋感觉这么别扭呢？
*   我咋导包？

但也发现了一些有意思的地方：

*   object 的 key 可以是任意字符串 这样的话把 object 当数据结构直接用的场景就被大大拓展了，在 JAVA 的时候字段的名称受到基础的标志符命名限制，很多字段名在映射的时候是无法直接使用的。

随后学习了 ES6 的标准，通读了文档 [网道文档 - ES6](https://wangdoc.com/es6)，这下感觉好多了，虽然很多历史包袱没法变更，但很多编程语言 “应该是” 和“应该有”的东西被加进来了，还有了一些之前未曾接触过的特性：

*   解构赋值、扩展运算符 很有意思的特性，刚开始有点排斥，后来开发过程中真香
*   null/undefined 相关的运算符 const foo = fun?.()?.field ?? ‘default’ 真甜，Java 啥时候能直接支持呢？
*   symbol 支持创建一个特有唯一`标志`，可以作为 object 的唯一 key 而不造成命名冲突，但也不仅限于此 刚开始有点不理解这个特性，但后来的实际项目开发中发现确实是有其存在的意义的，除了命名冲突外，还能承载一些`私有`属性的功能。
*   Proxy cool, 居然可以直接代理对象的 has/get/set ，你管我是个啥，反正我能装的像~

### TypeScript[](#typescript)

JavaScript 是弱类型语言，通过实际测试使用情况和以前使用弱类型语言的经验，自己实在是无法在纯弱类型语言情况下进行开发，有太多的内容需要自己去关注、太多的问题需要自己在运行时去发现。

遂通过[官方文档](https://www.typescriptlang.org/)对 TypeScript 进行了学习，这过程中我对类型系统着实是开了眼界。

*   结构型类型匹配 代表着只要结构相同，不管是不是基于同一个父类型，也认为类型相同。 想起了自己用 JAVA 时完全相同的结构但不同的类型，想互通时得写各种适配器的痛苦~ 但 JAVA8 的 lambda 表达式倒也提供了一些有限的结构型匹配写法。
*   空指针安全 之前一直有听说过一些语言层规避 NPE 的方案，但一直没有实际落地用过，结果是：真香，感觉光为了这个就值得以后学学 Kotlin 了。
*   联合类型 还能这样？？？这也太有用了吧！！！我已经想象到用 JAVA 时想给变量声明不同的类型的痛苦了。
*   值类型 这样也行？？？这个也很有用哈！！！直接把类型限制到几个实际值里面，对提供者和使用者都减少了太多负担。
*   类型别名 & 各种类型操作符 TS 提供了很多类型操作符诸如 keyof 、typeof 、ConditionalType、MappedType… 初读很不理解这么多类型操作符有啥实际使用场景，后来实际开发中发现又是大型真香现场，这些操作符使类型有了动态能力可以各种组合使用，从而更大限度的达到代码的类型安全。 回想用 JAVA 时，想类型安全的在枚举之外给每个枚举项维护一个映射值都不行。

学习时有很多不理解的地方，主要是因为受到了 JAVA 类型系统的影响，思想上先入为主了，在项目之后实际的开发中，慢慢熟悉熟练了 JS 后才理解了 TS 为什么这么设计。种种特性带来了很多好处但也带来了一些问题：

*   结构型类型匹配在想要区分相同结构但不同类型会挺麻烦。
*   联合类型及各种类型操作符复杂联用时，想要排查具体匹配到的类型、或为什么没匹配到指定类型时很头大，IDE 也很难给出容易理解的错误提示，甚至到后来 IDE 对类型提示及补全提示的分析已经很迟钝了，从 IDE 的补全提示比我打字快到我最后需要主动等提示，有时复杂的情况下甚至补全提示直接摆烂。 另外经对比，在 TS 的类型匹配、补全提示上 VS Code 做的比 WebStorm 更好一些。

当然是可以理解的，设计总会有成本，新增了特性解决了以前无法解决的问题，同时也必然了类型系统的复杂性。

基础框架学习阶段[](#基础框架学习阶段)
---------------------

基础知识掌握的差不多了，之后是学习实际要使用的框架、工具库。

### [React](http://reactjs.org/)[](#react)

之前在同事那里有了解过 VUE, 但感觉写法上很不喜欢，声明一个 “组件” 有些重，生命周期等内容写起来有些繁琐，也不支持 TypeScript。(因为对 VUE 并没有真正的深入使用过，所以对 VUE 的主观感受可能有失偏颇)

随即转向了 React ，通读了 [React 官网文档](http://reactjs.org/)，很喜欢，开心的决定了使用 React 当做项目的前端框架。React 有很多我喜欢的优点：

*   UI 组件只是 JS 中的普通 “元素”：一个函数、一个 Class，可以任意传递任意处理，而非模板类框架将组件定义为 JS 外的一个 “特例”。这使得开发者可以使用 JS 语言本身的全部能力：面向对象、组合、封装、设计模式等。 实际官方也推荐了类似的用法，例如 [组合 vs 继承](https://reactjs.org/docs/composition-vs-inheritance.html)、[高阶组件](https://reactjs.org/docs/higher-order-components.html)。
*   UI 组件足够小，小到甚至可以只有一个函数。
*   巧妙的 Hook API, 可以将框架提供的各项能力例如生命周期能力 “勾” 到函数组件中，同时可以使用 hook 来组合更强大的能力，与 Class 类似的繁重组件比起来异常优雅。
*   支持 TypeScript。
*   有大量的社区库。

实际使用体验也很棒，从 JAVA 积攒的各种组合、封装、复用经验都能直接套用。

与更集成化的 Vue 对比的话，Vue 对初学者蛮友好，Vue 有很多开箱即用的功能：路由、Scope CSS 等。这些在 React 中则要费些心思去社区寻找合适的库并集成。

### [Ionic](https://ionicframework.com/) / [Capacitor](https://capacitorjs.com/)[](#ionic--capacitor)

Hybrid 混合开发框架，支持 React, 提供了 UI 组件、Android/iOS 运行容器的支持、各类混合开发需要的原生交互插件。我也是直接通过官方文档进行的学习。

在后来的开发过程中，体会到了它带来的很多好处，但也真的带来了很多坑，如果再选一次的话，我可能会再认真看看其它框架：

*   官方提供的 UI 组件很不灵活、扩展性差，后来美化阶段全换成了 [MUI](https://mui.com/)
*   社区和网上支持更多以 Angular 为主， React 相关的内容鲜少
*   框架开放的自由定制 API 少，实际使用不灵活，资料也不多
*   不影响使用的奇怪 BUG 也蛮多
*   官方插件的国际化支持不友好，BUG 也不少，ISSUE、PR 不活跃。所以后来为了方便修改，很多库都是在项目代码里本地集成，提升了很多复杂度。

### 工具库[](#工具库)

*   [Loadsh](https://lodash.com/) 前端三方基础库，有各种工具方法。但感觉对 TS 的类型声明不太完善，很多复杂的函数比如 `chain` 的类型声明感觉都很草率…… 只有最基础的内容。
*   [rx.js](https://rxjs.dev/) 虽然换了语言，但 rx 不能换。另外由于 Promise 不支持 cancel , 所以 rx.js 也算是对需要 cancel 的任务的替代品（例如网络请求）。
*   [Axios](https://github.com/axios/axios) 网络请求库，可能没有对比所以没感觉有什么特殊的地方，在项目实际使用中也被我又用 rx.js 封装了一层，所以没有太大的存在感。
*   [React Hook Form](https://react-hook-form.com/) React 表单工具库，涵盖封装了表单的状态维护、数据验证、性能优化等各项功能，灵活强大。最终项目中几乎所有的表单业务都是由该库处理的。
*   [make-error-cause](https://github.com/blakeembrey/make-error-cause) JS 的 error 没有 cause，找到了这个替代品。

项目各基础设施封装[](#项目各基础设施封装)
-----------------------

### 数据验证器[](#数据验证器)

在封装基础网络请求时，遇到了对服务器响应结构类型的验证问题。

在 JAVA 中，一般直接将响应数据映射到一个新建的 Model Bean, 在三方库 (例如: GSON, Jackson) 映射过程中就相当于对数据结构和类型做了基础校验，然后可以使用 JSR303 对内容进行校验。

但在 JS 中，服务器响应数据在解析后会被直接转换为 JS 中对应结构和类型，TS 的类型信息运行时被抹除无法利用，所以只能交给程序员自行处理，并且还要考虑对 TS 类型的支持，会产生很多复杂性。

检查搜索后发现也有蛮多开源解决方案，怎么能造轮子呢，我要为开源世界多贡献一份人气。

#### [yup](https://github.com/jquense/yup)[](#yup)

首先发现了验证库 [yup](https://github.com/jquense/yup), 认真读完了 readme, 我想到的我没想到的都给做了，确认过眼神是我要找的人，很开心的吭哧吭哧集成到项目中各个基础设施中。可集成结束后，临下班了，突然发现一个问题：[yup 不保证链式验证的顺序](https://github.com/jquense/yup/issues/851)，类似后面验证依赖前面验证的情况都会存在问题，这样的话实际复杂验证的情况下如果每个验证都要考虑前置条件的话会耗费很大心力，于是决定还是再找找其它对眼神的人。

#### [Zod](https://github.com/colinhacks/zod)[](#zod)

通过 React Hook Form 的验证器集成文档中发现了更年轻一些的 [Zod](https://github.com/colinhacks/zod) ，又一次认真读完了 readme, 并特意测试了链式顺序，果然不俗，确认过眼神又是我要找的人。

Zod 的设计是 TS 优先的 ，支持从 schema 导出 TS 类型。Zod 的预定义的校验都是尽可能的贴合 TS 的类型，除了 string, number, object, literal, null, undefined 等基础类型还提供了 record, tuple, map, promise, function, enum 等日用类型。更强大的是还提供了 union, and, merbe 等常用类型操作符的支持。 由于 Zod 对 TS 的各种类型及操作符都提供的校验能力，并且 schema 可以直接导出为 TS 类型，所以在实际使用中，对于需要运行时保证类型信息的任何场景，都可以直接使用 ZodSchema 来替代，由 TS 来保证编译时类型安全，Zod 来保证运行时类型安全。

这里有一个使用示例：

```
// TS 类型声明
type TsUserType {
  name: string, age: number | undefined, gender: "man" | "woman",
  identity: {
      type: "student", clazz: string
  } | {
    type: "programmer", language: "JAVA" | "C++"
  },
  attrs: {[key: string]: string},
}

// Zod 校验 Schema
const UserSchema = z.object({
  name: z.string(),
  age: z.number().optional(),
  gender: z.union([
    z.literal("man"), z.literal("woman")
  ]),
  identity: z.union([
    z.object({
      type: z.literal("student"),
      clazz: z.string(),
    }),
    z.object({
      type: z.literal("programmer"),
      language: z.union([
        z.literal("man"), z.literal("woman")
      ]),
    }),
  ]),
  attrs: z.record(z.string(), z.string()),
})

// 从 schema 导出 TS 类型
type ZodUserType = z.infer<typeof UserSchema>
// ZodUserType 与 TsUserType 结构将相等，实际使用中无需单独重复声明 TS 类型，可直接从 schema 中导出类型使用
```

并且 Zod 支持对数据转换且保留转换后的类型信息，在实际书写验证规则的时候非常灵活：

```
const TransformSchema = z.string().transform(value => ({value: value}))
// z.input<typeof TransformSchema> == string
// z.infer<typeof TransformSchema> == { value: string }
TransformSchema.parse("Hello World!!!")
> { value: "Hello World" }
```

经进一步使用，发现 Zod 没有直接提供数据类型隐式转换的能力，例如 字符串 `'1'` 对于 `z.number()` 来说，虽然字符串类型与数字类型不匹配是应该校验失败的，但是有些场景其实不怎么关心原始数据类型，只要能转为目标类型即可。例如对于服务器响应数据来说，string(1) 如果能自动转换为 number(1) ，反而能提高前后端接口交互的灵活性和健壮性。

Zod 提供了 [preprocess](https://github.com/colinhacks/zod#preprocess) 方法来对原始数据进行预处理，所以最终我使用了该能力封装了常见数据类型的隐式转换逻辑: `zc.toString()`, `zc.toNumber()`, `zc.toEnum()` …

最终对网络请求封装后的使用示例如下：

```
api
  .get({
    url: "/user",
    param: {...},
    dataSchema: z.object({
      name: zc.toString(),
      age: zc.toNumber(),
      phone: zc.phone()
    })
  })
  .subscribe(user => {
    // typesafe: user == {name: string, age: number, phone: string}
    ...
  })
```

### 页面路由[](#页面路由)

Ionic 的 React 版本定制绑定了三方开源路由库 [React Router](https://reactrouter.com/)，不过实际使用时与原库没多大差别。

React Router 提供的路由分发能力很棒，但在学习的过程中，我发现路由的维护工作也是一个难题：

*   应用中都有哪些路由，URI 及匹配规则是怎样的？
*   每个路由对应哪个页面组件？
*   路由有哪些参数，参数的传递方式是怎样的，每个参数的数据类型又是什么？

参考了很多开源项目对 React Router 的使用，发现大多都是直接使用硬编码，并没有做什么处理。考虑了下觉得这样实在太容易出错，作为一个基础设施还是应该有一个类型安全的统一方案。

最终我对项目路由作了如下设计达到了路由信息的类型安全：

1.  收集整个项目的路由类型信息 声明一个名为 Routes 的 object 空类型，通过 TS 的 [Declaration Merging](https://www.typescriptlang.org/docs/handbook/declaration-merging.html) 和 [Module Augmentation](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#module-augmentation) 特性，在每个需要路由的页面组件中，以路由的 URI 值作为 key 的类型，路由的所需参数、详细配置项等为值类型，对 Routes 类型进行补充声明。这样项目所有的路由及其配置项的类型信息则被统一合并收集到了 Routes 类型中。
2.  实际落地记录路由信息 由于 Routes 只是类型信息，而 TS 在编译后类型信息会被全部抹除，运行时无法感受到 Routes, 所以以 Routes 类型维护了一个实际值 RouteTable 在运行时使用，它以 Routes 为类型，落地记录了整个项目每个路由的配置信息，每当页面中对路由类型声明有了变更，在 RouteTable 中都要作相应的同步，对于带参数的路由还需提供 toUri 函数 (param) => string 以将参数转换为具体 uri。
3.  将路由信息配置到路由框架 直接在应用入口通过遍历 RouteTable 获取路由配置信息将整个项目路由配置到 ReactRouter。
4.  为项目中使用路由信息跳转页面时提供类型安全的方法 使用 TS 的 [Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html) 对 Routes 类型进行处理，应用到 getUri 函数 (uri, param) => string，其中 uri 参数对应 Routes 的 key (即路由 uri)，param 参数对应该 uri 对应页面所需要的具体参数，实现代码为调用该 uri 在 RouteTable 配置的 toUri 函数并将结果返回。
5.  为路由页面组件透明提供地提供路由参数的解析、验证及转换能力 编写高阶组件 withRoute(component, schema)：将 URL 中各个部分的参数取出，根据 Zod Schema 参数使用验证库对参数进行验证、转换，最终无误后作为 props 提供给实际页面组件。

也是在落地该方案后，开始感受到了 TS 的那些类型操作符的大用所在。

### 表单[](#表单)

试着手写了个表单页，写的我怀疑人生。数据双向绑定，页面的展示依赖于数据，每个字段都要声明一个组件变量，每个对应控件也都要指定对应的变更监听，当然每个字段变更也会导致整个组件重新渲染。如果使用传统方法直接拿到控件对象也是很麻烦并且 React 也不推荐操作 DOM 类似的写法。

开源是我的好朋友，他给我介绍了 [React Hook Form](https://react-hook-form.com/), 真好，遇到的问题都被解决：React Hook Form 系统对表单状态、字段状态、数据校验、性能优化等等等都做了封装，对各种常见的表单需求提供支持，并对表单实际使用中的各个部分提供了足够的类型安全。

我在项目中对各种日用组件为 React Hook Form 作了二次封装，得益于 TS 类型系统的强大，中间对公共参数、组件私有参数的各种增减处理重声明非常简洁，如果是 JAVA 的话怕是得新建各种四不像的 Bean 了。

但也是在使用 React Hook Form 期间开始发觉了 TS 强大的类型系统带来的复杂性：一些复杂的情况，类型匹配错误我已经很难根据各种类型操作符来判断到底是哪里错了。再到了后来，连编译器、WebStorm 都开始对类型补全、错误提示变的迟钝。

### 各种 “积木” 工具组件的封装[](#各种积木工具组件的封装)

从安卓开发期间积攒来的经验，将常见的逻辑封装为组件，实际使用时只需像堆积木一样各种组合就可以快速健壮的堆起来各种功能，可以极大地提升开发效率。

得益于 React Hook API 对 生命周期等能力的封装，比安卓有更多的封装姿势。

*   Dialog
    
    *   命令式调用，自动管理展示、关闭状态
    *   自动跟随 Page 生命周期，Page 不可见时隐藏 Page 下 Dialog，Page 被关闭时关闭 Page 下 Dialog
    *   支持指定异步行为，并管理 Progress/Error 状态展示、避免内存泄露 Dialog 被关闭时 cancel 未完成的异步行为
*   StatusComponent 不同状态展示不同 UI 的组件的封装，支持类型安全的定义状态列表、状态对应的参数类型和 UI 渲染器
    
*   AsyncDataComponent
    
    需要先异步获取数据组件的封装：
    
    *   对数据请求状态 Loading/Error 的处理与展示，复用了 StatusComponent
    *   避免内存泄露，组件被卸载时 cancel 所有未完成的请求
    *   支持下拉刷新
*   AsyncListDataComponent
    
    复用了 AsyncDataComponent, 对需要先异步获取列表类数据组件的封装：
    
    *   分页逻辑、数据追加逻辑
    *   支持上拉加载更多
    *   各种 List 渲染器：列表、平铺、带索引、可手动切换……
*   SearchableAsyncListDataComponent
    
*   SelectableAsyncListDataComponent
    
*   ……
    

项目实际业务功能开发[](#项目实际业务功能开发)
-------------------------

该学的都学了，该准备的也都准备了，开始正式推进工作进度。

因为到目前我学到的美化技能明显很弱，但代码逻辑上有之前安卓的沉淀，为了加快速度和集中工作方向，决定这个阶段不考虑任何页面美化，只写功能和页面基础结构，但业务功能必须是完备的，不能偷工减料增加后期的美化、验收阶段的工作量。

业务功能开发阶段前期还是蛮有意思的，因为什么都是全新学习的，所以会不停的在实际开发中发现新问题、思考解决方案、学习必要的新技能、集成封装落地 ……

但到了中后期时，大多问题也都已经被遇到和解决了，不再有什么 “魔法” 和“怪兽”，工作逐渐趋于枯燥。与之前同样的每一天，同样的窗外风景，却是完全不同的感受。

移动端本地能力适配[](#移动端本地能力适配)
-----------------------

因为是混合开发项目，最终要打包安卓版本和 iOS 版本，所以要对各端的通用能力、特有能力进行适配。

我没做过苹果开发，所以初期考虑自己先适配安卓，我自身把所有的坑踩完，然后约个苹果开发的朋友适配 iOS 端。

但在安卓适配过程中，发现常用能力的插件 [Capacitor](https://capacitorjs.com/) 官方有提供或三方也有现成的，大多都同时适配了安卓端和 iOS 端。想着反正都要经历一遍，为何不集中一点？就捡起了苹果电脑，对常用能力同时适配安卓和 iOS, 我做的越多后期朋友可以做的少些。

返回键响应、左滑返回、分享、相机、图片选择、图片编辑、文件选择、文件上传、下载、打开本地文件、定位、地图、推送、红点徽标、错误报告、统计分析 ……

虽然大多能力都能找到官方或三方插件，但问题也挺多：质量参差不齐、已过时、功能欠缺…… 所以有很多库都被我下载后本地集成，修改成需要的样子，为项目新增了很多复杂度。

另外在适配苹果端时为了解决在两台电脑之间难以同步互相变更的问题，发现一个很有用的双向文件同步工具 [Unison](https://www.cis.upenn.edu/~bcpierce/unison/), 极大的提高了开发效率。

窗外日升日落，日子一天天过去，我把每个功能不停的在 PC 浏览器端、安卓端、苹果端、安卓浏览器端、苹果浏览器端、微信端反复调试，我把适配工作表上的内容一项项打钩，日子略有繁琐。

UI 美化[](#ui-美化)
---------------

是时候给彩虹上色了。

之前的 CSS 知识已经尽数归还，遂又捧起 MDN 把 CSS 重学了一遍。不得不说，CSS 美化界面的能力比安卓强的不是一星半点，很多安卓中实现很麻烦的效果在 CSS 里也就是三两行，优雅又强大。

然后是选择一个 UI 组件库，中间选了很多个库，也发现了很多问题：

*   [Ionic](https://ionicframework.com/) 自带的组件库限制很多，使用起来很不灵活，PC 端效果也欠佳
*   初期选择的 [Ant Design Mobile](https://mobile.ant.design/) 也是一言难尽，各部分 API 不统一不规范，效果也只适合手机端
*   [Ant Design](https://ant.design/) 各部分比 Ant Design Mobile 的设计要好很多，但效果只支持电脑端
*   [Element UI](https://element.eleme.cn/) 只支持 Vue, 看起来手机端效果不合适

最后在 Github 发现了 buling buling 的 [MUI](https://mui.com/)，着实让我眼前一亮，太多太多优点了，可以说跟这个一比，其它的 UI 组件库都没了颜色：

*   好看！ 遵循 Material Design 风格
*   效果同时兼顾 PC 端和手机端 组件在大屏小屏都有良好的效果，特殊组件还有针对手机端的 UI 设计
*   统一的 API 设计及风格 没有 “特例”，没有多余的精神损耗
*   组件大而全 各种组件统统都有
*   极大的灵活性 一个大组件会尽可能把所有能更改的地方都开放出来，想怎么用怎么用
*   多种不同的 UI 定制方法 props、sx、css…… 太好用导致我的 CSS 能力其实没怎么得到锻炼，MUI 自身的相关内容就已经够用到大部分场景了。
*   主题定制除了可以指定各组件的 CSS 外，还支持指定默认属性
*   对响应式布局的良好支持
*   对常用布局的良好封装

之后就是一点点更换组件、美化各页面、适配大屏效果、优化交互。中间也感觉到了一些问题：

*   CSS 很强大，但也可能是历史包袱的原因，也有很多的 “魔法”，在某些情况下某些属性不能用或者要怎么怎么处理后才能生效……
*   CSS 解决屏幕适配问题的一般都是用 Media Query, 可关键这玩意儿的 Query 只作用于设备、系统的全局固定属性，对更精细的控制欠佳 如果能有作用于父级容器的 Query 的话就很方便了，解决屏幕适配问题会更加灵活。估计以后会成为一个标准，也看到 Chrome 有个类似的库 [container-query-polyfill](https://github.com/GoogleChromeLabs/container-query-polyfill)，但对浏览器的最低版本要求略高。
*   项目好像…… 有点开始变慢了……

界面一天天好看起来，成就感也一天天起来。好吧我承认美化工作到了后期也变的有些枯燥。

热更新能力集成[](#热更新能力集成)
-------------------

都混合开发了，肯定要吃点 Web 的红利啦，热更新安排上。

本来我以为我要做的就是从一大堆商业或开源解决方案中翻一个自己喜欢的牌子，然而现实并没有给我太多选择。

Ionic 官方提供了商业服务 [Appflow](https://ionic.io/appflow)，包含了很多功能，从构建到部署到热更新到商店，并且价格可人：$499/Month。但 Appflow 包含的东西太多了，在国内也有些水土不服，价格也不太合适。也找到了一些其它的服务 [VoltBuilder](https://volt.build/)、[Capgo](https://capgo.app/)，也都是国外服务。

还发现了一些开源项目，但大多都是只支持 Cordova，我又没那么多时间精力去定制。

后来我偶然发现一篇教程 [Implementing Code Push in Capacitor(3.x) Applications.](https://tolutronics.medium.com/implementing-code-push-in-capacitor-3-x-applications-22bd6a204a04) ，原来微软的 AppCenter 有热更新的支持叫 CodePush，巨硬威武，虽然官方只支持 Cordova 但社区有提供 Capacitor 版本的插件。我喜极而不泣，开心的按照教程注册用户，新建应用，我已经在幻想着热更新带来的红利。然鹅，新建应用时的应用类型并没有 Cordova，我来来回回看了很多遍，心想一定是我的姿势不对，可最终还是发现了 [CodePush 对 Cordova 的支持已经停止的通知](https://devblogs.microsoft.com/appcenter/announcing-apache-cordova-retirement/)，而停止时间刚好在我还在学习基础知识的那一个月。我悲上心头起，心想果然，红利都不是那么容易吃的。

我不是悲上心头起的唯一一个，在停止服务的通知的[评论](https://devblogs.microsoft.com/appcenter/announcing-apache-cordova-retirement/#comment-232)下找到了组织 [ReplaceAppCenter](https://github.com/IllusionVK/ReplaceAppCenter) , 大家在一起讨论寻找或制作一个替代性服务，因为 CodePush 的客户端相关功能都是开源的，所以方向是如果可以弄出个服务端就可以解决了。幸运的是，通过 [byronigoe](https://github.com/byronigoe) 的 [ISSUE: Solved!](https://github.com/IllusionVK/ReplaceAppCenter/issues/3) 发现原来之前就已经有项目做过这件事了：[lisong/code-push-server](https://github.com/lisong/code-push-server), 并且看项目信息很明显还是国人项目，还另外添加了一些本土化支持，但该版本已经蛮久不维护了，目前更活跃的是 [shm-open/code-push-server](https://github.com/shm-open/code-push-server) 的 Fork ，看起来还是国人维护，看到一堆歪果仁的救命稻草项目是一个国人项目，民族自豪感不禁油然而生。但 byronigoe 只在 Cordova 下测试过，所以我还是需要趟趟水看看能不能过 Capacitor 的河。

不负所望，最终被成功集成到项目中，以下是各组件详情：

*   服务端
    *   shm-open/code-push-server:v2.0.3
        *   docker image: [shmopen/code-push-server:2.0.3](https://hub.docker.com/layers/code-push-server/shmopen/code-push-server/2.0.3/images/sha256-0b7998871d5f4aa14f26ca812366adb664854e28122e24e93249790945592618)
*   SDK
    *   [mapiacompany/capacitor-codepush:037174d2c00fa1a095f1ed2a445a31ccd70815df](https://github.com/mapiacompany/capacitor-codepush/tree/037174d2c00fa1a095f1ed2a445a31ccd70815df)
*   客户端
    *   shm-open/code-push-cli:v2.5.3
        *   npm repo: [@shm-open/code-push-cli@2.5.3](https://www.npmjs.com/package/@shm-open/code-push-cli/v/2.5.3)

这其中有一些坑或 BUG：

1.  开启更新包签名验证的情况下，App 验证失败，无法执行更新行为。
    
    各种翻相关源码发现，客户端在生成更新包时，会带上内容的父目录，而
    
    服务端生成签名时则用了一个固定前缀`CodePush`
    
    , 导致 SDK 拿到更新包校验签名时发现不一致，无法完成更新，有两种解决方案：
    
    1.  将服务端生成签名时的前缀改成自己所使用的父目录名称 [https://github.dev/shm-open/code-push-server/blob/bb0a27dbe4b37329a18736327747a9c0ce89278d/src/core/utils/security.ts#L188-L189](https://github.dev/shm-open/code-push-server/blob/bb0a27dbe4b37329a18736327747a9c0ce89278d/src/core/utils/security.ts#L188-L189)
    2.  客户端生成更新包时把包父目录名称修改为 `CodePush`
2.  开启更新包签名验证的情况下，使用相同包分别发布更新到不同应用 (例如同时发布给安卓和 iOS) 时，由于内容 hash 一致，服务端会直接复用包，但不同应用预置的公钥一般不一样，所以使用相同包发布的话，后一个应用更新时会验签失败无法更新。这个属于服务端 BUG 也已经提了 [ISSUE](https://github.com/shm-open/code-push-server/issues/107) ，但一直没有进展，我也没本事修复 - - 。自行来规避这个问题的方法也很简单，在发布之前改变一下包内容即可，可以新增一个空标志文件后发布更新包。
    

实际使用方法的话除了项目自身的文档外，还参考了以下链接，大多是基于 Cordova 的内容，所以要从中摘取对自己有用的：

*   [https://tolutronics.medium.com/implementing-code-push-in-capacitor-3-x-applications-22bd6a204a04](https://tolutronics.medium.com/implementing-code-push-in-capacitor-3-x-applications-22bd6a204a04)
*   [https://github.com/lisong/code-push-server/issues/135](https://github.com/lisong/code-push-server/issues/135)
*   [https://www.jianshu.com/p/ca4beb5973bb](https://www.jianshu.com/p/ca4beb5973bb)
*   [https://github.com/crazycodeboy/RNStudyNotes/tree/master/React%20Native%E5%BA%94%E7%94%A8%E9%83%A8%E7%BD%B2%E3%80%81%E7%83%AD%E6%9B%B4%E6%96%B0-CodePush%E6%9C%80%E6%96%B0%E9%9B%86%E6%88%90%E6%80%BB%E7%BB%93#%E9%9B%86%E6%88%90codepush-sdk](https://github.com/crazycodeboy/RNStudyNotes/tree/master/React%20Native%E5%BA%94%E7%94%A8%E9%83%A8%E7%BD%B2%E3%80%81%E7%83%AD%E6%9B%B4%E6%96%B0-CodePush%E6%9C%80%E6%96%B0%E9%9B%86%E6%88%90%E6%80%BB%E7%BB%93#%E9%9B%86%E6%88%90codepush-sdk)

持续集成、自动交付[](#持续集成自动交付)
----------------------

这个阶段也没遇到啥大问题，node/npm/install/build 几步走。就多了一步调用 code-push-cli 发布热更新到移动端。

一些小情况：

*   构建环境与开发时的环境要保持完全一致 时隔半年后的发布，试图用最新版本的 node 已经无法正常构建我的项目了……
*   code-push-server 的 TOKEN 有固定的有效期，每隔一大段时间后要重新换一下
*   相同包更新同时发布给不同应用时记得发布前要在包里添加个标识，规避 code-push-server 的签名复用问题 (上文提到过)

旧版本浏览器、设备适配[](#旧版本浏览器设备适配)
--------------------------

### 浏览器端适配[](#浏览器端适配)

#### JavaScript 语法兼容[](#javascript-语法兼容)

JS 语法的兼容不用操心，TS、babel 等技术可以将代码编译转换为 ES5 的语法，[Caniuse 显示 ES5 有 97% 以上用户浏览器支持率](https://caniuse.com/es5), 虽然会带来一些性能损耗，但显然是值得的。

#### JavaScript API 兼容[](#javascript-api-兼容)

一些新的 API 可能在旧浏览器上无法使用，且受影响的用占比也不低，例如 Object.fromEntries 在 Chrome73 才开始支持，国内浏览器的内核版本普遍不高，稍微旧一些的版本就会遇到类似的兼容性问题。 解决方案也挺简单，在项目把 [zloirock/core-js](https://github.com/zloirock/core-js) 配置集成一下即可，该库会根据情况自动作兼容处理。感谢作者，感谢开源，作者的生活之前遇到了一些变故，不知道现在怎么样了，望安好。

#### 跨域 CORS 配置[](#跨域-cors-配置)

移动端访问的是本地 Web Server，与服务端接口在不同域，所以要配置 CORS, 但经实际测试，不同的浏览器版本对各 CORS Header 参数的处理并不一致：

*   有的版本 Origin/Methods/Headers 都支持通配符
*   有的版本只有 Origin/Methods 支持通配符
*   有的版本都不支持

三长一短选最短，所以只能以都不支持通配符的方式来处理，最终为 nginx 新增了如下配置：

```
http {
  # https://stackoverflow.com/a/65206580/9605834
  map $http_origin $allow_origin {
    ~^(http|capacitor)?://localhost(:\d+)?$ $http_origin;
    # NGINX won't set empty string headers, so if no match, header is unset.
    default "";
  }
  map $request_method $allow_headers {
    ~^OPTIONS$ $http_access_control_request_headers;
    # NGINX won't set empty string headers, so if no match, header is unset.
    default "*";
  }
  server {
    add_header Access-Control-Allow-Origin "$allow_origin";
    add_header Access-Control-Allow-Methods '*';
    add_header Access-Control-Allow-Headers "$allow_headers";
    if ($request_method = 'OPTIONS') {
      return 200;
    }
  }
}
```

### 设备端适配: 内置 Webview 内核[](#设备端适配-内置-webview-内核)

经测试， iOS 12 版本下项目运行正常，所以 iOS 设备端兼容性问题不用操心。

但安卓端的兼容性就没有那么幸运了，国产手机内置的 Webview 版本参差不齐也普遍不高，Capacitor 的最低支持版本是 Chrome60, 因为项目特殊性，有部分用户使用的普遍是两三年前的手机，经实测还是有挺多在 Chrome60 以下的版本的。

虽然安卓 5.0 开始，系统 Webview 内核已经支持通过外部安装来替换，但在国内的实施也一言难尽。如果能像 Electron 一样直接将浏览器内核集成到安卓包中就好了，这样就不会受到系统 Webview 版本的影响了。

顺着这个思路找到了 [crosswalk-project/crosswalk](https://github.com/crosswalk-project/crosswalk), 但项目早在五年前就已经停止更新，在[相关讨论](https://github.com/crosswalk-project/crosswalk/issues/4001)中也看到了一些衍生版本：

*   [tenta-browser/crosswalk](https://github.com/tenta-browser/crosswalk) 看起来是 Tenda 浏览器的前身项目，也蛮久没有更新了，最大支持到 chrome77 但看起来只有源码，集成怕是很困难
*   [ks32/CrosswalkNative](https://github.com/ks32/CrosswalkNative) 居然也是最大支持到 chrome77, 这俩项目可能有啥渊源？ 该项目有提供 Demo 和编译后的可集成库文件。

虽然有能跑起来看得见摸得着的 demo, 但感觉还是心虚，不活跃、用户量少、不知道有没有人在生产环境使用。

后来想起了腾讯的 [X5-TBS](https://x5.tencent.com/) 浏览服务，腾讯系产品都在用，那稳定性应该还是蛮靠谱的，之前因为略有排斥腾讯和考虑到它只支持在线集成就没考虑，但目前看来也只能从这个方向再努努力了，看看有没有办法能魔改为本地集成。

再次翻起腾讯一如既往不清晰的文档，果然还是不支持。

但在网上发现了一些其他人的[魔改离线集成方案](https://blog.csdn.net/xiangyuecn/article/details/107855550)，真复杂…… 不过居然看到了说最新版本 TBS 已经支持本地集成了，开放出来了一个 API: QbSdk.installLocalTbsCore() ，也[有人已经有过成功集成的经历](https://blog.csdn.net/qq_34205629/article/details/122375262)。

既然有希望了，那就开始吧，实际集成的时候我分为了两步走：

#### 集成 TBS 的在线版本到项目中[](#集成-tbs-的在线版本到项目中)

由于是混合开发项目，并且基于 Capacitor, 所以比普通纯安卓项目的集成要复杂一些，除了集成还要将 Capacitor 框架对系统 Webview 的依赖全部修改为 TBS。

我找到一个已过时的集成案例：[@ionia/capacitor-engine-x5](https://www.npmjs.com/package/@ionia/capacitor-engine-x5), 虽然基于的 Capacitor 大版本不一致，但也有很大参考意义，实际集成步骤如下：

1.  将 Capacitor-Android 库修改为本地依赖，方便对其变更
2.  添加对 TBS 的依赖
3.  一一审阅 [@ionia/capacitor-engine-x5](https://www.npmjs.com/package/@ionia/capacitor-engine-x5) 对 Capacitor-Android 库的变更，并根据实际情况将变更同步到本地的 Capacitor-Android 库。
4.  测试各功能是否存在问题

过程也蛮枯燥，由于 Webview 是混合开发框架的根基，所以这个变更也牵动了很多相关库，没办法，只能一一改为本地集成并修改代码。中间也会存在一些各种各样的小 BUG, 但心细点都能解决的。

#### 将 TBS 魔改为离线集成[](#将-tbs-魔改为离线集成)

这部分实际操作时是以 [TBS 文件浏览自主安装内核方案](https://blog.csdn.net/qq_34205629/article/details/122375262) 作为参考进行集成，但也仅仅是指引一个方向，实际操作过程中有很多需要根据项目细心特别调整的地方：

*   由于项目最低支持到 Chrome 60，如果系统 Webview 版本低于 60，则直接安装，且安装成功前不允许操作。
    *   TBS 的离线安装 API 实际上只是应用中内置了内核包，实际还是要耗时走一遍解压复制过程的，所以在这期间新增了 Loading 提示
    *   各种试 API 后终于达到目的，但用了各种方法并不能 TBS 直接生效，最后只能代码中在安装后自动重启 APP
*   如果系统 Webview 版本低于 80 则在后台离线安装 TBS 内核，在下次启动后生效
*   Webview 版本高于 80 则不安装也不使用 TBS
*   内核包体积大概 30-40M 左右，为了减少体积，放弃了 APP 对 arm32 的支持。

这个过程整体就是在被 TBS SDK 折磨，腾讯系的 SDK 也都是这性子，文档不全、API 设计不合理……

没办法，谁让没得选呢？还是感谢腾讯大大至少将项目开放了出来。

性能优化[](#性能优化)
-------------

混合开发该面对的还是要面对的，项目在旧设备下有性能问题，尽最大的努力去优化吧：

*   低性能设备关闭所有动画
*   路由入口对页面组件的依赖全部修改为异步依赖 这里使用到了开源项目：[jamiebuilds/react-loadable](https://github.com/jamiebuilds/react-loadable)
*   排查项目中的多余渲染、耗时操作并优化
*   ……

一些想法[](#一些想法)
-------------

项目终于结束，磕磕绊绊也到了相对稳定的阶段，这个项目真的让我学到了也经历了太多东西了：

*   TypeScript 真的是让我开了眼界，之前一直被 JAVA 先入为主，没想到类型系统还可以是这样的，TS 使得更多的内容可以被 “类型安全”。 我现在再使用 JAVA 有时会很沮丧，回想着要是 JAVA 有 TS 的 xxx 就好了…… 所以我觉得 Kotlin 确实可以安排上了~ 但好像还是有一些前端开发者排斥 TS, 觉得有点束手束脚而始终没有迈出第一步，就像我刚接触到 TS 的那些类型特性时也感觉不到有个啥用，但都放心大胆地用吧，用起来之后就是大型真香现场，保证之后就不想回到 JS 了。
*   空指针安全真的应该是每个编程语言的必要特性，对于类型提供者和使用者都降低了太多的心力负担，快让这个价值 10 亿美元的错误消失吧。
*   前端再也不是以前那个随便学着玩玩的技术领域了，前端的热度引来了语言上、模板上、工程化上的各种各样的技术工具，且还在不断的推陈出新，很多社区上大家提出问题很快就会陈旧。我在准备阶段学习的一些内容有些已经有了更新的替代品，很多主要库也都发布了全新大版本，我的依赖库的版本号都不能随便更新，要不就构建不起来了……
*   前端有的技术很有意思，但感觉也有蛮多技术方案设计不周，实际使用中要开发者手动多操心蛮多东西，可能是前端相关技术发展太快了的原因，野蛮生长。 开发这个项目的过程中处理了太多太多奇怪问题，回想起来真的是有些心力憔悴。
*   混合开发性能问题确实是一个大问题，[Flutter](https://flutter.dev/) 等类似的技术还是非常有意义的，既能跨平台，又能兼顾性能。
*   感觉自己还是运气很好的，虽然是小白入门，但在选型上没有遇到特别大的坑，遇到的问题也最终解决了，初期的预想也绝大多数都予以实现，很开心能有这次的项目经历。

居家办公又独立开发真的是很磨人心性，这次的开发过程中我也是真真切切的感受到了 “孤独”。虽然编码本身就是一个排异的工作，我一直都很习惯。但这次我自己入门、查资料、学习、选型、设计方案、代码实现、本地适配、UI 美化…… 因为是一个人，所以工作内容都是一轮一轮的推进，每次推进一个方向，就这样不断的换方向推进，一次次的把项目构建的更完善，时刻感受到自己进度拖沓的紧张，工作计划屡屡未完成的挫败，没有反馈、没有指导、没有批评…… 回想这个过程觉得是有些崩溃的。

但其实身在其中开发的时候倒还好，能很快的将状态调整回来，因为编码本身、解决问题的过程还是我所享受的。

在此，向项目中所有 阅读 / 参考 / 使用 的 技术 / 文档 / 教程 的作者致以最诚挚的敬意；向期间陪伴着我的爱人给予最热烈的感情。

* * *