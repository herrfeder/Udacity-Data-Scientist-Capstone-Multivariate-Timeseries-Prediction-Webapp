# Multivariate-Timeseries-Prediction-Webapp
This webapp is part of the Project Repository :https://github.com/herrfeder/DataScientist/tree/master/Project_05_Capstone_Stock_Chart_Analysis

I created this seperate Repository for easier Docker deployment.

## Screenshots of Webapp

| Forecast Application | Buy And Sell Simulation | Timeshift Correlation |
|--------------------------------------|--------------------------------------|--------------------------------------|
| ![](https://github.com/herrfeder/DataScientist/raw/master/Project_05_Capstone_Stock_Chart_Analysis/images/forecast_full_view.png) | ![](https://github.com/herrfeder/DataScientist/raw/master/Project_05_Capstone_Stock_Chart_Analysis/images/buy_and_sell_sim.png) | ![](https://github.com/herrfeder/DataScientist/raw/master/Project_05_Capstone_Stock_Chart_Analysis/images/corr_timeshift.png) |

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
  
## Installation

An example of this web app is temporary accessible on https://federland.dnshome.de/bitcoinprediction .
Please be gentle, the resources are restricted. This app __isn't responsive__.

### Docker Instructions

1. Create directory and download Dockerfile:
    ```
    mkdir bitcoinpred_docker && cd bitcoinpred_docker
    wget https://raw.githubusercontent.com/herrfeder/Udacity-Data-Scientist-Capstone-Multivariate-Timeseries-Prediction-Webapp/master/Dockerfile
    ```

2. Build Docker Container:
    ```
    docker build . -t bitcoinpred
    ```
    
    All models are pretrained and the build process shouldn't take too long.
    
3. Run Docker Container:
    ```
    docker run -p 8050:8050 bitcoinpred:latest
    ```

4. Go to http://127.0.0.1:8050/
