# Helping real estate buyers make the right choice

## Introduction/Business Problem
A real estate start-up company wants to recommend properties to it's clients based on various market factors and include ease of life as one of the key aspects. Rather than going with intuitions and general assumptions, they are interested in bring in the insights from the openly available data to identify which neighborhoods are best fo their clients looking at various factors such as proximity of facilities such as 
* restaurants
* groceries
* transportation
* education
* sports complexes
* crime rate in the neighborhood
* etc.

Our task is to help the company classify the neighborhoods via statistical means and bring the right level of insights for the customers of the company and ease them into making "the right choice".

## Data
Below are the data sets used for execution of this project

1. Web scrapping - To fetch the neighborhood details of Toronto. This is the core data set and will act as the platform for our project. All the data sets used in the project will directly or indirectly find its way to this information
2. Foursquare API - To fetch the attractions around neighborhoods. The data from the API will help us find various kinds of venues around the neighborhood in 500m distance.
   * Venue category roll up - A manually created file to reduce the number of Venue categories
3. Crime reports - A detailed list of crime reported by Toronto police dating between 2015 and 2019. A clean form of this data with latitude and longitude was available on Kaggle. https://www.kaggle.com/kapastor/toronto-police-data-crime-rates-by-neighbourhood

## Methodology

### The core
The core data set for this project was created by pulling the Neighborhoods of Toronto along with Borough, & PostalCode from a [Wikipedia page](https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M). An address field was created using the information which was then passed on to the Geocoder API to fetch the latitude and longitude of each neighborhood.

### Nice to have
Next step was to bring in the venues/attractions for each neighborhood and then categorize them before rolling them up to create a neighborhood wise count of venues. This was achieved using Foursqaure API. The Foursqaure API had categories at very granular level and needed to be brought down to control the results of the unsupervised model we were to build. A manual lookup file was created to roll up the categories in broader groups. These broad groups replaced the venue categories retreived from Foursquare API and then the data was rolled up to get the neighborhood wise venue counts for each category.

### Crime scene
Integrating the [crime reports](https://www.kaggle.com/kapastor/toronto-police-data-crime-rates-by-neighbourhood) with the core data was the next step. It was an uphill task as the crime data though was clean it was not at the same granulrity as our core data. First the latitude and longitude of crime scene was used as pivot to rollup all the crime reports. This data snippet was then cross joined with the core data set. Using the latitude and longitude of Neighborhood and crime scene, euclidean distance was calculated. This was used to identify the closest neighborhood from the crime scene. The idea behind this was to calculate the number of crime reports by each neighborhood. The crime reports were futher aggreagted to get the crime reports by each neighborhood.

Further more to get a sense of which time of the day the crime reports are more often and overlay on the map was created to show a heatwap that cycles between 24 hours of the day to show the aggregated number of crime reported.

### The model
The core data, venues/attractions data, & the crime data was brought together to create a master data for our model building. Only the necessary columns were retained and the data was scaled(standardized) prior to clustering. KMeans cluster algorithm was used to created multiple versions of models with different count of clusters. A scree plot helped us identify that 8 clusters will be optimal.

# The Result
Analyzing the clusters with average number of attractions and the crime reported in last 5 years, we identify the neighborhoods labeled as 2, 3, & 4 are the best for real estate investments. These neighborhoods have high number of attractions in/around them and also have very low count of crime reported in last 5 years.

![image](https://user-images.githubusercontent.com/76211413/124779036-1446bf00-df5f-11eb-895a-0c837a0f1e9d.png)

The overlay with crime report heatmap also helps get a sense of the areas where the ocurences are high and help the customers avoid making investments in such areas.

![image](https://user-images.githubusercontent.com/76211413/124845130-b2fd0b00-dfb3-11eb-865f-4b4ecc3a9160.png)

# The discussion
The likeness or desirability of a property is one of the key fators in deciding the price. A data driven analysis by looking at as many aspects no matter how trivial they may appear should be done to assess their impacts. This project was an attempt to bring together all such aspects and look at the problem statement from statistical lens.

# The conclusion
This project was an attempt to add another dimension to the decision making process when a customer is looking to make an investment in a property. We were able to address the problem statement by clustering and grouping the neighborhoods considering various factors. It was found that some neighborhoods have low count of attractions but bery high crime rates. These would be the areas where the investors need to avoid making any investments.

This analysis can further help the administration to identify the reasons why certain areas have high crime rate and take preventive measures.
