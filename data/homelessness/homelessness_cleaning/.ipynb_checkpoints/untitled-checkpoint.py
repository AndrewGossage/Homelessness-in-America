{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3ea6f2d0",
   "metadata": {},
   "source": [
    "## Software needed"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "177ab6b2",
   "metadata": {},
   "source": [
    "pandas, matplotlib, seaborn, sklearn "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2dc5d3d6",
   "metadata": {},
   "source": [
    " ## Data Collection"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "93c471c3",
   "metadata": {},
   "source": [
    "The US Census department collects data on income and costs for both renters and homeowners down to the city level.  This data was very detailed and had the breakdown for the number of residents in $10,000 intervals for income and $300 intervals for costs.  For this study we just used the median for the years 2017 to 2019\n",
    "\n",
    "https://data.census.gov"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7001638c",
   "metadata": {},
   "source": [
    "| Features                | Description                       |\n",
    "|-------------------------|-----------------------------------|\n",
    "| Median household Income | Median Income for the entire city |\n",
    "| Median household Cost   | Median cost for the entire city   |\n",
    "| Owner Occupied Income   | Median income for property owners |\n",
    "| Owner Occupied Cost     | Median cost for property owners   |\n",
    "| Renter Occupied Income  | Median income for renters         |\n",
    "| Renter Occupied Cost    | Median cost for renters           |"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "255026f8",
   "metadata": {},
   "source": [
    "## EDA"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "371ace4b",
   "metadata": {},
   "source": [
    "The next step was to look for trends in the data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16f69559",
   "metadata": {},
   "source": [
    "<img scr=\"./images/EDA.png\">"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d4ef08bf",
   "metadata": {},
   "source": [
    "What was Interesting about this was we could start to see a trend (a sort of triangular shape) in the main clustering of the data.  Upon discussion with the team this was found to correlate with some of their findings and on the plot to the right the center of the cluster was around 60,000 which is also the median income in the US.\n",
    "\n",
    "The next step was building a Linear Regression model.  We chose Linear Regression for its simplicity and wanted easily interpretable features.  Although our model was a poor fit with an R^2 score of 33% we were able to see that the rental cost stood out as a large feature.  We took this information and started the next part of the research.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7c990faf",
   "metadata": {},
   "source": [
    "In our research we found an interesting article by Continum of Care outlining how cities are dealing with homeless and places that have had success and those that have not.  The article pointed out that when a city surpasses a rental cost to income ratio of 32% the city can start experiencing chronic homelessness.  So we created a column of this ratio and looked at cities above that ratio and compared it to our homeless counts.\n",
    "\n",
    "https://dupagehomeless.org/research-demonstrates-connection-between-housing-affordability-homelessness/"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2684554f",
   "metadata": {},
   "source": [
    "<img scr=\"/images/rent_ratio.png\">"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d944d1a8",
   "metadata": {},
   "source": [
    "Although we tried to match our data to what the research had said we were unable to.  We could not identify a direct tie between the increasing rental ratio and increasing homelessness.  This was also a good indication of how complex this problem is for America and that there is not an easy solution."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14b7658e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ad37c80",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "70e03dcc",
   "metadata": {},
   "source": [
    "The article mentioned my current city as a success story and so I investigated further as to why Houston had experienced success.  The two big takeaways from the article:\n",
    "\n",
    "- Development of the HMIS system (an integrated system that coordinates community involvement and departments across the city.\n",
    "\n",
    "- Trying to find more permanent housing than temporary\n",
    "\n",
    "https://www.texastribune.org/2019/07/02/why-homelessness-going-down-houston-dallas/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a41fbc5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "41401bad",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "985f074d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b8fa3f4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b87679b0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}