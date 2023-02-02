# pip install pycaret
# pip install numba --upgrade

import pandas as pd
import pycaret
from pycaret.regression import *

# check pycaret version
print('PyCaret: %s' % pycaret.__version__)

# read data
dataset = pd.read_csv('scaled_onehot_log_all_data.csv')

# train/test split
data = dataset.sample(frac=0.9, random_state=786).reset_index(drop=True)
data_unseen = dataset.drop(data.index).reset_index(drop=True)

print('Data for Modeling: ' + str(data.shape))
print('Unseen Data For Predictions: ' + str(data_unseen.shape))

# autoML setup
model_stp = setup(data = data, target = 'log_wait_time_max', session_id=123)

# create a model - decision tree chosen after assessing different models
dt = create_model('dt')

# tune model - requires a lot of resources currently not utilised
# tuned_dt = tune_model(dt)

# predict
unseen_predictions = predict_model(dt, data=data_unseen)

# export predictions
unseen_predictions.to_csv('predictions.csv')
