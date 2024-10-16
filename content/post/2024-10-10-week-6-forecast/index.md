---
title: Forecast 10/14/2024
author: Catherine Stanton
date: '2024-10-10'
slug: week-6-forecast
categories: []
tags: []
---

<h1>Week 6: October 14, 2024</h1>  
This blog is an ongoing project for Professor Ryan Enos' Election Analytics Course at Harvard College (GOV 1347, Fall 2024). It will be updated weekly with posts analyzing how different features impact the likelihood of Kamala Harris (D) or Donald Trump (R) winning the 2024 U.S. Presidential Election or winning specific states in the election. The blog will culminate in a final predictive model for the outcome of the general election.

<h2>Context & Question</h2>
The focus of this week's post is campaign advertising. I decided to do a callback to the post from September 30th and investigate the difference between incumbent candidates and challenger candidates when it comes to advertising. Do ad tones change for incumbent candidates and challengers? Are the tones of advertisements markedly different for successful candidates versus unsuccessful ones?

<h2>Exploratory Analysis</h2>
Before I investigate the relationships between ad tone and incumbency, I want to expose some of the trends in campaign ads since the 2000 election.



First we can get an idea of *why* campaigns run ads. The following plot shows the distributions of campaign motives for Democratic and Republican candidates in the elections between 200 and 2016. Candidates could run "personal," versus "policy," versus "other" ads. Both parties' candidates *tended* to air ads that focused on policy, a trend that was broken in 2016 when candidate Donald Trump devoted a significant majority of his advertising to personal issues/causes.


```
## Joining with `by = join_by(creative, party, cycle)`
## `summarise()` has grouped output by 'cycle', 'party'. You can override using
## the `.groups` argument.
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-2-1.png" width="672" />

Next, I wonder how ad tone corresponds to candidate success. Below are two plots, one showing the ad tones of all winning candidates in elections since 2000 and one showing the tones of all losing candidates since 2000. Ad tones were classified as "attacking" one's opponent, "promoting" oneself, or "contrasting" oneself with the opponent in this dataset. 


```
## `summarise()` has grouped output by 'cycle', 'winner'. You can override using
## the `.groups` argument.
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-3-1.png" width="672" />

As we can see the 2004 and 2012 elections were marked by attacks whereas the 2008 election was largely contrast ads. The most promotional ads were in the 2000 election. One limitation with this data is that it only contains information about ad tones from the elections between 2000 and 2012. However, as we saw in the previous plot, the 2016 election represented a shift in *ad motivation,* and it's likely that that may have corresponded to a shift in ad tone (i.e. "personal" ads may be more likely to be "attacking" or "promoting" for a certain candidate than "policy" ads or "other" ads). 

<h2>Incorporating Incumbency</h2>
I decided to investigate how incumbency influences a candidate's tone in advertisements. Given that incumbent candidates have the advantage of 4-years of publicity and media spotlight that their opponents do not, I though that may manifest difference in ad tone. Further, incumbent candidates sometimes run on different issues that challengers (e.g. many presidents running for a first term focus on domestic politics while many running for reelection focus on foreign policy). Different issues may be more partial/conducive to different ad tones. Lastly, incumbent candidates probably have an advantage in portraying the previous four years in a very positive light while challengers likely have an advantage in pointing out its problems. This would seem to correspond quite directly to ad tone.




```
## `summarise()` has grouped output by 'cycle', 'incumbent'. You can override
## using the `.groups` argument.
```

<img src="{{< blogdown/postref >}}index_files/figure-html/unnamed-chunk-5-1.png" width="672" />

Some of the individual bars in the plot above are the same as those from the plot looking at successful/unsuccessful ad tones, but these are divided by whether the candidate was an incumbent or not. For example, since the incumbent was successful in 2004, the 2004 bar under the 'incumbent TRUE' plot here is the same as the 2004 bar under the 'successful TRUE' bar on the previous plot.  
As expected, the portions of "promoting ads" were greater for incumbent candidates than challengers between 2000 and 2012. Surprisingly, the portions of attacking ads were relatively equal, or at least they changed together (i.e. an incumbent did not attack a challenger more than they got attacked in any given election between 2000 and 2012--rates of attacks between the candidates were approximately symmetrical). The difference then is made up in "contrasting" advertisements, of which challenger candidates tended to run more.  
The decrease in attacks in the 2008 election between Barack Obama and John McCain is interesting. This was the first election that an African American candidate won, and it's plausible that both candidates strayed *away* from attacks to avoid allegations that they were made on the basis of race.

<h2>Takeaways</h2>
This analysis showed that, incumbent candidates and challenger candidates increased and decreased their attacks/promotional ads simultaneously, even if one (usually the incumbent) had *more* attacking ads than the other.  
It's worth noting that ads are not the only arena in which candidates get to set the tones of their campaigns. The candidates from the two major U.S. parties each attend and speak at a National Convention, which is a widely-viewed and publicized event by much of the electorate. They usually debate each other at least once in the year before the election, which likewise provides an opportunity to establish the tone of their campaign and personal "brand."  
Another notable limitation to this analysis is that it treats all ads the same, rather than accounting for their medium. For example, posters are treated equivalent to radio ads are equivalent to TV ads. It's possible that voters will implicitly assign different tones to the same candidate's ads on the basis of how the ad is presented to them, even if the ads objectively have the same tone or convey the same information.  
Further, the focus on incumbency and ad tone provides something interesting for voters to think about while viewing campaign ads. It gives them more context, and possibly helps them understand why candidates may choose to emphasize the messages they do, but it does not necessarily lend itself to a "prediction" of the 2024 election. Something like the plot in the second section, showing the tones of winning and losing candidates in elections since 2000 would do better at this.

