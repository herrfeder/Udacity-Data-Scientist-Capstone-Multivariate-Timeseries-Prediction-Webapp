resources = """
## Causality Resources

  * General Explanation and Tutorial for Stationarity Analysis of Time Series:
    * https://www.analyticsvidhya.com/blog/2018/09/non-stationary-time-series-python/
  * Explanation of Difference Correlation and Causalisation: 
    * https://calculatedcontent.com/2013/05/27/causation-vs-correlation-granger-causality/
  * Used Granger Causality Function from: 
    * https://www.machinelearningplus.com/time-series/vector-autoregression-examples-python/

## SARIMAX Resources

  * Good Overview about ARIMA Models: 
    * https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/
  * How to prepare Explanatory Variables for Multivariate SARIMAX Model: 
    * https://www.kaggle.com/viridisquotient/arimax
  * How to prepare Time Series data for Multivariate SARIMAX Model: 
    * https://www.machinelearningplus.com/time-series/time-series-analysis-python/

## GRU Resources

  * Great visual explanation of RNN (LSTM/GRU):
    * https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21
  * Data Preprocessing for Keras GRU:
    * https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras
  * The GRU Code is inspired and Model Concept is used from there: https://github.com/ninja3697/Stocks-Price-Prediction-using-Multivariate-Analysis/blob/master/Multivatiate-GRU/Multivariate-3-GRU.ipynb
"""

view_data_conclusion = """
## Conclusions from Viewing the Data

  * Gold behaves highly differently compared to Bitcoin
  * the other Stock Charts share some similarities with Bitcoin regarding peaks and bottoms --> deeper investigation
  * from the first point of view the Twitter Sentiments and Google Trends doesn't share any similarity with Bitcoin Chart --> deeper investigation
"""

correlation_conclusion = """
## Simple Correlation

There are some obvious correlations but some interesting as well:
  * Positive Economic Sentiments are strongly correlated with Bitcoin Indicators
  * Google Price is strongly correlated with Bitcoin Indicators
  * SP500 Price is strongly correlated with Bitcoin Indicators
  * Bitcoin Google Trends and Cryptocurrency Google Trends are strongly correlated with Bitcoin Indicators
  

## Shifting Correlation

It's very interesting, as:
  * 30 Day into Past shifted Economy Positive Sentiments increased its correlation with Bitcoin Price Indicators
  * 30 Day into Past shifted Cryptocurrency Google Trends increased its correlation with Bitcoin Price Indicators
  * 30 Day into Past shifted Bitcoin Google Trends remains its correlation with Bitcoin Price
  * 30 Day into Past shifted Google, SP500 and Dax Prices increased its correlation with Bitcoin Price
  
It's very interesting as well:
  * The Gold Price isn't correlated with Bitcoin Price in any way
"""

stationarity_causality_conclusion = """
## Conclusions from Seasonality/Stationarity

It lies in the nature of an financial market chart, that it has a trend and in the case of Bitcoin a very high volatility and therefore very high residiuals. We can call the Bitcoin Chart very unpredictable due to this result. This fact doesn't need any statistical testing as it's well known that financial chart data is hard to predict. The ADF Test clearly indicated the non-stationarity of most input time series. By diffing them, we can easily remove this stationarity.

For this reason it was my initial approach to add many features for an Multivariate Timeseries Prediction.

As nearly all collected input time series are associated with financial market data they are all not stationary apart from the two added binary columns "month-1" and "month-2". We can easily remove this stationarity by diffing the single columns whereby the next value of a time series is subtracted with the previous one:

## Conclusions from Granger Causality

By adding pre-shifted time series to our granger causality function we can identify several time series that have a significant Granger Causality on the Bitcoin Price:

  * Bitcoin Price of previous Month
  * Alibaba Price of Previous Month
  * "Bitcoin" Google Trends of Previous Month
  * "Cryptocurrency" Google Trends of Previous Month
  * Positive Twitter Sentiments for "#economy"
  * and other
  
It's very promising that so many "Third Party" Indicators like __Google Trends__ and __Twitter Sentiments__ seems to have an impact to the monthly future of Bitcoin Price. 

I will choose the features for my multivariate Time Series Modelling based on the results from the Correlational Analysis and the Causality Analysis.
"""

