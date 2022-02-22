> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [javascript.plainenglish.io](https://javascript.plainenglish.io/deploying-any-app-to-github-pages-1e8e946bf890)

> GitHub Pages is a website holder for your projects. You can host your code directly from your GitHub ......

![](https://miro.medium.com/max/700/1*kC-xl8XOmmaDm_GUI-eChw.jpeg)

Photo by [SpaceX](https://unsplash.com/@spacex?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/nasa?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

[GitHub Pages](https://pages.github.com/) is a website holder for you & your projects. You can host your code directly from your GitHub repo. This article will help you how to manage your app in the `master` branch and deploy the code in the `gh-pages` branch easily.

You can choose any front-end framework like [React](https://reactjs.org/), [Vue](https://vuejs.org/), [Gatsby](http://gatsbyjs.com/), [Next](https://nextjs.org/), [Nuxt](https://nuxtjs.org/), [Gridsome](https://gridsome.org/), and build the app in the master branch and build the code using the `npm run build` command and host directly using the `gh-pages` branch.

The quickest way to put your app to GitHub Pages is by using a package — [gh-pages](https://github.com/tschaub/gh-pages).

```
npm i gh-pages -D
```

Or you can install the package globally:

```
npm i gh-pages -g
```

Add this simple script to your **package.json**:

```
{
  "scripts": {
    "deploy": "npm run build && gh-pages -d dist"
  }
}
```

**Note**: Assuming the build folder to be `dist`.

When you run `npm run deploy` all the contents of the build folder will be pushed to your repository’s gh-pages branch.

Create a repository with your username like `username.github.io`, Create a branch called `code` or you can name the branch anything. Build the app in this branch and when it comes to deploying the app use the `gh-pages`command to push the build folder contents to the gh-pages branch

**_Note_**_: In this case, you need to push your build directory to_ `_master_` _branch, use the following command_

```
{
  "scripts": {
     "deploy": "npm run build && gh-pages -d dist -b master",
  }
}
```

After running `npm run deploy` you should see your website at `[http://username.github.io](http://username.github.io/)`.

Run **gh-pages — help** to list all the supported options of the gh-pages package.

If your source code of the app is in a private repository, create a public repository named about, the source code will reside in the private repository and the static content generated from the build will go into the public repository

```
{
  "scripts": {
    "deploy": "npm run build && gh-pages -d dist --repo <url>",
  }
}
```

Deploy to another branch [which is not gh-pages]:

```
{
  "scripts": {
    "deploy": "gridsome build && gh-pages -d dist -b master",
  }
}
```

To include dotfiles while pushing the changes to the branch:

```
{
  "scripts": {
    "deploy": "npm run build && gh-pages -d dist -t"
  }
}
```

To change the commit message when publishing the change:

```
{
  "scripts": {
    "deploy": "npm run build && gh-pages -d dist -m Build v1"
  }
}
```

JavaScript In Plain English
---------------------------

Did you know that we have three publications and a YouTube channel? Find links to everything at [**plainenglish.io**](https://plainenglish.io/)!