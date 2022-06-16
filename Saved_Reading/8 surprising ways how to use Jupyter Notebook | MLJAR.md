> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [mljar.com](https://mljar.com/blog/how-to-use-jupyter-notebook/)

> The Jupyter Notebook is a great tool for experimentation with code. It provides the REPL (read-eval-p......

![](https://mljar.com/blog/how-to-use-jupyter-notebook/banner.jpg)The Jupyter Notebook is a great tool for experimentation with code. It provides the REPL (read-eval-print loop) with a visual interface for plots, tables and many more. You can mix Markdown and selected programming language (usually [Python](https://www.python.org/)). It is a default choice of development and experimentation environment for data scientists and machine learning practitioners. Have you heard about other ways to use the [Jupyter Notebook](https://jupyter.org/)? Let’s explore 8 alternative ways of how to use Jupyter Notebook that might surprise you!

1. Package development
----------------------

Surprise, surprise! The Jupyter Notebook can be used for python package development. There is a package [`nbdev`](https://github.com/fastai/nbdev) for this. It can greatly speed-up package development with:

*   automatic documentation generation and publishing on GitHub pages,
*   write tests in notebook (wow!) and setup Continous Integration (CI) with GitHub Actions,
*   automatic publishing on PyPi and conda,
*   two-way synchronize between notebook and source code - yes, you can use traditional IDE for code edits and then see it in Jupyter!

![](https://github.com/mljar/visual-identity/blob/main/media/nbdev-code-to-docs.gif?raw=true)

The package is developed by [Fast.ai](https://fast.ai/) (the company behind courses about Machine Learning for developers). Below is the video of Jeremy Howard (Fast.ai founder) about why notebooks are great for software development:

2. Web app
----------

There are two ways to convert Jupyter Notebook to web apps with use of open-source tools. You can use:

*   [`voila`](https://github.com/voila-dashboards/voila) with [`ipywidgets`](https://github.com/jupyter-widgets/ipywidgets),
*   [`Mercury`](https://github.com/mljar/mercury) framework.

The `voila` turns Jupyter Notebook into a standalone web application. The interactive widgets are added with `ipywidgets` package. The `voila` starts a [Tornado](https://www.tornadoweb.org/en/stable/) application with Jupyter kernel for each user.

The `Mercury` is an alternative to `voila`. It adds interactive widgets to the notebook without changes in the code. The YAML header is used to define online presence of the notebook. It makes the process of converting notebook to web application very easy - there is no need to write additional code for User Interface. Additional features of `Mercury` are:

*   built-in app gallery, you can serve multiple notebooks as web app,
*   download executed notebook as HTML or PDF,
*   add authentication to notebook - only logged users can see the notebook (super easy to add with one line of YAML!),
*   produce files with notebook and make them available for download.

Example application created with `Mercury` for converting images into sketches:

![](https://raw.githubusercontent.com/pplonski/artistic-sketches-jupyter-mercury/main/media/mercury_demo_2.gif)

Tutorials with example applications built with `Mercury`:

*   [Computer Vision web app from Jupyter Notebook](https://mljar.com/blog/computer-vision-app-python-opencv-mercury/) for converting images to sketches,
*   [NLP web app from Jupyter Notebook](https://mljar.com/blog/nlp-web-app-python-notebook/) to compute text sentiment.

3. Slides
---------

You can create slides with Jupyter Notebook. This might be a life saver if your presentation has a lot of plots that need to be often updated. You don’t need to do this manually, you can simply execute notebook with slides as output. The presentation created with Jupyter Notebook is using [reveal.js](https://github.com/hakimel/reveal.js/) package. Notebook can be converted to slides with [`nbconvert`](https://github.com/jupyter/nbconvert) or [`Mercury`](https://github.com/mljar/mercury). The `nbconvert` tool needs to be called in the terminal. The conversion command is below:

```
jupyter nbconvert --to slides <your-notebook>
```

If you decide to use `Mercury` tool, then you will need to add YAML configuration in the notebook. You can simply run:

in the directory with your notebook and the `Mercury` will generate slides for you. The important difference between `nbconvert` and `Mercury` is that latter allows to add widgets to the presentation and recompute slides even during the presentation. What is more, `Mercury` makes it super easy to deploy presentations to the cloud (it can be done with [one command](https://mercury-docs.readthedocs.io/en/latest/deploy/heroku/) on Heroku!). Below is a YouTube video with the presentation that was made in Jupyter Notebook. The code for presentation is on the [GitHub](https://github.com/pplonski/budapest-ml-forum-2022), it is also hosted on Heroku (free dyno) at [budapest-ml-forum-2022.herokuapp.com](https://budapest-ml-forum-2022.herokuapp.com/).

When building slides with Jupyter Notebook you might find the [RISE extension](https://github.com/damianavila/RISE) very helpfull. It allows you to preview to slides during writing.

4. Book
-------

You can create books with Jupyter Notebooks! There is a project called [`jupyter-book`](https://github.com/executablebooks/jupyter-book). It is an open-source tool for building publication-quality books and online documents. The book can be published as online website or can be exported to PDF file. It is a perfect for publishing computational materials. You can write code and include output of cells in the content.

The documentation of the tool is also created with `jupyter-book`. It is available at [jupyterbook.org](https://jupyterbook.org/en/stable/intro.html).

![](https://mljar.com/blog/how-to-use-jupyter-notebook/jupyter-book.png)

5. Blog
-------

You can create a blog with Jupyter Notebook. Of course, you can do it manually, for example export every notebook to HTML file (with `nbconvert`) and then just publish all files as static website. But you can do much better with [Nikola](https://getnikola.com/) framework. It reads your Jupyter Notebooks and produce the static website. The tool is open-source with MIT License (Nikola [GitHub repo](https://github.com/getnikola/nikola)). It comes with many [themes](https://themes.getnikola.com/), tags, feeds, archives, comments and can be easily extended.

![](https://mljar.com/blog/how-to-use-jupyter-notebook/nikola-themes.png)

6. Report
---------

You can automate report generation with Jupyter Notebook (and Python of course!). This can be achieved in many ways:

*   you can convert your notebook into PDF with [`nbconvert`](https://nbconvert.readthedocs.io/en/latest/). It is important to know that `nbconvert` not only converts Jupyter Notebooks into different formats, like HTML, Markdown, PDF, Latex, but also can execute the notebook.
*   you can use [`papermill`](https://nbconvert.readthedocs.io/en/latest/) to execute parametrized notebooks. It can be very usefull if you would like to create several versions of the report.
*   you can use [`Mercury`](https://github.com/mljar/mercury) for sharing notebooks as parametrized reports. What is more, you can schedule report generation and export final reports as HTML or PDF files.

7. Dashboard
------------

The interactive dashboards can be easily created with Python in Jupyter Notebook. The `Mercury` tool can be used to convert it to web-based application that can be shared over the internet. What is more, there is a `schedule` option available in `Mercury` that allows the notebook (dashboard) execution in predefined time intervals. It accepts the crontab-like string with interval definition.

Example YAML for notebook scheduling:

```
mercury run
```

![](https://mljar.com/blog/how-to-use-jupyter-notebook/jupyter-notebook-dashboard-example.png)

8. REST API
-----------

You can build REST API endpoints with Jupyter Notebooks. There are two packages for doing this:

*   [Jupyter Kernel Gateway](https://github.com/jupyter-server/kernel_gateway),
*   [Mercury](https://github.com/mljar/mercury) framework.

The `Jupyter Kernel Gateway` can be used to define many endpoints in the single notebook. For example:

```
---
title: Dashboard ⏰
description: Schedule execution every minute!
schedule: '*/1 * * * *'
---
```

```
# GET /hello/world
print("hello world")
```

The above code will create the GET endpoint at `/hello/world` address and POST endpoint at `/contacts`.

The `Mercury` can be alternative to `Jupyter Kernel Gateway`. It has different approach - one notebook is a one POST endpoint. The notebook name (to be strict, a slug) is the endpoint name. The notebook during the execution saves the response as JSON file. After notebook execution, the response is returned by the server. You can read more about this approach in the [documentation](https://mercury-docs.readthedocs.io/en/latest/notebook-as-rest-api/).

![](https://mercury-docs.readthedocs.io/en/latest/media/notebook-rest-api-view.png)

Summary
-------

The Jupyter Notebook is a great tool not only for experiments but also for software development. There are plenty of things that can be created with it. You can use Jupyter Notebook to create web apps, packages, blogs, dashboards, slides, REST API, books, and reports. The mix of code and Markdown with a connection of rich outputs gives endless possibilities.

### 💌 Let's stay in touch 💌

Please subscribe to the newsletter to be notified about our product updates and new articles. We will send you one e-mail per month.

 [![](https://mljar.com/images/mercury/mercury_banner_down.png)](https://github.com/mljar/mercury) 

### Share your Python Notebooks with others

  

<hr /> <div style="box-shadow: 12px black;"> <section> <div style="text-align: center;"> <h3>Check our open-source AutoML framework for tabular data!</h3> <br /> <div class="dark-button" style="padding-bottom: 60px;"> <a href="https://github.com/mljar/mljar-supervised" target="_blank">Check on GitHub!</a> </div> </div> <a href="https://github.com/mljar/mljar-supervised" target="_blank"> <div class="container flex blog-mljar-section"> </div> </a> </section> </div>