# Data Science Portfolio
This portfolio page documents my personal experience with various data science tools and concepts, sorted by publication date
I hope you find these projects as interesting as I have!

# Contents

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