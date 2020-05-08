# 09-Surfs_up
Module 9: Surf's Up with Advanced Data Storage and Retrieval

## Project Overview
We've been tasked to create a Weather Analysis from a SQLite Weather Data in Oahu, Hawaii, to back up a business plan to open a Surf&Shake Shop.

## Resources
- Python 3.7.6, Anaconda 4.8.3, Jupyter Notebook, Pandas, Numpy, SQLalchemy, SQLite
- hawaii.sqlite

## Summary
- we started by doing a weather analysis on 1 full year (2016-8-23 - 2017-8-23). We can see that some months have higher amount of precipitation than others. 75% of measurements are lower than the mean, which is still relatively low - it doesn't rain much, except for some short tropical rains. 

<img src="images/prcp_12_months.png" width="250"> <img src="images/prcp_12.png" width="100"> 

- from the most active station, we got the histogram of temperatures for one year showing that the temnperature remains mostly between 67° and 80° - with 325 days over 67°.
<img src="images/tobs_histo.png" width="250">

- we built a Flask app that returns
     
     - all the precipiation data for the same full year - precipitation route
     
     - the different stations providing the data - station route
     
     - all the temperatures observed at the most active station during the same year - tobs route
     
     - the key statistics (min, avg, max) temperatures between 2 dates - temp route
      
## Challenge Overview
Getting the key statistics for the weather data for the months of June and December across all the stations.

## Challenge Summary

Using the SQLite "extract" method, we could filter through all the data by month, get the key statistics, and box-and-whisker plots to easily compare both.

<img src="images/tobs_june.png" width="100"><img src="images/tobs_dec.png" width="100"><img src="images/tobs_plot.png" width="250">

Not suprisingly, we can see that the weather temperatures are pleasant in both June and December, with both means between 70° and 75°, and the temperature in Decembner generally lower by 3-5°. There are very few outliers in this 7-year-range data. We notice more cold outliers in December that must happen at night. 

<img src="images/prcp_june.png" width="100"><img src="images/prcp_dec.png" width="100"><img src="images/prcp_plot.png" width="250"> 

As we saw looking at the precipitation data during a full year, we see that 75% of the measurements are lower than the mean in both cases. The mean for December is almost twice as big as the mean for June, even if both are relatively low - it definitely rains more in December. There a lot of outliers with both maximums max at around 30 times the mean - shwowing a nice weather prone to short intense showers. These whowers happoen more often and get more intense in December. It may still look like a Surf & Shake weather in both months - we can shelter with an icecream during the shower.

Recommendations for further analysis: look more closely at the precipitations outliers:
- geographically by getting the precipitation key statistics for each station ion June and December:
<img src="images/prcp_stations_june.png" width="250"> <img src="images/prcp_stations_dec.png" width="250"> 











