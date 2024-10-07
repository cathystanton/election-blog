---
title: Week 5 Forecast
author: Catherine Stanton
date: '2024-10-04'
slug: week-5-forecast
categories: []
tags: []
---

<h1>Week 5: October 7, 2024</h1>  
This blog is an ongoing project for Professor Ryan Enos' Election Analytics Course at Harvard College (GOV 1347, Fall 2024). It will be updated weekly with posts analyzing how different features impact the likelihood of Kamala Harris (D) or Donald Trump (R) winning the 2024 U.S. Presidential Election or winning specific states in the election. The blog will culminate in a final predictive model for the outcome of the general election.

<h2>Context & Question</h2>
A [study analyzing errors in 2016 election polling](https://digitalcommons.unl.edu/sociologyfacpub/543/) found that most pollsters overweighted the responses of people who didn't actually cast a ballot on election day. They may have weighted all responses equally, failing to account for people's likelihoods to vote, or they could have weighted responses based on a factor not-related or inversely related to voter turnout. But how would a pollster know if a surveyed subject was "likely to vote." According to the researchers, those most likely to vote were people who owned landline phones!  
I'm skeptical that the sheer act of having a wall/landline phone in one's home, and walking over to it every time they receive a call makes them likely to vote... but it's possible that there are *other demographic features* of people with landline phones that *also and independently* influence their decision to cast a ballot. These could include age, race, type of residence/neighborhood, and those are exactly the factors that I'll analyze in this week's post!  
In this post I build a model for predicting the national democratic vote share by creating three likelihoods that people will turnout to vote, based on race, age, and education level, respectively. I code these variables into 4 categories, and one limitation is the 64 distinct combinations of identities that people can possess. It's impossible to predict turnout at the *individual level* from this data, because different voters may be swayed based on *different* elements of their identify (i.e. while one voter may strongly identify and vote alongside people of the same race, another voter may be more encouraged by voters their own age.)

<h2>The Data</h2>
I cleaned datasets for voter age, race, education level, turnout rate, and share of the electorate for all general and midterm elections since 1986. The charts below summarize turnout rate for each category over time:


```
## ── Attaching core tidyverse packages ──────────────────────── tidyverse 2.0.0 ──
## ✔ dplyr     1.1.3     ✔ readr     2.1.5
## ✔ forcats   1.0.0     ✔ stringr   1.5.0
## ✔ ggplot2   3.4.4     ✔ tibble    3.2.1
## ✔ lubridate 1.9.3     ✔ tidyr     1.3.0
## ✔ purrr     1.0.2     
## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
## ✖ dplyr::filter() masks stats::filter()
## ✖ dplyr::lag()    masks stats::lag()
## ℹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-2-1.png" width="672" /><img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-2-2.png" width="672" /><img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-2-3.png" width="672" />

