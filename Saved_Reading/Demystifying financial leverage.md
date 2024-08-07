> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.bitsaboutmoney.com](https://www.bitsaboutmoney.com/archive/demystifying-financial-leverage/)

> Leverage is actually reasonably easy to understand, both in the math and in the implications for fina......

One of the hardest concepts for non-specialists to wrap their heads around in finance is leverage. It is a bit arcane, requires some facility with math, sounds vaguely spooky, and routinely finds itself near smoking craters asking “Did I do that?”

Financial leverage is much easier to understand than many people believe it to be.

Basic balance sheet math  

---------------------------

Every business has a balance sheet, which contrasts its assets (valuable things it owns) against liabilities (valuable things it owes to other people). The difference between assets and liabilities is equity.

Financial businesses will frequently have non-financial assets and liabilities. Ignore those for the sake of simplicity. Ignore the nice building, the computers, the payroll due on Friday for work which has already been completed. Focus just on the _financial_ assets and liabilities, things like “mortgages our bank owns” (asset) and “deposits from customers” (liability).

Leverage is the ratio of your liabilities to your equity. Simple division. Fourth grade math. If you have $110 million in assets and $100 million in liabilities you, by subtraction, have $10 million in equity against your $100 million in liabilities. You are said to be levered 10:1.

Why leverage as a concept is useful
-----------------------------------

Finance is in the business of teleporting value over time and space. This is an enormously useful business to be in, but it requires taking various risks. Leverage provides a quick way to quantify how much risk a financial business is taking on.

This is easiest to understand in the banking example. Imagine the simplest possible toy version of a bank, which offers only two products: checking accounts and mortgages. The bank’s primary source of value as a business is _maturity transformation_: it teleports value over time to allow someone whose checking account currently has much less in it than the cost of a house to buy a house anyway and gain the benefits of living in it. It does this by putting a bit of the bank’s own capital at risk and _levering_ that capital using the deposits in the checking accounts.

This bank is exposed to a variety of risks. One is that, because people can ask for money from their checking accounts at any time, impecunious operation of the bank could cause trouble if the value of the mortgages is impaired just a tiny little bit at a time when people need most of the money in their checking accounts. This has killed many, many banks.

(Values of mortgages sometimes decline both for easy-to-understand reasons like the homeowner suddenly not wanting to pay it back and for reasons which are striking to many non-specialists, like prevailing interest rates increasing. This is a long story, which we will not tell today. Back to leverage.)

How much impairment to assets can the bank take before its equity is exhausted? If you know the leverage ratio, you can mental math out an approximation trivially. Add one to the leverage ratio. Take the reciprocal. Bam, that’s how much of a decline in the value of the assets wipes out the equity.

A 10:1 levered firm is wiped out if assets lose 1/11th (~9.09%) of their value.

Managing leverage of one’s customers  

---------------------------------------

Many financial firms are levered as a matter of course; it is required to do the work. Interestingly, their customers are _also_ often levered. A homeowner who has just made their 20% down payment is levered 4:1.

Financial firms frequently have to manage the leverage of their customers, because just like a financial firm gets riskier as the leverage ratio goes up, so do their customer accounts. Past a certain point, the financial firm will take painful actions to delever you.

Consider the example of margin accounts at stock brokerages. Google costs about $100 a share these days, so you could buy about 10 shares for $1,000 at your brokerage of choice.

Your stock brokerage, though, is willing to _offer you leverage_ on your assets. In return for a fee (and to gain your business, because this is considered a high-saliency feature for the customers of brokerages), they will lend you money against your assets, allowing you to buy more Google than you had cash for. They might allow you 2:1 leverage when you buy stock: your $1,000 buys 20 shares now.

Why would you want that? Because you like Google, and want more exposure to it than you can afford. In future worlds where Google successfully sells ads and cancels chat apps, you'd make even more money that way.

So: The brokerage lent you money (where it comes from is a wonderful topic for another day) to match your money, and then you sent all that money to the person who previously owned those 20 shares, and now they are all yours.

But you now owe $1,000 to your brokerage, and are 1:1 levered. And this is fine… for now.

In some unfortunate future universes, perhaps one in which Google runs out of chat apps to cancel, the price of Google drops by more than 50%. In this case, the value of your stock is now below your debt to the brokerage. Your equity has been vaporized.

But let's not go immediately to that calamitous case. Googlers are, even now, working on more chat apps to refill the cancelable chat app inventory. Perf is just around the corner.

Say the price of Google is now $80. It only took a moderate hit.

Now your brokerage has a few choices, and none of them are fun, because someone has lost money and that can never be made fun. The value destruction has already happened, principally at Google. The results of that destruction are being communicated to you, because you chose to be a part-owner of their business, partially using other people's money.

One thing your brokerage could do is to ask you nicely to de-lever. You’re not 1:1 levered, which is relatively safe. You’ve got $1,600 in assets against $1,000 in debt, so $600 in equity, so ~1.67:1 levered.

To bring that leverage ratio down, the brokerage could potentially issue a **margin call**. This is anachronistic lingo (you, if you are reading this and do not work in finance, are unlikely to actually get a telephone call) to require you to either deposit more cash or sell stock. Either of these will decrease your leverage ratio.

If you sell $400 worth of stock, you now have $1,200 in assets against $600 in debt. This is 1:1 leverage.

If you deposit $400 of shares, you now have $2,000 in assets against $1,000 in debt. You’re back to 1:1 leverage.

If you deposit $400 and pay back the loan, you have $1,600 in assets against 600 in debt. You’re now 0.6:1 levered; even safer than 1:1.

Why the discrepancy in the impact of $400? Because leverage measures risk, and depositing $400 in shares _dilutes your risk by adding assets that are themselves an incremental source of risk_. Repaying the loan, on the other hand, strictly decreases your risk.  

Mismanaging customer leverage  

--------------------------------

Why do brokerages care about customer leverage? Because if they do not promptly de-leverage customers, the margin loans are unlikely to get repaid. The risk of the stock decline has, effectively, been transferred from the customer to the broker. The losses it is incurring are eating into the equity _of the brokerage_ now.

In principle, brokerages can pursue customers for bad margin debt. In practice, this is rarely going to restore them to whole, particularly not for retail customers, because the financial picture of someone whose brokerage account has lost all value is rarely rosy elsewhere. Brokerages take substantial efforts to avoid losing money on margin accounts.

In addition to the capitalistic reason to do this, their regulators are acutely aware of the risk that overextended customers pose to the brokerage. You can sort of think of society as being the broker’s broker: if we do not manage your leverage, because you do not manage your customer’s leverage, your losses eat into _our_ equity. So we are supportive of you taking a carefully measured amount of risk, because risk makes your business possible, but will be cross if you take an impecunious amount and then stick us with the losses.

Brokerages really do lose money on margin accounts sometimes! It’s relatively rare. Large losses usually have [a complicated story](https://www.bloomberg.com/news/articles/2019-04-29/china-firm-s-plunge-is-said-to-cost-interactive-brokers-millions). But since they happen, brokerages spend a lot of effort carefully managing their balance sheets such that the hit does not impair their solvency.

Decentralized finance innovations in leverage management  

-----------------------------------------------------------

I was recently playing around with a decentralized finance (DeFi) protocol. I am notoriously a crypto skeptic and do not perceive there to be much value in DeFi, but a friend won me over with this argument:

> You believe Tether is a fraud. You want to short them, but do not trust cryptocurrency exchanges. So short them using DeFi. In worlds where you are right about Tether, you make money and will feel vindicated. In worlds where you are wrong about Tether, you will feel appropriately chastened, but you think basically no worlds like that exist so what do you care. And in worlds where the DeFi protocol blows up due to any of a long list of causes, you will get a great story out of it.

So let me tell you a story about [Solend](https://solend.fi/) this week.

Solend would be described by many people as operating a decentralized protocol. I would describe it as an API with an ops team attached, but whatever, not germane to the following.

Solend lets you deposit assets that are on the Solana slow database, earn interest, and withdraw assets that other people have deposited back to the Solana slow database, paying interest for the privilege.

This allows you to do things like e.g. lever up on buying the Solana token.

In my case, the specific use was “Deposit USDC, a [stablecoin](https://www.bitsaboutmoney.com/archive/stablecoin-mechanisms-and-use-cases/) that I have some degree of trust for. Borrow Tether. Use a separate DeFi program to sell those Tether for USDC. Wait for the price of Tether to decline, buy the now cheaper Tether with the USDC, repay the Tether-denominated loan to Solend, profit according to the degree of decline less the net interest paid over the interval.”

Now a funny thing happened while I was patiently waiting for Tether to blow up: global systemic crypto calamity. Somehow, this was not caused by Tether. _Dang it_. They can’t get anything right.

That quickly became relevant to my interests, because there was another borrower on Solend. Let’s call him the whale. (His identity is knowable but not germane to this story.)

The whale had, previously, deposited a lot of Solana tokens (SOL) to Solend and withdrawn a lot of USDC stablecoins, back when the price of Solana was [much higher](https://coinmarketcap.com/currencies/solana/). At that point, he was conservatively leveraged. What did he do with the stablecoins? Who cares; they’re money.

The price of SOL declined precipitously recently. Solend, the computer program, and Solend, the team, had planned for this eventuality, and the program started doing what it was designed to do.

The design was “Make some of the whale’s debts assumable by third parties, if and only if they ask for that to happen, in return for an incentive payment of the whale’s collateral.” The idea was that fast-acting bots, operating in a tight loop and incentivized by the juicy 5% discount to the market price of SOL, would quickly eat the collateral, deleveraging the account and bringing it back to a healthy state. (Small detail: a portion of that 5% would get paid by the bot back to the Solend team, partly as compensation for their efforts and partially to help build a buffer against bad debt.)

That… didn’t happen.

Why not? Well, the whale is much, much bigger than the bots, and it was out of their price-range to liquidate in one go. Instead, they’d have to chip away at it, buying up to the USDC they were willing to spend with their little bot brains, getting attractively-priced SOL, selling the SOL for even more USDC, and repeating.

And with the price of SOL in freefall, some of the bots (or operators of the bots) couldn’t find liquidity at attractive prices for people wanting to buy their SOL. This let them unable to loop.

So the price of SOL kept falling, and the whale went from conservatively leveraged to dangerously leveraged to insolvent.

Many people in DeFi believe that, if this happens, you can basically just walk away from your collateral and that is the end of it. I take no position on that point of view or the righteousness of it; it’s just very different from the default expectation for traditional finance.

Given that the whale was assumed likely to just walk away, the hole in the balance sheet is now someone else’s problem, and it grew as SOL declined.

How did this present to users of the protocol? Well, Solend was owed USDC and it had SOL. But one thing people like doing when the price of an asset is in freefall is borrowing it to short it, so other users borrowed alllll the whale’s SOL and sold it… somewhere. Now the protocol had no SOL, and claim against USDC from a whale that was in another ocean.

And so if you liquidated the whale now, you would not get SOL for your USDC. You would get a wrapped token—an extremely technologically sophisticated IOU—instead, entitling you to some future SOL from Solend whenever they had the SOL to give you and you asked for it.

So Solend (the people, not the computer program) did some active liquidity management, by tweaking parameters to their program, causing the offered interest rate for SOL deposits to be 2,400% to 2,600%.

In the midst of the market contagion, even 2,600% was insufficient to attract lots of SOL, for a long list of market microstructure reasons. Many of the bots were off and their creators went to bed, worrying that Solend would have an even larger hole in it when they woke up.

Who pays for that hole? The default answer is “It’s the people who deposited other assets into the same pool but will not be able to withdrawal them, even if they repaid their loans, because their collateral are… swimming with a whale, in another ocean.” A frequent addendum to this answer in DeFi is “And since people would be really annoyed in that circumstance, there exists a side pocket of money—the project treasury—which would step in to make depositors less-damaged in this circumstance. Of course, if the treasury is exhausted... well, that would be bad.” (Ask Solend for their actual resolution here.)

But as the price of SOL kept going down, the hole kept getting deeper, and some combination of depositors and the project treasury was hemorrhaging money. So they kept doing things to entice liquidators. (And they banned people from further borrowings of any assets, because... you can predict the logic, right.)

A funny thing happens when you create incentive systems. For example, you might induce a technically proficient financial columnist to spend a few hours playing a very boring video game for money. Perhaps he knows enough about slow databases to understand how the words "epoch" and "unstaking" relate to each other and to know what this implied for the difficulty level of the video game in the early Tokyo evening.

That video game, in lieu of being able to quickly program a bot, was taking a trivial amount of USDC, waiting for more SOL to be deposited in response to the 2,600% interest rate offered, and quickly liquidate as much of the whale’s debt as the program would let me. The video game crashed about 70% of the time I tried to do this, but I pressed on.

Then, I’d use my 5%-cheaper-than-market-price-recently SOL and use a different video game to convert them into USDC, tolerating both a high chance of the video game crashing and a very real risk of slippage in the price of SOL between when the slow database first detected me buying it and the slow database would allow me to sell it. (The Solana slow database is a fast database as far as slow databases go, but due to market conditions, both it and some other necessary technological infrastructure were having a very bad day. What sounds like "click two buttons in a web app with a barely perceptible lag between them" took between 3 and 12 minutes per iteration.)

And so I round-tripped that transaction, twenty two times, each time with more money used to liquidate. Then people in other time zones woke up, looked at market conditions, and turned their bots back on. Once that happened, AI stole my button-pushing job.

Now you might naively think that means I roughly tripled my starting capital (1.05 ^ 22), but the combination of the slippage and the fees I was paying to the designers of the video games meant it was actually more like a 50% gain. I made more money than I typically would playing poker for 2 hours while probably at worse risk, and would probably choose to play [Dyson Sphere Program](https://store.steampowered.com/app/1366540/Dyson_Sphere_Program/) in the future, but Outsourced APAC DeFi Defaulting Accounts Risk Manager did push my buttons for a few hours.

Well, I pushed its buttons, at any rate.

What can be learned from this experience?  

--------------------------------------------

The source of the payment for my button pushing was the built-in incentive to deleverage (via forced liquidation) the defaulting account. The programmers chose to build in that incentive so that someone, and they had (sensibly) no idea it would be me or operate any way like how I chose to operate, would save them the downside risk of a defaulting borrower’s collateral continuing to fail.

Was this the only thing happening on Solend yesterday? Oh no, feel free to read their official spaces for details. I’ve successfully mined the anecdote for my teachable moment now.

Am I a DeFi fan as a result of this experience? Not so much, no, but at least in reinventing things from first principles the folks seem to have created a very concrete demonstration of what leverage management (and mismanagement) looks like.

Hopefully that helps demystify leverage and leverage management to you. You will, in both the near future and long after that, read a lot about leverage, and how it blew someone up. And hopefully you will remember that it is not some dark art only accessible to the high priests of finance.

And now you know enough to understand what I'm saying with an otherwise opaque statement like"Tether is [35:1 levered](https://www.kalzumeus.com//2022/11/11/tether-required-recapitalization-again/) on risky assets during market contagion."  

Want more essays in your inbox?
-------------------------------

I write about the intersection of tech and finance, approximately weekly. It's free.