model_eval_conclusion= """
## SARIMAX Conclusions

Regarding the ranges of my resulting prediction and real plot the resulting RMSE (root-mean-squared-error) value is a good first result and may will be used for prediction and catching good forecasting signals and triggers.

We can see, that the resulting prediction is very noisy. That's due to the high volatility in the Google Trends and Sentiment Time Series.


## GRU Conclusions


"""

chances_roadmap ="""
blubb
"""

granger_prob_expl = """
#### Granger Causality tests on a Null hypothesis:

  * __Null Hypothesis__: X does not granger cause Y.
  
  * If __P-Value < Significance level__ (0.05), then Null hypothesis would be rejected.
  >
  > Example: __cryptocurrency_Google_Trends_x__ does granger cause __bitcoin_Price_y__ 
  >
  
  * If __P-Value > Significance level__ (0.05), then Null hypothesis cannot be rejected.
  >  
  > Example: __alibaba_Price_x__ doesn't granger cause __gold_Price_y__
  >
"""

introduction = """
# Capstone Project: Multivariate Timeseries Analysis and Prediction (Stock Market)
## Purpose

Building an Time Series Forecast Application to predict and forecast __Bitcoin financial data__
using supervised and unsupervised Machine Learning Approaches, this includes:
  * search, collection and of supportive Features in form of suitable Time Series (social media, other similar charts)
  * preparation, analysis, merging of Data and Feature Engineering using:
    * Correlative Analysis
    * Stationarity Analysis
    * Causality Analysis
  * Model Preprocessing and Model Fitting with this Machine Learning Algorithms:
    * supervised SARIMAX (Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors model)
    * unsupervised GRU (Gated Recurrent Unit)
  * building an Web Application using a Dash Webapp (see folder __webapp__)
    * explains my roadmap of analysis and conclusions
    * provides feature of daily forecasting using designed models
    * Own Webapp Repository: https://github.com/herrfeder/Udacity-Data-Scientist-Capstone-Multivariate-Timeseries-Prediction-Webapp
  

## Approach/Idea

It's nearly impossible to give an accurate prediction for Stock Charts or Cryptocurrency Charts for the Future.
Therefore I will only try to find signals or triggers that may announce major Movements on the Bitcoin Chart and may occur
right before the real movements.

I want to find Correlation and Causality to the Bitcoin Price by shifting all other collected time series in time.
For Example: Shifting all supportive Features one month to past gives me the freedom to look one month into the future for forcasting.
These notebooks will show my course of action:

  * [01 Correlation Analysis](https://github.com/herrfeder/DataScientist/blob/master/Project_05_Capstone_Stock_Chart_Analysis/01_corr_analysis.ipynb)
  * [02 Stationarity and Causality Analysis](https://github.com/herrfeder/DataScientist/blob/master/Project_05_Capstone_Stock_Chart_Analysis/stationarity_causality_analysis.ipynb)
  * [03 SARIMA Modelling](https://github.com/herrfeder/DataScientist/blob/master/Project_05_Capstone_Stock_Chart_Analysis/03_1_model_ARIMAX.ipynb)
  * [04 GRU Modelling](https://github.com/herrfeder/DataScientist/blob/master/Project_05_Capstone_Stock_Chart_Analysis/04_model_GRU.ipynb)
  * [05 Decision Algorithm](https://github.com/herrfeder/DataScientist/blob/master/Project_05_Capstone_Stock_Chart_Analysis/05_decision_algorithm.ipynb)

## Used Data

1. Stock Market Data for the last five years from [Investing.com](https://www.investing.com) for:
  * Bitcoin
  * DAX
  * SP500
  * Google
  * Amazon
  * Alibaba
2. Google Trends for keywords "bitcoin", "cryptocurrency", "ethereum", "trading", "etf" using this notebook 
  * [00_scrape_googletrend.ipynb](https://github.com/herrfeder/DataScientist/blob/master/Project_05_Capstone_Stock_Chart_Analysis/00_scrape_googletrend.ipynb)
3. Twitter Sentiments for keyword "bitcoin" and "#economy" using notebooks 
  * [00_scrape_twitter.py](blubb)
  * [00_tweet_to_sent.ipynb](blubb)
"""

