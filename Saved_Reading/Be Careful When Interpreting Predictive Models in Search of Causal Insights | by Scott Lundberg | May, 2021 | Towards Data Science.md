> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [towardsdatascience.com](https://towardsdatascience.com/be-careful-when-interpreting-predictive-models-in-search-of-causal-insights-e68626e664b6)

> A careful exploration of the pitfalls of trying to extract causal insights from modern predictive mac......

[Thoughts and Theory](https://towardsdatascience.com/tagged/thoughts-and-theory)
--------------------------------------------------------------------------------

A careful exploration of the pitfalls of trying to extract causal insights from modern predictive machine learning models.
--------------------------------------------------------------------------------------------------------------------------

[![](https://miro.medium.com/fit/c/56/56/1*SD3hMVq2yKA5BoxDIOp-AA.jpeg)](https://medium.com/@scottmlundberg?source=post_page-----e68626e664b6--------------------------------)

![](https://miro.medium.com/max/4000/1*v4eLsTUWLHpsTF5NxRvmTg.jpeg)

© Scott Lundberg / Ilkercelik — iStock

_A joint article about causality and interpretable machine learning with Eleanor Dillon, Jacob LaRiviere, Jonathan Roth, and Vasilis Syrgkanis from Microsoft._

Predictive machine learning models like XGBoost become even more powerful when paired with interpretability tools like SHAP. These tools identify the most informative relationships between the input features and the predicted outcome, which is useful for explaining what the model is doing, getting stakeholder buy-in, and diagnosing potential problems. It is tempting to take this analysis one step further and assume that interpretation tools can also identify what features decision makers should manipulate if they want to change outcomes in the future. However, **in this article, we discuss how using predictive models to guide this kind of policy choice can often be misleading.**

The reason relates to the fundamental difference between _correlation_ and _causation_. SHAP makes transparent the correlations picked up by predictive ML models. But making correlations transparent does not make them causal! All predictive models implicitly assume that everyone will keep behaving the same way in the future, and therefore correlation patterns will stay constant. To understand what happens if someone starts behaving differently, we need to build causal models, which requires making assumptions and using the tools of causal analysis.

Imagine we are tasked with building a model that predicts whether a customer will renew their product subscription. Let’s assume that after a bit of digging we manage to get eight features which are important for predicting churn: customer discount, ad spending, customer’s monthly usage, last upgrade, bugs reported by a customer, interactions with a customer, sales calls with a customer, and macroeconomic activity. We then use those features to train a basic XGBoost model to predict if a customer will renew their subscription when it expires:

```
X, y = user_retention_dataset()
model = fit_xgboost(X, y)
```

Once we have our XGBoost customer retention model in hand, we can begin exploring what it has learned with an interpretability tool like SHAP. We start by plotting the global importance of each feature in the model:

```
explainer = shap.Explainer(model)
shap_values = explainer(X)clust = shap.utils.hclust(X, y, linkage="single")
shap.plots.bar(shap_values, clustering=clust, clustering_cutoff=1)
```

![](https://miro.medium.com/max/2488/1*uZ-3K-srpab0vVR2TE-9MA.png)

This bar plot shows that the discount offered, ad spend, and number of bugs reported are the top three factors driving the model’s prediction of customer retention (it also includes a feature redundancy clustering which we will use later). This is interesting and at first glance looks reasonable.

However, when we dig deeper and look at how changing the value of each feature impacts the model’s prediction, we find some unintuitive patterns. SHAP scatter plots show how changing the value of a feature impacts the model’s prediction of renewal probabilities. If the blue dots follow an increasing pattern, this means that the larger the feature, the higher is the model’s predicted renewal probability.

```
shap.plots.scatter(shap_values)
```

The scatter plots show some surprising findings:

*   Users who report more bugs are more likely to renew!
*   Users with larger discounts are less likely to renew!

We triple-check our code and data pipelines to rule out a bug, then talk to some business partners who offer an intuitive explanation:

*   Users with high usage who value the product are more likely to report bugs and to renew their subscriptions.
*   The sales force tends to give high discounts to customers they think are less likely to be interested in the product, and these customers have higher churn.

Are these at-first counter-intuitive relationships in the model a problem? _That depends on what our goal is!_

Our original goal for this model was to predict customer retention, which is useful for projects like estimating future revenue for financial planning. Since users reporting more bugs are in fact more likely to renew, capturing this relationship in the model is helpful for prediction. As long as our model has good fit out-of-sample, we should be able to provide finance with a good prediction, and therefore shouldn’t worry about the direction of this relationship in the model.

This is an example of a class of tasks called **prediction tasks**. In a prediction task, the goal is to predict an outcome `Y` (e.g. renewals) given a set of features `X`. A key component of a prediction exercise is that we only care that the prediction `model(X)` is close to `Y` in data distributions similar to our training set. A simple correlation between `X` and `Y` can be helpful for these types of predictions.

However, suppose a second team picks up our prediction model with the new goal of determining what actions our company can take to retain more customers. This team cares a lot about how each `X` feature relates to `Y`, not just in our training distribution, but the _counterfactual_ scenario produced when the world changes. In that use case, it is no longer sufficient to identify a stable correlation between variables; this team wants to know whether manipulating feature `X` will _cause_ a change in `Y`. Picture the face of the chief of engineering when you tell him that you want him to introduce new bugs to increase customer renewals!

This is an example of a class of tasks called **causal tasks**. In a causal task, we want to know how changing an aspect of the world `X` (e.g bugs reported) affects an outcome `Y` (renewals). In this case, it’s critical to know whether changing `X` causes an increase in `Y`, or whether the relationship in the data is merely correlational.

A useful tool to understanding causal relationships is writing down a causal graph of the data generating process we’re interested in. A causal graph of our example illustrates why the robust predictive relationships picked up by our XGBoost customer retention model differ from the causal relationships of interest to the team that wants to plan interventions to increase retention. This graph is just a summary of the true data generating mechanism (which can be found in the [notebook version](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/Be%20careful%20when%20interpreting%20predictive%20models%20in%20search%20of%20causal%C2%A0insights.html) of this article). Solid ovals represent features that we observe, while dashed ovals represent hidden features that we don’t measure. Each feature is a function of all the features with an arrow to it, plus some random effects.

In our example we know the causal graph because we simulate the data. In practice the true causal graph will not be known, but we may be able to use context-specific domain knowledge about how the world works to infer which relationships can or cannot exist.

![](https://miro.medium.com/max/3048/1*YzB59LKARyCPxwZqu9MHCA.png)

There are lots of relationships in this graph, but the first important concern is that some of the features we can measure are influenced by **unmeasured confounding features** like product need and bugs faced. For example, users who report more bugs are encountering more bugs because they use the product more, and they are also more likely to report those bugs because they need the product more. Product need has its own direct causal effect on renewal. Because we can’t directly measure product need, the correlation we end up capturing in predictive models between bugs reported and renewal combines a small negative direct effect of bugs faced and a large positive confounding effect from product need. The figure below plots the SHAP values in our example against the true causal effect of each feature (known in this example since we generated the data).

The predictive model captures an overall positive effect of bugs reported on retention (as shown with SHAP), even though the causal effect of reporting a bug is zero, and the effect of encoutering a bug is negative.

We see a similar problem with Discounts, which are also driven by unobserved customer need for the product. Our predictive model finds a negative relationship between discounts and retention, driven by this correlation with the unobserved feature, Product Need, even though there is actually a small positive causal effect of discounts on renewal! Put another way, if two customers with have the same Product Need and are otherwise similar, then the customer with the larger discount is more likely to renew.

This plot also reveals a second, sneakier problem when we start to interpret predictive models as if they were causal. Notice that Ad Spend has a similar problem — it has no causal effect on retention (the black line is flat), but the predictive model is picking up a positive effect!

In this case, Ad Spend is only driven by Last Upgrade and Monthly Usage, so we don’t have an _unobserved_ confounding problem, instead we have an _observed_ confounding problem. There is statistical redundancy between Ad Spend and features that influence Ad Spend. When we have the same information captured by several features, predictive models can use any of those features for prediction, even though they are not all causal. While Ad Spend has no causal effect on renewal itself, it is strongly correlated with several features that do drive renewal. Our regularized model identifies Ad Spend as a useful predictor because it summarizes multiple causal drivers (so leading to a sparser model), but that becomes seriously misleading if we start to interpret it as a causal effect.

We will now tackle each piece of our example in turn to illustrate when predictive models can accurately measure causal effects, and when they cannot. We will also introduce some causal tools that can sometimes estimate causal effects in cases where predictive models fail.

Let’s start with the successes in our example. Notice that our predictive model does a good job of capturing the real causal effect of the Economy feature (a better economy has a positive effect on retention). So when can we expect predictive models to capture true causal effects?

The important ingredient that allowed XGBoost to get a good causal effect estimate for Economy is the feature’s **strong independent component** (in this simulation); its predictive power for retention is not strongly redundant with any other measured features, or with any unmeasured confounders. In consequence, it is not subject to bias from either unmeasured confounders or feature redundancy.

![](https://miro.medium.com/max/2488/1*VcQT3mN6iVB-AfpQ_aaKsw.png)

Economy is independent of other measured features.

Since we have added clustering to the right side of the SHAP bar plot we can see the redundancy structure of our data as a dendrogram. When features merge together at the bottom (left) of the dendrogram it means that that the information those features contain about the outcome (renewal) is very redundant and the model could have used either feature. When features merge together at the top (right) of the dendrogram it means the information they contain about the outcome is independent from each other.

We can see that Economy is independent from all the other measured features by noting that Economy does not merge with any other features until the very top of the clustering dendrogram. This tells us that Economy does not suffer from observed confounding. But to trust that the Economy effect is causal we also need to check for unobserved confounding. Checking for unmeasured confounders is harder and requires using domain knowledge (provided by the business partners in our example above).

For classic predictive ML models to deliver causal results the features need to be independent not only of other features in the model, but also of unobserved confounders. It’s not common to find examples of drivers of interest that exhibit this level of independence naturally, but we can often find examples of independent features when our data contains some experiments.

In most real-world datasets features are not independent and unconfounded, so standard predictive models will not learn the true causal effects. As a result, explaining them with SHAP will not reveal causal effects. But all is not lost, sometimes we can fix or at least minimize this problem using the tools of observational causal inference.

Observed confounding
--------------------

The first scenario where causal inference can help is observed confounding. A feature is “confounded” when there is another feature that causally affects both the original feature and the outcome we are predicting. If we can measure that other feature it is called an _observed confounder_.

![](https://miro.medium.com/max/2488/1*_Lo_52B7n8dMBJEj3GsCWg.png)

Ad spend is very redundant with Monthly usage and Last upgrade.

An example of this in our scenario is the Ad Spend feature. Even though Ad Spend has no direct causal effect on retention, it is correlated with the Last Upgrade and Monthly Usage features, which do drive retention. Our predictive model identifies Ad Spend as the one of the best single predictors of retention because it captures so many of the true causal drivers through correlations. XGBoost imposes _regularization_, which is a fancy way of saying that it tries to choose the simplest possible model that still predicts well. If it could predict equally well using one feature rather than three, it will tend to do that to avoid overfitting. But this means that if Ad Spend is highly correlated with both Last Upgrade and Monthly Usage, XGBoost may use Ad Spend instead of the causal features! This property of XGBoost (or any other machine learning model with regularization) is very useful for generating robust predictions of future retention, but not good for understanding which features we should manipulate if we want to increase retention.

This highlights the importance of matching the right modeling tools to each question. Unlike the bug reporting example, there is nothing intuitively wrong with the conclusion that increasing ad spend increases retention. Without proper attention to what our predictive model is, and is not, measuring, we could easily have proceeded with this finding and only learned our mistake after increasing spending on advertising and not getting the renewal results we expected.

Observational Causal Inference
------------------------------

The good news for Ad Spend is that we can measure all the features that could confound it (those features with arrows into Ad Spend in our causal graph above). Therefore, this is an example of observed confounding, and we should be able to disentangle the correlation patterns using only the data we’ve already collected; we just need to use the right tools from observational causal inference. These tools allow us to specify what features could confound Ad Spend and then adjust for those features, to get an **unconfounded** estimate of the causal effect of Ad Spend on product renewal.

One particularly flexible tool for observational causal inference is double/debiased machine learning. It uses any machine learning model you want to first deconfound the feature of interest (i.e. Ad Spend) and then estimate the average causal effect of changing that feature (i.e. the average slope of the causal effect).

Double ML works as follows:

1.  Train a model to predict a feature of interest (i.e. Ad Spend) using a set of possible confounders (i.e. any features not caused by Ad Spend).
2.  Train a model to predict the outcome (i.e. Did Renew) using the same set of possible confounders.
3.  Train a model to predict the residual variation of the outcome (the variation left after subtracting our prediction) using the residual variation of the causal feature of interest.

The intuition is that if Ad Spend causes renewal, then the part of Ad Spend that can’t be predicted by other confounding features should be correlated with the part of renewal that can’t be predicted by other confounding features. Stated another way, double ML assumes that there is an independent (unobserved) noise feature that impacts Ad Spend (since Ad Spend is not perfectly determined by the other features), so we can impute the value of this independent noise feature and then train a model on this independent feature to predict the output.

While we could do all the double ML steps manually, it is easier to use a causal inference package like econML or CausalML. Here we use econML’s LinearDML model (see [notebook](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/Be%20careful%20when%20interpreting%20predictive%20models%20in%20search%20of%20causal%C2%A0insights.html) for details). This returns a P-value of whether that treatment has a non-zero a causal effect, and works beautifully in our scenario, correctly identifying that there is no evidence for a causal effect of ad spending on renewal (P-value = 0.85):

![](https://miro.medium.com/max/2800/1*LMNgagwRANYrz6EEX8cGFA.png)

Remember, double ML (or any other observational causal inference method) only works when you can measure and identify all the possible confounders of the feature for which you want to estimate causal effects. Here we know the causal graph and can see that Monthly Usage and Last Upgrade are the two direct confounders we need to control for. But if we didn’t know the causal graph we could still look at the redundancy in the SHAP bar plot and see that Monthly Usage and Last Upgrade are the most redundant features and so are good candidates to control for (as are Discounts and Bugs Reported).

Non-confounding redundancy
--------------------------

The second scenario where causal inference can help is non-confounding redundancy. This occurs when the feature we want causal effects for causally drives, or is driven by, another feature included in the model, but that other feature is not a confounder of our feature of interest.

![](https://miro.medium.com/max/2400/1*bCP_0mrOI4uYM68ePSHhVg.png)

An example of this is the Sales Calls feature. Sales Calls directly impact retention, but also have an indirect effect on retention through Interactions. When we include both the Interactions and Sales Calls features in the model the causal effect shared by both features is forced to spread out between them. We can see this in the SHAP scatter plots above, which show how XGBoost underestimates the true causal effect of Sales Calls because most of that effect got put onto the Interactions feature.

Non-confounding redundancy can be fixed in principle by removing the redundant variables from the model (see [notebook](http://localhost:9999/notebooks/shap/notebooks/overviews/Be%20careful%20when%20interpreting%20predictive%20models%20in%20search%20of%20causal%C2%A0insights.ipynb)). For example, if we removed Interactions from the model then we will capture the full effect of making a sales call on renewal probability. This removal is also important for double ML, since double ML will fail to capture indirect causal effects if you control for downstream features caused by the feature of interest. In this case double ML will only measure the “direct” effect that does not pass through the other feature. Double ML is however robust to controlling for upstream non-confounding redundancy (where the redundant feature causes the feature of interest), though this will reduce your statistical power to detect true effects.

Unfortunately, we often don’t know the true causal graph so it can be hard to know when another feature is redundant with our feature of interest because of observed confounding vs. non-confounding redundancy. If it is because of confounding then we should control for that feature using a method like double ML, whereas if it is a downstream consequence then we should drop the feature from our model if we want full causal effects rather than only direct effects. Controlling for a feature we shouldn’t tends to hide or split up causal effects, while failing to control for a feature we should have controlled for tends to infer causal effects that do not exist. This generally makes controlling for a feature the safer option when you are uncertain.

Double ML (or any other causal inference method that assumes unconfoundedness) only works when you can measure and identify all the possible confounders of the feature for which you want to estimate causal effects. If you can’t measure all the confounders then you are in the hardest possible scenario: unobserved confounding.

![](https://miro.medium.com/max/2488/1*ZrAp5PnPjGi-YiBZ1c4AvQ.png)

The Discount and Bugs Reported features both suffer from unobserved confounding because not all important variables (e.g., Product Need and Bugs Faced) are measured in the data. Even though both features are relatively independent of all the other features in the model, there are important drivers that are unmeasured. In this case, both predictive models and causal models that require confounders to be observed, like double ML, will fail. This is why double ML estimates a large negative causal effect for the Discount feature even when controlling for all other observed features:

![](https://miro.medium.com/max/2800/1*4Du-ZN6tIHeXk06CRxd0JQ.png)

Barring the ability to measure the previously unmeasured features (or features correlated with them), finding causal effects in the presence of unobserved confounding is difficult. In these situations, the only way to identify causal effects that can inform policy is to create or exploit some randomization that breaks the correlation between the features of interest and the unmeasured confounders. Randomized experiments remain the gold standard for finding causal effects in this context.

Specialized causal tools based on the principals of instrumental variables, differences-in-differences, or regression discontinuities can sometimes exploit partial randomization even in cases where a full experiment is impossible. For example, instrumental variable techniques can be used to identify causal effects in cases where we cannot randomly assign a treatment, but we can randomly nudge some customers towards treatment, like sending an email encouraging them to explore a new product feature. Difference-in-difference approaches can be helpful when the introduction of new treatments is staggered across groups. Finally, regression discontinuity approaches are a good option when patterns of treatment exhibit sharp cut-offs (for example qualification for treatment based on a specific, measurable trait like revenue over $5,000 per month).

Flexible predictive models like XGBoost or LightGBM are powerful tools for solving _prediction_ problems. However, they are not inherently causal models, so interpreting them with SHAP will fail to accurately answer _causal_ questions in many common situations. Unless features in a model are the result of experimental variation, applying SHAP to predictive models without considering confounding is generally not an appropriate tool to measure causal impacts used to inform policy. SHAP and other interpretability tools can be useful for causal inference, and SHAP is integrated into many causal inference packages, but those use cases are explicitly causal in nature. To that end, using the same data we would collect for prediction problems and using causal inference methods like double ML that are particularly designed to return causal effects is often a good approach for informing policy. In other situations, only an experiment or other source of randomization can really answer _what if_ questions. Causal inference always requires us to make important assumptions. The main point of this article is that the assumptions we make by interpreting a normal predictive model as causal are often unrealistic.