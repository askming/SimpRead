> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [support.sas.com](https://support.sas.com/kb/22/954.html)

> PROC LOGISTIC automatically computes a test of the proportional odds assumption when the response is ......

PROC LOGISTIC automatically computes a test of the proportional odds assumption when the response is ordinal and the default logit link is used. For such a response, several cumulative logits are simultaneously modeled while only a single logit is modeled for a binary response. Conceptually, you could fit a model that has a complete set of parameter estimates for each of the cumulative logits. The simpler model that PROC LOGISTIC fits constrains each predictor's parameter estimates to be the same across all of the logits. This means that the fitted surfaces for the logits are all parallel and they are only allowed to differ by a constant shift that necessitates the separate intercepts that you get when you fit an ordinal model. When the logit link is used, this parallelism assumption also implies that the effect of a given predictor is the same regardless of where you"cut" the ordinal response to dichotomize it. The proportional odds test in PROC LOGISTIC simply tests whether the parameters are the same across logits, simultaneously for all predictors. PROC GENMOD fits the same proportional odds model, but it does not provide a proportional odds test.

Peterson and Harrell (1990) note that this proportional odds/parallelism test is known to be liberal when the sample size is small, which means that the _p_-value for the test could be artificially too small in small samples, possibly leading to inappropriate rejection of the proportional odds assumption. Because of this, graphical assessment of the parallelism assumption is useful and is discussed and illustrated in [this note](http://support.sas.com/kb/37944.html). However, nonsignificant test results (large _p_-values) are not affected and reliably indicate adequacy of the proportional odds/parallel assumption. [Stokes, et. al. (2012)](http://support.sas.com/kb/22572.html) suggests doing cross-tabulations of the response with each predictor involved in the model. If all cell counts are about five or larger, then the sample size should be adequate.

### Alternative models for nonproportional odds

If the sample size is adequate and the test or the graphs convince you to reject the assumption of proportional odds, then there are two alternative models that are often used. The first is the _generalized logit model_ which can be fit by simply specifying the LINK=GLOGIT option in the MODEL statement of PROC LOGISTIC. This model treats the response as nominal (unordered) rather than ordinal and has a full set of parameters for each generalized logit.

The second alternative is the _partial proportional odds model_. This model continues to treat the response as ordinal, but allows you to assume proportional odds for some predictors while not for others. To do this, the model contains separate parameters across the logits for model effects exhibiting a lack of proportionality. A single parameter is used for effects where proportionality holds. At the extreme, the fully nonproportional odds model can be fit in which separate parameters are used for every effect in the model. Beginning in SAS® 9.3 TS1M2, you can fit this model using the UNEQUALSLOPES option in the MODEL statement of PROC LOGISTIC. In earlier releases, the model can also be fit using PROC NLMIXED as shown in the addendum at the end of this note.

In the following sections, proportional, fully nonproportional, and partial proportional odds models are fit to data from a study of a new analgesic for dental pain relief. Increasing relief from pain was recorded on a 5-point scale (0-4). Initially, PROC LOGISTIC is used to fit a proportional odds model involving three categorical predictors: the research center (CENTER=1 or 2), the treatment dosage (TRT=ACL, TL, ACH, TH, or P), and baseline pain (BASELINE=0 or 1). The proportional odds test is significant and tables produced with PROC FREQ (not shown) of each predictor against the response show generally adequate sample size. The alternative models are then fit.

[Derr (2013)](http://support.sas.com/kb/22592.html) also discusses the testing and assessment of the proportional odds assumption. When the proportional odds assumption is rejected, he illustrates fitting the partial proportional odds model.

### Fitting the proportional odds model

The following statements fit the proportional odds model to the dental data using PROC LOGISTIC. In PROC LOGISTIC, the CLASS statement creates reference-coded dummy variables for each of the three categorical predictors. The ORDER=DATA option causes predictor levels to be ordered as they first appear in the data set. The DESCENDING response variable option allows you to model the probability of the higher response levels[NOTE](#note). The OUTPUT statement saves the cumulative predicted probabilities and the individual predicted probabilities to data set LOG.

```
      proc logistic data=dent;
         class center baseline trt / param=ref order=data;
         model resp(descending)=center baseline trt;
         output out=log predprobs=(c i);
         run;


```

The test of the proportional odds assumption in PROC LOGISTIC is significant (_p_=0.0089) indicating that proportional odds does not hold and suggesting that separate parameters are needed across the logits for at least one predictor. A visual assessment of the assumption is provided by [plotting the empirical logits](http://support.sas.com/kb/37944.html).

<table bordercolor="#C1C1C1" summary="Procedure Logistic: Cumulative Model Test"><colgroup><col> <col> <col> </colgroup><thead><tr><th colspan="3" scope="colgroup">Score Test for the Proportional<br>Odds Assumption</th></tr><tr><th scope="col">Chi-Square</th><th scope="col">DF</th><th scope="col">Pr&nbsp;&gt;&nbsp;ChiSq</th></tr></thead><tbody><tr><td>35.2185</td><td>18</td><td>0.0089</td></tr></tbody></table> <table bordercolor="#C1C1C1" summary="Procedure Logistic: Parameter Estimates"><colgroup><col> <col> </colgroup> <colgroup> <col> <col> <col> <col> <col> </colgroup><thead><tr><th colspan="7" scope="colgroup">Analysis of Maximum Likelihood Estimates</th></tr><tr><th scope="col">Parameter</th><th scope="col">&nbsp;</th><th scope="col">DF</th><th scope="col">Estimate</th><th scope="col">Standard<br>Error</th><th scope="col">Wald<br>Chi-Square</th><th scope="col">Pr&nbsp;&gt;&nbsp;ChiSq</th></tr></thead><tbody><tr><th scope="row">Intercept</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-2.8017</td><td>0.4814</td><td>33.8722</td><td>&lt;.0001</td></tr><tr><th scope="row">Intercept</th><th scope="row">3</th><td>1</td><td nowrap="nowrap">-1.0732</td><td>0.4472</td><td>5.7600</td><td>0.0164</td></tr><tr><th scope="row">Intercept</th><th scope="row">2</th><td>1</td><td nowrap="nowrap">-0.0434</td><td>0.4436</td><td>0.0096</td><td>0.9221</td></tr><tr><th scope="row">Intercept</th><th scope="row">1</th><td>1</td><td>0.9330</td><td>0.4476</td><td>4.3440</td><td>0.0371</td></tr><tr><th scope="row">CENTER</th><th scope="row">1</th><td>1</td><td nowrap="nowrap">-1.9388</td><td>0.2555</td><td>57.5778</td><td>&lt;.0001</td></tr><tr><th scope="row">BASELINE</th><th scope="row">0</th><td>1</td><td nowrap="nowrap">-0.6137</td><td>0.3361</td><td>3.3342</td><td>0.0679</td></tr><tr><th scope="row">TRT</th><th scope="row">ACL</th><td>1</td><td>1.5309</td><td>0.3978</td><td>14.8129</td><td>0.0001</td></tr><tr><th scope="row">TRT</th><th scope="row">TL</th><td>1</td><td>1.5045</td><td>0.3993</td><td>14.1940</td><td>0.0002</td></tr><tr><th scope="row">TRT</th><th scope="row">ACH</th><td>1</td><td>1.8204</td><td>0.4002</td><td>20.6867</td><td>&lt;.0001</td></tr><tr><th scope="row">TRT</th><th scope="row">TH</th><td>1</td><td>2.0204</td><td>0.4010</td><td>25.3863</td><td>&lt;.0001</td></tr></tbody></table>

### Fitting the fully nonproportional odds model

The addition of the UNEQUALSLOPES option causes PROC LOGISTIC to fit the fully nonproportional odds model which includes separate slope parameters for each effect on each of the logits. If you also include the EQUALSLOPES option (available beginning in SAS 9.4 TS1M2), the model includes both a common, reference slope (slope on last logit) for each effect as well as parameters representing the differences between the reference slope and the separate slopes. The results include joint tests of these sets of difference parameters in the "Type 3 Analysis of Effects" table. Each set is labeled U__effect_ which is a test of the proportional odds assumption for _effect_. These statements fit the fully nonproportional odds model, parametrized to test the proportional odds assumption in each model effect.

```
      proc logistic data=dent;
         class center baseline trt / param=ref order=data;
         model resp(descending) = center baseline trt / unequalslopes equalslopes;
         run;


```

The nonsignificant tests for the CENTER and BASELINE effects (_p_=0.1782 and _p_=0.1727, respectively) suggest that the proportional odds assumption is reasonable for those effects. The test of proportional odds for the TRT effect (_p_=0.0688) is marginally significant. This seems consistent with the [plots of the empirical logits](http://support.sas.com/kb/37944.html).

<table bordercolor="#C1C1C1" summary="Procedure Logistic: Type 3 Tests"><colgroup><col> </colgroup> <colgroup> <col> <col> <col> </colgroup><thead><tr><th colspan="4" scope="colgroup">Type 3 Analysis of Effects</th></tr><tr><th scope="col">Effect</th><th scope="col">DF</th><th scope="col">Wald<br>Chi-Square</th><th scope="col">Pr&nbsp;&gt;&nbsp;ChiSq</th></tr></thead><tbody><tr><th scope="row">CENTER</th><td>1</td><td>42.7602</td><td>&lt;.0001</td></tr><tr><th scope="row">U_CENTER</th><td>3</td><td>4.9138</td><td>0.1782</td></tr><tr><th scope="row">BASELINE</th><td>1</td><td>2.6708</td><td>0.1022</td></tr><tr><th scope="row">U_BASELINE</th><td>3</td><td>4.9871</td><td>0.1727</td></tr><tr><th scope="row">TRT</th><td>4</td><td>32.1236</td><td>&lt;.0001</td></tr><tr><th scope="row">U_TRT</th><td>12</td><td>19.9122</td><td>0.0688</td></tr></tbody></table>

In the Parameter Estimates table, notice that the parameter estimates for each effect include a common, reference slope parameter (slope on RESP=1 logit) followed by three difference parameters for a total of four degrees of freedom. The three difference parameters for CENTER and BASELINE are all nonsignificant, as expected, but the difference parameters for TRT="ACH" show some significance which explains the marginally significant proportional odds test for the TRT effect.

<table bordercolor="#C1C1C1" summary="Procedure Logistic: Parameter Estimates"><colgroup><col> <col> <col> </colgroup> <colgroup> <col> <col> <col> <col> <col> </colgroup><thead><tr><th colspan="8" scope="colgroup">Analysis of Maximum Likelihood Estimates</th></tr><tr><th scope="col">Parameter</th><th scope="col">&nbsp;</th><th scope="col">RESP</th><th scope="col">DF</th><th scope="col">Estimate</th><th scope="col">Standard<br>Error</th><th scope="col">Wald<br>Chi-Square</th><th scope="col">Pr&nbsp;&gt;&nbsp;ChiSq</th></tr></thead><tbody><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-1.9143</td><td>0.7984</td><td>5.7487</td><td>0.0165</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">3</th><td>1</td><td nowrap="nowrap">-0.8706</td><td>0.5798</td><td>2.2549</td><td>0.1332</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">2</th><td>1</td><td nowrap="nowrap">-0.6624</td><td>0.5321</td><td>1.5495</td><td>0.2132</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">1</th><td>1</td><td>1.1911</td><td>0.5724</td><td>4.3307</td><td>0.0374</td></tr><tr><th scope="row">CENTER</th><th scope="row">1</th><th scope="row">&nbsp;</th><td>1</td><td nowrap="nowrap">-2.2391</td><td>0.3424</td><td>42.7602</td><td>&lt;.0001</td></tr><tr><th scope="row">U_CENTER</th><th scope="row">1</th><th scope="row">4</th><td>1</td><td>0.7502</td><td>0.6000</td><td>1.5632</td><td>0.2112</td></tr><tr><th scope="row">U_CENTER</th><th scope="row">1</th><th scope="row">3</th><td>1</td><td>0.1533</td><td>0.3906</td><td>0.1542</td><td>0.6946</td></tr><tr><th scope="row">U_CENTER</th><th scope="row">1</th><th scope="row">2</th><td>1</td><td>0.4673</td><td>0.2899</td><td>2.5984</td><td>0.1070</td></tr><tr><th scope="row">U_CENTER</th><th scope="row">1</th><th scope="row">1</th><td>0</td><td>0</td><td>.</td><td>.</td><td>.</td></tr><tr><th scope="row">BASELINE</th><th scope="row">0</th><th scope="row">&nbsp;</th><td>1</td><td nowrap="nowrap">-0.7744</td><td>0.4739</td><td>2.6708</td><td>0.1022</td></tr><tr><th scope="row">U_BASELINE</th><th scope="row">0</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-0.3549</td><td>0.7036</td><td>0.2544</td><td>0.6140</td></tr><tr><th scope="row">U_BASELINE</th><th scope="row">0</th><th scope="row">3</th><td>1</td><td>0.2538</td><td>0.5107</td><td>0.2471</td><td>0.6191</td></tr><tr><th scope="row">U_BASELINE</th><th scope="row">0</th><th scope="row">2</th><td>1</td><td>0.6892</td><td>0.4248</td><td>2.6313</td><td>0.1048</td></tr><tr><th scope="row">U_BASELINE</th><th scope="row">0</th><th scope="row">1</th><td>0</td><td>0</td><td>.</td><td>.</td><td>.</td></tr><tr><th scope="row">TRT</th><th scope="row">ACL</th><th scope="row">&nbsp;</th><td>1</td><td>1.4190</td><td>0.4639</td><td>9.3557</td><td>0.0022</td></tr><tr><th scope="row">TRT</th><th scope="row">TL</th><th scope="row">&nbsp;</th><td>1</td><td>1.2923</td><td>0.4723</td><td>7.4848</td><td>0.0062</td></tr><tr><th scope="row">TRT</th><th scope="row">ACH</th><th scope="row">&nbsp;</th><td>1</td><td>2.6977</td><td>0.5334</td><td>25.5815</td><td>&lt;.0001</td></tr><tr><th scope="row">TRT</th><th scope="row">TH</th><th scope="row">&nbsp;</th><td>1</td><td>2.2822</td><td>0.5102</td><td>20.0106</td><td>&lt;.0001</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACL</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-0.2071</td><td>0.9075</td><td>0.0521</td><td>0.8195</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACL</th><th scope="row">3</th><td>1</td><td>0.0644</td><td>0.5647</td><td>0.0130</td><td>0.9093</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACL</th><th scope="row">2</th><td>1</td><td>0.1693</td><td>0.4180</td><td>0.1640</td><td>0.6855</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACL</th><th scope="row">1</th><td>0</td><td>0</td><td>.</td><td>.</td><td>.</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TL</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-0.6549</td><td>1.0232</td><td>0.4097</td><td>0.5221</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TL</th><th scope="row">3</th><td>1</td><td>0.3176</td><td>0.5639</td><td>0.3171</td><td>0.5733</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TL</th><th scope="row">2</th><td>1</td><td>0.5526</td><td>0.3919</td><td>1.9879</td><td>0.1586</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TL</th><th scope="row">1</th><td>0</td><td>0</td><td>.</td><td>.</td><td>.</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACH</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-1.7339</td><td>1.0334</td><td>2.8149</td><td>0.0934</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACH</th><th scope="row">3</th><td>1</td><td nowrap="nowrap">-1.4494</td><td>0.6550</td><td>4.8959</td><td>0.0269</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACH</th><th scope="row">2</th><td>1</td><td nowrap="nowrap">-1.0150</td><td>0.5355</td><td>3.5931</td><td>0.0580</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACH</th><th scope="row">1</th><td>0</td><td>0</td><td>.</td><td>.</td><td>.</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TH</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-0.8238</td><td>1.0052</td><td>0.6717</td><td>0.4125</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TH</th><th scope="row">3</th><td>1</td><td nowrap="nowrap">-0.6984</td><td>0.6156</td><td>1.2872</td><td>0.2566</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TH</th><th scope="row">2</th><td>1</td><td>0.0129</td><td>0.4655</td><td>0.0008</td><td>0.9779</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TH</th><th scope="row">1</th><td>0</td><td>0</td><td>.</td><td>.</td><td>.</td></tr></tbody></table>

Note that you can also test for proportionality in each of the model effects and overall by omitting the EQUALSLOPES option and including appropriate TEST statements. When the UNEQUALSLOPES option appears without the EQUALSLOPES option, the parameters for each effect are the separate slopes on the logits rather than differences from the reference slope. The following four labeled TEST statements following the MODEL statement provide tests of proportionality. The first three TEST statements test for proportional odds in each of the three predictors. In the CENTER proportionality test (labeled CENTER_PO), the equality of the CENTER parameters across the four logits is tested. Similarly for the BASELINE proportionality test. For the TRT test, equality across the logits is tested simultaneously within each level of TRT. Parameter names used in the TEST statement are specified as described in "Parameter Names in the OUTEST= Data Set" in the Details section of the [LOGISTIC documentation](http://support.sas.com/kb/22930.html). The final TEST statement provides an overall test of proportional odds, similar to the test provided when the UNEQUALSLOPES option is not used. It combines the previous three tests into a single, joint test.

```
      proc logistic data=dent;
         class center baseline trt / param=ref order=data;
         model resp(descending) = center baseline trt / unequalslopes;
         CENTER_PO:test center1_4=center1_3=center1_2=center1_1;
         BASELINE_PO:test baseline0_4=baseline0_3=baseline0_2=baseline0_1;
         TRT_PO:test trtacl_4=trtacl_3=trtacl_2=trtacl_1,
                     trttl_4=trttl_3=trttl_2=trttl_1,
                     trtach_4=trtach_3=trtach_2=trtach_1,
                     trtth_4=trtth_3=trtth_2=trtth_1;
         OVERALL_PO:test center1_4=center1_3=center1_2=center1_1,
                         baseline0_4=baseline0_3=baseline0_2=baseline0_1,
                         trtacl_4=trtacl_3=trtacl_2=trtacl_1,
                         trttl_4=trttl_3=trttl_2=trttl_1,
                         trtach_4=trtach_3=trtach_2=trtach_1,
                         trtth_4=trtth_3=trtth_2=trtth_1;
         run;


```

In this parameterization of the fully nonproportional odds model, the separate slopes of each effect on each logit are given. The logit to which each parameter estimate applies is given in the RESP column. The value in the RESP column is the level after which the ordered response levels are cut to dichotomize the response. For instance, the value 4 indicates the logit comparing level 4 with levels 3, 2, and 1. The value 3 indicates the logit comparing levels 4 and 3 with levels 2 and 1, and so on.

<table bordercolor="#C1C1C1" summary="Procedure Logistic: Parameter Estimates"><colgroup><col> <col> <col> </colgroup> <colgroup> <col> <col> <col> <col> <col> </colgroup><thead><tr><th colspan="8" scope="colgroup">Analysis of Maximum Likelihood Estimates</th></tr><tr><th scope="col">Parameter</th><th scope="col">&nbsp;</th><th scope="col">RESP</th><th scope="col">DF</th><th scope="col">Estimate</th><th scope="col">Standard<br>Error</th><th scope="col">Wald<br>Chi-Square</th><th scope="col">Pr&nbsp;&gt;&nbsp;ChiSq</th></tr></thead><tbody><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-1.9143</td><td>0.7984</td><td>5.7487</td><td>0.0165</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">3</th><td>1</td><td nowrap="nowrap">-0.8706</td><td>0.5798</td><td>2.2549</td><td>0.1332</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">2</th><td>1</td><td nowrap="nowrap">-0.6624</td><td>0.5321</td><td>1.5495</td><td>0.2132</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">1</th><td>1</td><td>1.1911</td><td>0.5724</td><td>4.3307</td><td>0.0374</td></tr><tr><th scope="row">CENTER</th><th scope="row">1</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-1.4890</td><td>0.5466</td><td>7.4205</td><td>0.0064</td></tr><tr><th scope="row">CENTER</th><th scope="row">1</th><th scope="row">3</th><td>1</td><td nowrap="nowrap">-2.0858</td><td>0.3372</td><td>38.2664</td><td>&lt;.0001</td></tr><tr><th scope="row">CENTER</th><th scope="row">1</th><th scope="row">2</th><td>1</td><td nowrap="nowrap">-1.7719</td><td>0.2903</td><td>37.2503</td><td>&lt;.0001</td></tr><tr><th scope="row">CENTER</th><th scope="row">1</th><th scope="row">1</th><td>1</td><td nowrap="nowrap">-2.2391</td><td>0.3424</td><td>42.7602</td><td>&lt;.0001</td></tr><tr><th scope="row">BASELINE</th><th scope="row">0</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-1.1293</td><td>0.6061</td><td>3.4723</td><td>0.0624</td></tr><tr><th scope="row">BASELINE</th><th scope="row">0</th><th scope="row">3</th><td>1</td><td nowrap="nowrap">-0.5206</td><td>0.4211</td><td>1.5280</td><td>0.2164</td></tr><tr><th scope="row">BASELINE</th><th scope="row">0</th><th scope="row">2</th><td>1</td><td nowrap="nowrap">-0.0853</td><td>0.4104</td><td>0.0432</td><td>0.8354</td></tr><tr><th scope="row">BASELINE</th><th scope="row">0</th><th scope="row">1</th><td>1</td><td nowrap="nowrap">-0.7744</td><td>0.4739</td><td>2.6708</td><td>0.1022</td></tr><tr><th scope="row">TRT</th><th scope="row">ACL</th><th scope="row">4</th><td>1</td><td>1.2119</td><td>0.8738</td><td>1.9233</td><td>0.1655</td></tr><tr><th scope="row">TRT</th><th scope="row">ACL</th><th scope="row">3</th><td>1</td><td>1.4833</td><td>0.5592</td><td>7.0359</td><td>0.0080</td></tr><tr><th scope="row">TRT</th><th scope="row">ACL</th><th scope="row">2</th><td>1</td><td>1.5883</td><td>0.4874</td><td>10.6201</td><td>0.0011</td></tr><tr><th scope="row">TRT</th><th scope="row">ACL</th><th scope="row">1</th><td>1</td><td>1.4190</td><td>0.4639</td><td>9.3557</td><td>0.0022</td></tr><tr><th scope="row">TRT</th><th scope="row">TL</th><th scope="row">4</th><td>1</td><td>0.6374</td><td>0.9853</td><td>0.4184</td><td>0.5177</td></tr><tr><th scope="row">TRT</th><th scope="row">TL</th><th scope="row">3</th><td>1</td><td>1.6098</td><td>0.5564</td><td>8.3716</td><td>0.0038</td></tr><tr><th scope="row">TRT</th><th scope="row">TL</th><th scope="row">2</th><td>1</td><td>1.8448</td><td>0.5008</td><td>13.5678</td><td>0.0002</td></tr><tr><th scope="row">TRT</th><th scope="row">TL</th><th scope="row">1</th><td>1</td><td>1.2923</td><td>0.4723</td><td>7.4848</td><td>0.0062</td></tr><tr><th scope="row">TRT</th><th scope="row">ACH</th><th scope="row">4</th><td>1</td><td>0.9638</td><td>0.9555</td><td>1.0175</td><td>0.3131</td></tr><tr><th scope="row">TRT</th><th scope="row">ACH</th><th scope="row">3</th><td>1</td><td>1.2483</td><td>0.5610</td><td>4.9512</td><td>0.0261</td></tr><tr><th scope="row">TRT</th><th scope="row">ACH</th><th scope="row">2</th><td>1</td><td>1.6827</td><td>0.4900</td><td>11.7902</td><td>0.0006</td></tr><tr><th scope="row">TRT</th><th scope="row">ACH</th><th scope="row">1</th><td>1</td><td>2.6977</td><td>0.5334</td><td>25.5815</td><td>&lt;.0001</td></tr><tr><th scope="row">TRT</th><th scope="row">TH</th><th scope="row">4</th><td>1</td><td>1.4583</td><td>0.9401</td><td>2.4062</td><td>0.1209</td></tr><tr><th scope="row">TRT</th><th scope="row">TH</th><th scope="row">3</th><td>1</td><td>1.5837</td><td>0.5475</td><td>8.3683</td><td>0.0038</td></tr><tr><th scope="row">TRT</th><th scope="row">TH</th><th scope="row">2</th><td>1</td><td>2.2951</td><td>0.4969</td><td>21.3320</td><td>&lt;.0001</td></tr><tr><th scope="row">TRT</th><th scope="row">TH</th><th scope="row">1</th><td>1</td><td>2.2822</td><td>0.5102</td><td>20.0106</td><td>&lt;.0001</td></tr></tbody></table>

The overall test of proportional odds from the fourth TEST statement (OVERALL_PO) is a Wald test and gives results (_p_=0.0038) similar to the score test provided with the proportional odds model above. As before, only the test of the TRT effect (TRT_PO) suggests the possibility of nonproportionality.

<table bordercolor="#C1C1C1" summary="Procedure Logistic: Test Statement Results"><colgroup><col> <col> <col> <col> </colgroup><thead><tr><th colspan="4" scope="colgroup">Linear Hypotheses Testing Results</th></tr><tr><th scope="col">Label</th><th scope="col">Wald<br>Chi-Square</th><th scope="col">DF</th><th scope="col">Pr&nbsp;&gt;&nbsp;ChiSq</th></tr></thead><tbody><tr><th scope="row">CENTER_PO</th><td>4.9138</td><td>3</td><td>0.1782</td></tr><tr><th scope="row">BASELINE_PO</th><td>4.9871</td><td>3</td><td>0.1727</td></tr><tr><th scope="row">TRT_PO</th><td>19.9122</td><td>12</td><td>0.0688</td></tr><tr><th scope="row">OVERALL_PO</th><td>38.0570</td><td>18</td><td>0.0038</td></tr></tbody></table>

### Fitting a partial proportional odds model

If you are willing to assume that proportional odds holds for the BASELINE and CENTER predictors, then a partial proportional odds model can be fit which allows for nonproportionality only in the TRT predictor by specifying the UNEQUALSLOPES=TRT option. A common parameter is used across the logits for BASELINE and CENTER while separate parameters are used for the TRT levels. The following statements fit this partial proportional odds model.

Additionally, suppose you want to test whether the TRT levels differ. Normally, this can be done using the DIFF option in an LSMEANS statement. However, this statement is not available when the UNEQUALSLOPES or EQUALSLOPES option is specified. Instead, TEST statements are used. The first four labeled TEST statements test for treatment differences in each of the four logits. The final TEST statement (TRT_PO) tests for proportional odds for TRT in this simplified model.

```
      proc logistic data=dent;
         class center baseline trt / param=ref order=data;
         model resp(descending)=center baseline trt / unequalslopes=trt;
         TRT_RESP4:test trtacl_4,trttl_4,trtach_4,trtth_4;
         TRT_RESP3:test trtacl_3,trttl_3,trtach_3,trtth_3;
         TRT_RESP2:test trtacl_2,trttl_2,trtach_2,trtth_2;
         TRT_RESP1:test trtacl_1,trttl_1,trtach_1,trtth_1;
         TRT_PO:test trtacl_4=trtacl_3=trtacl_2=trtacl_1,
                     trttl_4=trttl_3=trttl_2=trttl_1,
                     trtach_4=trtach_3=trtach_2=trtach_1,
                     trtth_4=trtth_3=trtth_2=trtth_1;
         run;


```

The table of parameter estimates shows the separate intercepts and separate TRT parameters for each logit, and the single parameter for each of BASELINE and CENTER in this partial proportional odds model.

<table bordercolor="#C1C1C1" summary="Procedure Logistic: Parameter Estimates"><colgroup><col> <col> <col> </colgroup> <colgroup> <col> <col> <col> <col> <col> </colgroup><thead><tr><th colspan="8" scope="colgroup">Analysis of Maximum Likelihood Estimates</th></tr><tr><th scope="col">Parameter</th><th scope="col">&nbsp;</th><th scope="col">RESP</th><th scope="col">DF</th><th scope="col">Estimate</th><th scope="col">Standard<br>Error</th><th scope="col">Wald<br>Chi-Square</th><th scope="col">Pr&nbsp;&gt;&nbsp;ChiSq</th></tr></thead><tbody><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-2.1728</td><td>0.7859</td><td>7.6441</td><td>0.0057</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">3</th><td>1</td><td nowrap="nowrap">-0.8979</td><td>0.5469</td><td>2.6959</td><td>0.1006</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">2</th><td>1</td><td nowrap="nowrap">-0.2045</td><td>0.4968</td><td>0.1694</td><td>0.6807</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">1</th><td>1</td><td>0.8796</td><td>0.4723</td><td>3.4687</td><td>0.0625</td></tr><tr><th scope="row">CENTER</th><th scope="row">1</th><th scope="row">&nbsp;</th><td>1</td><td nowrap="nowrap">-1.9788</td><td>0.2595</td><td>58.1542</td><td>&lt;.0001</td></tr><tr><th scope="row">BASELINE</th><th scope="row">0</th><th scope="row">&nbsp;</th><td>1</td><td nowrap="nowrap">-0.5606</td><td>0.3537</td><td>2.5120</td><td>0.1130</td></tr><tr><th scope="row">TRT</th><th scope="row">ACL</th><th scope="row">4</th><td>1</td><td>1.2763</td><td>0.8569</td><td>2.2185</td><td>0.1364</td></tr><tr><th scope="row">TRT</th><th scope="row">ACL</th><th scope="row">3</th><td>1</td><td>1.4614</td><td>0.5565</td><td>6.8963</td><td>0.0086</td></tr><tr><th scope="row">TRT</th><th scope="row">ACL</th><th scope="row">2</th><td>1</td><td>1.6651</td><td>0.4839</td><td>11.8382</td><td>0.0006</td></tr><tr><th scope="row">TRT</th><th scope="row">ACL</th><th scope="row">1</th><td>1</td><td>1.3353</td><td>0.4501</td><td>8.8001</td><td>0.0030</td></tr><tr><th scope="row">TRT</th><th scope="row">TL</th><th scope="row">4</th><td>1</td><td>0.4960</td><td>0.9463</td><td>0.2747</td><td>0.6002</td></tr><tr><th scope="row">TRT</th><th scope="row">TL</th><th scope="row">3</th><td>1</td><td>1.6643</td><td>0.5524</td><td>9.0763</td><td>0.0026</td></tr><tr><th scope="row">TRT</th><th scope="row">TL</th><th scope="row">2</th><td>1</td><td>1.8728</td><td>0.4887</td><td>14.6887</td><td>0.0001</td></tr><tr><th scope="row">TRT</th><th scope="row">TL</th><th scope="row">1</th><td>1</td><td>1.1711</td><td>0.4519</td><td>6.7144</td><td>0.0096</td></tr><tr><th scope="row">TRT</th><th scope="row">ACH</th><th scope="row">4</th><td>1</td><td>0.8320</td><td>0.9026</td><td>0.8497</td><td>0.3566</td></tr><tr><th scope="row">TRT</th><th scope="row">ACH</th><th scope="row">3</th><td>1</td><td>1.3112</td><td>0.5594</td><td>5.4943</td><td>0.0191</td></tr><tr><th scope="row">TRT</th><th scope="row">ACH</th><th scope="row">2</th><td>1</td><td>1.7105</td><td>0.4868</td><td>12.3490</td><td>0.0004</td></tr><tr><th scope="row">TRT</th><th scope="row">ACH</th><th scope="row">1</th><td>1</td><td>2.5727</td><td>0.5195</td><td>24.5251</td><td>&lt;.0001</td></tr><tr><th scope="row">TRT</th><th scope="row">TH</th><th scope="row">4</th><td>1</td><td>1.2844</td><td>0.8549</td><td>2.2571</td><td>0.1330</td></tr><tr><th scope="row">TRT</th><th scope="row">TH</th><th scope="row">3</th><td>1</td><td>1.6081</td><td>0.5453</td><td>8.6972</td><td>0.0032</td></tr><tr><th scope="row">TRT</th><th scope="row">TH</th><th scope="row">2</th><td>1</td><td>2.3383</td><td>0.4918</td><td>22.6063</td><td>&lt;.0001</td></tr><tr><th scope="row">TRT</th><th scope="row">TH</th><th scope="row">1</th><td>1</td><td>2.2175</td><td>0.4942</td><td>20.1352</td><td>&lt;.0001</td></tr></tbody></table>

The tests for treatment differences suggest that the treatments differ on logits 1, 2, and 3, but not on logit 4 (_p_=0.4925). The test for proportional odds in the treatment effect (TEST_PO) continues to indicate possible lack of proportionality (_p_=0.0729).

<table bordercolor="#C1C1C1" summary="Procedure Logistic: Test Statement Results"><colgroup><col> <col> <col> <col> </colgroup><thead><tr><th colspan="4" scope="colgroup">Linear Hypotheses Testing Results</th></tr><tr><th scope="col">Label</th><th scope="col">Wald<br>Chi-Square</th><th scope="col">DF</th><th scope="col">Pr&nbsp;&gt;&nbsp;ChiSq</th></tr></thead><tbody><tr><th scope="row">TRT_RESP4</th><td>3.4046</td><td>4</td><td>0.4925</td></tr><tr><th scope="row">TRT_RESP3</th><td>10.7834</td><td>4</td><td>0.0291</td></tr><tr><th scope="row">TRT_RESP2</th><td>24.3858</td><td>4</td><td>&lt;.0001</td></tr><tr><th scope="row">TRT_RESP1</th><td>31.9492</td><td>4</td><td>&lt;.0001</td></tr><tr><th scope="row">TRT_PO</th><td>19.7037</td><td>12</td><td>0.0729</td></tr></tbody></table>

### Using SELECTION= to choose a partial proportional odds model

You can use the SELECTION= option to have PROC LOGISTIC determine which effects exhibit nonproportional odds and choose a final model. The following statements use stepwise effect selection to select a final model from a set of candidate effects that includes all equal and unequal slope parameters. Beginning in SAS 9.4 TS1M2, the EQUALSLOPES option makes the equal slope parameters available. Used with the UNEQUALSLOPES option, all equal and unequal slope parameters are available for effect selection. The INCLUDE=EQUALSLOPES option restricts the selection by requiring every model in the selection process to include the equal slope parameters. The selection process tests the unequal slope parameters for an effect and includes and retains them if significant at the 0.1 level. The DETAILS option shows the tests of the candidate effects at each step.

```
      proc logistic data=dent;
         class center baseline trt / param=ref order=data;
         model resp(descending)=center baseline trt / selection=stepwise slentry=0.1 slstay=0.1
            equalslopes unequalslopes include=equalslopes details;
         run;


```

The model in the first step includes the intercepts and equal slope parameters. This is the same proportional odds model as shown above. The analysis at this step includes tests of the remaining candidate effects, which are the unequal slope parameters for each of the three predictors. The U_ prefix indicates that these are the unequal slope parameters for each predictor. The score tests give similar results to the Wald tests for proportional odds shown above.

<table bordercolor="#C1C1C1" summary="Procedure Logistic: Score Tests of Effects Not in the Model"><colgroup><col> </colgroup> <colgroup> <col> <col> <col> </colgroup><thead><tr><th colspan="4" scope="colgroup">Analysis of Effects Eligible for Entry</th></tr><tr><th scope="col">Effect</th><th scope="col">DF</th><th scope="col">Score<br>Chi-Square</th><th scope="col">Pr&nbsp;&gt;&nbsp;ChiSq</th></tr></thead><tbody><tr><th scope="row">U_CENTER</th><td>3</td><td>6.1038</td><td>0.1067</td></tr><tr><th scope="row">U_BASELINE</th><td>3</td><td>5.6195</td><td>0.1317</td></tr><tr><th scope="row">U_TRT</th><td>12</td><td>21.8632</td><td>0.0391</td></tr></tbody></table>

Since the unequal slopes effect for TRT is significant at the 0.1 level, it is included in the next step of the model selection process. This results in the same partial proportional odds model shown above but is parameterized slightly differently with a set of equal slope parameters followed by sets of unequal slope parameters. For each TRT level, the equal slope parameter is used as the slope for the last logit (RESP=1), and the unequal slope parameters (U_TRT) are deviations from the equal slope parameter.

<table bordercolor="#C1C1C1" summary="Procedure Logistic: Parameter Estimates"><colgroup><col> <col> <col> </colgroup> <colgroup> <col> <col> <col> <col> <col> </colgroup><thead><tr><th colspan="8" scope="colgroup">Analysis of Maximum Likelihood Estimates</th></tr><tr><th scope="col">Parameter</th><th scope="col">&nbsp;</th><th scope="col">RESP</th><th scope="col">DF</th><th scope="col">Estimate</th><th scope="col">Standard<br>Error</th><th scope="col">Wald<br>Chi-Square</th><th scope="col">Pr&nbsp;&gt;&nbsp;ChiSq</th></tr></thead><tbody><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-2.1728</td><td>0.7859</td><td>7.6441</td><td>0.0057</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">3</th><td>1</td><td nowrap="nowrap">-0.8979</td><td>0.5469</td><td>2.6959</td><td>0.1006</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">2</th><td>1</td><td nowrap="nowrap">-0.2045</td><td>0.4968</td><td>0.1694</td><td>0.6807</td></tr><tr><th scope="row">Intercept</th><th scope="row">&nbsp;</th><th scope="row">1</th><td>1</td><td>0.8796</td><td>0.4723</td><td>3.4687</td><td>0.0625</td></tr><tr><th scope="row">CENTER</th><th scope="row">1</th><th scope="row">&nbsp;</th><td>1</td><td nowrap="nowrap">-1.9788</td><td>0.2595</td><td>58.1542</td><td>&lt;.0001</td></tr><tr><th scope="row">BASELINE</th><th scope="row">0</th><th scope="row">&nbsp;</th><td>1</td><td nowrap="nowrap">-0.5606</td><td>0.3537</td><td>2.5120</td><td>0.1130</td></tr><tr><th scope="row">TRT</th><th scope="row">ACL</th><th scope="row">&nbsp;</th><td>1</td><td>1.3353</td><td>0.4501</td><td>8.8001</td><td>0.0030</td></tr><tr><th scope="row">TRT</th><th scope="row">TL</th><th scope="row">&nbsp;</th><td>1</td><td>1.1711</td><td>0.4519</td><td>6.7144</td><td>0.0096</td></tr><tr><th scope="row">TRT</th><th scope="row">ACH</th><th scope="row">&nbsp;</th><td>1</td><td>2.5727</td><td>0.5195</td><td>24.5251</td><td>&lt;.0001</td></tr><tr><th scope="row">TRT</th><th scope="row">TH</th><th scope="row">&nbsp;</th><td>1</td><td>2.2175</td><td>0.4942</td><td>20.1352</td><td>&lt;.0001</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACL</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-0.0590</td><td>0.8864</td><td>0.0044</td><td>0.9469</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACL</th><th scope="row">3</th><td>1</td><td>0.1261</td><td>0.5553</td><td>0.0516</td><td>0.8204</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACL</th><th scope="row">2</th><td>1</td><td>0.3298</td><td>0.4085</td><td>0.6519</td><td>0.4194</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACL</th><th scope="row">1</th><td>0</td><td>0</td><td>.</td><td>.</td><td>.</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TL</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-0.6751</td><td>0.9757</td><td>0.4787</td><td>0.4890</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TL</th><th scope="row">3</th><td>1</td><td>0.4932</td><td>0.5380</td><td>0.8403</td><td>0.3593</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TL</th><th scope="row">2</th><td>1</td><td>0.7018</td><td>0.3744</td><td>3.5136</td><td>0.0609</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TL</th><th scope="row">1</th><td>0</td><td>0</td><td>.</td><td>.</td><td>.</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACH</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-1.7407</td><td>0.9761</td><td>3.1801</td><td>0.0745</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACH</th><th scope="row">3</th><td>1</td><td nowrap="nowrap">-1.2615</td><td>0.6411</td><td>3.8725</td><td>0.0491</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACH</th><th scope="row">2</th><td>1</td><td nowrap="nowrap">-0.8622</td><td>0.5248</td><td>2.6986</td><td>0.1004</td></tr><tr><th scope="row">U_TRT</th><th scope="row">ACH</th><th scope="row">1</th><td>0</td><td>0</td><td>.</td><td>.</td><td>.</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TH</th><th scope="row">4</th><td>1</td><td nowrap="nowrap">-0.9331</td><td>0.9171</td><td>1.0352</td><td>0.3089</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TH</th><th scope="row">3</th><td>1</td><td nowrap="nowrap">-0.6094</td><td>0.6031</td><td>1.0210</td><td>0.3123</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TH</th><th scope="row">2</th><td>1</td><td>0.1208</td><td>0.4509</td><td>0.0717</td><td>0.7888</td></tr><tr><th scope="row">U_TRT</th><th scope="row">TH</th><th scope="row">1</th><td>0</td><td>0</td><td>.</td><td>.</td><td>.</td></tr></tbody></table>

Since tests of the remaining nonproportional odds effects are not significant, the selection process ends.

<table bordercolor="#C1C1C1" summary="Procedure Logistic: Score Tests of Effects Not in the Model"><colgroup><col> </colgroup> <colgroup> <col> <col> <col> </colgroup><thead><tr><th colspan="4" scope="colgroup">Analysis of Effects Eligible for Entry</th></tr><tr><th scope="col">Effect</th><th scope="col">DF</th><th scope="col">Score<br>Chi-Square</th><th scope="col">Pr&nbsp;&gt;&nbsp;ChiSq</th></tr></thead><tbody><tr><th scope="row">U_CENTER</th><td>3</td><td>5.6487</td><td>0.1300</td></tr><tr><th scope="row">U_BASELINE</th><td>3</td><td>5.9237</td><td>0.1154</td></tr></tbody></table>

An additional example of fitting nonproportional odds models and using model selection can be found in the example titled "Partial Proportional Odds Model" in the [LOGISTIC documentation](http://support.sas.com/kb/22930.html).

**References**

Peterson, B. and F. Harrell (1990), "Partial Proportional Odds Models for Ordinal Response Variables," _Applied Statistics_ , 39:205-217.

[Stokes, M.E., Davis, C.S., and Koch, G.G.](http://support.sas.com/kb/22572.html)

**Addendum: Using NLMIXED to fit ordinal logistic models**

The following section fits the same models as above using PROC NLMIXED.

#### Proportional odds model

In PROC NLMIXED, reference-coded dummies (T1-T4, B, and C) are created ![](https://support.sas.com/kb/22/addl/fusion_22954_1_circle1.jpg) in the same way as done by the CLASS statement in PROC LOGISTIC. Four cumulative probabilities (CP1-CP4) are computed on the five levels of the response (RESP=0, 1, 2, 3, 4) ![](https://support.sas.com/kb/22/addl/fusion_22954_2_circle2.jpg). The model is contained in these statements. INT1-INT4 are the four intercepts of the proportional odds model. Note that the same name is used across the four cumulative probabilities for each of the other model parameters (BC1, BB0, BACL, BTL, BACH, and BTH). Initial values for the intercepts are provided in the previous PARMS statement. The increasing initial values help ensure properly increasing cumulative probabilities and avoid estimation problems. All other parameters are started at the default value of one. The individual probabilities ![](https://support.sas.com/kb/22/addl/fusion_22954_3_circle3.jpg) are computed from the cumulative probabilities by taking differences. For instance, the probability of response 3 is obtained by subtracting the probability of response 4 from the probability of response 3 or 4. These statements result in modeling the probability of higher response levels as in the LOGISTIC model[NOTE](#note). The next three statements ![](https://support.sas.com/kb/22/addl/fusion_22954_4_circle4.jpg) ensure that the predicted probability values are valid and define the log likelihood to be maximized by the procedure. The ID and PREDICT statements ![](https://support.sas.com/kb/22/addl/fusion_22954_5_circle5.jpg) save the cumulative probabilities and the predicted probability of the observed response to data set NLM.

```
      proc nlmixed data=dent;
         parms Int4 = -1, Int3 = 0, Int2 = 1, Int1 = 2;

      t1=(trt='ACL'); t2=(trt='TL'); t3=(trt='ACH'); t4=(trt='TH');
         b=(baseline=0); c=(center=1);
            
      cp4= logistic(Int4 + bc1*c + bb0*b + bACL*t1 + bTL*t2 + bACH*t3 + bTH*t4);
         cp3= logistic(Int3 + bc1*c + bb0*b + bACL*t1 + bTL*t2 + bACH*t3 + bTH*t4);
         cp2= logistic(Int2 + bc1*c + bb0*b + bACL*t1 + bTL*t2 + bACH*t3 + bTH*t4);
         cp1= logistic(Int1 + bc1*c + bb0*b + bACL*t1 + bTL*t2 + bACH*t3 + bTH*t4);
      
      if      resp=4 then ip = cp4;         /* CP4 is Pr(resp=4) */
         else if resp=3 then ip = cp3-cp4;     /* CP3 is Pr(resp=4 or 3) */
         else if resp=2 then ip = cp2-cp3;     /* CP2 is Pr(resp=4 or 3 or 2) */
         else if resp=1 then ip = cp1-cp2;     /* CP1 is Pr(resp=4 or 3 or 2 or 1) */
         else                ip = 1-cp1;       /* IP  is Pr(resp=observed level) */
         
      p = (ip>0 and ip<=1)*ip + (ip<=0)*1e-8 + (ip>1);
         loglik = log(p);
         model resp ~ general(loglik);
         
      id cp1-cp4;
         predict ip out=nlm;
         run;


```

The parameter estimates from PROC NLMIXED agree closely with those from PROC LOGISTIC. The standard errors differ slightly since LOGISTIC constructs Wald tests while NLMIXED uses t-tests based on the available degrees of freedom. The predicted probabilities produced by the two procedures (in data sets LOG and NLM) are also very similar.

#### Fully nonproportional odds model

Note that unique names are used across the cumulative probabilities ![](https://support.sas.com/kb/22/addl/fusion_22954_1_circle1.jpg) for each model effect. For instance, instead of the common parameter BC1 for the CENTER effect in the proportional odds model above, there are now four parameters, BC11, BC12, BC13, and BC14. Similarly for the BASELINE and TRT effects. The four CONTRAST statements ![](https://support.sas.com/kb/22/addl/fusion_22954_2_circle2.jpg) with "PO" in their labels provide proportional odds tests for each of the predictors as well as an overall test comparable to the test provided by PROC LOGISTIC. Preceding these, additional contrasts are done to test the effect of each predictor on logit 1 which contrasts response level 0 (no relief) with the higher response levels representing varying degrees of relief.

The parameter estimates of the fully nonproportional odds model has four complete sets of parameter estimates compared to the single set in the proportional odds model. The logit to which the parameter estimate applies is given in the last character of its name. For instance, the estimates Int4, bc14, bb04, bACL4, bTL4, bACH4, and bTH4 are the parameter estimates associated with the fourth logit which contrasts the highest level of relief against all other levels.

```
      proc nlmixed data=dent;
         parms Int4 = -1, Int3 = 0, Int2 = 1, Int1 = 2;
      
         t1=(trt='ACL'); t2=(trt='TL'); t3=(trt='ACH'); t4=(trt='TH');
         b=(baseline=0); c=(center=1);
      
      cp4= logistic(Int4 + bc14*c + bb04*b + bACL4*t1 + bTL4*t2 + bACH4*t3 + bTH4*t4);
         cp3= logistic(Int3 + bc13*c + bb03*b + bACL3*t1 + bTL3*t2 + bACH3*t3 + bTH3*t4);
         cp2= logistic(Int2 + bc12*c + bb02*b + bACL2*t1 + bTL2*t2 + bACH2*t3 + bTH2*t4);
         cp1= logistic(Int1 + bc11*c + bb01*b + bACL1*t1 + bTL1*t2 + bACH1*t3 + bTH1*t4);
      
         if      resp=4 then ip = cp4;
         else if resp=3 then ip = cp3-cp4;
         else if resp=2 then ip = cp2-cp3;
         else if resp=1 then ip = cp1-cp2;
         else                ip = 1-cp1;
         
         p = (ip>0 and ip<=1)*ip + (ip<=0)*1e-8 + (ip>1);
         loglik = log(p);
         model resp ~ general(loglik);
         
         id cp1-cp4;
         predict ip out=nlm;
         
         contrast 'center on logit1 (4321 vs 0)' bc11;
         contrast 'baseline on logit1 (4321 vs 0)' bb01;
         contrast 'trt on logit1 (4321 vs 0)' 
                       bACL1, bTL1, bACH1, bTH1;
      contrast 'center PO' 
                       bc11-bc14, bc12-bc14, bc13-bc14;
         contrast 'baseline PO' 
                       bb01-bb04, bb02-bb04, bb03-bb04;
         contrast 'trt PO' 
                       bACL1-bACL4, bACL2-bACL4, bACL3-bACL4,
                       bTL1-bTL4, bTL2-bTL4, bTL3-bTL4,
                       bACH1-bACH4, bACH2-bACH4, bACH3-bACH4,
                       bTH1-bTH4, bTH2-bTH4, bTH3-bTH4;
         contrast 'overall PO' 
                       bc11-bc14, bc12-bc14, bc13-bc14,
                       bb01-bb04, bb02-bb04, bb03-bb04,
                       bACL1-bACL4, bACL2-bACL4, bACL3-bACL4,
                       bTL1-bTL4, bTL2-bTL4, bTL3-bTL4,
                       bACH1-bACH4, bACH2-bACH4, bACH3-bACH4,
                       bTH1-bTH4, bTH2-bTH4, bTH3-bTH4;
         run;


```

#### Partial proportional odds model

A partial proportional odds model is fit with a common parameter across the logits for BASELINE (BB0) and CENTER (BC1) and separate parameters for the TRT levels. The following statements fit this partial proportional odds model in PROC NLMIXED.

```
      proc nlmixed data=dent;
         parms Int4 = -1, Int3 = 0, Int2 = 1, Int1 = 2;
      
         t1=(trt='ACL'); t2=(trt='TL'); t3=(trt='ACH'); t4=(trt='TH');
         b=(baseline=0); c=(center=1);
      
         cp4= logistic(Int4 + bc1*c + bb0*b + bACL4*t1 + bTL4*t2 + bACH4*t3 + bTH4*t4);
         cp3= logistic(Int3 + bc1*c + bb0*b + bACL3*t1 + bTL3*t2 + bACH3*t3 + bTH3*t4);
         cp2= logistic(Int2 + bc1*c + bb0*b + bACL2*t1 + bTL2*t2 + bACH2*t3 + bTH2*t4);
         cp1= logistic(Int1 + bc1*c + bb0*b + bACL1*t1 + bTL1*t2 + bACH1*t3 + bTH1*t4);
      
         if      resp=4 then ip = cp4;
         else if resp=3 then ip = cp3-cp4;
         else if resp=2 then ip = cp2-cp3;
         else if resp=1 then ip = cp1-cp2;
         else                ip = 1-cp1;
         
         p = (ip>0 and ip<=1)*ip + (ip<=0)*1e-8 + (ip>1);
         loglik = log(p);
         model resp ~ general(loglik);
         
         id cp1-cp4;
         predict ip out=nlm;
         run;


```

__________

NOTE: If you want to model the probability of lower, rather than higher, response levels omit the DESCENDING response variable option in the MODEL statement of PROC LOGISTIC. In PROC NLMIXED, you could simply use increasing values of RESP in the statements defining the individual probability. For instance:

```
         if      resp=0 then ip = cp4;
         else if resp=1 then ip = cp3-cp4;
         else if resp=2 then ip = cp2-cp3;
         else if resp=3 then ip = cp1-cp2;
         else                ip = 1-cp1;


```

But the results will be more meaningfully labeled if you also change the names of the parameters and cumulative probabilities as below for the proportional odds model:

```
     proc nlmixed data=dent;
         parms Int0 = -1, Int1 = 0, Int2 = 1, Int3 = 2;

         t1=(trt='ACL'); t2=(trt='TL'); t3=(trt='ACH'); t4=(trt='TH');
         b=(baseline=0); c=(center=1);

         cp0= logistic(Int0 + bc1*c + bb0*b + bACL*t1 + bTL*t2 + bACH*t3 + bTH*t4);
         cp1= logistic(Int1 + bc1*c + bb0*b + bACL*t1 + bTL*t2 + bACH*t3 + bTH*t4);
         cp2= logistic(Int2 + bc1*c + bb0*b + bACL*t1 + bTL*t2 + bACH*t3 + bTH*t4);
         cp3= logistic(Int3 + bc1*c + bb0*b + bACL*t1 + bTL*t2 + bACH*t3 + bTH*t4);

         if      resp=0 then ip = cp0;         /* CP0 is Pr(resp=0) */
         else if resp=1 then ip = cp1-cp0;     /* CP1 is Pr(resp=0 or 1) */
         else if resp=2 then ip = cp2-cp1;     /* CP2 is Pr(resp=0 or 1 or 2) */
         else if resp=3 then ip = cp3-cp2;     /* CP3 is Pr(resp=0 or 1 or 2 or 3) */
         else                ip = 1-cp3;       /* IP  is Pr(resp=observed level) */

         p = (ip>0 and ip<=1)*ip + (ip<=0)*1e-8 + (ip>1);
         loglik = log(p);
         model resp ~ general(loglik);

         id cp1-cp4;
         predict ip out=nlm;
         run;


```

data dent; input patient center trt $ baseline ldose resp @@; datalines; 2 1 ACL 0 5.29832 0 131 1 TL 0 3.91202 2 1 1 ACH 1 5.99146 1 3 1 TH 0 4.60517 1 130 1 P 0 0.00000 0 132 1 P 0 0.00000 0 4 1 P 0 0.00000 0 133 1 P 0 0.00000 0 5 1 P 0 0.00000 0 134 2 ACH 0 5.99146 4 6 1 TL 1 3.91202 2 135 2 ACL 0 5.29832 4 7 1 ACH 0 5.99146 1 136 2 TH 0 4.60517 3 8 1 ACL 0 5.29832 0 137 2 ACL 0 5.29832 4 9 1 TL 1 3.91202 0 138 2 TL 0 3.91202 3 10 1 TL 1 3.91202 4 139 2 P 0 0.00000 4 11 1 ACL 0 5.29832 2 140 2 TL 0 3.91202 3 12 1 ACH 0 5.99146 0 141 2 TL 0 3.91202 3 13 1 P 0 0.00000 0 142 2 ACL 1 5.29832 3 14 1 TL 0 3.91202 0 143 2 ACH 0 5.99146 1 15 1 P 0 0.00000 0 144 2 ACH 0 5.99146 3 16 1 TH 1 4.60517 4 145 2 P 0 0.00000 1 17 1 TH 0 4.60517 2 146 2 P 0 0.00000 0 18 1 ACH 0 5.99146 1 147 2 ACH 0 5.99146 4 19 1 ACL 0 5.29832 0 148 2 TL 0 3.91202 2 20 1 TH 0 4.60517 3 149 2 TH 0 4.60517 3 21 1 P 1 0.00000 1 150 2 P 0 0.00000 0 22 1 TH 1 4.60517 0 151 2 TH 0 4.60517 2 23 1 TL 0 3.91202 2 152 2 ACL 1 5.29832 3 24 1 ACL 1 5.29832 0 153 2 TH 0 4.60517 2 25 1 P 0 0.00000 0 154 2 ACH 0 5.99146 3 26 1 ACH 0 5.99146 0 155 2 ACL 0 5.29832 1 27 1 ACL 0 5.29832 0 156 2 ACL 0 5.29832 0 28 1 P 0 0.00000 0 157 2 ACL 0 5.29832 3 29 1 ACH 0 5.99146 2 158 2 TH 0 4.60517 3 30 1 TL 0 3.91202 0 159 2 ACL 0 5.29832 1 31 1 P 0 0.00000 0 160 2 TL 0 3.91202 3 32 1 ACH 0 5.99146 1 161 2 P 0 0.00000 2 33 1 TL 0 3.91202 0 162 2 TH 0 4.60517 3 34 1 TH 1 4.60517 4 163 2 TH 0 4.60517 4 35 1 TL 0 3.91202 2 164 2 ACH 0 5.99146 3 36 1 ACH 0 5.99146 0 165 2 TH 0 4.60517 2 37 1 ACL 1 5.29832 1 166 2 P 0 0.00000 3 38 1 ACL 0 5.29832 3 167 2 ACH 0 5.99146 1 39 1 TH 0 4.60517 2 168 2 P 0 0.00000 2 40 1 TH 0 4.60517 0 169 2 TL 1 3.91202 2 41 1 ACL 0 5.29832 2 170 2 P 0 0.00000 0 42 1 TL 0 3.91202 3 171 2 TL 0 3.91202 0 43 1 ACL 0 5.29832 2 172 2 TL 0 3.91202 3 44 1 ACL 0 5.29832 0 173 2 ACH 1 5.99146 2 45 1 TH 0 4.60517 2 174 2 ACL 0 5.29832 3 46 1 ACH 0 5.99146 0 175 2 P 0 0.00000 4 47 1 P 0 0.00000 0 176 2 TL 1 3.91202 0 48 1 ACL 0 5.29832 0 177 2 ACH 0 5.99146 1 49 1 TL 0 3.91202 0 178 2 ACH 1 5.99146 2 50 1 TL 0 3.91202 2 179 2 ACL 0 5.29832 2 51 1 TL 0 3.91202 0 180 2 ACL 0 5.29832 2 52 1 ACH 0 5.99146 4 181 2 TH 0 4.60517 2 53 1 TH 0 4.60517 4 182 2 TL 0 3.91202 3 54 1 TH 0 4.60517 0 183 2 TH 0 4.60517 3 55 1 P 0 0.00000 0 184 2 ACH 0 5.99146 1 56 1 ACH 0 5.99146 3 185 2 P 0 0.00000 1 57 1 ACH 0 5.99146 2 186 2 ACL 0 5.29832 1 58 1 P 0 0.00000 0 187 2 TH 0 4.60517 2 59 1 TH 0 4.60517 0 188 2 ACH 1 5.99146 3 60 1 P 0 0.00000 0 189 2 TH 0 4.60517 2 61 1 TL 0 3.91202 1 190 2 TL 0 3.91202 3 62 1 P 0 0.00000 0 191 2 P 0 0.00000 1 63 1 TH 1 4.60517 1 192 2 TL 0 3.91202 3 64 1 TL 0 3.91202 0 193 2 P 0 0.00000 0 65 1 ACH 0 5.99146 2 194 2 TH 0 4.60517 2 66 1 ACL 0 5.29832 2 195 2 ACH 0 5.99146 4 67 1 P 0 0.00000 2 196 2 ACH 0 5.99146 2 68 1 TH 0 4.60517 1 197 2 ACL 0 5.29832 3 69 1 ACH 0 5.99146 0 198 2 P 0 0.00000 0 70 1 P 0 0.00000 0 199 2 P 0 0.00000 3 71 1 TL 0 3.91202 0 200 2 ACL 0 5.29832 0 72 1 ACH 0 5.99146 2 201 2 ACL 1 5.29832 4 73 1 P 0 0.00000 0 202 2 TH 0 4.60517 3 74 1 TL 0 3.91202 2 203 2 P 0 0.00000 1 75 1 TH 0 4.60517 2 204 2 TH 0 4.60517 1 76 1 ACL 1 5.29832 0 205 2 TH 0 4.60517 3 77 1 TH 1 4.60517 0 206 2 TL 0 3.91202 3 78 1 ACL 0 5.29832 0 207 2 TL 0 3.91202 3 79 1 ACL 1 5.29832 3 208 2 TL 0 3.91202 3 80 1 ACH 0 5.99146 2 209 2 ACL 0 5.29832 2 81 1 ACL 0 5.29832 0 210 2 ACH 0 5.99146 3 82 1 P 0 0.00000 0 211 2 TL 1 3.91202 1 83 1 TH 0 4.60517 0 212 2 ACH 0 5.99146 3 84 1 ACH 0 5.99146 1 213 2 P 0 0.00000 2 85 1 TL 0 3.91202 0 214 2 P 0 0.00000 0 86 1 TH 0 4.60517 3 215 2 TL 0 3.91202 0 87 1 ACH 0 5.99146 0 216 2 TH 0 4.60517 4 88 1 P 0 0.00000 0 217 2 ACH 0 5.99146 2 89 1 ACH 0 5.99146 1 218 2 P 0 0.00000 0 90 1 TL 0 3.91202 0 219 2 TH 0 4.60517 2 91 1 ACL 0 5.29832 1 220 2 TL 0 3.91202 1 92 1 TH 0 4.60517 0 221 2 ACH 0 5.99146 2 93 1 ACL 0 5.29832 1 222 2 TL 0 3.91202 4 94 1 TL 1 3.91202 1 223 2 TH 0 4.60517 2 95 1 TL 1 3.91202 3 224 2 TH 1 4.60517 1 96 1 P 0 0.00000 0 225 2 ACH 0 5.99146 1 97 1 TH 0 4.60517 0 226 2 ACL 0 5.29832 4 98 1 ACL 0 5.29832 0 227 2 P 1 0.00000 3 99 1 P 1 0.00000 0 228 2 ACL 0 5.29832 2 100 1 ACH 0 5.99146 2 229 2 TL 0 3.91202 0 101 1 TH 0 4.60517 0 230 2 ACL 0 5.29832 1 102 1 TL 0 3.91202 0 231 2 ACH 0 5.99146 3 103 1 ACL 0 5.29832 1 232 2 ACL 0 5.29832 3 104 1 TL 0 3.91202 0 233 2 P 0 0.00000 1 105 1 P 0 0.00000 1 234 2 ACL 0 5.29832 4 106 1 ACL 0 5.29832 0 235 2 ACH 0 5.99146 1 107 1 TH 1 4.60517 2 236 2 TH 0 4.60517 1 108 1 P 0 0.00000 0 237 2 ACL 0 5.29832 0 109 1 ACH 0 5.99146 1 238 2 ACL 1 5.29832 4 110 1 TH 1 4.60517 1 239 2 ACL 0 5.29832 3 111 1 TL 0 3.91202 0 240 2 P 0 0.00000 0 112 1 ACH 0 5.99146 0 241 2 P 1 0.00000 3 113 1 TL 0 3.91202 0 242 2 TL 0 3.91202 2 114 1 ACH 0 5.99146 1 243 2 P 0 0.00000 0 115 1 P 0 0.00000 0 244 2 TH 0 4.60517 3 116 1 ACL 0 5.29832 0 245 2 TL 1 3.91202 4 117 1 P 0 0.00000 0 246 2 ACH 1 5.99146 1 118 1 ACH 0 5.99146 3 247 2 P 0 0.00000 1 119 1 TH 0 4.60517 3 248 2 TH 0 4.60517 4 120 1 ACL 0 5.29832 2 249 2 TL 0 3.91202 0 121 1 TH 0 4.60517 2 250 2 TL 0 3.91202 3 122 1 TH 0 4.60517 1 251 2 ACH 0 5.99146 3 123 1 TL 0 3.91202 0 252 2 TH 0 4.60517 3 124 1 ACH 0 5.99146 0 253 2 ACH 0 5.99146 1 125 1 ACL 0 5.29832 0 254 2 TH 0 4.60517 3 126 1 TH 1 4.60517 0 255 2 ACL 0 5.29832 0 127 1 ACL 0 5.29832 0 256 2 TL 0 3.91202 3 128 1 ACH 0 5.99146 1 257 2 P 0 0.00000 1 129 1 ACL 0 5.29832 3 258 2 ACH 0 5.99146 3 ;

#### Operating System and Release Information

<table><tbody><tr><td rowspan="2">Product Family</td><td rowspan="2">Product</td><td rowspan="2">System</td><td colspan="2">SAS Release</td></tr><tr><td>Reported</td><td>Fixed*</td></tr><tr><td rowspan="1">SAS System</td><td rowspan="1">SAS/STAT</td><td>All</td><td>n/a</td><td></td></tr></tbody></table>

***** For software releases that are not yet generally available, the Fixed Release is the software release in which the problem is planned to be fixed.