## Site Energy Intensity Prediction

[Blog Post](https://vedanthvbaliga.netlify.app/blog/site-energy-intensity-pred/) explaining the entire project

Unfortunately plotly graphs dont display on github as the latter is set for static plots only, hence please 
use this nbviewer [link](https://nbviewer.org/github/vedanthv/Site-Energy-Intensity-Prediction/blob/master/version1.ipynb) to view the notebook.

## Abstract

Climate change is a globally relevant, urgent, and multi-faceted issue heavily impacted by energy policy and infrastructure. Addressing climate change involves mitigation (i.e. mitigating greenhouse gas emissions) and adaptation (i.e. preparing for unavoidable consequences). Mitigation of GHG emissions requires changes to electricity systems, transportation, buildings, industry, and land use.

the lifecycle of buildings from construction to demolition were responsible for 37% of global energy-related and process-related CO2 emissions in 2020. Yet it is possible to drastically reduce the energy consumption of buildings by a combination of easy-to-implement fixes and state-of-the-art strategies.

## Dataset

The WiDS Datathon dataset was created in collaboration with Climate Change AI (CCAI) and Lawrence Berkeley National Laboratory (Berkeley Lab). WiDS Datathon participants will analyze differences in building energy efficiency, creating models to predict building energy consumption. Participants will use a dataset consisting of variables that describe building characteristics and climate and weather variables for the regions in which the buildings are located. Accurate predictions of energy consumption can help policymakers target retrofitting efforts to maximize emissions reductions.

## Brief Description of the Solution 

The project involves predicting a buildings Site Energy Usage Intensity metric, which was the `site_eui` feature in the dataset (regression problem).  To solve this problem, I first separated the dataset into twelve individual datasets based on buildings with similar `site_eui` usage patterns and other characteristics.  I then engineer features, perform leave one group out cross validation, and finally train an ensemble model (XGBoost, LightGBM, and CatBoost regressors) for each dataset on the most powerful features.  My final solution ended up in the top 10% of the final leaderboard.


# Helper Functions

To make the code in the projects modular, I have used helper functions that include reusable code for **reading data**, **preprocessing tasks**, **feature engineering**, **cross validation** and **modelling**. Feel free to check out my [github](https://github.com/vedanthv/Site-Energy-Intensity-Prediction/blob/master/site-eui-pred-final.ipynb) repository for indepth docstrings of each function and post an [issue](https://github.com/vedanthv/Site-Energy-Intensity-Prediction/issues) if you want to report a bug for any of the functions.

# Data Preprocessing

## Dealing with Duplicate Data

* We see that there are 39 duplicated buildings in the train set and 5 duplicate buildings in the test set. 

* Since the number of duplicates is very less compared to the 75k samples in the dataset, I have removed the duplicates.

* I have left the duplicates in the test set as otherwise, it could affect the predictions.
