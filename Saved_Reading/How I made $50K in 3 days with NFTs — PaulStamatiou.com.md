> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [paulstamatiou.com](https://paulstamatiou.com/how-i-made-50k-in-3-days-with-nfts/)

> I created Crypto Mondrians, a set of code-generated art NFTs on the blockchain.

### I created Crypto Mondrians, a set of code-generated art NFTs on the blockchain.

[![](https://turbo.paulstamatiou.com/uploads/2021/09/paul-stamatiou-CryptoMondrianDark-1500.jpg)](https://turbo.paulstamatiou.com/uploads/2021/09/paul-stamatiou-CryptoMondrianDark-2000.jpg)

II first dabbled with cryptocurrency in 2011 when I wrote [an article about mining Bitcoin](https://paulstamatiou.com/bitcoin-mining/) on AWS EC2 GPU clusters. My interest in crypto ebbed and flowed over the years before actively avoiding the space until earlier this year. It felt like there was a lot of noise and hype around volatile, speculative asset holding and not much innovation happening.

It wasn’t until a few months ago that I began to take a closer look at the state of crypto and see how much the landscape has evolved. The big thing for me was seeing how the blockchain has become programmable with smart contracts, little pieces of automatically-executing code running on the blockchain.

The new functionality afforded by smart contracts, along with the relative consumer ease of simply being able to connect your crypto wallet with any decentralized service and be able to quickly interact, has led to a flurry of new product developments. Most of these are categorized under the moniker dApps (decentralized applications that run on the blockchain or in a p2p capacity). A large chunk of dApps are in the so-called DeFi, or Decentralized Finance, space (yes, there's lots of terms and abbreviations in the crypto space). I wrote a brief thread about [what I learned about crypto and DeFi](https://twitter.com/Stammy/status/1417201411155120143) my first few weeks diving into it.

[Ethereum](https://ethereum.org/en/ "Ethereum is the community-run technology powering the cryptocurrency, ether (ETH) and thousands of decentralized applications.") was much more interesting to me now than Bitcoin. So much is being built on top of it with smart contracts and other [Ethereum-based tokens](https://coinmarketcap.com/tokens/views/all/). There are crypto-based games like [Axie Infinity](https://axieinfinity.com/), robust decentralized exchanges like Uniswap and Matcha.xyz, to communities and DAOs built around their own tokens like [FWB](https://www.fwb.help/) and [Kong.land](https://kong.land/). There's far too much activity going on for me to accurately summarize the different types of innovation happening here and I'm definitely still learning myself.

NFTs are one particular realm of the crypto community that has been experiencing stratospheric growth over the last year. By now you’ve probably heard about them in some form. It could have been the news of digital artist [Beeple selling his NFT artwork for $69 million dollars](https://www.theverge.com/2021/3/11/22325054/beeple-christies-nft-sale-cost-everydays-69-million). Or maybe the news of Figma founder [Dylan Field selling a CryptoPunk NFT](https://www.forbes.com/sites/alexkonrad/2021/03/18/figma-ceo-dylan-field-talks-cryptopunks-nft-beeple-metaverse/) for $7.5M.

NFTs are approaching mainstream status now—[Paris Hilton sold her own NFTs](https://www.youtube.com/watch?v=oiN1_6pb_eE "Paris Hilton Schools Jimmy on NFTs | The Tonight Show"), [Jay-Z bought a CryptoPunk](https://www.theblockcrypto.com/post/109655/jay-z-puts-a-cryptopunk-nft-as-his-twitter-profile-picture) for $126k for his Twitter avatar and NBA player [Steph Curry bought a $180k Bored Ape NFT](https://markets.businessinsider.com/news/currencies/steph-curry-nft-bored-ape-yacht-club-180000-ethereum-nba-2021-8) for his Twitter avatar and even Mila Kunis and Ashton Kutcher launching [NFTs that unlock TV show episodes](https://www.forbes.com/sites/nadjasayej/2021/07/26/is-stoner-cats-the-first-ever-nft-tv-show/).

One thing that stands out to me about crypto now, as opposed to the last time I was involved years ago, is that **you can actually _do_ stuff with your crypto now**.

Before, it seemed like the most you could do was hold on to your crypto as an investment, sending it between wallets, or exchange it back to your local fiat currency. Now, people are able to spend their crypto.. largely on other crypto dApps or into the hands of creators with NFTs. And most of those people will continue investing in and building for crypto and decentralized services, so things continue growing and evolving.

However, all the press around NFTs reminds me of the hype around ICOs and speculative asset _hodling_ of meme coins.. are NFTs just the latest example of a fleeting crypto fad?

What are NFTs?
--------------

### Digital art, collectibles, identity, tickets and more..

I didn’t really get NFTs for a long time.. and honestly I don’t even know if I fully understand them now. Can’t someone just screenshot the NFT you paid a bundle for and have the same thing you have? That's the common question you hear from anyone when they first hear about NFTs.

That's like seeing [the Mona Lisa in person](https://paulstamatiou.com/photos/france/france-day-6/), taking a photo, turning that into a print on your wall and saying yours is worth the same. It's not the original. With the public nature of NFTs on the blockchain, it's easy for anyone to verify who owns it, who has owned it and when it first appeared. Anyone can look up your wallet address (or more recently ENS domain name if you set one up) to see what NFTs you own.

But let me take a step back for a moment..

NFTs are unique, non-fungible tokens on the blockchain. Regular cryptocurrency tokens like Ether or other [Ethereum-based ERC20 tokens](https://coinmarketcap.com/tokens/views/all/) are fungible and can easily be traded and swapped for one another. They're all the same thing.

By contrast, each NFT has a unique identifier allowing it to be paired with metadata that cannot be changed. While an NFT can be sold and transferred like any fungible token, each NFT has its own unique value and worth. This identifier also makes it possible to trace the ownership history for the NFT. It's also possible to prove the scarcity of an NFT and know how many of a certain type exist and how many can exist.

Being able to programmatically prove ownership is where it gets interesting; NFTs can also be used like keys or digital tickets to unlock certain functionality, experiences, membership, events and so on.

And an NFT can never be taken from you. There is no middleman. This is not like [Amazon being able to remotely delete a Kindle book](https://slate.com/technology/2009/07/how-amazon-s-remote-deletion-of-e-books-from-the-kindle-paves-the-way-for-book-banning-s-digital-future.html) you purchased because they want to. No one can take your NFT from your (non-custodial) wallet.

These traits of NFTs lead to some unique value propositions and capabilities. They can be used for digital art, content, collectibles and gaming but they can also be used for utilities like .eth domains like with the Ethereum Name Service or even tokenized real-world assets.

NFTs are status, identity, community, self-expression, access and more.

I could go on and get philosophical about the different ways NFTs provide value, but I'll leave it at that. The value of an NFT always depends on what someone is willing to pay for it. The market always wins as they say; NFTs are no exception. Fortunately, now that market is open globally 24/7/365 and has a quick payment system. Not quite like the old days of trying to sell your Magic: The Gathering cards in person and not finding any buyers (just me?).

Even though NFTs have been around in some form since 2012 and then more media-focused from 2016, it's still very early. I’m sure we’ll continue see a significant evolution of how they are used and how they are valued. Right now NFTs may get a bit of a mixed reputation due to the high level speculation on collectible assets and many buyers trying to quickly flip NFTs that are part of a limited set.

There are also private communities focused on investing in NFTs that have been growing, such as with [PleasrDAO](https://pleasr.org/) and [Flamingo DAO](https://flamingodao.xyz/). While [Flamingo DAO](https://flamingodao.xyz/) has done very well with their NFT investments so far, having experienced a 40X gain and [owning NFTs worth $1B+](https://twitter.com/litocoen/status/1432047312738660356), they take a longer view on what NFTs can provide:

> The growth of NFTs is just beginning, because NFTs represent the digitization and financialization of digital property and intellectual property. Trillions of creative works swirl around the Internet and are difficult to monetize, except through licensing models. NFTs hold out the hope of bringing back to the Internet an ownership economy. Creators can create, sell, and fractionalize ownership in their works, opening up a new chapter for creative endeavor. NFTs can be:
> 
> - fractionalized;  
> - combined into token sets;  
> - used as collateral for lending and stablecoin protocols; and  
> - dynamic and interactive, incorporating outside data feeds.
> 
> Over the longer arc, NFTs hold out the hope of becoming increasingly financialized, interacting with other core blockchain-based financial primitives. They may prove to be a core primitive for decentralized identity solutions, and may increasingly serve as a cornerstone for monetizing emerging metaverses and other gaming platforms.

Whatever your thoughts are on NFTs, it's hard not to pay attention to what's happening in the space. I very often think about how [the next big thing will start out looking like a toy](https://cdixon.org/2010/01/03/the-next-big-thing-will-start-out-looking-like-a-toy "The next big thing will start out looking like a toy") in the context of everything happening in crypto now, like the early days of the Internet.

#### Common types of NFT projects

10k PFPs, collectibles, games and more

With the basics out of the way, lets see what types of media-focused NFTs and cryptoart are common right now. First off, we have the very popular so-called “10k PFP” collections. These are sets limited to 10,000 media assets geared towards being used as a profile picture, usually because the image looks like some kind of being: human, alien or otherwise anthropomorphized entity.

There are the popular ones like CryptoPunks and [Bored Apes](https://boredapeyachtclub.com/) and then there are the many derivative collections trying to capitalize on these types of sets. Owning an NFT from one of these collections has led to being a new sort of status and community.

There are interesting trading card-like NFTs like [Parallels](https://parallel.life/) and gaming NFTs like [Zed](https://zed.run/). And then a section of the NFT space that I'll just call experiments because I'm not sure what else to call them. Things like [Blitmap](https://www.blitmap.com/), [Loot](https://collisions.substack.com/p/gimme-the-loot) and [Tunes Project](https://tunesproject.org/) that test the waters of how certain types of NFTs can invite others to build on top of them. In this case of Loot, building a whole game ecosystem with characters, loot, music and more.

And of course, there's a ton of NFTs that encompass all other forms of art. It has also been inspiring to see artists adapt to the new format and reap the benefits; getting paid more easily and generously than previously. There are computer-assisted artists making 2D and 3D creations by hand and there are all sorts of artists making digital versions of their hand-made creations. There's even a painter [selling NFT sketches](https://opensea.io/collection/seasketch) that come paired with an offer to unlock a physical painting, shipped to whoever owns the NFT during a particular time each year.

But there’s one type of NFTs that I became particularly fond of: [generative art](https://en.m.wikipedia.org/wiki/Generative_art). Generative art can be defined in many ways but at a high level it's any art that was created in part or in whole with the artist being hands-off and having an automated computer system or program do the rest, leading to each creation being entirely unique.

One of the popular players in this space is [Art Blocks](https://artblocks.io/). This example below sold for 777 ETH (around $2.5M when it sold):

> Wow... just shocked. When I set this price (yesterday) I didn't really expect it to sell this quickly. Thank you [@tylerxhobbs](https://twitter.com/tylerxhobbs?ref_src=twsrc%5Etfw) for your fantastic work. I will certainly reinvest this in new and upcoming artists / donate a portion to charity. 🙏🤯 [https://t.co/rbaJQ73D48](https://t.co/rbaJQ73D48)
> 
> — KΞvin R◎se (@kevinrose) [August 25, 2021](https://twitter.com/kevinrose/status/1430560685172297729?ref_src=twsrc%5Etfw)

Making my NFTs
--------------

### How I got inspired, built and listed them

I knew I wanted to get involved with NFTs somehow. Over the past few months I had been seeing designers I follow experiment with and find success creating and selling their own cryptoart NFTs. Friends and family had been suggesting I do something with NFTs; I just didn’t know what.

I’m a designer and developer but my forte is definitely not the type of graphic and 3D design I had seen as being common with NFTs: detailed illustrations, 3D concepting/rendering and 3D animation. I didn’t want to design another collection of PFPs. It had to be something that I could feasibly write a simple program myself with regular web and mobile languages I already know.

I thought about picking up [Processing](https://processing.org/), which I had last touched in college more than a decade ago, and making some art out of things like [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life "https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life") and other cellular automata. But I didn't find that to be particularly aesthetically pleasing or how I could make it pleasing.

I began thinking about modern, abstract art I like, wondering if I could do a "crypto" take on that. I like geometric art and something with simple geometric shapes would be feasible for me to code with regular web/software technologies I already know. And hopefully by being heavily inspired by existing traditional artwork, these NFTs would might already feel familiar to viewers.

A few years ago I visited [Amsterdam (my photoset)](https://paulstamatiou.com/photos/amsterdam/) and visited museums like the Stedelijk Museum of modern and contemporary art where I had seen lots of [De Stijl](https://en.wikipedia.org/wiki/De_Stijl) pieces. Piet Mondrian's compositions came to mind along with pieces by Gerrit Rietveld.

I decided to try writing some code to generate Mondrian-inspired art that would be unique each time I ran it. But **I wanted to make it feel like what crypto _feels_ like to me** at first glance. I think Mr. Robot, [Shadowy super coders](https://decrypt.co/79422/shadowy-super-coder-pack-315m-perks-ethereum-nft-devs "‘Shadowy Super Coder’ Pack Offers $315M of Perks for Ethereum NFT Devs: Polygon, Alchemy, Gitcoin, and other projects have poured benefits into this free pack from Project Galaxy."), dark web, The Matrix, Blade Runner, Altered Carbon, Ready Player One.. **lots of neon colors, glows and darkness**.

[![](https://turbo.paulstamatiou.com/uploads/2021/09/paul-stamatiou-crypto-vibes-moodboard-1500.jpg)](https://turbo.paulstamatiou.com/uploads/2021/09/paul-stamatiou-crypto-vibes-moodboard-2000.jpg)

After I had a general idea of what I wanted to create, I thought about how to build it. I knew I wanted to do a limited set, something under 1,000. I figured 100 would be a nice way to get started and test the waters. Just enough that I would need to have whatever code I wrote be able to export directly to PNG. I didn't want to hack around with taking screenshots for each of them.

[![](https://turbo.paulstamatiou.com/uploads/2021/09/paul-stamatiou-crypto-mondrian-glow.png)](https://turbo.paulstamatiou.com/uploads/2021/09/paul-stamatiou-crypto-mondrian-glow.png)

The general vibe I was going for.. bright colors seeping into generous glows.

I decided to start by making a simple HTML page that used `canvas` and JavaScript to create the art and easily let me export the canvas. I had become familiar with canvas recently when making the [Stocketa](https://stocketa.com/) site:

> Spent a good chunk of the weekend building out the last bits of the new [@StocketaApp](https://twitter.com/StocketaApp?ref_src=twsrc%5Etfw) website. Happy with how it's turning out... will probably deploy later tonight
> 
> Used Canvas to composite JPG frames (for smaller size) using PNG masks (for alpha) for Apple-like 3d scroll effect [pic.twitter.com/2OBNhIR3y8](https://t.co/2OBNhIR3y8)
> 
> — Paul Stamatiou (@Stammy) [April 20, 2021](https://twitter.com/Stammy/status/1384509594991534082?ref_src=twsrc%5Etfw)

After a Sunday afternoon of tinkering, I had a working concept. Every time the page loaded, a new random design would be created. I used the localStorage API to keep track of views and name each file for export, which I would simply do via a download button on the page. I was too eager to get this out and didn't spend much time on additional code to automate things.

Much of the code revolves around randomly selecting the number of iterations to complete, what color palettes to use, modifying colors and the intensity of the glows. Some of them used color palettes of 3-5 colors I put together myself, while others I had the code pick from a random color and then find pentadic, tetradic or triadic colors to use or use varying alphas of a single color. Figuring out the colors took a decent chunk of time and I think there was still some room for improvement. I ended up having around 15 different color palettes I was having the code randomly select between at one point.

This is what it ended up being—a simple HTML page with a few hundred lines of JavaScript and a download button to export the canvas to a 4800x4800 PNG.

[![](https://turbo.paulstamatiou.com/uploads/2021/09/paul-stamatiou-crypto-mondrian-chrome.png)](https://turbo.paulstamatiou.com/uploads/2021/09/paul-stamatiou-crypto-mondrian-chrome.png)

The single HTML file responsible for generating the artwork.

One issue I ran into and was with color profiles. Dealing with very saturated colors and lots of glows, I wanted to use the P3 color space instead of sRGB, which was the default color space/profile when exporting the contents of a canvas. This is something I became quite familiar with years back when writing [my post about building a Lightroom PC](https://paulstamatiou.com/building-a-windows-10-lightroom-photo-editing-pc/#the_display).

![](https://turbo.paulstamatiou.com/uploads/2018/01/copyright-paulstamatiou_com-cie1931-custom-chart.jpg)

Relying on sRGB meant some visible color banding that annoyed me. Unfortunately, it seemed like this was out of my control and it's not yet possible to specify a color profile for canvas to use when exporting after a cursory investigation. It wasn't a huge issue, so I moved on.

#### Publishing PNGs as NFTs

Now I had a pile of PNGs and needed to list them for sale as NFTs. This started out as a small project so I just wanted something very turnkey to manually list each piece. I already knew I wanted to use OpenSea. It's hard to look at NFTs online and not come across them; something like 98% of all NFT trade volume flows through OpenSea.

The other nice thing about OpenSea is that there is no cost to the seller to mint each NFT. There's a one time gas fee the first time you sell anything but I had done that a while back with another NFT that I'm not even sure how much that cost.

Minting an NFT is the process of putting your art/media and its associated metadata on the blockchain by creating a new, unique token (usually ERC-721 but there's a newer format called ERC-1155 that supports both non-fungible and fungible tokens). In my case, I would be putting these on the Ethereum blockchain. It's also possible to mint on other blockchains for lower costs, such as the [Ethereum-compatible sidechain Polygon](https://rainbow.me/learn/a-beginners-guide-to-layer-2-networks "A Beginner's Guide to Layer 2 Networks"), or a faster blockchain, [Solana](https://solana.com/), but that's outside the scope of this article. For now, we'll stick with Ethereum. It's currently the most popular for NFTs.

If I was doing a much larger NFT project, I would probably spend a bunch of time and money developing and deploying my own smart contract on Ethereum. NFTs are minted through a smart contract, small bits of code running on the blockchain itself. Owning your own smart contract gives you complete control over your NFT collection and doesn't delegate any control over to a NFT marketplace. It just costs a lot to develop and deploy (for example, I tested deploying a simple smart contract and the estimated gas fees required to publish the smart contact to the Ethereum blockchain were around 0.25-0.35 ETH or ~$1,000).

This is a growing space so you're at no shortage of options for how you want to publish your NFTs from [Nifty Kit](https://niftykit.com/), Bitski, Foundation, Rarible, Zora.co, UNifty.io, [Showtime](https://tryshowtime.com/) and many more.

##### Listing on OpenSea

So I ended up sticking with OpenSea: easy to get started and no fees to mint NFTs, but they take a 2.5% cut on each sale. Other marketplaces like Foundation require you to pay gas to mint each NFT, which can get expensive quickly if you're unsure your items will sell, with each item costing potentially around $100 of gas to mint.

There's a bit of nuance to how OpenSea does things. They do so-called _lazy minting_. While you may need to pay an initial gas fee to list a new collection, each NFT listing does not require any fees. This works because the NFT is not actually minted yet. It gets officially minted once the buyer pays the gas fees to mint the artwork on the blockchain.

I created a new collection then began adding each NFT one by one; first adding the item, then marking it for sale at a set price. If I had a more complex set, I might have spent the time to add detailed metadata such as unique stats or traits of the individual NFTs to help people more easily filter and find what they're looking for.

When it came to pricing, I wasn't really sure how to approach this. I started with the first few priced around $200, between Ξ0.05-0.065 (Ξ is the symbol for ETH, or ether). I wasn't sure if these would sell at all and since I was manually uploading and listing each NFT, I started slow and released them in batches over a 3 day period. I listed the first three in a new [Crypto Mondrian //DARK](https://opensea.io/collection/cryptomondrian "A new take on the classic Mondrian abstract paintings. All NFTs unique and created using generative code. Limited edition of 100 NFTs.") collection, Tweeted about it and then went out to dinner that Sunday evening.

Surprisingly, all 3 sold quickly. The next day, I released 20 more NFTs. Every few minutes I would hear the ding from my email app and then open my [Rainbow Ethereum wallet](https://rainbow.me/) to see each new inbound ETH transfer from OpenSea.

> — Paul Stamatiou (@Stammy) [September 6, 2021](https://twitter.com/Stammy/status/1434923524754493443?ref_src=twsrc%5Etfw)

I kept releasing in batches over a 3 day period at varying prices. As they started to sell I noticed people quickly listing theirs for sale at much higher prices so I experimented with increasing my prices.

It was interesting to see where the sales came from. While I think a good portion came from those that follow me on Twitter, I believe a large set of folks found me through various crypto community Discord and Telegram groups where my collection was eventually shared. I also saw lots of folks that purchased them ending up sharing the new NFTs they added to their collection with their own audiences. It was awesome to see it all come together.

By the end of day 3, all NFTs had sold (except #099 and #100 I wanted to keep for myself as a memento). To say that I was shocked that my Crypto Mondrian art was selling and selling well would be a huge understatement. The reaction far exceeded my expectations. The average sale price was around Ξ0.189, though that includes all sales (some of which were much higher like Ξ0.6-0.9) not just ones listed for sale by me directly.

My collection ended up being **ranked #469 out of all NFT collections on OpenSea** that week, and #132 in the Art category:

![](https://turbo.paulstamatiou.com/uploads/2021/09/paul-stamatiou-crypto-mondrian-ranking.png)

Breaking down the sales
-----------------------

### The grand total was Ξ14.085, just over $50,000 at the current ETH price

[![](https://turbo.paulstamatiou.com/uploads/2021/09/paul-stamatiou-CryptoMondrianDarkCollection-1500.jpg)](https://turbo.paulstamatiou.com/uploads/2021/09/paul-stamatiou-CryptoMondrianDarkCollection-2000.jpg)

One interesting thing about certain NFT marketplaces like OpenSea is the ability for creators to specify a royalty percentage when listing their collection. This means that the creator will continually receive payment for any sale of their NFTs, even if they are not involved in the transaction and it is between two other users. This is amazingly creator-friendly. Currently, this is a feature of some individual NFT marketplaces, not actually part of any NFT standard.. yet.

That being said, I did set a 10% royalty on my Crypto Mondrian collection. OpenSea batches up the royalties and delivers them in a separate, single payment every few weeks.

Here's a breakdown of the sales and royalties so far:

I'm extremely thankful and amazed at what was able to happen with this project, and the power of the crypto technology and community that enabled this to happen. It has been awesome to see creators quit their full-time jobs to pursue their passions, fueled by their newfound ability to quickly be able to earn a tremendous amount of money with NFT collections. It will be fun to see how this space evolves and what new types of things can be created using NFTs, even beyond art and collectibles.

On the other hand, it's clear that a lot of people are interested in NFTs to be able to quickly flip them (often within hours or days of a purchase) and make a quick profit. As a creator, the first time I saw someone purchase my NFT and then immediately list it for 13x their purchase price.. that stung a bit. I get it though, and I have definitely been on the other side before. I wish there was a way to specify separate types of NFTs that might let me sell differently to those that enjoy the artwork vs those that are in it for the investment and speculation.

For example, I might sell an NFT at a discount if it meant the buyer would either not be able to sell it, or would not be able to sell it for some period of time. Not unlike a [6-month IPO lock-up period](https://www.investopedia.com/ask/answer/12/ipo-lockup-period.asp) for employees.

#### What's next?

Just tinkering and learning

I had a lot of fun diving into the world of NFTs lately. While I'm interested in continuing the journey with another collection, I won't do anything unless it's a slight evolution from what I just did with this set. Either a new style or something different (video? animated?).

I have been particularly interested in learning about smart contracts and would love to deploy a smart contract that is able to generate media completely on-chain. It's been fun to watch all the smart contract experiments that [Dom Hoffman](https://twitter.com/dhof) (creator of Loot, Blitmap, Vine..) has been tweeting out. As I wrote this, another interesting NFT experiment called [Manny's Game](https://mannys.game/about) was gaining popularity and had a unique set of rules.

But one thing seems to be certain with NFTs: creativity is valued highly. Being the second person to do something without evolving the format much won't get you too far, especially in the future as the popularity of NFTs go up and down.

> Qualities to look for in NFTs
> 
> ⛓ on chain  
> 🖼 good art  
> 🌐 public domain  
> 💻 open source  
> 💎 unique  
> 🤝 not anonymous  
> 💗 healthy community  
> ❌ not super markety  
> 🧑‍🎨 committed artist  
> 💸 you like it  
> 💵 you can afford it  
> 📉 ur cool if it goes down
> 
> — Dame.eth (@jacksondame) [September 14, 2021](https://twitter.com/jacksondame/status/1437753067085107210?ref_src=twsrc%5Etfw)

But, of course, I have lots of work left on my other project [Stocketa](https://stocketa.com/), where I recently added [basic crypto support](https://twitter.com/StocketaApp/status/1425456454316740612).

Published 17 Sep 2021