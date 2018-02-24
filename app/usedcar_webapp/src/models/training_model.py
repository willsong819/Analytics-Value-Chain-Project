#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:02:49 2018

@author: Willie
"""

import pandas as pd
import statsmodels.api as sm
from sklearn import linear_model

car = pd.read_csv('/Users/Willie/Desktop/MSiA/Winter 2018/MSiA 423 Analytics Value Chain/used_cars_new.csv',
                  low_memory=False)
car.dtypes
car2=car[car.price_eur<1000000]
car_train = car2[['mileage','door_count','seat_count','engine_displacement',
                  'engine_power']]
car_y = car2['price_eur']

lm1=sm.OLS(car_y,car_train)
results_lm1=lm1.fit()
results_lm1.summary()

pickle.dump()


# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
result=regr.fit(car_train, car_y)
print('Coefficients: \n', regr.coef_)


# Make predictions using the testing set
car_y_pred = regr.predict(car_train)



import pickle
favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump( favorite_color, open( "/Users/Willie/Desktop/save.p", "wb" ) )

favorite_color2 = pickle.load( open( "/Users/Willie/Desktop/save.p", "rb" ) )




