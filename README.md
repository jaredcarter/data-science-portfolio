# Data Science Portfolio
This portfolio page documents my personal experience with various data science tools and concepts, sorted by publication date
I hope you find these projects as interesting as I have!

# Contents

## Taylor Swift Eras Song Data

- tags: python, plotly, interactive, data analysis, API, requests
- [Link to project](https://nbviewer.org/github/jaredcarter/data-science-portfolio/blob/main/spotify-data/Eras.ipynb)

Taylor Swift music is popular in my household.
Given the recent success of her Eras tour, I decided to look into the popularity and audio features of her different albums.
This allowed me to explore the functionality of the interactive plotting library plotly.

## Airport Usage by Private Planes

- tags: python, pandas, seaborn, visualization, exploratory data analysis, FBOs
- [Link to project](private-planes/Private%20Planes%20at%20Airports.ipynb)

After recently learning about fixed base operators (FBOs), I used publicly available FAA data to determine which regional airports have the most small airplane traffic.
I used exploratory data analysis and visualization techniques to identify the most heavily used airports and identified airports which have been growing the most rapidly.

## Customer Segmentation from Online Retailer Data

- tags: python, scikit-learn, unsupervised learning, clustering analysis, RFM
- [Link to project](customer-segmentation/Customer%20Segmentation.ipynb)

Customers are not one giant monolith, all thinking the same way and making the same decisions. Inside any customer base there are usually different factions, each with their own preferences. An advertisement or promotion that is received favorably by one faction may have no effect on other factions. Additionally, with the quantity of data and customers it generally isn't feasible to consider every potential new customer and manually decide which "bucket" this customer falls into. By automatically segmenting customers into different groups based off of data, we can better understand the kinds of customers that constitute the customer base and attempt to cater to each group's specific interests, increasing customer satisfaction (and sales).


## Time Series Analysis with Increasingly Complex Methods

- tags: statsmodels, ARIMA, time-series analysis, autoregression, exponential smoothing, python
- [Link to project](statistics/Time%20Series%20Analysis%20With%20Increasingly%20Complex%20Methods.ipynb)

Time series data is quite relevant to organizations that need to understand how past indicators can predict future trends.
This sort of data usually features long term trends, periodic seasonality, and random noise that can confound simpler regression analysis.
Read on to see how to generate time series data, why linear regression, even when non-linear in parameters are ill-equipped to model this sort of data, and how the autoregression and moving averages are combined in ARIMA models.

## Introduction to Regression in Python with statsmodels

- tags: statsmodels, regression, confidence interval, jupyter notebook, python, statistics, decision science
- [Link to project](statistics/Regression%20Intro.ipynb)

We can reduce the uncertainty of predictions if we correctly apply our understanding of the relevant data.
Since a key element of decision making involves accurate predictions, this skill is quite necessary.
This article starts with some generated data, then we apply increasingly useful models to fit the data--from random guesses to ordinary least squares linear regression.

## Analyzing Songs with Spotify Data

- tags: jupyter notebook, pandas, python, requests, plotly
- [Link to project](spotify-data)

The final project for the Summer 2023 data science bootcamp that I facilitated had participants use Spotify's API to request song information from artists of their choosing, then use that data to learn more about differences between their favorite artists.

## Introduction to Pandas

- tags: jupyter notebook, pandas, python
- [Link to project](intro-pandas/Introduction%20to%20Pandas.ipynb)

Pandas is an essential component of data analysis in Python.
This notebook is an excerpt from a data science introductory bootcamp for high school teachers that I facilitated in the summer of 2023.

## Micro:bit Gesture recognition

- tags: edge ML, decision tree, micro:bit, microcontroller, micropython, jupyter notebook, scikit-learn, python
- [Link to project](microbit-gesture)

Running machine learning models on edge devices can aid greatly in simplifying requirements for many different kinds of projects.
In this example, I use a micro:bit microcontroller to measure accelerometer data, train a decision tree classifier on this data in order to recognize different gestures, then run the model locally on the micro:bit to classify gestures in real time.