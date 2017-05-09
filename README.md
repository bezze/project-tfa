Star Wars The Force Awakens IMDB Review distribution
====================================================

To understand the data beyond the mere stars rating where opinions are difficult to transform into a quantitative result, i.e. people use different scales to rate, I assigned to each review an approval or confidence rating. This number is the percentage of people that found the review "useful", according to IMDB's description of the number. I prefer to interpret this value as the "affinity" or "approval" a user has towards the opinion portrayed in the review. As this number alone is not enough, I also added the weight of the opinion, the number of people who judged the review. It's not the same a 4 stars opinion with 54/1086 approval than a 7 with 845/933. 

I proceeded to plot the star distribution and the approval ratio:

![alt text](https://github.com/bezze/project-tfa/blob/master/figure_1.png "figure_1")

The approval ratio marker sizes are related to the mean weight of the reviews in that bin category. The biggest marker weighs 165.7 while the smallest weighs 18.0.

The star rating distribution (blue bars) presents a linear behaviour from 2 to 10, with a peak of "hateful" ratings at 1. This peak is slightly higher than the one at 10.

Surprisingly, I found great polarization in the approval ratio (red squares), taking an almost constant value around 0.67 under the 6 stars rating and around 0.2 over 6 stars. Assuming equal likelihood of reading any review (which is not), this means that the more "solid" reviews are below 6. On the other hand, opinions that rated over 6 lack the users approval. This is at odds with the rating distribution which states a great number of positive ratings. A plausible explanation would be that only the more "zealous" users from the other side of the spectrum took the time to share review other critics. The exact 6 stars value plays the role of some kind of critical parameter so I will use it as a reference to differentiate the "good" rating reviews (over 6) against the "bad" rating reviews (under 6).



TOTAL =  4018

bad = 1683 (below 6)

even = 362 (6)

good = 1973 (above 6)

Using this data, the average score is

average = 5.905674 

against IMDB's 8.1. They admit using a [weighted average](http://www.imdb.com/help/show_leaf?ratingsexplanation) to "reduce attempts at vote stuffing" adding that "the exact methods we use will not be disclosed". To introduce a bit of context, ["The Godfather"](http://www.imdb.com/title/tt0068646/?ref_=nv_sr_1) rates 9.2, ["2001: A Space Odyssey"](http://www.imdb.com/title/tt0062622/?ref_=nv_sr_1) 8.3, and ["Mary Poppins"](http://www.imdb.com/title/tt0058331/?ref_=nv_sr_2) a sober 7.8. Although this is not the fairest of comparisons, it helps to introduce similar ratings. If one were to only look at the rating distribution, the abnormal peak at 1 would confirm IMDB's fears. But the approval ratio suggests true agreement between users over certain ratings, suggesting IMDB's secret filters are dangerously biased.

To picture the review polarization, I ignored weight and made a 2d histogram of stars against approval.

![alt text](https://github.com/bezze/project-tfa/blob/master/figure_2.png "figure_2")

The graph shows two well defined density peaks, one around 2.5 stars and 0.85 approval and another a bit more diffuse, but bigger in size around 8 stars and 0.3 apporval ratio. The blobs share roughly the same amount of reviews, easily identifiable as the "bad" and "good" reviews.

##### About

The data used is in the raw.dat file, extracted using the main.py python script on Monday 8th of May, 2017. The columns in the raw.dat file are as follows: stars, usefulness, total. The analysis was also performed in python, using the stats.py script. The files are easily tweakable to further investigate other films. 
