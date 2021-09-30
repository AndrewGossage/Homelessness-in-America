# Project 5 Homelessness in America

## Contents

1. [Introduction](#Introduction)
2. [Data Cleaning and EDA of homeless counts](#Data-Cleaning-and-EDA-of-homeless-counts)
5. [Conclusions and TODO](#Conclusions-and-TODO)

## Introduction



## Data Cleaning and EDA of homeless counts

### The Data

The department of Housing and Urban Development (HUD) publishes counts of sheltered and unsheltered homeless populations  every year ([source](https://www.hudexchange.info/programs/coc/coc-homeless-populations-and-subpopulations-reports/)). These counts are based on Point-in-Time (PIT) information provided to HUD by Continuum of Care (CoC) Homeless Assistance Programs  in the application for CoC Homeless Assistance Programs. The PIT Count provides a count of sheltered and unsheltered homeless persons on a single night during the last ten days in January for each CoC.



### Data Cleaning

The PIT estimates for the years for the years 2014 to 2020 were obtained from the reports published by the HUD. These reports contain the counts of homeless for each CoC. Data cleaning involved gathering information about the city served by the CoC from separate tables from the HUD's website, merging this with the PIT estimates data and then aggregating these counts at the city level for each year between 2014 to 2020. The details of this data processing can be found in this [notebook](https://github.com/AndrewGossage/Project5/blob/master/data/homelessness/homelessness_cleaning/PIT%20and%20HIC%20Data%20Cleaning.ipynb)

The tables containing the aggregated information for PIT estimates along with the cities served by each CoC for all years from 2014 to 2019 can be downloaded from [here](https://github.com/AndrewGossage/Project5/blob/master/data/homelessness/homelessness_cleaning/2014-2021-PIT-esimates-cleanish.csv)

HUD also publishes the Housing Inventory Count or the HIC which is the number of housing units (both permanent and transitional) provided by each CoC. This data was also cleaned and merged with the city data of each CoC and can be downloaded from [here](https://github.com/AndrewGossage/Project5/blob/master/data/homelessness/homelessness_cleaning/2014-2021-HIC-cleanish.csv)

### EDA

In 2020, a little over half a million people (574577) were homeless in the US. The states with the highest numbers of homeless population are

| State      | Homeless population |
|------------|---------------------|
| California | 161548              |
| New York   | 91271               |
| Texas      | 27229               |
| Florida    | 25977               |
| Washington | 22923               |

![homeless_state_2020.png](/figures/homeless_state_2020.png)
