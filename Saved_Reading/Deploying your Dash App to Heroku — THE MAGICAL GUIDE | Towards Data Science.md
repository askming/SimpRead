> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [towardsdatascience.com](https://towardsdatascience.com/deploying-your-dash-app-to-heroku-the-magical-guide-39bd6a0c586c)

> So you have your Dash app running on your local machine and you’re finally ready to share it with the......

![](https://miro.medium.com/max/1400/1*XUI3DmnqWVQgBQNTgCnyEQ.png)

(Image by author, inspired by [Charlie the Unicorn](https://www.youtube.com/watch?v=CsGYh8AacgY) and [Gunicorn](https://gunicorn.org/))

[Hands-on Tutorials](https://towardsdatascience.com/tagged/hands-on-tutorials)
------------------------------------------------------------------------------

So you have your [Dash](https://plotly.com/dash/) app running on your local machine and you’re finally ready to share it with the world on a public site.

The problem is: words like like Git, Flask, Gunicorn and Heroku sound like strange mythical creatures, even after a few drinks. Worry not: having just been through the process of deploying Dash to Heroku myself for the first time, I’ll share what I’ve learned along the way. I’ll outline some surprising pitfalls and solutions I found, in the hope this will save you time and effort. This is the guide I wish I had when I started.

**Quickstart  
**I’ve built a [Dash-Heroku starter pack](https://github.com/danny-baker/dash-heroku) on Github. This is a barebones Dash app fully setup and tested that runs on Heroku. It has all the necessary special files and tweaks so you can serve static files (such as images) which is the most common pain point. For first timers, I’d recommend you get this demo running on Heroku first, and then transfer your locally running Dash project code carefully over to it :)

**Background**

The process to successfully deploy a Dash app on Heroku is not trivial for many first timers. For example, simply serving static files (like documents, audio, images, video) doesn’t work out of the box with Heroku like it does from your local machine. I didn’t realise this, along with a few other quirks.

This essay is designed to supplement the existing documentation, and attempts to fill in some gaps, explain the quirks, and provide a very brief fly-over of each component and how everything fits together. I’ll share notes from my personal experience. I’ll also attempt to explain the technology stack based on my imperfect understanding of how it all works. No doubt I’ve got some things wrong, so I welcome corrections from the community.

**Assumptions**

*   You have a running Dash app locally hosted (with a requirements.txt)
*   You’re relatively new to Python
*   You have a strong cup of coffee (better yet, a glass of red)
*   You’ve never deployed a public web app before
*   Words like Heroku and Gunicorn scare you.

**The Problem**

In my research I scanned many blog articles and guides about deploying Dash to Heroku, but found most to be a little lacklustre or not specific to Dash. YouTube videos, too, are often super quick (do it in 15 minutes!!) and don’t explain the core concepts. The majority of the guidance I’ve seen so far is bare minimum, light on explanation, and doesn’t outline key issues you’ll encounter in the detail you need. If you’re working with Dash, chances are you are new to Flask as well, so many concepts are not well understood. I’ve yet to read a guide that outlines the core concepts and pitfalls for _specifically_ deploying a Dash app to Heroku. I believe this lack of comprehensive written guidance is a (solvable) barrier to entry for many potential Dash users.

**How much pain is this going to be? (about 10 hours)**

How hard really is it to Deploy to Heroku as a first timer? How much pain is involved? What problems will you encounter? I’m glad you asked. In short, I’d say optimistically it can be done in a few hours ground-up, but realistically about 10hrs for a first timer. Pain meter: medium spicy.

This is because it takes _time_ to create the accounts and setup the environments like GitHub and Heroku command line interface, add special new files to your project directory (repository), modify the code in a few spots, and get used to the commands you need in order to see what’s going on and make it all work. It can be a little daunting at first, but once you’ve done the initial setup, you’re on easy street. Deploying code running on your laptop to your live public web app is a few mouse clicks and single command in a terminal, which is super cool. (Caveat: this does not cover security and authentication — this is purely to deploy a hobby app).

**Why Heroku?**

Like myself, you’ve probably heard of Heroku as a well-loved platform for deploying hobbyist web applications for free. Of course, it’s not the only one — there are many, and it is scalable to enterprise-level deployments. But it is universally known and liked by the community, so I chose to go this route and see what all the fuss was about. Verdict so far: _loving it_. Key reasons the community loves Heroku (as far as I know):

*   It’s free for hobby apps, which is great to get started and for demos
*   It’s got clear, concise documentation
*   It natively supports Python web apps (read: minimal config needed)

**What is Heroku?**

It’s a platform-as-a-service (PaaS) for deploying and hosting web applications. In the context of your Dash app, this means Heroku provides the physical hardware (storage, compute), software services (linux/unix/sql), and dependencies (packages), in a containerised environment to deploy and host your application on a publicly accessible URL (end-point). It does this through provision of virtualised linux containers called “Dynos” which essentially act as your personal linux webserver, with ram, cpu, and linux ‘installed’. (It’s not quite like this in reality but a good analogy).

Dynos come in a variety of shapes and sizes and can be scaled vertically (more ram, compute, storage per instance) or horizontally (duplicate dynos in parallel) as your specific project requirements demand. You can hot swap dyno types instantaneously at command line while your app is live, which is mint. The free version gets you one dyno with up to 500MB storage and 500MB ram. It sleeps after 30 minutes of inactivity, presumably so Heroku resources are not drained. So the catch with the free version is that your website can take a good 30–60 seconds to load initially, as your free Dyno is provisioned on demand. If you go to a paid plan, starting at about $7USD/month, your dyno(s) stay on and ready 24hrs/day.

The biggest constraint with Heroku dynos is RAM; you don’t get much. At least in my experience, I’ve found that Python (Dash) apps often require a decent amount of RAM as you are reading in Pandas dataframes and doing all sorts of fun stuff. It’s fine for a single instance of your app for a select small group of users, but if you want to scale out you will need to run duplicate parallel instances of your app, and this will cost you $$ in RAM to either run more dynos in parallel, or multiple instances of your app in larger tier dynos.

**Why GitHub?**

In short — Heroku natively supports deploying repositories that reside in GitHub. This is good news. Basically it means if your project is already in a GitHub repository (free for private/public repos) then you can easily deploy it on Heroku AFTER you have added a few additional files that are outlined in the deployment guides, and in a section further below.

If you’ve been developing your pet project on a local machine, before you can deploy on Heroku you first need to get your project onto GitHub. (Note you don’t have to use GitHub, but it’s an easy option.) This is an important step to take your code to a public (or private) cloud repository. It’s a good move anyway because you have full versioning history, you are protected from hard drive failure, and you can share publicly or privately. It does, however, come with intellectual debt, with some interesting concepts and terminology to get your head around, like clone, fork, merge, push, pull, and commit.

Yet another barrier to newcomers is the issue with security and how this affects you accessing and changing the code in your cloud repository on GitHub or similar. Basically, GitHub wants a secure connection between your computer and its servers before it will happily accept code changes. There are two main ways it achieves this: using credential authentication over HTTPS (requiring a username/pass every time a connection is made), or via SSH public/private key encryption, which is not natively supported by Windows. This extra complication, combined with the other scary words like clone, fork, and merge can be a little overwhelming at first. Fear not: there’s a desktop app that can setup a secure connection between itself and your GitHub repo, facilitating seamless easy updates to your code repository.

If you’re developing on a windows/mac machine (which I assume the majority of first timers are), I’d highly recommend getting the [Github Desktop](https://desktop.github.com/) application. This just makes the process of cloning, fetching and pushing changes back to your repository on Github _MUCH_ easier without the need for any command line. It’s not that I’m against command line, it’s just that this particular process can be clunky on windows, requiring either user credential authentication or SSH keys mentioned above.

(Special note: if you are more hardcore you can of course install [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) which is a way to have a fully functioning Linux system on Windows without the need for dual boot options etc. If you do this you can setup SSH keys and enjoy the benefits of linux for managing your code repo but it’s really not necessary for first timers.)

In short, you can avoid a _lot_ of hassle just by using the Desktop app, and setting up the security within the app — then it’s single click of the mouse to commit changes and push updated code to your remote repo on GitHub.

**What is Git?**

No one really knows.

**What is Gunicorn?**

When you figure it out, let me know. [Gunicorn](https://gunicorn.org/), to the best of my understanding, is a production-ready HTTP server specifically for Python web applications which runs natively in Unix; it’s the thing that actually _serves_ the web browser request. If you’ve been developing your Dash app purely on your local machine @ ‘localhost:8080’ or ‘http://127.0.0.1:8050/’ you will be running a light weight HTTP server that is shipped with your Python installation. This is not Gunicorn. It’s likely you have not yet glimpsed this rare and mythical creature of the forest.

The local HTTP server (shipped with your Python installation) is automatically run by your Python Kernel when your dash app is executed on your local machine. The issue is that it’s not designed for handling incoming traffic from a production website and so when you deploy to the web, you need a production-ready HTTP server. A popular one is Gunicorn. Notably, Heroku provides native support for Gunicorn, which makes things easy. It’s all outlined in the guides, but just to clarify, all you need to do is add a single line of code to your dash app (‘server = app.server’), add Gunicorn into your requirements.txt so it is installed as a package on your local machine (and by Heroku during deployment), and reference it in a special file you will create called the Procfile. More on this later but I think it’s worth briefly touching on the HTTP server as it’s all a bit mysterious the first time.

**What is Flask?**

Before cups and bottles, in the medieval times people used to drink out of flasks. This of course has no bearing whatsoever on what Flask is in the context of Python, but hold onto the drinking analogy. Flask is a micro-framework for Python web applications. If you are not familiar with frameworks and why they matter, essentially they provide a structure (a pattern) for you to develop your project in a way that supports growth and multiple collaborators. Some are rigid and some are more flexible, but the ultimate goal is to help a complex project become manageable by separating functional components of code (and other things) into logical places, as well as providing tools and libraries to assist with common tasks (e.g. setting up sql databases, accessing the underlying host operating system, user authentication etc.)

Popular frameworks in Python include Flask and [Django](https://www.djangoproject.com/). In Ruby, you have probably heard of [Ruby on Rails](https://rubyonrails.org/), which is a well known framework for developing Ruby web apps. If you are sticking to a bare minimum Dash app, you don’t need to worry about frameworks, but just note they are for proper, serious, software development and they are important. Your Dash app is in reality still a Flask app (Dash sits on top), Flask has just been hidden away behind the scenes. The reason Flask is popular is it is non-rigid, and does not enforce strict directory structures and file names. It can also be used piecemeal, so parts of it can be plucked out as needed, keeping the project as simple as it can be while retaining features. This is probably why Plotly chose it for Dash! To return to the ‘drinking analogy’: unlike many other frameworks, Flask as a framework can be ‘sipped’ as it is needed to support just the features that are what is needed for a given project, and no more.

**Web is hard**

This is a simple truth. Web is multi-layer, multi-language, multi-protocol, multi-platform, and multi-user. It’s a mind-boggling chain of infrastructure bolted to other infrastructure to make a modern (scalable) web application run. For many non-IT people (and IT people for that matter), even the concept of a locally hosted webserver takes a bit of abstract thought, let alone understanding the true technology stack that lies underneath a real client-server architecture. It’s also worth reflecting on just how new some of this technology really is, so I’ve indicated the year these tools were created in the table below.

**The simplified technology stack**

This is imperfect, so please help me to correct it. But it’s useful, I think, to see some of the layers required to get your code deployed onto the web. We start with your actual code at the very top of the stack, and drill down layers all the way to Heroku.

The way I think of the technology stack

The point I’m trying to make here is that this grossly oversimplified web technology stack is still far from simple; to say nothing about front end layers such as Javascript, CSS etc. Web is hard because of the sheer number of abstraction layers.

> Dash, to me, is a beautiful abstraction at the very top of the technology stack — building upon everything below it — in order to simplify what is actually an insanely complex machine: the modern data-rich web application.

**Dash-Heroku deployment, in a nutshell**

What actually needs to be done:

1.  Dash app running on localhost
2.  Install [Git](https://git-scm.com/downloads)
3.  Setup GitHub account (+ recommend install GitHub Desktop)
4.  Setup Heroku account (+ install the command line interface)
5.  Add dependencies and special files (i.e. install and import Gunicorn, create Procfile and runtime.txt)
6.  Clone repo from GitHub to local machine (only once)
7.  Create Heroku app linked to your repo (only once, ref deployment guides, Heroku CLI)
8.  Commit and push your code changes to GitHub repo (repetitively)
9.  Deploy/Re-deploy Heroku app by pushing changes (“git push Heroku main”)

Just to be super clear here for those that are very new to this process. Once you’ve created a Heroku app linked to your repo, this means that when changes are pushed to your Heroku remote repo on Github, this will actually trigger a Heroku build of your app. What that means is, when you type `git push heroku main`this is pushing your local code to your remote heroku repository on github (on a branch called main, which is the default primary). As soon as this happens, this will trigger a build and you should see this in your terminal (console) immediately after you type the command.

**Deployment Guides**

The guides below are concise and useful, and I would of course start with these. If I’m honest, I think they are a little light on detail for newcomers and would benefit greatly by having a supplementary _explanatory guide_ akin to something like this essay.

*   Plotly’s [Dash deployment guide](https://dash.plotly.com/deployment)
*   [Heroku’s guide](https://devcenter.heroku.com/articles/getting-started-with-python)
*   Recommendations: Install [Heroku command line interface](https://devcenter.heroku.com/articles/heroku-cli) (CLI) and [GitHub Desktop](https://desktop.github.com/) if a windows/mac user
*   Also, this YouTube [tutorial](https://www.youtube.com/watch?v=b-M2KQ6_bM4&feature=youtu.be) from a fellow [Plotly Community Forum member](https://community.plotly.com/).
*   My [Dash-Heroku](https://github.com/danny-baker/dash-heroku) starter pack on GitHub is a running base to build on.

![](https://miro.medium.com/max/1200/1*UDbTISUcXgNXNpwTEV130Q.png)

(Image from [pixilart.com](https://www.pixilart.com/), Source: [https://art.pixilart.com/6977a966cd0f6a7.png](https://art.pixilart.com/6977a966cd0f6a7.png))

A quick note on the special files you need uniquely to get your python project deployed to Heroku. This is outlined in the deployment guide, so I’ve just provided a few notes from my experience:

**Ingredient 1: Procfile**

This strange extensionless file must reside in your project root, and tells Heroku how to handle web processes (in our case using Gunicorn HTTP server) and the name of your Python application.

Typically the Procfile would contain a single line:

```
web: gunicorn app:server
```

Where:

*   ‘web:’ tells Heroku the dyno main process is a web process
*   ‘gunicorn’ tells heroku that the HTTP server to use is Gunicorn (for which it has native support for)
*   ‘app’ references the _filename_ of the main python file without the .py extension. So if you follow the convention of ‘app.py’ you would use ‘app’ here. But note if your main python file is ‘anything.py’, you would have ‘anything’ in place of ‘app’.
*   ‘server’ references the underlying flask app. Commonly you would define a _variable_ ‘server = app.server’ and this references that variable, I believe. To be more confusing, the ‘app’ in this variable declaration actually refers to the dash instantiation variable in the snippet below:

```
app = dash.Dash(__name__)
server = app.server
```

Yes I know what you’re thinking, this is finicky and it’s really easy to misunderstand with all these ‘app’ references everywhere. Take home is: as long as you’re using an app.py main file, as is the convention, and you declare a ‘server = app.server’ line of code after your Dash declaration, you can use the example Procfile and it should work. If you get anything with the Procfile wrong, pain and suffering will ensue.

To make the Procfile in Windows, you can just create a text file, and enter the single line. Then strip out the extension. This worked for me and I don’t need to have a secondary Procfile.win, which is sometimes talked about in the documentation. Not, Heroku is case-sensitive and the Procfile filename _MUST_ be with a capital ‘P’. Lower case ‘p’ will not be detected properly by Heroku.

**Ingredient 2: runtime.txt**

This file (which must also be in your root project folder) simply tells Heroku which Python runtime to use. Currently it can contain a single line, e.g.:

```
python-3.7.8
```

Just create this as a notepad .txt file in your project folder, and commit-push to your remote GitHub repo. Done.

That’s really it. It’s mainly these two files (Procfile, runtime.txt) that Heroku needs in your repo project directory in order to work. As long as you have followed the basics, and added Gunicorn to your requirements.txt etc, in theory you are good to go.

**Ingredient 3: perseverance**

Not to be underestimated. Dogged… stubborn… raw perseverance is a key ingredient to the potion.

![](https://miro.medium.com/max/1400/1*xVwkKNCRXO_vXpqBFf-SAA.png)

(Image from [pixilart.com](https://www.pixilart.com/), Source: [https://art.pixilart.com/6977a966cd0f6a7.png](https://www.pixilart.com/art/green-forrest-3b0fcf2469d413f))

You’ve got your code in a GitHub repository, with the required tweaks and files created. You have Heroku CLI installed and have created a Heroku app linked to your GitHub repo. It’s 4am and the sun is coming up soon. The scene is grim with pizza boxes on the floor and red wine stains on the keyboard. It’s show time.

Cast the magic spell:

```
git push heroku main
```

These four words are the spell that makes the magic happen. Type them into the terminal in the right conditions, sit back smugly, and enjoy the show.

For those new to Heroku, if everything has worked after your “git push Heroku main” from the terminal, your app will be deployed to a Heroku subdomain like:

[http://blah.herokuapp.com/](http://blah.herokuapp.com/)

If this is the case, recommend a little dance.

Copy-paste the URL displayed in the terminal into your browser and get ready…to be disappointed. Chances are the first time you will see “APPLICATION ERROR” in the browser or something like that. Don’t panic.

The first thing you should do is bring up the log (which is effectively your python console) and see what’s going on, from the terminal. Any print statements, or logger outputs from your code will display here just as they do in the console on your local machine. But most importantly, you also see Heroku system outputs such as Dyno restarts, crashes, and error messages. This is the critical way to see what’s happening with your app at a low level. I usually keep a dedicated CMD window open running Heroku logs, which is my console output.

View logs:

```
heroku logs --tail
```

Check for things like “Module not found errors” and simple things like that. The most common problems I’ve found are forgetting to add packages to my requirements.txt file because I frantically installed them to my local machine with conda/pip to get something working. If you’ve found some obvious problems, fix them, commit-push your code to GitHub, and then redeploy from Heroku CLI with `git push heroku main`.

Notably though, the first time is indeed the hardest. Errors in your Procfile, for example, can still cause Heroku to deploy successfully, but the dynos will crash or fail to start, so definitely check the Procfile.

Special note if there are no changes to your remote repo on GitHub, Heroku will not deploy. (Which makes sense.) So if you have a GitHub repo cloned onto your local machine, and you are making changes, be sure to commit and push changes back to your remote GitHub repo first (either with command or with GitHub desktop), then in the Heroku CLI terminal, just type in the “git push heroku main” deploy command.

Below is my cheat-sheet of important tips, pitfalls, and pitfall solutions when using Heroku.

Explicitly referencing your app name:

Note that Heroku can sometimes be funny about requiring you to explicitly specify your app in the command. If you just have a single Heroku app, often you can avoid it. But sometimes (without any apparent reason) you may need to append “-a <yourapp>” to the Heroku command.

Display current apps:

```
heroku apps
```

Display current dynos:

```
heroku psheroku ps -a <yourapp>
```

[Scale dynos](https://devcenter.heroku.com/articles/scaling):

```
heroku ps:scale web=2:standard-1x
```

In this case, we are provisioning two standard-1x dynos to run concurrently. Special note, if WEB_CONCURRENCY=4, this means each Dyno can serve 4 simultaneous HTTP incoming requests, meaning your whole Dash application can serve 8 concurrent requests — the benefit of horizontal scaling. More on this later.

Run bash terminal:

```
heroku run bash -a <yourapp>
```

Restart dynos:

```
heroku dyno:restart
```

Add additional log metrics:

```
heroku labs:enable log-runtime-metrics
```

View logs:

```
heroku logs --tail
```

From the Heroku CLI (once logged in) when you have deployed your app, you can view a live log tail by typing

```
heroku logs --tail
```

Repeated just in case you missed it. This is mission critical. It essentially gives you your console output. One thing I’d suggest is adding in a new feature that outputs resources statistics of your dyno(s) timestamped every ~20 seconds, like memory levels, cpu load etc, which is very useful. Type this in the Heroku CLI, to permanently add it:

```
heroku labs:enable log-runtime-metrics
```

I repeat: serving static files _DOES NOT WORK_. Something of paramount importance that is not obvious, is that out-of-the-box, Heroku (I think more correctly: Gunicorn itself) does not natively support serving static files. This means that while your python application itself can access files in any subfolder in your project folder (such as .csv files etc.), it’s a very different story to actually serve them via http in the client browser.

Any images, documents, video, audio, anything you are currently serving from your ‘localhost’ webserver will fail on deployment with Heroku. I believe this is a quirk of the PaaS model in that files themselves are not stored in the traditional way you would imagine them to be on a file system, so there are issues with low level connection/packet headers that are attached to files, and/or Gunicorn itself does not natively support serving static files. In any case, there’s magic under the hood.

As an aside, if you don’t already know from the docs, it’s important to understand that the Heroku file system is not persistent. Like many of my past relationships, Heroku’s file system is ephemeral or transient; it lasts about as long as a one-night stand. With the exception of the files you deploy with your project repo (e.g. csv, json files etc.), any new files created at runtime will disappear after a few days, like that fleeting love interest that wasn’t to be, or that person who never called.

Anyway, to store and serve persistent static files, as I said, any files uploaded to Heroku as part of your project file suite will be fine, persistent, and accessible by your dash app internally. BUT the moment you want to serve static files externally to browser, you will rapidly run into problems. There are two main solutions I know of. One is simple and fast.

Solutions:

1.  Host your files on a 3rd party like [S3](https://aws.amazon.com/s3/), [Cloudfront](https://aws.amazon.com/cloudfront/) and link the URL in your dash app (Worth doing if you will be hosting a serious footprint of files)
2.  Use the [Whitenoise](http://whitenoise.evans.io/en/stable/) library. Quick and easy. A few lines of code and you’re serving files just like in your localhost setup.

Personally I found Whitenoise to be a life saver. Literally “pip install whitenoise” (and make sure it’s in your requirements.txt) and you’re almost there. A few lines of code needed in your dash app:

```
from whitenoise import WhiteNoise
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root=‘static/’)
```

You should already have the “server=app.server” anyway, as this is needed by Gunicorn and for the Procfile.

What this essentially does is wrap Whitenoise around your underlying Flask app. You can then have a folder (which you must create) called “static/” in your root. Everything contained within this (including subfolders) can be statically served by Heroku. Images, videos, pdfs, whatever you want.

Special note: the ‘static’ folder effectively becomes root when you are serving files, so you would use ‘image.blah’ in your code rather than ‘static/image.blah’ even though your actual file is in /static/image.blah.

Special note: Heroku is _file extension case-sensitive_. So blah.png is different to blah.PNG.

Also, don’t try to get smart and change the ‘static’ folder name in the Whitenoise code declaration to some arbitrary name or ‘assets’ or anything like that: it must be ‘static’ due to an underlying Flask constraint.

This seems like a pretty major issue that I don’t think much documentation exists on. I spent a long time on Stack Overflow looking it up.

Also, the Whitenoise documentation is not specific to Dash — it is more focused on general Python apps which are typically Flask apps. This means that it’s still not obvious what you need to do, and the code snippets will not work without modification. For example Whitenoise states that, for Flask apps, you must add the following code to your app:

```
app.wsgi_app = WhiteNoise(app.wsgi_app, root=‘static/’)
```

This won’t work for your dash app. In this case ‘app’ is the Flask app. So in a Dash app (which sits on top of Flask) you actually need to replace the ‘app’ references (both of them) with ‘app.server’ in the snippet above to reference the underlying Flask app and for Whitenoise to work. Or simply define a variable such as ‘server = app.server’ and use the code snippet I outlined at the beginning of this section.

Again, lots of these things are a two second fix if you know how. But can cost you literally HOURS AND HOURS……AND HOURS of time if you don’t know. Trivial for Flask developers. Not trivial _at all_ for newcomers.

For some reason, I had lots of trouble with this. Anyway, I managed to get it going by simply having a:

```
/assets/favicon.ico
```

From my root project directory. Special note that no other static files are served from here; it’s a stand-alone folder. In fact, don’t be lulled into thinking you can serve static files from your /assets folder on Heroku: you can’t. (see Whitenoise section).

Others have had problems with Heroku changing the extension name of the favicon causing it to fail. One failsafe option to note is that you can log into a Heroku Bash shell after you have deployed, and navigate to all your project folders/files to see what Heroku sees. See [this](https://community.plotly.com/t/display-favicon-in-heroku-dash-app/44013/3) post.

From heroku CLI:

```
heroku run bash -a <yourappname>
```

This will provision a new Dyno container running a Bash shell. Basically, it’s a terminal to your deployed app.

There is lots of ‘worker’ and ‘web’ terminology that gets confusing. Out of the box when using Gunicorn as your Python HTTP server, Heroku essentially guesses how many concurrent web-worker-processes to run for each dyno instance running your web app. Typically this is 1–6 concurrent ‘gunicorn — web-worker-processes’ per dyno for the commonly used hobby to standard 2-x dynos. This is how many client requests (i.e. from a web browser) can be simultaneously served by your app at an instantaneous point in time.

A Gunicorn web-worker-process is a process capable of serving a _single_ HTTP request at a time. So if you only had one, this means your website becomes quite unresponsive with a few users making simultaneous requests, and having to wait for these requests to be actioned from a queue. Essentially this is the magic of what Gunicorn does: it forks the main web process running on its Dyno into multiple processes so that it can serve simultaneous HTTP requests from each given Dyno resource.

Web concurrency, in Heroku, therefore, essentially allows each dyno instance to carve up it’s resources to serve multiple concurrent HTTP requests, which it terms WEB_CONCURRENCY. Unfortunately this can sometimes lead to Heroku (by default) underestimating resources needed, and running over Dyno memory limits, causing failure, restarts, massive slow-downs due to disk swap having to be used, etc. At least, this is what I experienced. Basically, you don’t want to have too much web concurrency because it might break your dyno, and the default setting chosen by Heroku may be too high.

You don’t need to worry about this on day one — your app will work. But as you start load testing it, you may find you run into memory overrun issues and all sorts of things like that. If you have a high horsepower python application that chews resources, I suggest you manually set your WEB_CONCURRENCY variable in Heroku command line.

For example:

```
heroku config:set WEB_CONCURRENCY=3heroku config:set WEB_CONCURRENCY=3 -a <herokuappname>
```

The above statement variations tell Heroku to carve up Dyno resources to support 3 concurrent HTTP requests per Dyno, for all Dynos running a Web process for your app. (So if you have multiple Dynos serving your app in parallel, it automatically sets them all to this same setting).

If performance is not compromised, you can increase web concurrency to increase the number of clients you can serve in parallel, while minimising Dyno cost. If you need to serve more, you can scale Dyno’s horizontally knowing that each one can serve an explicit number of concurrent HTTP requests that you have set.

And of course, you can monitor this with “heroku logs --tail” or in the Heroku dashboard ‘metrics’ section.

It’s important to be aware that Heroku has an immutable 30 second timeout for serving HTTP requests. This is a common problem especially encountered by Dash users because many of the data science applications have long load times — see [this](https://community.plotly.com/t/dash-heroku-timeout/36517) post. These might work fine running on your local host, but be aware that your Heroku deployed app must be able to serve within 30 seconds or it will time out. Heroku [docs](https://devcenter.heroku.com/articles/request-timeout) state a few work arounds but take special note of this problem.

If you’re new to GitHub, just know that you can have multiple ‘branches’ of your project, as you might take it in different directions. These can be merged or left as separate branches. The central branch by default is called ‘master’ or ‘main’ in GitHub. When you create your Heroku app it interacts with your GitHub repository to create a kind of Heroku mirror image behind the scenes. If you’re developing your current code on a branch that is not master or main, prepare for pain. It’s not that it can’t be done, I just had a lot of trouble with this when trying to deploy to Heroku. I found the best rule of thumb is to just develop all my code on the default ‘main/master’ branch in my GitHub repository.

A quick run down of other useful stuff.

**Custom Domain**

It’s not too difficult to set up a custom domain for your Heroku app. Obviously, you need to purchase a domain first. Once you’ve done that, the provider will typically have a portal where you can login and adjust settings.

Heroku will generate a unique DNS target in the SETTINGS area of the Heroku web portal dashboard, once logged in. Such as:

```
Animate-salamander-8duwlndghfqbtj0t90uep8bmu.herokudns.com
```

What you need to do is copy this (your own) DNS target from the Heroku web portal (settings page) and then login to your domain provider portal and for your domain, create a new “CNAME record” with host “www” value “Animate-salamander-8duwlndghfqbtj0t90uep8bmu.herokudns.com” (your unique Heroku DNS target).

If it worked ok, in a few hours your new domain should work!

Essentially all this is doing is redirecting to the Heroku DNS target when someone types your actual domain name. If your new domain is [www.blah.com](http://www.blah.com/) it now has a CNAME record to redirect the incoming HTTP request to Heroku infrastructure, which then serves the actual page (as if you’d typed in [blah.herokuapp.com](http://blah.herokuapp.com/)). It’s a tricky thing to set this stuff up because it’s not done very often and you don’t know if it has worked for hours (because it takes time for DNS servers around the world to replicate the new domain list). But there is [good documentation](https://devcenter.heroku.com/articles/custom-domains).

**Flask Caching on Heroku**  
If you have Flask Caching running on your local machine, it’s straight forward to setup on Heroku with a free Memcachier account. And the [docs](https://devcenter.heroku.com/articles/memcachier#python) are good. You can cache to the ephemeral Heroku file-system without Memcachier, noting you might max out your 500MB of Dyno storage, otherwise you can get 100MB free high performance cache via Memcachier.

**Getting Fancy with security and autoscaling etc.**

When you want to go to the next level and setup auto-scaling of machines, proper security/authentication etc, I think this is when it starts becoming worth considering [Dash Enterprise](https://dash.plotly.com/dash-enterprise), upgrading to top-tier Dynos with Heroku (gets $$) OR going down the path of setting up custom infrastructure manually. If you are going manual you could, for example, provision your own virtual machines, set up containerised pipelines using Docker and Kubernetes, manage autoscaling/self healing with Rancher, etc. It’s well and truly DevOps and cloud engineering territory. I’m sure there are lots of other midrange steps you can take like run Docker to build your own containers to deploy, but I want to keep this guide to the bare minimum you need to get on Heroku.

**Closing thoughts**

For the newbies and hobbyists out there, I sincerely hope this short novel has been useful to help get your project up and running faster with less pain. Don’t forget I have a fully running [starter pack](https://github.com/danny-baker/dash-heroku) on Github that you can use as a guide to see EXACTLY what you need as a bare minimum.

I think Dash is a game-changing tool that is helping to bring data science literacy (and data visualisation technology) to the mainstream public and business world. This can only be a good thing, and this is why I’ve taken the time to write this piece.

Final caveat: I’m not an expert on web, but I do think there is a major gap in the documentation for new starters. I’ve done my best to research all the facts, so this content is to the best of my understanding. I certainly invite corrections and clarifications by the experts.

![](https://miro.medium.com/max/144/0*mTDIB04BC7HQsE1E)