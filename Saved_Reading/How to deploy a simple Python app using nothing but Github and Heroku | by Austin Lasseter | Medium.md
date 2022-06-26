> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [austinlasseter.medium.com](https://austinlasseter.medium.com/how-to-deploy-a-simple-plotly-dash-app-to-heroku-622a2216eb73)

> This is a step-by-step guide to deploying your first Python app. It’s intended for a complete beginne......

This is a step-by-step guide to deploying your first Python app. It’s intended for a complete beginner.

Start out on [github](https://github.com/) — a development platform for sharing and developing code. After signing up for a free github account, [fork](https://help.github.com/articles/fork-a-repo/) my [repo](https://github.com/plotly-dash-apps/102-flying-dog-beers) — it will have all the files you need to get started. It’s easy: at the top right, click on the `fork` button (note that in the screenshot it’s greyed out for me because I can’t fork my own repo):

![](https://miro.medium.com/max/1400/1*jByohcPdY469BwhsVlHgUA.png)

After a brief wait, you should now see the same repo but under your own name, not mine. While github makes sure to provide a reference to the source author of forked code, this is now yours to play with and develop as you please!

A quick tour of the necessary files in here:

*   `app.py` is the most important file. It contains all the code to personalize and get creative with the app, and most of your development work will happen here. Note that it must be named exactly like this if you want to deploy on Heroku — nothing other than `app.py` will work!
*   `requirements.txt` contains a list of all the Python libraries which Heroku will need to install in order to run your app. You’ll need to update this file from time to time, as requirements may change.
*   `runtime.txt` tells Heroku which version of Python to install. You’ll need to update this, too.
*   `Procfile` links `app.py` to the `gunicorn` library in your `requirements.txt`. You should never change the contents of this file.
*   The `assets` folder is where Heroku will look for any images or other secondary files to be used by `app.py` .
*   The `README.md` file is an optional description of your project.
*   The `.gitignore` is an optional housecleaning file that prevents you from showing the dirty laundry to your guests.
*   You can read more about all of these files and their purpose [here](https://dash.plotly.com/deployment#:~:text=GPU%20support-,Heroku%20for%20Sharing%20Public%20Dash%20apps%20for%20Free,-Heroku%20is%20one).

Okay, we’ll come back to github in a moment. First let’s go to [Heroku](https://www.heroku.com/), a free platform for deploying code. After signing up for an account, create your first app like this:

![](https://miro.medium.com/max/1400/1*SmjIEaSRd6bCofGNG42YFw.png)

Give it a memorable name and create:

![](https://miro.medium.com/max/1400/1*Ozb1RdGGwdBW0yQEhsRo4w.png)

Select `github` as your deployment method, and then search for your repo (note that it will appear under your name, not mine, since you already forked it!). Go ahead and pick “connect”.

![](https://miro.medium.com/max/1400/1*9DkMgBhoZzo_AaxM-NyoDg.png)

Heroku will offer you the option to enable automatic deploys, but just skip that for now and select manual deploy, “deploy branch”.

![](https://miro.medium.com/max/1400/1*ZC0lXi42U6vvSSTYK1wKew.png)

Heroku will display a status window showing the steps in the deployment process. This will take a couple of minutes.

![](https://miro.medium.com/max/1400/1*NLn1SLM_Ds8mEh7AqK5DgQ.png)

When it’s finished, Heroku will give you the option to view your app.

![](https://miro.medium.com/max/1400/1*HYhCjOIVRuyYRT2FeSxJeQ.png)

Your app should now be running smoothly on Heroku’s web service:

![](https://miro.medium.com/max/1400/1*9N0Ab_0qVtWuJ9bLm9h6OQ.png)

Now to modify the appearance of the app, go to github and click on`app.py` as follows:

![](https://miro.medium.com/max/1400/1*HzkM1udz6wVZyfEeAc8s3A.png)

You’ll notice there’s a small pencil icon at the right hand side, which will allow you to edit the file.

![](https://miro.medium.com/max/1400/1*Msj0Sa_pp243TV72kCkP2A.png)

Let’s take a look:

![](https://miro.medium.com/max/1400/1*g60EW9M-ime3m_c92f207Q.png)

As we can see from the `import` statements, we’re using a Python library called [Dash by Plot.ly](https://plot.ly/products/dash/). Other popular libraries for deploying Python apps are [Flask](http://flask.pocoo.org/) and [Bokeh](https://bokeh.pydata.org/en/latest/). Most of the code in this file you’ll want to leave untouched until you become more familiar with Dash, but lines 7–19 should be pretty safe for you to tinker with. This is where we’re defining the data (bitterness and alcohol for four beers from [Flying Dog Brewery](https://www.flyingdog.com/)). For example, we have a Python variable named `beer` whose value is a list — which is why the values are written inside square brackets. Below that, inside `bitterness` (which is known in Python as an instance of a Class object) we see four more Python variables: `x`, `y`, `name`, and `marker`. (Note: the screenshots below probably have a different color scheme from what you’re seeing on Github, but the code is the same).

![](https://miro.medium.com/max/1400/1*HJ4z_w0oCx1wtXyknhTu1w.png)

The first three are lists, like `beer`. The last one, `marker`, is a dictionary — which is why its values are inside curly brackets.

Try changing the color from `lightblue`to `darkgreen`. Try replacing one of the beers, too — for example, you might replace the [Chesapeake stout](https://www.flyingdog.com/beers/pearl-necklace/) with [blood orange ale](https://www.flyingdog.com/beers/bloodline/), which has an ABV of 7.0 and an IBU of 40. Save the `app.py` file when you’re done. Make sure that you update the `y` values in both the `bitterness` and the `alcohol` class objects.

![](https://miro.medium.com/max/1400/1*9T8T7OzU5YwEf_E0uz2C_A.png)

When you’re finished editing, write a short message to yourself (describing what you did) and commit your changes.

![](https://miro.medium.com/max/1400/1*j6F8ClaglIYgqY2xQjvC1Q.png)

Back on the main page of the repo, you should now see your commit message appearing by the name of the `app.py` file:

![](https://miro.medium.com/max/1400/1*T3PUHEEhdaOzgDjYq1DHbA.png)

Return to Heroku, click on your app, and select “deploy”:

![](https://miro.medium.com/max/1400/1*pZkG8aicInocWCweNeqEGg.png)

Scroll to the bottom of the page, and under “Manual Deploy”, select “Deploy branch”:

![](https://miro.medium.com/max/1400/1*BkjwF-1dPZyue2qkL9rkgQ.png)

Wait for a minute, and then select “View”. Your updates should now be visible on your app. You can view mine [here](https://flying-dog.herokuapp.com/). Congratulations! You’ve just built and updated your first Python app.