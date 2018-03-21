#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def initial_clean():
	"""This function performs initial cleansing of the raw data and saves the new version used for training the model"""

	
	# 1. read in the original data and do some summary statistics
	# Note: The original data need to be downloaded from kaggle. The link can be found under README.md in the root directory.
	car = pd.read_csv('used_cars.csv')


	# 2. first manipulation of the data, taking out unusual mileage records and imputing NA's
	car['mileage']=car['mileage'].fillna(np.nanmedian(car['mileage']))
	car['engine_displacement']=car['engine_displacement'].fillna(np.nanmedian(car['engine_displacement']))
	car['engine_power']=car['engine_power'].fillna(np.nanmedian(car['engine_power']))
	car=car[car.mileage<1000000]

	car['door_count']=pd.to_numeric(car['door_count'],errors="coerce")
	car['seat_count']=pd.to_numeric(car['seat_count'],errors="coerce")
	car['door_count']=car['door_count'].fillna(np.nanmedian(car['door_count']))
	car['seat_count']=car['seat_count'].fillna(np.nanmedian(car['seat_count']))


	# 3. subset the data to get rid off weird values
	car=car[(car.seat_count<10) & (car.door_count<9)]
	car=car[(~np.isnan(car.manufacture_year)) & (~pd.isnull(car.fuel_type)) & (~pd.isnull(car.body_type))]
	car=car[car.manufacture_year>np.mean(car.manufacture_year)]


	# 4. now we have a total of about 470K cleaned data ==> write out
	car.to_csv("used_cars_new.csv")
	return 


if __name__ == '__main__':
	initial_clean()


