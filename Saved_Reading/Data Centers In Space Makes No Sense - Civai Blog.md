---
saved_date: 2026-02-12T05:56:27.754Z
title: "Data centers in space makes no sense - CivAI Blog"
---

# Data Centers In Space Makes No Sense - Civai Blog

# Data centers in space makes no sense 

 February 3, 2026 at 11:25 AM • by Andrew Yoon 
[SpaceX acquired xAI on Monday](https://www.foxbusiness.com/fox-news-science/spacex-acquires-xai-record-setting-deal-valued-over-1t), forming a $1.25 trillion behemoth with the goal of sending data centers into space. They’re not alone either: [Google](https://fortune.com/2025/12/01/google-ceo-sundar-pichai-project-suncatcher-extraterrestrial-data-centers-environment/) and a host of startups like [Lonestar](https://www.foxbusiness.com/technology/data-centers-outer-space-emerge-solution-ais-massive-energy-requirements), [Axiom](https://www.space.com/space-exploration/private-spaceflight/axiom-space-to-launch-its-1st-orbiting-data-centers-this-year), and Nvidia-backed [Starcloud](https://www.cnbc.com/2025/12/10/nvidia-backed-starcloud-trains-first-ai-model-in-space-orbital-data-centers.html) are scrambling into the field. Endless solar power, free real estate, and most importantly, huge rockets! What more could you want?


A [study from Google](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/) last year looked at the viability of doing AI in space. The authors envision a constellation of 81 satellites flying in close proximity, and argue that if the cost of launching stuff into low earth orbit fell to $200/kg, it could be competitive with an equivalent ground-based data center. They project this might happen around 2035 if SpaceX’s [Starship](https://en.wikipedia.org/wiki/SpaceX_Starship) program succeeds.


But even if we stipulate that radiation, cooling, latency, and launch costs are all solved, other fundamental issues still make orbital data centers, at least as SpaceX understands them, a complete fantasy. Three in particular come to mind:


1. Training and serving frontier AI at scale takes hundreds of thousands of GPUs. [xAI’s Colossus cluster](https://x.ai/colossus) reportedly has 200,000 GPUs. [OpenAI has plans](https://openai.com/index/openai-nvidia-systems-partnership/) for millions of them. Competing in this market would require launching hundreds of thousands, [if not millions](https://www.pcmag.com/news/spacex-eyes-1-million-satellites-for-orbital-data-center-push?test_uuid=04IpBmWGZleS0I0J3epvMrC&test_variant=A), of satellites into space. This would utterly dwarf the [roughly 15,000 satellites](https://www.discovermagazine.com/about-15-000-satellites-are-circling-earth-and-they-re-disrupting-the-sky-48550) that are currently orbiting the earth. Satellite deployments at this scale would dramatically increase the risk of [Kessler syndrome](https://en.wikipedia.org/wiki/Kessler_syndrome): a cascading explosion of debris [crippling our access to space](https://www.youtube.com/watch?v=yS1ibDImAYU).
2. Satellites can’t be upgraded at scale. Today when a new generation of AI hardware is released, companies can start rolling them out across their data centers immediately. In space, you have to launch a whole new fleet of a gazillion satellites.
3.  Data centers in space only make sense if they are cost effective _relative to normal data centers_. This means that even if, in 2035, the cost of rockets and extremely specialized satellite hardware fall to the point where they’re competitive with an AI server today, they will still need to be competitive with the price of running a normal AI server _in 2035,_ and for as long as data centers exist. Ground-based solar panels have been getting [more cost effective for decades](https://ourworldindata.org/grapher/solar-pv-prices) and show no sign of slowing down. With every improvement in normal energy production, data centers in space make less and less sense.


![A chart of solar cost per watt, 1975 to 2024. Source: Our World in Data](https://files.civai.org/blog/pv-price.webp) A chart of solar cost per watt, 1975 to 2024. Source: Our World in Data 


So if this is clearly nonsense, why are serious companies and investors piling into it? At least in the case of SpaceX, the company is [targeting an IPO](https://sherwood.news/markets/spacexs-planned-usd1-5-trillion-ipo-is-on-track-to-be-gargantuan-enough-even/) this year and has a huge incentive to raise excitement ahead of that. [xAI is burning mountains of cash](https://www.bloomberg.com/news/articles/2026-01-09/musk-s-xai-reports-higher-quarterly-loss-plans-to-power-optimus) every day and needs regular top-ups to keep the lights on. Investors themselves can be perfectly rational while buying into a project they (or at least their analysts) know isn’t feasible. They only need an expectation of profiting by selling to the next guy. Since the timelines to actually putting meaningful compute in space are so long, there’s plenty of time for companies and investors to ride this wave before coming back down to earth.