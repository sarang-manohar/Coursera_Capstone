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
4. Crime reports - A detailed list of crime reported by Toronto police dating between 2015 and 2019. A clean form of this data with latitude and longitude was available on Kaggle. https://www.kaggle.com/kapastor/toronto-police-data-crime-rates-by-neighbourhood
