## Software needed

pandas, matplotlib, seaborn, sklearn 

 ## Data Collection

The US Census department collects data on income and costs for both renters and homeowners down to the city level.  This data was very detailed and had the breakdown for the number of residents in 10,000 intervals for income and 300 intervals for costs.  For this study we just used the median for the years 2017 to 2019

https://data.census.gov

| Features                | Description                       |
|-------------------------|-----------------------------------|
| Median household Income | Median Income for the entire city |
| Median household Cost   | Median cost for the entire city   |
| Owner Occupied Income   | Median income for property owners |
| Owner Occupied Cost     | Median cost for property owners   |
| Renter Occupied Income  | Median income for renters         |
| Renter Occupied Cost    | Median cost for renters           |

## EDA

The next step was to look for trends in the data

<img src="images/EDA.png">

What was Interesting about this was we could start to see a trend (a sort of triangular shape) in the main clustering of the data.  Upon discussion with the team this was found to correlate with some of their findings and on the plot to the right the center of the cluster was around 60,000 which is also the median income in the US.

The next step was building a Linear Regression model.  We chose Linear Regression for its simplicity and wanted easily interpretable features.  Although our model was a poor fit with an R^2 score of 33% we were able to see that the rental cost stood out as a large feature.  We took this information and started the next part of the research.



In our research we found an interesting article by Continum of Care outlining how cities are dealing with homeless and places that have had success and those that have not.  The article pointed out that when a city surpasses a rental cost to income ratio of 32% the city can start experiencing chronic homelessness.  So we created a column of this ratio and looked at cities above that ratio and compared it to our homeless counts.

https://dupagehomeless.org/research-demonstrates-connection-between-housing-affordability-homelessness/

<img src="images/rent_ratio.png">

Although we tried to match our data to what the research had said we were unable to.  We could not identify a direct tie between the increasing rental ratio and increasing homelessness.  This was also a good indication of how complex this problem is for America and that there is not an easy solution.

-------

The article mentioned my current city as a success story and so I investigated further as to why Houston had experienced success.  The two big takeaways from the article:

- Development of the HMIS system (an integrated system that coordinates community involvement and departments across the city.

- Trying to find more permanent housing than temporary

https://www.texastribune.org/2019/07/02/why-homelessness-going-down-houston-dallas/
