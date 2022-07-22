import pickle
import streamlit as st
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from prediction import get_prediction



st.set_page_config(page_title='Site Energy Intensity Prediction', page_icon="⚡", 
                   layout="wide", initial_sidebar_state='expanded')

pickle_in = open('cb_model.pkl', 'rb') 
cb_model = pickle.load(pickle_in)

#creating option list for dropdown menu  

features = ['floor_area','year_built','energy_star_rating','ELEVATION','january_min_temp','january_max_temp','february_min_temp','february_max_temp',' march_min_temp','march_max_temp',
            'april_min_temp','april_max_temp','may_min_temp','may_max_temp','june_min_temp','june_max_temp',' july_min_temp',' july_max_temp',' august_min_temp','august_max_temp','september_min_temp',
            'september_max_temp','october_min_temp','october_max_temp','november_min_temp','november_max_temp','december_min_temp','december_max_temp',' cooling_degree_days',
            'heating_degree_days','snowfall_inches','days_below_20F','days_above_80F','direction_max_wind_speed','direction_peak_wind_speed','days_with_fog']


st.markdown("<h1 style='text-align: center;'>Site Energy Intensity Prediction App ⚡ </h1>", unsafe_allow_html=True)


