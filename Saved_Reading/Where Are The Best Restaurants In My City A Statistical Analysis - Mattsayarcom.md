---
saved_date: 2026-02-23T06:30:52.163Z
title: "Where are the best restaurants in my city? A statistical analysis - mattsayar.com"
---

# Where Are The Best Restaurants In My City A Statistical Analysis - Mattsayarcom

# Where are the best restaurants in my city? A statistical analysis

![](https://mattsayar.com/media/website/me-removebg-preview.png) [Matt Sayar](https://mattsayar.com/authors/matt-sayar/) February 12, 2025![](https://mattsayar.com/media/posts/29/avo_toast.jpg)
Everyone wants to know the best places to eat, but the "best place" is inherently subjective. Sure you can read the multitude of "Best Restaurants in Town" lists (which are usually pretty good!), but I wanted to use _data_ to answer the question: "What are the best restaurants in Colorado Springs?" I've been having a [lot of fun with LLMs](https://mattsayar.com/tags/toy-code/), so why not use them for some data analysis? 


This simple question turned into quite the data science project. I broke it down into the sections. If you're just here for the goods, feel free to skip ahead. If you're here for the journey, read on.


### Table of Contents


- [Gather the data](#mcetoc_1ijouhimg67)
- [Google API Registration](#mcetoc_1ijp2gk67ck)
- [Places API (New) > Nearby Search (New)](#mcetoc_1ijp2gk67cl)


- [Cleanup and Analysis](#mcetoc_1ijouhimg68)
- [Cleanup](#mcetoc_1ijpm6gjkjq)
- [Analysis and Ranking](#mcetoc_1ijpm6gjkjr)
- [Show me the list already!](#mcetoc_1ijs8r50mhq)


- [Visualize the data](#mcetoc_1ijouhimg69)
- [Observations](#mcetoc_1ijs8r50mhr)
- [Hidden Gems](#mcetoc_1ijs8r50mhs)




- [Conclusion](#mcetoc_1ijouhimg6a)


_[Update: I wrote some insights about just fast-food and chain restaurants.](https://mattsayar.com/best-and-worst-chain-restaurant-rankings-in-colorado-springs/)_


### Gather the data


OK, to start, what data do I need to collect to get a decent list of restaurants?


- Restaurant names
- Overall rating
- Number of reviews
- Location


Additionally, I needed to limit my search to a reasonable scope. I wanted to focus on the core of Colorado Springs, so I settled on this **15km radius** around the center-ish of the city. If a restaurant is outside of this, well too bad. I'm not trying to boil the ocean, I just wanna eat good food.

![](https://mattsayar.com/media/posts/29/base_map.png)
I didn't spend much time thinking about where I wanted to gather the data: I wanted to use Google Maps. GMaps has been around a long time, it's very popular, has lots of user reviews, I'm familiar with the the kind of data available, and I didn't want to bother with a one-off platform like Yelp ([poor reputation](https://www.google.com/search?q=yelp+sucks)), TripAdvisor (more focused on vacations) etc. So how do I get the data from Maps?


My first thought was to use Google Maps' API, but I didn't want to risk spending money on this project. I need that money to eat at restaurants! I saw some shady third-party tool that scrapes the data, but it's against the Terms of Service and I don't want to worry about being banned from my entire Google ecosystem. 


I know that the Google Maps app lets you download maps for offline use. What if I could get that file off my phone and parse the restaurants out of it? First issue: the list of restaurants in that file are incomplete based on a quick offline search in the app. Second: I scanned my phone's filesystem with MacDroid and couldn't find the file ¯\_(ツ)_/¯ I honestly didn't look too hard because all signs were pointing to using the API.


#### Google API Registration


I started by checking out the [Google Maps Platform](https://mapsplatform.google.com/). In order to use that, I had to register as a [Google Developer](https://developers.google.com/). After I did THAT I could log into a [Google Cloud Console](https://console.cloud.google.com/). After I did THAT I had to set up a [Project](https://console.cloud.google.com/projectcreate). After I did THAT I had to set up a [Billing Account](https://console.cloud.google.com/billing/create). After I did THAT I had to enable the [Places API (New)](https://console.cloud.google.com/google/maps-apis/api-list). After I did THAT I had to create an [API key](https://console.cloud.google.com/google/maps-apis/credentials). THEN I could start making queries to get restaurant data.

![](https://mattsayar.com/media/posts/29/hal_lightbulb.gif)[It do be like that sometimes](https://www.youtube.com/watch?v=AbSehcT19u0)
If I sound like I'm complaining, I promise I'm only complaining a little bit. Between every step I tried to run some queries and the API's error responses did a great job explaining, "Wait, you need to set up a billing account first by going to this link," "Wait, you need to enable the billing account first by going to that link," etc. Too bad I didn't [follow this guide](https://developers.google.com/maps/documentation/javascript/cloud-setup) to begin with.


Developer-friendliness aside, I was still worried about accidentally spending money. Apparently every month everybody gets $200 in credits to use Maps stuff, and starting [March 1st everyone is getting $3,250/mo in credits](https://mapsplatform.google.com/resources/blog/build-more-for-free-and-access-more-discounts-online-with-google-maps-platform-updates/). I don't have anything negative to say about that! In the end, my worries weren't entirely unfounded as I spent a total of $38.61 (in credits) to get all the data I needed.


Unfortunately, like many cloud platforms, I can't find a kill switch that will turn everything off after I've exhausted my credits. I wish there was, so I could embed the maps and such in this post and everyone can play with it, but I don't want to risk getting a bill. So screenshots it is!

![](https://mattsayar.com/media/posts/29/tomahawk.jpg)One more step closer to the payoff
#### Places API (New) > Nearby Search (New)


After getting everything in place, I could finally start playing with the "Places API (New)," not to be confused with the old, haggard "Places API." I sympathize with refactoring old APIs vs just starting fresh. It's a long process before you can stop calling things "new." Case in point, it looks like the new API was [released Oct 2023](https://developers.google.com/maps/documentation/places/web-service/release-notes).


The [docs and playground](https://developers.google.com/maps/documentation/places/web-service/nearby-search) were exactly what I needed to draw me in and get me the data I need. I started off running curl commands using examples from the [Nearby Search (New) doc](https://developers.google.com/maps/documentation/places/web-service/nearby-search). You get a LOT of data about a place if you don't use the `X-Goog-FieldMask` header. I eventually narrowed down the parameters to:


- `places.displayName.text`
- `places.primaryTypeDisplayName.text`
- `places.rating`
- `places.id`
- `places.shortFormattedAddress`
- `places.userRatingCount`
- `places.location`
- `places.googleMapsUri`


Which gave me a result like:


```
{
    "name": "Arnold's Donuts and Coffee",
    "place_id": "ChIJxZ3YBa5HE4cRlucg9jTNos0",
    "type": "Donut Shop",
    "rating": 4.8,
    "user_ratings_total": 428,
    "location": {
        "latitude": 38.8556089,
        "longitude": -104.7184834
    },
    "address": "5883 Palmer Park Blvd site B, Colorado Springs",
    "maps_url": "https://maps.google.com/?cid=14817631351353698198"
}
```


I started to get excited since I'm only one more API call away from getting all the results I need! The `curl` I was practicing with looked sorta like


```
curl -X POST -d '{
  "maxResultCount": 10,
  "locationRestriction": {
    "circle": {
      "center": { # Colorado Springs
        "latitude": 38.878400,
        "longitude": -104.767914
      },
      "radius": 1000.0 #meters
    }
  }
```


So now I just need to set some higher limits


- `"maxResultCount": 9999`
- `"radius": 15000`


and we're off to the races! Oh wait, what's this?


```
{
  "error": {
    "code": 400,
    "message": "Max number of place results to return must be between 1 and 20 inclusively.",
    "status": "INVALID_ARGUMENT"
  }
}
```


Well, that's a little bit of a setback, but it's not the end of the world. If I can only get 20 results at a time, how can I capture every restaurant in the city? I needed to break down that 15km radius into smaller chunks and search those first. Just make sure there's a little bit of overlap, dedup the results, and _then_ I'm off to the races! Visualizing that strategy looks something like this.

![](https://mattsayar.com/media/posts/29/restaurant_search_sm.gif)
Using [Claude](https://claude.ai/new), I gave it the working `curl` request and asked it to write a Python script with an algorithm like I described. A few iterations later, I dropped it in VSCode, used GitHub Copilot to work out some runtime errors, then I executed the script to output all the restaurants into a .json file.

![](https://mattsayar.com/media/posts/29/charcut.jpg)A culinary representation of the .json file
### Cleanup and Analysis


First things first, gotta check the data and make sure it's workable. I cast a wide net and got 1200+ results and nearly half a megabyte of .json. To start, I simply looked at some of the data to see what shakes out on first glance. The cleanup section below is very Colorado-Springs-specific, so feel free to scroll on through to the analysis, or read on if you wanna see how the sausage is made. 


#### Cleanup


Google Maps is community-curated, so by definition its data cannot be perfect. Additionally, it's ephemeral because even as I write this people are leaving ratings, reviews, and restaurants are opening and closing. I gathered this list on **February 9th 2025**, so at best this is a snapshot in time. Maybe someday another enterprising individual can take this concept and make it more generic and up-to-date for every city, but I'm just trying to find the best places to eat in my city!


Within the first two results, I see a non-restaurant location that's listed as a synagogue. 


```
{
      "name": "Chabad of Colorado Springs Jewish Community",
      "place_id": "ChIJi1_uDLpPE4cR8CvBDjJPCEA",
      "type": "Synagogue",
      "rating": 5,
      "user_ratings_total": 181,
      "location": {
        "latitude": 38.920195,
        "longitude": -104.787714
      },
      "address": "6062 Hollow Tree Ct, Colorado Springs",
      "maps_url": "https://maps.google.com/?cid=4614024894655572976"
    },
```


Looking at its website, I see they [serve meals](https://www.jewishcs.org/#Impact), which explains how it got the "restaurant" tag, since a place can have multiple `types`, but only one `primary type`. Then, I happened upon an entry for the Garden of the Gods Trading Post. Yes, [they have food](https://www.gardenofthegodstradingpost.com/restaurant-menu/), but still, it's primarily a gift shop. 


I decided to take the entire .json and run it through an LLM to get suggestions on what else could be removed. The .json is ~218k tokens (huge), so I used [Gemini 2.0 Flash Experimental](https://aistudio.google.com/prompts/new_chat) with its 1M token limit (and free price!). It suggested removing the following places, and the list was small enough that I could make a judgement call on each one.


- **Chabad of Colorado Springs Jewish Community** - agree, removed
- **Royal Clean Roots LLC** - agree, removed
- **XITE THC** - agree, removed
- **Cinemark Carefree Circle XD and IMAX** - agree, it ain't an Alamo Drafthouse
- **Cinemark Tinseltown Colorado Springs and XD** - agree, see above
- **Shop Old Colorado City** - agree, removed
- **Hillside Gardens & Event Center** - agree, removed
- **SoccerHaus Sports and Events Center** - I left it because they have a "[tavern](https://soccerhauscs.com/upper-90-tavern/)" 
- **Appliance Factory** - how did this even get in here??
- **Honey Baked Ham Seasonal Store** - only open during holidays to sell hams, removed
- **World Golf & Sand Creek Golf Course** - they've got a [restaurant](https://www.worldgolfsandcreek.com/food-beverage), I'll allow it 
- **The Broadmoor** - their restaurants are included separately in the list, so I'll remove the hotel proper
- **Garden of the Gods Trading Post** - if I'm allowing SoccerHaus I guess I'll leave this too


I decided to remove breweries that aren't brewpubs (eg removed [Mash Mechanix](https://www.mashmechanix.com/) but left [Voodoo Brewing](https://coloradosprings.voodoobrewery.com/)). I also allowed ice cream shops, bakeries, etc. since they're still primarily serving food, even if they're not "proper" restaurants.


I noticed an issue where a bunch of restaurants didn't have reviews. Most of them seemed like user-made duplicates in error (eg "Fargo's pizza" instead of "Fargo's Pizza Co."), wrong names (eg "Third Watch" instead of "First Watch"), made-up places, places with an address that is just someone's house, or otherwise not really relevant to this analysis (eg "Bon Fire" the food counter inside Maverick gas stations). None of these had reviews, so it was essentially junk data, and I deleted them all. The only legit one seemed to be [Kissing Camels Grille and Bar](https://maps.app.goo.gl/qDq5zPVTmmYLeTWs7). Why doesn't it have any reviews? If you like the place, go leave a review! _Update: someone reviewed it. It's on the list now!_


The rest of the list includes places that are **temporarily closed**, but I verified it doesn't have anything that's permanently closed, so I kept them in the dataset. Sometimes news changes faster than the community can update things. For example, **Wild Goose Meeting House** is listed as [Permanently Closed](https://maps.app.goo.gl/sAnfPwCrzUEJTm2E8) and doesn't show up in my dataset. However, [recent news](https://www.sidedishschniper.com/p/reclaiming-spaces) reports that new owners are taking over.


The only way to verify 100% quality is to read every line and evaluate every item, and I'm not going to do that. I've got stuff to do and restaurants to visit! At a certain point, you just need to accept that the data you've gathered is "good enough." Don't let perfect be the enemy of good. The final list ended up being **1130 1378 restaurants**.

![](https://mattsayar.com/media/posts/29/sadie_spaghet-2.jpg)A different kind of cleanup will be required here
#### Analysis and Ranking


The script I ran to gather all the restaurant data also sorted all the restaurants with a crude sort. It put all the five-star reviews together, descending by restaurants with the most reviews. Then, it grouped all 4.9-star reviews together, descending by restaurants with the most reviews, etc. This is an _okay_ way to sort things, but it doesn't quite capture the quality accurately enough. For example:

![](https://mattsayar.com/media/posts/29/drave_reviews.jpeg)The audience not dumb
How do we rank them with proper weighting in mind? I once found a list of [all the breweries in Colorado Springs](https://denvergazette.com/outtherecolorado/news/colorado-springs-breweries-ranked-according-to-google-reviews/article_36c1dda6-33ce-5984-98b5-7156abcc3cc8.html) ranked the same naive way, and I thought there must be a better way! I found a method called the [Bayesian Average](https://en.wikipedia.org/wiki/Bayesian_average) to rank the breweries in a better order. 

![](https://mattsayar.com/media/posts/29/SCR-20250211-hzbz-2.png)The crossed-out breweries closed since I made this list. It's been tough out there
I like that this ranking factors in the number of reviews, but it looks like it punishes the most-reviewed breweries. Are Cerberus and Bristol, the most popular breweries, _really_ the bottom of the barrel? Probably not. Is there another ranking method where they aren't punished so much?


I learned about Baysian Averages before LLMs, so I described the situation with ChatGPT-4o and one of its recommendations was to use a ranking called the [Wilson Score Interval](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval).


[Wilson Score Interval is] best if you want a statistically robust confidence-based ranking that prevents small sample sizes from skewing the results. It's widely used in ranking systems like Reddit and IMDB.


Is it _really_ used for Reddit and IMDB? Maybe it's a hallucination, but in this case, who cares? It'll take two seconds to try it out. Before I applied this method to the large restaurant dataset, I applied it to the brewery list as a test.

![](https://mattsayar.com/media/posts/29/SCR-20250211-iavm-2.png)
It definitely passes my vibe test; Cerberus and Bristol aren't at the bottom, and the top-ranked breweries are still near the top.


With the small test complete, I used Claude to create a script to take the restaurant list as input and spit out the list in the correct order. The algorithm requires a confidence level as input, and I chose a 99% confidence level. That value is more conservative, which means it tends to favor more established places, while a lower confidence level (eg 90%) would give newer places a bigger boost. Since we're dealing with restaurants, I feel more-established institutions should get the edge because they must be doing something right (ie making delicious food) to be open a long time and accumulate reviews.


That said, the list still features some newer 5-star upstarts near the top. That's math for you.


#### Show me the list already!

1[Arelita Authentic Cuban Food](https://maps.google.com/?cid=7997648668171497084)11[Taste of Ethiopia restaurant and coffee shop](https://maps.google.com/?cid=11568241016327120430)2[Starving](https://maps.google.com/?cid=14650812538361090246)12[Por Favor Tacos & Tragos](https://maps.google.com/?cid=6837405683728498551)3[Manitou Baked](https://maps.google.com/?cid=4172085632371742627)13[PETES Jamaican restaurant](https://maps.google.com/?cid=10665894754248702656)4[Crepe Amour CO](https://maps.google.com/?cid=18215604945407901105)14[Po' Brothers](https://maps.google.com/?cid=18225677543645498074)5[ArkCleoRich African Kitchen](https://maps.google.com/?cid=9842173075613705318)15[Roots Cafe](https://maps.google.com/?cid=3517180099783849568)6[B&B's Bunzy's and Booze](https://maps.google.com/?cid=3668443372041459561)16[Otis’s BBQ](https://maps.google.com/?cid=12227972586137526839)7[Shah Kabob House](https://maps.google.com/?cid=15161605575384883276)17[The Chuckwagon](https://maps.google.com/?cid=8956398435681866393)8[Turmeric Indian Cuisine at Power Center Point](https://maps.google.com/?cid=13469646130261908388)18[HAPPY EATS PASTA](https://maps.google.com/?cid=3241261187626057283)9[Momo Korean Restaurant](https://maps.google.com/?cid=9590968799704809556)19[Native Grill](https://maps.google.com/?cid=12523237067593518222)10[Mountain View Cafe and Catering](https://maps.google.com/?cid=13829676206660105633)20[Somjai Thai Cuisine](https://maps.google.com/?cid=9504524098400038078)
[View the full list here](https://mattsayar.com/ranking-the-best-restaurants-in-colorado-springs/) 


_Update: an earlier version of the list missed a few places because of my search algorithm. The list has been updated! It didn't really affect the heatmap insights in the visualizations._


Are the results what I expected? Not really! I only recognize a handful of these places, and they're great, which makes me excited to try the other places on this list. It's different from a human-curated list because there's no theme whatsoever, except "math did this."


If you'd like to do this with your own city, [feel free to use my code](https://github.com/MattSayar/restaurants_rankings).


### Visualize the data


A list is fun and all, but we've got location data too, so let's plot some stuff. Google Maps supports [heatmaps](https://developers.google.com/maps/documentation/javascript/heatmaplayer), and thanks to their decent code samples, it was easy to show where all the restaurants are.

![](https://mattsayar.com/media/posts/29/locations_narrow.png)Neat
It's fun to see where all the restaurants are located, but where are the BEST restaurants located? I started with an attempt to use [weighted data points](https://developers.google.com/maps/documentation/javascript/heatmaplayer#add_weighted_data_points), but the results were nearly identical to the map above. With so many data points, it's hard to distinguish them in a heatmap with limited colors. I considered tweaking opacity/intensity/colors, but I had an easier idea: just chop off the lower 75% of the list. That produced a far better comparison.

![](https://mattsayar.com/media/posts/29/SCR-20250210-lgov.gif)All the restaurants vs the top 25% restaurants
Much better! Here's a still image of just the top 25% so you don't get a seizure while trying to find the hottest food spots around town.

![](https://mattsayar.com/media/posts/29/SCR-20250211-sobw.jpeg)Once again, I'm sorry it's just images instead of interactive maps. It's more fun to pan and zoom!
#### Observations


The hotspots don't [JUST map to the population](https://xkcd.com/1138/), but many spots aren't surprising to anybody who's lived in Colorado Springs for a while. That said, there are some hidden gems that I was happy to unearth.


- Not surprising at all
- Downtown
- Old Colorado City
- Manitou


- Popular but not AS popular but also still not surprising
- Garden of the Gods Rd West of I-25
- University Village (shoutout Ambli Kitchen and Bar!)
- Interquest and Voyager
- All along Academy




##### Hidden Gems


**This may be the biggest benefit of this data analysis**. Here are some off-the-beaten-path locations worth checking out, including:


- [Space Village Ave cluster](https://www.sidedishschniper.com/p/dine-and-dash-a-space-village-ave)
- Astrozon and Academy ([Deluxe Wings](https://mattsayar.com/wings-in-the-springs/), Juanita's)
- Knob Hill (#1 Arelita's, #14 Po' Brothers)
- Powers and Dublin (Urban Egg, Skirted Heifer)


### Conclusion


It's a lot of fun to have an idea and be able to execute it quickly with help from LLMs. Previously, I wouldn't have had the time or patience to write quick scripts to parse data, format data, transform and analyze the aforementioned parsed and formatted data... but doing those things quickly feels like a superpower. I generally have the technical know-how to Get Stuff Done, and LLMs help quickly plug the gaps. Now, I have a broader understanding of how Google APIs work, I'm swifter using GitHub Copilot with VSCode, and I'm hungry to learn more.


But I'm more hungry to try some new eats in my town! Although, in the end, none of these places hold a fork to my delicious [backyard barbecue](https://mattsayar.com/tags/bbq/), so it's probably all wrong and not worth listening to.

![](https://mattsayar.com/media/posts/29/brisket.jpg)
But _definitely_ don't eat at Trailer Birds.


- [bbq](https://mattsayar.com/tags/bbq/)
- [chatgpt](https://mattsayar.com/tags/chatgpt/)
- [claude](https://mattsayar.com/tags/claude/)
- [colorado](https://mattsayar.com/tags/colorado/)
- [gemini](https://mattsayar.com/tags/gemini/)
- [llm](https://mattsayar.com/tags/llm/)
- [tech](https://mattsayar.com/tags/tech/)

 Share It[ Twitter ](https://twitter.com/intent/tweet?url=https%3A%2F%2Fmattsayar.com%2Fwhere-are-the-best-restaurants-in-my-city-a-statistical-analysis%2F&via=mattsayar&text=Where%20are%20the%20best%20restaurants%20in%20my%20city%3F%20A%20statistical%20analysis)[ LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fmattsayar.com%2Fwhere-are-the-best-restaurants-in-my-city-a-statistical-analysis%2F)![](https://mattsayar.com/media/website/me-removebg-preview.png)
### [Matt Sayar](https://mattsayar.com/authors/matt-sayar/)


Oh hey, it's me, the guy who owns this site. But who even is Matt Sayar? I'm still trying to figure that out. Here's some more places I'm at around the web.


- [BlueSky](https://bsky.app/profile/mattsayar.com) – you should follow me on BlueSky [here](https://bsky.app/profile/mattsayar.com)
- [LinkedIn](https://www.linkedin.com/in/mattsayar/) – Business Facebook
- [Stack Overflow](https://stackoverflow.com/users/557/mattsayar) – one of the first 500-ish to sign up!
- [GitHub](https://github.com/MattSayar) – projects
- [Tildes](https://tildes.net/user/mattsayar) – reddit alternative I prefer these days
- [Reddit](https://www.reddit.com/user/MattSayar/) – been here a while though
- [X (Twitter)](https://x.com/mattsayar) – don't use much anymore
- [Mastodon](https://infosec.exchange/@MattSayar) – I mean I started one but don't really use it
- Here - in case you find my ideas intriguing and wish to [subscribe to my newsletter](https://mattsayar.com/newsletter-signup/)

[![](https://mattsayar.com/media/posts/16/responsive/office-925806_1920-xs.webp)Previous Just pick a Static Site Generator and start writing](https://mattsayar.com/just-pick-a-static-site-generator-and-start-writing/)[Next Best and worst chain restaurant rankings in Colorado Springs![](https://mattsayar.com/media/posts/31/responsive/pexels-ian-panelo-11873775-xs.webp)](https://mattsayar.com/best-and-worst-chain-restaurant-rankings-in-colorado-springs/)