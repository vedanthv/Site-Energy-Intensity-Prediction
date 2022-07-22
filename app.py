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

