#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import statsmodels.api as sm
import pickle


def modelresult():
	"""This function trains the linear regression model and writes out the model object as a pickle file"""

	car = pd.read_csv('/Users/Willie/Desktop/MSiA/Winter 2018/MSiA 423 Analytics Value Chain/used_cars_new.csv',low_memory=False)
	car2=car[car.price_eur<1000000]
	car_train = car2[['mileage','door_count','seat_count','engine_displacement','engine_power']]
	car_y = car2['price_eur']

	lm1=sm.OLS(car_y,car_train)
	results_lm1=lm1.fit()
	results_lm1.summary()

	return results_lm1
