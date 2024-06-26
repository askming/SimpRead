> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [rachelbythebay.com](https://rachelbythebay.com/w/2023/09/26/hue/)

> If you've gotten into the home automation thing in the past few years, it's possible you set up some......

If you've gotten into the home automation thing in the past few years, it's possible you set up some Philips Hue devices along the way. This was an ecosystem which had a bunch of bulbs, switches, outlets and a hub that spoke Zigbee on one side and Ethernet on the other. It was pretty much no-nonsense, never dropped commands, and just sat there and worked. Also, it integrated with the Apple Homekit ecosystem perfectly.

Unfortunately, the idiot C-suite phenomenon has happened here too, and they have been slowly walking down the road to full-on enshittification. I figured something was up a few years ago when their iOS app would block entry until you pushed an upgrade to the hub box. That kind of behavior would never fly with any product team that gives a damn about their users - want to control something, so you start up the app? Forget it, we are making you placate us first! How is that user-focused, you ask? It isn't.

Their latest round of stupidity pops up a new EULA and forces you to take it or, again, you can't access your stuff. But that's just more unenforceable garbage, so who cares, right? Well, it's getting worse.

It seems they are planning on dropping an update which will force you to log in. Yep, no longer will your stuff Just Work across the local network. Now it will have yet another garbage "cloud" "integration" involved, and they certainly will find a way to make things suck even worse for you.

If you ever saw the [South Park episode](https://en.wikipedia.org/wiki/Informative_Murder_Porn) where they try to get the cable company to do something on their behalf and the cable company people just touch themselves inappropriately upon hearing the lamentations of their customers, well, I suspect that's what's going on here. The management of these places are fundamentally sadists, and they are going to auger all of these things into the ground to make their short-term money before flying the coop for the next big thing they can destroy.

What can you do about it? Before you say "~Home Assistant~Homebridge", let me stop you right there. Javascript plus a "curl | sudo sh" attitude to life equals "yeah no, I am never touching this thing".

Instead, I have a simpler workaround, assuming you just have lights and "smart outlets" in your life. Get a hold of an Ikea Dirigera hub. Then delete the units from the Hue Hub and add them to the Ikea side of things. It'll run them just fine, and will also export them to HomeKit so that much will keep working as well.

I will warn you that Ikea isn't perfect here, either. They won't plumb through the Hue light/motion/temp sensors or the remote controllers to HomeKit. This means you lose any motion sensor data, the light level, and the temperature of that room. You also lose the ability to do custom behaviors with those buttons, like having one turn something on and then automatically switch it off a few minutes later. (Don't laugh - this is perfect for making kitchen appliances less sketchy when unattended.)

Also, there's no guarantee that Ikea won't hop on the train to sketchville and start screwing over their users as well.

My hope is that someone with good taste and some sensibility in terms of their technology choices will make something that does Zigbee on one side, Homekit on the other, and is at least as flexible as the Hue setup that existed originally. Until then, it's going to be yet another shit show.

And people wonder why I don't trust these things.

October 3, 2023: This post has an [update](https://rachelbythebay.com/w/2023/10/03/js/).