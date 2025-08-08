> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [bowshock.nl](https://bowshock.nl/irc/#short-version)

> Thanks to war, geopolitics, and climate change, Europe will have more frequent and more severe intern......

Thanks to war, geopolitics, and climate change, Europe will have more frequent and more severe [internet disruptions](https://nltimes.nl/2025/05/09/russia-preparing-war-europe-dutch-pm-activities-finnish-border) in the very near future. Governments and businesses need to prepare for catastrophic loss of communications. Unfortunately, the necessary changes are risky and expensive, which means they won’t do it until a [crisis](https://layeraleph.com/) is already here. However, small groups of volunteers with a little bit of time and money can provide crucial initial leadership to bootstrap recovery.

An Internet Resiliency Club is a group of internet experts who can communicate with each other across a few kilometers without any centralized infrastructure using cheap, low-power, unlicensed [LoRa](https://en.wikipedia.org/wiki/LoRa) radios and open source [Meshtastic](https://meshtastic.org/) text messaging software. These volunteer groups can use their radios, technical skills, and personal connections with other experts to restore internet connectivity.

This page is a quick-start guide to forming your own Internet Resiliency Club. You can also join a [mailing list](https://lists.bowshock.nl/mailman/listinfo/irc) for general questions and discussion about internet resiliency clubs:

[https://lists.bowshock.nl/mailman/listinfo/irc](https://lists.bowshock.nl/mailman/listinfo/irc)

*   [Skip directly to the section with hardware recommendations and setup instructions](#short-version)
*   [Watch the 10 minute video](https://ripe90.ripe.net/archives/video/1565/) of the RIPE 90 talk
*   [Read the slides](https://ripe90.ripe.net/wp-content/uploads/presentations/36-Internet-Resiliency-Club-RIPE-90.pdf) for the 10 minute RIPE 90 talk
*   [Read the longer slides](https://pretalx.t-dose.org/media/2025/submissions/LYGXHY/resources/Internet_Resiliency_Club_T-DOSE_YqGkZ7U.pdf) for the 45 minute T-DOSE 2025 talk

I am [Valerie Aurora](https://www.linkedin.com/in/valerieaurora/), a systems software engineer with 25 years of experience in open source software, operating systems, networking, file systems, and volunteer organizing. When I moved from San Francisco to Amsterdam in 2023, I started looking for ways to give back to my new home. In addition to systems consulting, I am a special rapporteur for the EU’s Cyber Resilience Act, serve as a RIPE Meeting program committee member, and speak at European technical conferences.

One of my nightmares is waking up one morning and discovering that the power is out, the internet is down, my cell phone doesn’t work, and when I turn on the emergency radio (if you have one), all you hear is “Swan Lake” on repeat.

As a recent immigrant to Amsterdam, I began to realize that this nightmare was increasingly likely. Russia regularly knocks out communications and power in Ukraine, using both bombs and hackers. In 2022, German windmills were disabled by malware aimed at Ukraine. Dubious tankers continue to “accidentally” drag their anchors and cut undersea cables in the Baltic. The head of NATO advised everyone to keep three days of supplies at home.

Ukraine’s advice on network resilience
--------------------------------------

What made me finally take action is watching a video created by [Ukrainian IXP 1-IX](https://1-ix.net/en/poslugy-en-translation/ua-exchange/) to teach other European countries what Ukrainian internet operators have learned about hardening and repairing internet infrastructure leading up to and following the 2022 Russian invasion. The practical realities of keeping networks operating during war were sobering: building camoflouged router rooms with 3 days of generator power, replacing active fiber optic cable with passive, getting military service exemptions for their personnel, etc.. You can watch the most recent version, [“Network Resilience: Experiences of survival and development during the war in Ukraine”](https://ripe90.ripe.net/archives/video/1582/), a 30 minute presentation at RIPE 90.

What is the Dutch government doing to prepare?
----------------------------------------------

Unfortunately, the government of the Netherlands is not following Ukraine’s lead. [Bert Hubert’s blog post](https://berthub.eu/articles/posts/cyber-security-pre-war-reality-check/) describes the Netherlands’ cloud-based “emergency communications” system, which will definitely not work in any emergency that affects power or internet connectivity.

I have asked many Dutch network operators if there is any official plan for the communications equivalent of a “black start” of the electrical grid. If there is one, it isn’t being shared with the people who will have to implement it.

Crisis engineering to the rescue
--------------------------------

The final piece of the idea came from a class I took on [Crisis Engineering](https://layeraleph.com/event/) from Layer Aleph, on how organizations facing an existential crisis either swiftly transform themselves into a more functional form, or they fail and become even more dysfunctional. Our class’s first question was, “How do you convince an organization that a crisis is coming and they need to prepare for it?”

Their answer was both depressing and freeing: “You can’t. All you can do is be prepared with tools and a plan for when the crisis arrives. That’s when the organization will listen.”

What can I do personally?
-------------------------

I started thinking about what I could personally do without any help from government or businesses. What if I could organize a group of volunteer networking experts who could communicate without any centralized infrastructure? We could effectively bootstrap communications recovery with just a few volunteers and some cheap hardware.

Ham radio is too expensive, difficult, and power-hungry
-------------------------------------------------------

Initially I looked into ham radio, but it is just too expensive, difficult, and power-hungry to be practical. Then Alexander Yurtchenko told me about LoRa (Long Range) radio and Meshtastic, a cheap, low-power method of sending text messages across a few kilometers.

After a few months of part-time research and organizing, the Amsterdam Internet Resiliency Club was born. This page exists to make it easier for other people to start Internet Resiliency Clubs in their area.

We need volunteer internet resiliency organizations
---------------------------------------------------

The evidence that Internet Resiliency Clubs are necessary keeps growing. Since I started this project, the city of Amsterdam announced that it is planning for three weeks without electricity. Spain and Portugal lost power for most of a day. The U.S. re-elected Donald Trump, who may at some point realize that he can hold Europe hostage by threatening to cut off access to U.S.-owned internet services like AWS and Microsoft Exchange. Simultaneously, large parts of Dutch government are migrating to email hosted by Microsoft, and major Dutch technology firms continue to migrate to AWS and Microsoft Azure.

If you and I don’t do this, dear reader, no one will.

How to form an Internet Resiliency Club:

*   Collect a group of internet-y people within ~10 km of each other
*   Decide how to communicate normally (Signal, Matrix, email, etc.)
*   Buy everyone LoRa (Long Range) radios and a powerbank with trickle charge
*   Install Meshtastic on the LoRa radios
*   Choose a LoRa channel to communicate on
*   Organize meetups, send messages over Meshtastic, have fun

If you work for a internet infrastructure company, you can suggest giving interested employees a LoRa radio, a mobile phone powerbank, and maybe even a small solar panel for their personal use (perhaps as part of an annual gift or bonus).

LoRa radios have several advantages for use in emergency communications:

*   no centralized infrastructure needed
*   no license needed
*   cheap (starting at ~€20)
*   low-power (<1W, can power with an ordinary mobile phone powerbank)
*   runs open source Meshtastic firmware
*   can send text messages across several line-of-sight hops (several kms)
*   can connect via Bluetooth or WiFi to phones/computers
*   many urban areas have a good Meshtastic network already

Amateur ham radio can transmit at higher bandwidth for longer distances, but requires extensive training, licensing, larger antennas, and more power. Ideally, both would be available in an emergency.

With a LoRa radio running the Meshtastic firmware, anyone can send text messages to anyone else with a Meshtastic node as long as it takes three or fewer forwards from other Meshtastic nodes to get from source to destination (usually around ~10 km but highly dependent on local terrain and weather).

Specifically, [LoRa](https://en.wikipedia.org/wiki/LoRa) is a proprietary technique for sending low bit-rate radio messages (~1 - 25 kbps) using very low power (<1W), derived from chirp spread spectrum techniques. [Meshtastic](https://meshtastic.org/) is open source firmware for LoRa radios that uses a flood-forward mesh protocol to send message across up to three line-of-sight hops between LoRa nodes running Meshtastic.

LoRa radios are for sale online. The cheapest versions are development boards, intended for companies to use while building a product, often without batteries, cases, or good antennas. To use them, you must connect to them from a phone or computer, either over Bluetooth via the Meshtastic app or over WiFi using a web browser. The more expensive systems may include an enclosure, battery, solar panel, larger screen, keyboard, etc. Some can be used without an additional phone or computer.

LoRa radios use relatively little power, often in the range of 100 - 200 mA. A normal mobile phone power bank with a capacity of 10000 - 20000 mAh can power a LoRa radio approximately 2 - 8 days, depending on chipset, time spent transmitting, whether WiFi or Bluetooth are in use, etc. The powerbank should support “trickle charging”; without this, many powerbanks will stop supplying power because the power draw of many LoRa radios is so low that the powerbank thinks nothing is connected and stops supplying power.

LoRa radios can be powered by directly plugging them into a small solar panel with USB output, or by charging a battery used by the LoRa radio. A small folding 800 cm^2 solar panel generating 15w with a 5W/500 mA max output is sufficient to power many LoRa radios. With this small of a setup, you don’t need fuses, charge controllers, buck/boost converters, or anything other than the solar panel and an optional mobile phone power bank.

LoRa radios are available in a huge range of capabilities and features. For an Internet Resiliency Club, we recommend one of:

*   Heltec V3: no case, no battery, WiFi/Bluetooth, OLED display, USB-C
*   LILYGO T-Echo: case, built-in battery, Bluetooth, e-ink display, USB-C

_IMPORTANT: Never turn on a LoRa device without an antenna attached! The power sent to the antenna can destroy the device if there is no antenna attached to radiate it._

Note: While many LoRa devices have USB-C ports, they often don’t implement USB-C PD (Power Delivery) and won’t charge their battery correctly on USB-C to USB-C cables. Use a USB-A to USB-C cable (often supplied with the device).

Heltec V3 series
----------------

If you have more time than money, try the latest Heltec V3, currently one of the cheapest boards available at around €20. It has a postage stamp-sized OLED screen, a couple of tiny buttons, WiFi/Bluetooth, and USB-C input/power (but use a USB-A to USB-C cable). Received messages are displayed on the OLED and can be cycled through with tiny buttons. Sending messages requires connecting to it via WiFi or Bluetooth.

It has no case, but the little plastic box it comes in can easily be turned into one with a sharp pen knife. It also has no battery, but it is a good idea to have a separate power bank anyway since you need a working phone or computer to send messages. It has no GPS.

The [Meshtastic page on this board](https://meshtastic.org/docs/hardware/devices/heltec-automation/lora32/?heltec=v3) includes links to purchase from in Europe. I bought mine from [TinyTronics](https://www.tinytronics.nl/en/development-boards/microcontroller-boards/with-lora/heltec-wifi-lora-32-esp32-s3-sx1262-with-0.96-inch-oled-display).

LILYGO T-Echo
-------------

If you have more money than time, I recommend the LILYGO T-Echo, a simple small low-power ready-to-use handheld device for about €80. It has ~3cm square e-ink display, a case with a few buttons, Bluetooth, GPS, and about a day’s worth of battery. Input/output/charging is via USB-C (but use a USB-A to USB-C cable). Received messages are displayed on the e-ink screen and can be cycled through with the buttons. Sending messages requires connecting with another device via Bluetooth.

The [Meshtastic page on this board](https://meshtastic.org/docs/hardware/devices/lilygo/techo/) includes links to purchase from in Europe. I bought mine from [TinyTronics](https://www.tinytronics.nl/en/development-boards/microcontroller-boards/with-gps/lilygo-ttgo-t-echo-nrf52840-lora-868mhz-bme280-gnss-black).

LILYGO T-Deck
-------------

If you want a standalone device that doesn’t require a separate phone or computer to send messages, the [LILYGO T-Deck](https://www.tinytronics.nl/nl/development-boards/microcontroller-boards/met-lora/lilygo-t-deck-esp32-s3-toetsenbord-met-2.8-inch-ips-display-en-touchscreen-lora-868mhz-zwart) includes a keyboard, trackball, and touch screen for about €70 - 80, depending on whether it includes a case and whether the antenna is internal or external. It has about 8 hours of battery. I’m not a fan because the screen and keyboard aren’t as good as the one on your phone and take extra battery to run. It is often out of stock, especially if you’re looking for a case and external antenna.

The [Meshtastic page on this board](https://meshtastic.org/docs/hardware/devices/lilygo/tdeck/) includes links to purchase from in Europe.

Upgrading the antenna
---------------------

Most of the antennas that ship with evaluation boards are not very good. One option for an upgrade if you’re using the recommended 868 MHz network is the [Taoglas TI.08.A](https://eleshop.eu/868-mhz-antenne-met-sma-connector.html).

_IMPORTANT: Never turn on a LoRa device without an antenna attached! The power sent to the antenna can destroy the device if there is no antenna attached to radiate it._

Some boards ship with Meshtastic already installed, but it’s undoubtedly several months out of date. Flashing LoRa boards is relatively easy; it can be as simple as using the [Meshtastic web browser flasher](https://meshtastic.org/docs/getting-started/flashing-firmware/esp32/) (requires Chrome or Edge) or dragging and dropping a file into a mounted USB drive presented by the device. A command line tool using a serial interface is also an option, but may require some fiddling with a Python env.

In Europe, two frequencies are available for use by LoRa: [868 MHz and 433 MHz](https://meshtastic.org/docs/configuration/region-by-country/). 868 MHz is the [most popular for Meshtastic users in Europe](https://meshtastic.org/docs/overview/radio-settings/). Several modem presets are available; use the default mode `LONG_FAST` unless you have a specific reason not to.

LoRa has [channels](https://meshtastic.org/docs/configuration/radio/channels/), a stream of messages using the same encryption key and channel name. Each device is configured with a default primary channel shared by all Meshtastic nodes. You can also configure secondary channels that can only be accessed by nodes with the same key and channel name. Choose an encryption key and channel name for a shared secondary channel. You can share a QR code to configure a device with the appropriate channels and settings.

The best time to learn how to work together with a group of people is before a crisis, not during it. Crisis engineering tells us that a team is more likely to be successful if everyone has already worked together.

Since this is a volunteer group, “working” together has to be fun. Invite your group to do fun things together, changing up what activity you are doing, where it is located, and what time it is held so that a wide variety of people can participate.

If you have more questions or suggestions, please join our [mailing list](https://lists.bowshock.nl/mailman/listinfo/irc):

[https://lists.bowshock.nl/mailman/listinfo/irc](https://lists.bowshock.nl/mailman/listinfo/irc)

Many people helped me with Internet Resiliency Club:

*   [Ukrainian IXP 1-IX](https://1-ix.net/en/poslugy-en-translation/ua-exchange/) and other Ukrainian operators for their video [“Network Resilience: Experiences of survival and development during the war in Ukraine”](https://ripe90.ripe.net/archives/video/1582/)
*   [Andrew Yourtchenko](https://www.linkedin.com/in/andrew-yourtchenko-9304551/) for early brainstorming
*   [Layer Aleph](https://layeraleph.com/) and their [Crisis Engineering](https://layeraleph.com/event/) class
*   Bert Hubert’s entire blog, but especially [Cyber Security: A Pre-War Reality Check](https://berthub.eu/articles/posts/cyber-security-pre-war-reality-check/)
*   [Trammell Hudson](https://trmm.net/) for helping me with battery and solar questions
*   Timo Hilbrink for researching antennas
*   The entire Amsterdam Internet Resiliency Club