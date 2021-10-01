> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [jacobian.org](https://jacobian.org/2021/apr/7/embrace-the-grind/)

> Sometimes, programming feels like magic: you chant some arcane incantation and a fleet of robots do y......

Embrace the Grind
=================

There’s this card trick I saw that I still think about all the time. It’s a simple presentation (which I’ve further simplified here for clarity): a volunteer chooses a card and seals the card in an envelope. Then, the magician invites the volunteer to choose some tea. There are dozens of boxes of tea, all sealed in plastic. The volunteer chooses one, rips the plastic, and chooses one of the sealed packets containing the tea bags. When the volunteer rips open the packet … inside is their card.

⚠️ _If you don’t want to know how the trick is done, stop reading now._

The secret is mundane, but to me it’s thrilling. The card choice is a [force](https://en.wikipedia.org/wiki/Forcing_(magic)). But choice from those dozens of boxes of tea really is a free choice, and the choice of tea bag within that box is also a free choice. There’s no sleight-of-hand: the magician doesn’t touch the tea boxes or the teabag that the volunteer chooses. The card really _is_ inside of that sealed tea packet.

The trick is all in the preparation. Before the trick, the magician buys dozens of boxes of tea, opens every single one, unwraps each tea packet. Puts a Three of Clubs into each packet. Reseals the packet. Puts the packets back in the box. Re-seals each box. And repeats this hundreds of times. This takes hours — days, even.

The only “trick” is that this preparation seems so boring, so impossibly tedious, that when we see the effect we can’t imagine that anyone would do something so tedious just for this simple effect.

Teller writes about this in an article about the [seven secrets of magic](https://www.smithsonianmag.com/arts-culture/teller-reveals-his-secrets-100744801/):

> You will be fooled by a trick if it involves more time, money and practice than you (or any other sane onlooker) would be willing to invest. My partner, Penn, and I once produced 500 live cockroaches from a top hat on the desk of talk-show host David Letterman. To prepare this took weeks. We hired an entomologist who provided slow-moving, camera-friendly cockroaches (the kind from under your stove don’t hang around for close-ups) and taught us to pick the bugs up without screaming like preadolescent girls. Then we built a secret compartment out of foam-core (one of the few materials cockroaches can’t cling to) and worked out a devious routine for sneaking the compartment into the hat. More trouble than the trick was worth? To you, probably. But not to magicians.

I often have people newer to the tech industry ask me for secrets to success. There aren’t many, really, but this secret — being willing to do something so terrifically tedious that it appears to be magic — works in tech too.

We’re an industry obsessed with automation, with streamlining, with efficiency. One of the foundational texts of our engineering culture, Larry Wall’s [virtues of the programmer](http://threevirtues.com/), includes laziness:

> **Laziness**: The quality that makes you go to great effort to reduce overall energy expenditure. It makes you write labor-saving programs that other people will find useful and document what you wrote so you don’t have to answer so many questions about it.

I don’t disagree: being able to offload repetitive tasks to a program is one of the best things about knowing how to code. However, sometimes problems can’t be solved by automation. If you’re willing to embrace the grind you’ll look like a magician.

For example, I once joined a team maintaining a system that was drowning in bugs. There were something like two thousand open bug reports. Nothing was tagged, categorized, or prioritized. The team couldn’t agree on which issues to tackle. They were stuck essentially pulling bugs at random, but it was never clear if that issue was important.. New bug reports couldn’t be triaged effectively because finding duplicates was nearly impossible. So the open ticket count continued to climb. The team had been stalled for months. I was tasked with solving the problem: get the team unstuck, get reverse the trend in the open ticket count, come up with a way to eventually drive it down to zero.

So I used the same trick as the magician, which is no trick at all: I did the work. I printed out all the issues - one page of paper for each issue. I read each page. I took over a huge room and started making piles on the floor. I wrote tags on sticky notes and stuck them to piles. I shuffled pages from one stack to another. I wrote ticket numbers on whiteboards in long columns; I imagined I was [Ben Affleck in The Accountant](https://www.nytimes.com/video/movies/100000004719216/anatomy-of-a-scene-the-accountant.html). I spent almost three weeks in that room, and emerged with every bug report reviewed, tagged, categorized, and prioritized.

The trend reversed immediately after that: we were able to close several hundred tickets immediately as duplicates, and triaging new issues now took minutes instead of a day. It took I think a year or more to drive the count to zero, but it was all fairly smooth sailing. People said I did the impossible, but that’s wrong: I merely did something so boring that nobody else had been willing to do it.

Sometimes, programming feels like magic: you chant some arcane incantation and a fleet of robots do your bidding. But sometimes, magic is mundane. If you’re willing to embrace the grind, you can pull off the impossible.