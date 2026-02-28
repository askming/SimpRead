---
saved_date: 2026-02-28T20:34:23.147Z
title: "How I built Timeframe, our family e-paper dashboard - Joel Hawksley"
tags: [Technology, Health]
---

# How I Built Timeframe Our Family E-paper Dashboard - Joel Hawksley

[![Joel Hawksley](https://hawksley.org/img/about/joel.jpg)](/)  [Joel Hawksley](/) [joel@hawksley.org](mailto:joel@hawksley.org)   
# How I built Timeframe, our family e-paper dashboard

 2026-02-17 
_**TL;DR:** Over the past decade, I’ve worked to build the perfect family dashboard system for our home, called [Timeframe](https://github.com/joelhawksley/timeframe). Combining calendar, weather, and smart home data, it’s become an important part of our daily lives._

 
_See [https://news.ycombinator.com/item?id=47113728](https://news.ycombinator.com/item?id=47113728) for a lively discussion of this post._

 
![Timeframe display in phone nook](https://hawksley.org/img/posts/2026-02-17-timeframe/nook-wide.jpg)

 
When Caitlin and I got married a decade ago, we set an intention to have a healthy relationship with technology in our home. We kept our bedroom free of any screens, charging our devices elsewhere overnight. But we missed our calendar and weather apps.

 
## Initial prototypes

 
So I set out to build a solution to our problem. First, I constructed a [Magic Mirror](https://magicmirror.builders/) using an off-the-shelf medicine cabinet and LCD display with its frame removed. It showed the calendar and weather data we needed:

 
![Magic Mirror prototype](https://hawksley.org/img/posts/2026-02-17-timeframe/magic-mirror.jpg)

 
But it was hard to read the text, especially during the day as we get significant natural light in Colorado. At night, it glowed like any backlit display, sticking out sorely in our living space.

 
I then spent about a year experimenting with various jailbroken Kindle devices, eventually landing on design with calendar and weather data on a pair of screens. The Kindles took a few seconds to refresh and flash the screen to reset the ink pixels, so they only updated every half hour. I designed wood enclosures and laser-cut them at the [local library makerspace](https://boulderlibrary.org/makerspaces/bldg-61/):

 
![Kindle e-paper display in laser-cut wood enclosure](https://hawksley.org/img/posts/2026-02-17-timeframe/kindle-enclosure.jpg)

 
Software-wise, I built a Ruby on Rails app for fetching the necessary data from Google Calendar and Dark Sky. The Kindles woke up on a schedule, loading a URL in the app that rendered a PNG using [IMGKit](https://github.com/csquared/IMGKit). The prototype proved e-paper was the right solution: it was unobtrusive regardless of lighting:

 
![Kindle display in low light](https://hawksley.org/img/posts/2026-02-17-timeframe/kindle-enclosure-lit.jpg)

 
## A more reliable approach

 
The Kindles were a hack, requiring constant tinkering to keep them working. It was time for a more reliable solution. I tried an OLED screen to see if the lack of a global backlight would be less distracting, but it wasn’t much better than the Magic Mirror:

 
![OLED tablet compared with epaper display](https://hawksley.org/img/posts/2026-02-17-timeframe/oled-comparison.jpg)

 
So it was back to e-paper. I found a system of displays from [Visionect](https://www.visionect.com/), which came in 6”/10”/13”/32” sizes and could update every ten minutes for 2-3 _months_ on a single charge:

 
![Visionect display range](https://hawksley.org/img/posts/2026-02-17-timeframe/visionect-range.jpg)

 
The 32” screen used an outdated lower-contrast panel and its resolution was too low to render text smoothly. The smaller sizes used a contrasty, high-PPI panel. I ended up using a combination of them around the house: a 6” in the mudroom for the weather, a 13” (with its built-in magnetic backing) in the kitchen attached to the side of the fridge, and a 10” in the bedroom.

 
![Visionect display on fridge](https://hawksley.org/img/posts/2026-02-17-timeframe/visionect-fridge.jpeg)

 
The Visionect displays required running custom closed-source software, either as a SaaS or locally with Docker. I opted for a local installation on the Raspberry Pi already running the Rails backend. I had my best results _pushing_ images to the Visionect displays every five minutes in a recurring background job. It used IMGKit to generate a PNG and send it to the Visionect API, logic I extracted into [visionect-ruby](https://github.com/joelhawksley/visionect-ruby). This setup proved to be incredibly reliable, without a single failure for months at a time.

 
## First customer pilot

 
Visiting friends often asked how they could have a similar system in their home. Three years after the initial prototype, I did my first market test with a potential customer. At their request, I experimented with different formats, including a month view on the 13” screen:

 
![Monthly calendar view on display](https://hawksley.org/img/posts/2026-02-17-timeframe/monthly.jpg)

 
Unfortunately, the customer didn’t see enough value to justify the $1000 price tag (in 2019!) for the 13” device, let alone anything I’d charge for a subscription service. At around the same time, Visionect started charging a $7/mo per-device fee to run their backend software on premises with Docker, after years of it being free to use. I’d have needed to charge $10/month, if not more, for a single screen!

 
## An unexpected pivot

 
In late 2021, the [Marshall Fire](https://en.wikipedia.org/wiki/Marshall_Fire) destroyed our home along with ~1,000 others. Our homeowner’s insurance gave us two years to rebuild, so we set off to redesign our home from the ground up.

 
![Redesigning our home](https://hawksley.org/img/posts/2026-02-17-timeframe/redesigning.jpg)

 
Around the same time, Boox released the [25.3” Mira Pro](https://onyxboox.com/boox_mirapro), the first high-resolution option for large e-paper screens. Best of all, it could update in realtime! Unlike the Visionect devices, it was just a display with an HDMI port and needed to be plugged into power. A quick prototype powered by an old Mac Mini made it immediately obvious that it was a huge step forward in capability. The larger screen allowed for significantly more information to be displayed:

 
![Boox Mira Pro e-paper display](https://hawksley.org/img/posts/2026-02-17-timeframe/mira-pro.jpg)

 
But the most compelling innovation was having the screen update in realtime. I added a clock, the current song playing on our Sonos system (using [jishi/node-sonos-http-api](https://github.com/jishi/node-sonos-http-api)) and the next-hour precipitation forecast from Dark Sky:

 
![Realtime display updates](https://hawksley.org/img/posts/2026-02-17-timeframe/realtime.jpg)

 
The working prototype was enough to convince me to build a place for it in the new house. We designed a “phone nook” on our main floor with an art light for the display:

 
![Timeframe display in phone nook](https://hawksley.org/img/posts/2026-02-17-timeframe/nook-wide.jpg)

 
We also ran power to two more locations for 13” Visionect displays, one in our bedroom and one by the door to our garage:

 
![Bedroom and mudroom displays](https://hawksley.org/img/posts/2026-02-17-timeframe/bedroom-mudroom.jpg)

 
## Backend overhaul

 
The real-time requirements of the Mira Pro immediately surfaced performance and complexity issues in the backend, prompting an almost complete rewrite.

 
While the Visionect system worked just fine with multiple-second response times, switching to long-polling every two seconds put a ceiling on how slow response times could be. To start, I moved away from generating images. The Visionect folks added the ability to render a URL directly in the backend, freeing up resources to serve the long-polling requests.

 
Most significantly, I started migrating towards Home Assistant (HA) as the primary data source. HA already had integrations for Google Calendar, Dark Sky (now Apple Weather), and Sonos, enabling me to remove over half of the code in the Timeframe codebase! I ended up landing a [PR to Home Assistant](https://github.com/home-assistant/core/pull/128900) to allow for the calendar behavior I needed, and will probably need to write a couple more before HA can be the sole data source.

 
With less data-fetching logic, I was able to remove both the database and Redis from the Rails application, a massive reduction in complexity. I now run the [background tasks](https://github.com/joelhawksley/timeframe/blob/434da5569bdb84037a5f6f09551ec29a04dd86ff/config/scheduler.rb) with [Rufus Scheduler](https://github.com/jmettraux/rufus-scheduler) and save data fetching results with the Rails [file store cache backend](https://github.com/joelhawksley/timeframe/blob/434da5569bdb84037a5f6f09551ec29a04dd86ff/app/apis/api.rb#L19).

 
In addition to data retrieval, I’ve also worked to move as much of the application logic into Home Assistant. I now [automatically display](https://github.com/joelhawksley/timeframe/blob/main/app/apis/home_assistant_api.rb#L33) the status of any sensor that begins with _sensor.timeframe_, using a simple _ICON,Label_ CSV format.

 
For example, the other day I wanted to have a reminder to start or schedule our dishwasher after 8pm if it wasn’t set to run. It took me about a minute to write a template sensor using the power level from the outlet:

 
```
{% if states('sensor.kitchen_dishwasher_switched_outlet_power')|float < 2 and now().hour > 19 %}
utensils,Run the dishwasher!
{% endif %}

```

 
In the month since adding the helper, it reminded me twice when I’d have otherwise forgotten. And I didn’t have to commit or deploy any code!

 
## Today

 
Since moving into our new home, we’ve come to rely on the real-time functionality much more significantly. Effectively, we’ve turned the top-left corner of the displays into a status indicator for the house. For example, it shows what doors are open/unlocked:

    
Or whether the laundry is done:

 
![Laundry done notification on display](https://hawksley.org/img/posts/2026-02-17-timeframe/laundry-done.jpg)

 
It has a powerful function: if the status on the display is blank, the house is in a “healthy” state and does not need any attention. This approach of only showing what information is relevant in a given moment flies right in the face of how most smart homes approach communicating their status:

 
![Home Assistant dashboard](https://hawksley.org/img/posts/2026-02-17-timeframe/ha-dashboard.jpg)

 
The single status indicator removes the need to scan an entire screen. This change in approach is possible because of one key difference: we have separated the _control_ of our devices from the _display_ of their status.

 
## What’s next

 
![Home Assistant dashboard](https://hawksley.org/img/posts/2026-02-17-timeframe/mudroom-dark.jpg)

 
I continue to receive significant interest in the project and remain focused on bringing it to market. A few key issues remain:

 
### Hardening for deployment

 
While I have made significant progress in [handling runtime errors gracefully](https://github.com/joelhawksley/timeframe/blob/main/app/controllers/displays_controller.rb#L15), I have plenty to learn about creating embedded systems that do not need maintenance.

 
### Home Assistant integration

 
There are still several data sources I fetch directly outside of Home Assistant. Once HA is the sole source of data, I’ll be able to have Timeframe be a Home Assistant App, making it significantly easier to distribute.

 
### Hardware cost and complexity

 
The current hardware setup is not ready for adoption by the average consumer. The 25” Boox display is excellent but costs about $2000! It also doesn’t include the hardware needed to drive the display. There are a couple of potential options to consider, such as Android-powered devices from [Boox](https://shop.boox.com/products/notemax) and [Philips](https://www.almoproav.com/productdetails/PHILIP/25BDL4150I/00) or low-cost options from [TRMNL](https://trmnl.com/).

 
## Conclusion

 
Building Timeframe continues to be a passion of mine. While my day job has me building software for over a hundred million people, it’s refreshing to work on a project that improves my family’s daily life.

 © 2004-2026 Joel Hawksley | [RSS](/feed.xml)   document.addEventListener('DOMContentLoaded', async function() { mermaid.initialize({startOnLoad:true}); await mermaid.run({ querySelector: '.language-mermaid', }); });  ![](chrome-extension://kipdpbpgbehkppnchehlfodlgclbcfkh/icon.png)