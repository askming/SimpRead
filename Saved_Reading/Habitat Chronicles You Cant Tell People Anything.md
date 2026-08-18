---
saved_date: 2026-08-18T04:39:05.902Z
title: "Habitat Chronicles:   You can't tell people anything"
url: "https://web.archive.org/web/20091025030730/https://habitatchronicles.com/2004/04/you-cant-tell-people-anything/"
word_count: 1231
---

# Habitat Chronicles You Cant Tell People Anything

### You can't tell people anything

 
This is sort of Morningstar’s version of Murphy’s Law.

 
When we were assembling our catalog of the things we had learned over the past decade and a half in this business, we almost didn’t include this one because it seems so banal. But I keep finding that it’s often the first thing I say when people ask me what about my experiences (and another thing I’ve learned is to pay attention to things I find myself saying; that way I’ll know what I really think). And, upon reflection, I think it’s actually one of the more important lessons that we’ve learned.

 
We all spend a lot of our time talking to bosses or investors or marketing people or press or friends or other developers. I’m totally convinced that a new idea or a new plan or a new technique is never really understood when you just explain it. People will often think they understand, and they’ll say they understand, but then their actions show that it just ain’t so.

 
Years ago, before Lucasfilm, I worked for [Project Xanadu](https://web.archive.org/web/20091025030730/http://xanadu.com/) (the original hypertext project, way before this newfangled World Wide Web thing). One of the things I did was travel around the country trying to evangelize the idea of hypertext. People loved it, but nobody _got_ it. Nobody. We provided lots of explanation. We had pictures. We had scenarios, little stories that told what it would be like. People would ask astonishing questions, like “who’s going to pay to make all those links?” or “why would anyone want to put documents online?” Alas, many things really must be experienced to be understood. We didn’t have much of an experience to deliver to them though — after all, the whole point of all this evangelizing was to get people to give us money to pay for developing the software in the first place! But someone who’s spent even 10 minutes using the Web would never think to ask some of the questions we got asked.

 
In 1988 we began consulting to Fujitsu, when they licensed Habitat from Lucasfilm to create Fujitsu Habitat in Japan. We started out with a week long seminar at Skywalker Ranch for their team, explaining everything we knew about Habitat. We gave them copious documentation and complete source code listings. Following that, for the next couple of years they had unlimited access to us via fax, phone and email to answer any questions they might have. We made several visits to Japan to advise them. On our visits they often asked questions that seemed a little, well, odd. We chalked it up to the language barrier, but still, there were clearly things they weren’t getting. For example, their server ran on five (not four, not six, five) Fujitsu A60 minicomputers, and became hopelessly bogged down after about 80 concurrent users. We were never able to get a clear picture of why. We asked lots of questions and they’d try to answer them, but none of the explanations made any sense that we could puzzle out. They were trying to tell us, you see, but you can’t tell people anything.

 
The mystery was solved a few years later when we began the WorldsAway project, still consulting to Fujitsu but in a role that was much more hands-on. Our initial plan had been to work from the Fujitsu Habitat code, back porting the client to Macs and Windows, and cleaning up their server (80 users, yeesh). When we took apart their code, we finally figured out what had been puzzling us all that time: _they had lost the architecture._ In spite of all the information we gave them, we had completely failed to communicate how things worked. Their guys hadn’t understood the whole client-server concept, which for that day and place was somewhat exotic, so they just implemented what they knew, which was a terminal-mainframe architecture. Their “client” was basically a fancy, highly specialized graphics terminal; all the real work was done on the server. For example, when you issued a command to an object, instead of sending a command message to the object on the server, the client would send the X-Y coordinates of your mouse click. The server would then render its own copy of the scene into an internal buffer to figure out what object you had clicked on. Not only was this extremely inefficient, but the race conditions inherent a multi-user environment meant that it also sometimes just got the wrong answer. It was amazing…

 
What’s going on is that without some kind of direct experience to use as a touchstone, people don’t have the context that gives them a place in their minds to put the things you are telling them. The things you say often don’t stick, and the few things that do stick are often distorted. Also, most people aren’t very good at visualizing hypotheticals, at imagining what something they haven’t experienced might be like, or even what something they _have_ experienced might be like if it were somewhat different. One of the things I really miss from my days at Lucasfilm is having artists on staff, being able to run down the hall and say, “hey Gary, draw me this picture.”

 
Eventually people can be educated, but what you have to do is find a way give them the experience, to put them in the situation. Sometimes this can only happen by making real the thing you are describing, but sometimes by dint of clever artifice you can simulate it.

 
With luck, eventually there will be an “Aha!”. If you’re really good, the “Aha!” will followed by “Oh, so _that’s_ what you meant”. But don’t be too surprised or upset if the “Aha!” is instead followed by “Why didn’t you _tell_ me that?”. At Communities.com we developed a system called Passport (I’ll save the astonishing trademark story for a later posting) that let us do some pretty amazing things with web browsers. For example, with just a few magic HTML tags we could stick avatars on a web page — pretty much any web page. For months Randy kept getting up at management meetings and saying, “We’ll be able to put avatars on web pages. Start thinking about what you might do with that.” Mostly, nobody reacted much. After a couple of months of this we had things working, and so he got up and presented a demo of avatars walking around on top of our company home page. People were amazed, joyful, and enthusiastic. But they also pretty much all said the same thing: “why didn’t you _tell_ us that we could put avatars on web pages?” You can’t tell people anything.

 
When people ask me about my life’s ambitions, I often joke that my goal is to become independently wealthy so that I can afford to get some work done. Mainly that’s about being able to do things without having to explain them first, so that the finished product can be the explanation. I think this will be a major labor saving improvement.

 
One final point: I expect none of you to really get what I’m talking about here, because this principle also applies to itself. But I fully expect I’ll get the occasional email saying “Oh! so _that’s_ what you meant.” or “Why didn’t you _tell_ me that?” I did, but you can’t tell people anything.