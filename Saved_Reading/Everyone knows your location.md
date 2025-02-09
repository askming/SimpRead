> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [timsh.org](https://timsh.org/tracking-myself-down-through-in-app-ads/)

> How I tracked myself down using leaked location data in the in-app ads, and what I found along the wa......

Recently I read about a [massive geolocation data leak from Gravy Analytics](https://www.404media.co/hackers-claim-massive-breach-of-location-data-giant-threaten-to-leak-data/?ref=timsh.org), which exposed more than 2000 apps, both in AppStore and Google Play, that secretly collect geolocation data without user consent. Oftentimes, even without developers` knowledge.

I looked into the list ([link here](https://docs.google.com/spreadsheets/d/1Ukgd0gIWd9gpV6bOx2pcSHsVO6yIUqbjnlM4ewjO6Cs/edit?gid=1257088277&ref=timsh.org#gid=1257088277)) and found at least 3 apps I have installed on my iPhone. Take a look for yourself!  
This made me come up with an idea to track myself down externally, e.g. to buy my geolocation data leaked by some application.

### TL;DR

After more than couple dozen hours of trying, here are the main takeaways:

1.  I found a couple requests sent by my phone with **my location** + 5 requests that leak **my IP address**, which can be turned into geolocation using reverse DNS.
2.  Learned a lot about the RTB (real-time bidding) auctions and OpenRTB protocol and was shocked by the amount and types of data sent with the bids to ad exchanges.
3.  Gave up on the idea to buy my location data from a data broker or a tracking service, because I don't have a big enough company to take a trial or $10-50k to buy a huge database with the data of millions of people + me.  
    Well maybe I do, but such expense seems a bit irrational.  
    Turns out that EU-based peoples` data is almost the most expensive.

But still, I know my location data was collected and I know where to buy it!

Starting point
--------------

My setup for this research included:

*   My old iPhone 11 restored to factory defaults + new apple id.  
    Felt too uncomfortable to do all this on my current phone.
*   Charles Proxy to record all traffic coming in and out.  
    I set up the SSL certificate on the iPhone to decrypt all https traffic.
*   A simple game called Stack by KetchApp - I remember playing it at school 10-12 years ago. Choosing it as a lab rat felt nostalgic.  
    To my surprise, there were a lot of KetchApp games on the list.

![](https://timsh.org/content/images/2025/01/image-1.png)

### Huge amount of requests

Ok, here we go: only 1 app installed without the default Apple ones, Charles on, launching Stack in 3, 2, 1....

<video src="https://timsh.org/content/media/2025/01/Screen-Recording-2025-01-19-at-00.02.51.mp4" control></video>

0:00

/0:11

These are the requests that the app sends in the first minute after launch.  
Take a look at the timing of the requests - almost every split second.

Let's take a look at the contents of the requests.  
I actually checked every single one of them - but I'll leave out only the interesting ones here.

### Unity [ads]

Let's start with the juiciest request sent to `https://o.isx.unity3d.com` - the first one that included my geo, while I **disabled Location Services** on iPhone for all apps!  
If you are as naive as I was before this, you might be surprised - what does Unity, the 3D engine, have to do with the in-app advertisement or location tracking?  
Perhaps that's just some monitoring data to help improve the engine?

Turns out that Unity's main revenue stream (they made $2 bln+ in 2023) is Unity Ads -"Mobile Game Ad Network". Sounds quite interesting.

Below is the request body in json format sent to Unity Ads. I will only leave the fields worth mentioning - the actual size is 200+ keys.

```
{
  "ts": "2025-01-18T23:27:39Z", 
  "c": "ES", 
  "d": "sports.bwin.es", 
  "bn": "molocoads-eu-banner", 
  "cip": "181.41.[redacted]", 
  "dm": "iPhone12,1", 
  "ct": "2", 
  "car": "Yoigo", 
  "ifv": "6B00D8E5-E37B-4EA0-BB58-[redacted]", 
  "lon": "2.[redacted]", 
  "lat": "41.[redacted]", 
  "sip": "34.227.224.225", 
  "uc": "1", 
}

```

Ok, so my IP + location + timestamp + some `ifv` id are shared with Unity → Moloco Ads → Bwin, and then I see the actual Bwin ad in the game.  
Wonderful!

As a quick note - location shared was not very precise (but still in the same postal index), I guess due to the fact that iPhone was connected to WiFi and had no SIM installed.  
If it was LTE, I bet the lat/lon would be much more precise.

### Hello Facebook... What are you doing here?

Next interesting request that leaks my IP + timestamp (= geo-datapoint) is Facebook.  
What?!

*   I don't have any Meta [Facebook] app installed on this iPhone
*   I didn't link the app nor my Apple ID to any Facebook account
*   I didn't consent to Facebook getting my IP address!

And yet here we are:

```
{ 
	"bundles": {
		"bidder_token_info": {
			"data": {
				"bt_extras": {
                  "ip":"181.41.[redacted], 
                  "ts":1737244649
			},
			"fingerprint": null
		},
        {
          "a lot of data: yes a loooooooot"
         }

```

We'll talk more about this one in the next section.

### Why do you need my screen brightness level?

Last request I found interesting was sent to... Unity again:  
[`https://configv2.unityads.unity3d.com`](https://configv2.unityads.unity3d.com/webview/4.12.1/release/config.json?ref=timsh.org).  
Let's see what's in that config Unity needs so much:

```
{
  "osVersion":"16.7.1",
  "connectionType":"wifi",
  "eventTimeStamp":1737244651,
  "vendorIdentifier":"6B00D8E5-E37B-[redacted]", 
  "wiredHeadset":false, 
  "volume":0.5,
  "cpuCount":6,
  "systemBootTime":1737215978,
  "batteryStatus":3,
  "screenBrightness":0.34999999403953552,
  "freeMemory":507888,
  "totalMemory":3550640, 
  "timeZone":"+0100",
  "deviceFreeSpace":112945148
  "networkOperator":"6553565535"
  "advertisingTrackingId":"00000000-0000....", 
  }

```

There's no"personal information" here, but honestly this amount of data shared with an arbitrary list of 3rd parties is scary.  
Why do they need to know my screen brightness, memory amount, current volume and if I'm wearing headphones?

I know the "right" answer - to help companies target their audience better!  
For example, if you're promoting a mobile app that is 1 GB of size, and the user only has 500 MB of space left - don't show him the ad, right?

But I also heard lots of controversies on this topic.  
Like Uber dynamically adjusting taxi price based on your battery level - because you're not waiting for a cheaper option with 4% left while standing in the street.

I can't know if that or another one is true.  
But the fact that this data is available and accessible by advertisers suggests that they should at least think of using it.  
I would.

Ok, enough with the requests.  
We can already see the examples of different ip and geolocation leaks.  
One more "provider" that **also got my IP** + timestamp was adjust.com - but the request body was too boring to include.

Let's talk IDs
--------------

You might've already noticed `ifv` and `advertisingTrackingId` == `IDFA` in the requests above - what are those?

IFV, or IDFV, is "ID for Vendor".  
This is my id unique for each vendor, a.k.a developer - in this case, KetchApp.  
This checks out: I installed another KetchApp game to quickly record the requests, and the `ifv` value was the same for it.

Advertising Tracking ID, on the other hand, is the cross-vendor value, the one that is shared with an app if you choose "Allow app to track your activity across ...".  
As you can see above, it was actually set to `000000-0000...` because I "Asked app not to track".

I checked this by manually disabling and enabling tracking option for the Stack app and comparing requests in both cases.

### **And that's the only difference between allowing and disallowing tracking**

  
I understand there might be nothing shocking to you in it - this is not really kept secret, you can go and check the docs for Apple developers, for example.

But I believe this is **not** communicated correctly to the end users, you and me, in any adequate way, shape or form: the free apps you install and use **collect your precise location** with timestamp and send it to some 3rd-party companies.

The only thing that stops anyone with access to bid data (yet another ad buying agent, or ad exchange, or a dataset bought or rented from data broker, as you'll see later) from tracking you down with all trips you make daily is this `IDFA` that is not shared when you disallow apps to "track you across apps" to "enhance and personalise your ads experience".

By the way: if you're using 10 apps from the same vendor (Playrix, KetchApp or another 1000-app company) and allow **a single app** to track you – it would mean that the data collected in all 10 apps will be enriched with your IDFA which can later be exchanged to your personal data.

At the same time, there is so much data in the requests that I'd expect ad exchanges to find some loophole ID that would allow cross-app tracking without the need for IDFA.  
I found at least 20 ids like `tid` and `sid`, `device_id` and `uid` (these 2 are shared with Facebook), and so on.

By the way, the fact that Facebook collected my IP + timestamp without any adequate consent / app connection from my end is crazy.  
I think Facebook is more than capable of connecting the dots and my Meta Account to this hit as soon as I login to Instagram or Facebook app on the same IP address.

How does the data flow?
-----------------------

Let's get back to the request that leaked my location for a second and look at its trace. We'll focus on the parties in the middle:

stack **→ o.isx.unity3d.com → molocoads →** bwin (advertiser)

Unity [ads] is an SSP (supply-side platform) that acts as a collector of data from the app via SDK.  
As an app developer, you don't need to worry about gathering the right data, registering as a publisher on an ad exchange or whatever - just install the SDK and receive the money.

All right, what about [Molocoads](https://www.moloco.com/?ref=timsh.org)?

![](https://timsh.org/content/images/2025/01/Screenshot-2025-01-29-at-23.06.38.png)screenshot from Molocoads landing page

Moloco ads is a DSP network that resells data from multiple SSPs (like Unity, Applovin, Chartboost). Basically, from almost every one of the requested hosts I've seen pop up in Charles Proxy.  
It then applies some "smart optimisation" and connects a vacant banner space on your phone screen with the advertiser.

Sounds like moloco aggregates a lot of data and basically anyone (_to be clear_ _- any company that becomes an ad partner_) can access the data by bidding lower than others.  
Or imagine a real ad exchange that bids normally and collects all of the data along the way "as a side gig".  
Basically, this is how intelligence companies and data brokers get their data.

At this point I was looking for any mentions of Moloco on Telegram and Reddit, and I ran into [this post](https://www.reddit.com/r/adops/comments/rqlr36/eli5_what_is_the_controversy_behind_bidstream?ref=timsh.org) that answered a lot of my questions:

![](https://timsh.org/content/images/2025/02/Screenshot-2025-02-03-at-12.38.37.png)

Especially, [this comment](https://www.reddit.com/r/adops/comments/rqlr36/comment/hqbwmbr/?ref=timsh.org). To quote a part of it:

> They access it if they integrate with the provider of bidstream, which would be the SSP. It's on the SSP to verify the vendor to whom they give access to bids. Usually, the requirement would be that you actually... bid.  
> SSPs want you to spend money, that's how their business makes revenue. They might open up only part of the traffic to specific vendors (i.e.. if you don't bid worldwide, you won't get the bidstream worldwide, only in the regions in which you operate).

Just wonderful.

### Data Brokers

Let's move further. When I found out how the data gets out, I started looking for any place where it's being sold. It was a quick search.

I found a data marketplace called [Datarade](https://datarade.ai/data-categories/device-graph-data?ref=timsh.org) which is a panel with all sorts of data. When I searched for MAID-specific data, hundreds of options showed up, like these two:

![](https://timsh.org/content/images/2025/01/Screenshot-2025-01-29-at-23.24.10.png)

The price of the Redmob dataset surprised me, - $120k a year... for what?  
Let's now take a look at their promo:

![](https://timsh.org/content/images/2025/01/Screenshot-2025-01-29-at-23.26.05.png)

Check out the list of features on the right - do any of them look familiar?

**Quick note**: "low latency" means they know your location from the last time any of the apps shared it. It can be as little as 5 seconds ago.  
What's even better is that Redmob provides a **free sample** of the data.

I tried to request it from their website, but the sample never landed in my mailbox (surprise-surprise, timsh.org doesn't seem like a customer with high potential).  
Thankfully, this sample is public on [Databricks Marketplace](https://marketplace.databricks.com/details/caa4c07a-b27e-4876-9c9c-3f3c2bbbc11f/Redmob_SAMPLE-Redmob-MAID-Data-for-Identity-Graph-I-Global-I-15B-Users-RealTime?ref=timsh.org) with this annotation:

> Enhance your products and services using our global location data covering over 1.5 billion devices. Using our extensive location dataset, you can unearth concealed patterns, conduct rapid analyses, and obtain profound knowledge.
> 
> We can also provide region-specific data (MENA, Africa, APAC, etc.) based on your specific requirements. Our pricing model includes an annual licensing option, and we provide free sample data so that you can evaluate the quality of our dataset for yourself.

![](https://timsh.org/content/images/2025/01/Screenshot-2025-01-31-at-01.12.16.png)Some sample data for better understanding

To me, the most absurd part is the `app` column - the source of the data can't be more obvious. I'm also quite interested in the `yod` column - if it's the birthyear, where did they get it from? Never mind, who cares about your birthyear.

### Show me the PII!

All right, imagine I bought the access to a huge stream of Redmob data.  
But my goal is to track and stalk people like myself or anyone else, so I need some way to exchange MAIDs (_=_`ifa`) for the actual personal info: name, address, phone number...

No problem! This kind of dataset is surprisingly also present on Datarade.  
Take a look at a sample table with `MAID <> PII` type that is provided by "[AGR Marketing Solutions](https://www.agrmarketingsolutions.com/data-nuggets/?ref=timsh.org)":

[

AGR_Mobile_Intent_PII20240903.xlsx

![](https://timsh.org/content/images/icon/spreadsheets_2023q4.ico)Google Docs

![](https://timsh.org/content/images/thumbnail/AHkbwyL0Y-RadP94i-3ntHlOyBNz5QtZLseHmdD1MAKSAFQi7l2fIzkQjGmDmSQRI2yTN7B1h5cNCpCeVlmlA0dsdek_xQhi6nazcP6xeg-w1200-h630-p)

](https://docs.google.com/spreadsheets/d/1gbom_3YO-oFB6Yrg_MAhrJKGkYtNHR2S/edit?gid=2029445799&ref=timsh.org#gid=2029445799)

Inside - all personal info (full name, email, phone number, physical address, property ownership... and IDFAs.

Congrats, you have just reached the bottom of this rabbit hole.  
Let's wrap it up and make a couple of bold statements.

How to track yourself down?
---------------------------

Easy! Just follow this simple step-by-step guide:

1.  Use some free apps for a bit.  
    Move around and commute - this makes the geo data more valuable.
2.  "Allow" or "ask not to track" - a combo of IP + location + User-agent + geolocation will still be leaked to hundreds of "3rd parties" regardless of your choice.
3.  Wait for a few seconds until fake DSPs and data brokers receive your data.
4.  Exchange your full name or phone number for an IDFA (if present), IP address and user-agent through the `MAID <> PII` data purchased somewhere.
5.  Now, access the "Mobility data" consisting of geolocation history, and filter it using the values from the previous step.

Congratulations! You found yourself.

I [created a flowchart](https://excalidraw.com/?ref=timsh.org#json=Ip5AaR-FPppPmtL3AcrBg,-woEvDuI7vER5B7skpT3zA) that includes almost all actors and data mentioned above - now you can see how it's all connected.

![](https://timsh.org/content/images/2025/02/dataflow_upd-1.png)

This is the worst thing about these data trades that happen constantly around the world - each small part of it is (or seems) legit. It's the bigger picture that makes them look ugly.

Afterwords
----------

Thanks for reading this story until the end!  
My research was heavily influenced by these posts and investigations:

[

The Global Surveillance Free-for-All in Mobile Ad Data

Not long ago, the ability to remotely track someone’s daily movements just by knowing their home address, employer, or place of worship was considered a powerful surveillance tool that should only be in the purview of nation states. But a…

![](https://timsh.org/content/images/icon/favicon.ico)Krebs on SecuritySkip to content

![](https://timsh.org/content/images/thumbnail/peoplephone.png)

](https://krebsonsecurity.com/2024/10/the-global-surveillance-free-for-all-in-mobile-ad-data/?ref=timsh.org)[

Candy Crush, Tinder, MyFitnessPal: See the Thousands of Apps Hijacked to Spy on Your Location

A hack of location data company Gravy Analytics has revealed which apps are—knowingly or not—being used to collect your information behind the scenes.

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAACbklEQVRoQ+2aMU4dMRCGZw6RC1CSSyQdLZJtKQ2REgoiRIpQkCYClCYpkgIESQFIpIlkW+IIcIC0gUNwiEFGz+hlmbG9b1nesvGW++zxfP7H4/H6IYzkwZFwQAUZmpJVkSeniFJKA8ASIi7MyfkrRPxjrT1JjZ8MLaXUDiJuzwngn2GJaNd7vyP5IoIYY94Q0fEQIKIPRGS8947zSQTRWh8CwLuBgZx479+2BTkHgBdDAgGAC+fcywoyIFWqInWN9BSONbTmFVp/AeA5o+rjKRJ2XwBYRsRXM4ZXgAg2LAPzOCDTJYQx5pSIVlrC3EI45y611osMTHuQUPUiYpiVooerg7TWRwDAlhSM0TuI+BsD0x4kGCuFSRVzSqkfiLiWmY17EALMbCAlMCmI6IwxZo+INgQYEYKBuW5da00PKikjhNNiiPGm01rrbwDwofGehQjjNcv1SZgddALhlJEgwgJFxDNr7acmjFLqCyJuTd6LEGFttpmkYC91Hrk3s1GZFERMmUT01Xv/sQljjPlMRMsxO6WULwnb2D8FEs4j680wScjO5f3vzrlNJszESWq2LYXJgTzjZm56MCHf3zVBxH1r7ftU1splxxKYHEgoUUpTo+grEf303rPH5hxENJqDKQEJtko2q9zGeeycWy3JhpKhWT8+NM/sufIhBwKI+Mta+7pkfxKMtd8Qtdbcx4dUQZcFCQ2I6DcAnLUpf6YMPxhIDDOuxC4C6djoQUE6+tKpewWZ1wlRkq0qUhXptKTlzv93aI3jWmE0Fz2TeujpX73F9TaKy9CeMk8vZusfBnqZ1g5GqyIdJq+XrqNR5AahKr9CCcxGSwAAAABJRU5ErkJggg==)404 MediaJoseph Cox

![](https://timsh.org/content/images/thumbnail/andrew-guan-lTUyP3RaLpw-unsplash.jpg)

](https://www.404media.co/candy-crush-tinder-myfitnesspal-see-the-thousands-of-apps-hijacked-to-spy-on-your-location/?ref=timsh.org)[

Under Surveillance

How Location Data Jeopardizes German Security

![](https://timsh.org/content/images/icon/apple-touch-icon.png)BRBR Data

![](https://timsh.org/content/images/thumbnail/teaser.png)

](https://interaktiv.br.de/ausspioniert-mit-standortdaten/en/index.html?ref=timsh.org)