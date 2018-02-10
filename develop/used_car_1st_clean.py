#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:18:16 2018

@author: Willie
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
1. read in the original data and do some summary statistics
"""

car = pd.read_csv('/Users/Willie/Desktop/MSiA/Winter 2018/MSiA 423 Analytics Value Chain/used_cars.csv')
car.dtypes
car.describe()


"""
2. first manipulation of the data, taking out unusual mileage records and imputing NA's
"""
car['mileage']=car['mileage'].fillna(np.nanmedian(car['mileage']))
car['engine_displacement']=car['engine_displacement'].fillna(np.nanmedian(car['engine_displacement']))
car['engine_power']=car['engine_power'].fillna(np.nanmedian(car['engine_power']))
car=car[car.mileage<1000000]

car.door_count.value_counts()
car.seat_count.value_counts()

car['door_count']=pd.to_numeric(car['door_count'],errors="coerce")
car['seat_count']=pd.to_numeric(car['seat_count'],errors="coerce")
car['door_count']=car['door_count'].fillna(np.nanmedian(car['door_count']))
car['seat_count']=car['seat_count'].fillna(np.nanmedian(car['seat_count']))


"""
3. subset the data to get rid off weird values
"""
car=car[(car.seat_count<10) & (car.door_count<9)]
car=car[(~np.isnan(car.manufacture_year)) & (~pd.isnull(car.fuel_type)) & (~pd.isnull(car.body_type))]
car=car[car.manufacture_year>np.mean(car.manufacture_year)]

"""
4. now we have a total of about 470K cleaned data ==> write out
"""
car.to_csv("/Users/Willie/Desktop/MSiA/Winter 2018/MSiA 423 Analytics Value Chain/used_cars_new.csv")


"""
5. EDAs on some key predictors
"""
car.describe()
car.mileage.plot(kind="hist")
plt.xlabel("mileage")
plt.title("Histogram of Mileage")

car.engine_power.plot(kind="hist")
plt.xlabel("engine_power")
plt.title("Histogram of Engine_power")


car.body_type.value_counts().plot(kind="bar")
plt.title("Barplot of Body_type")
car.fuel_type.value_counts().plot(kind="bar")
plt.title("Barplot of Fuel_type")
car.door_count.value_counts().plot(kind="bar")
plt.title("Barplot of Door_count")
car.seat_count.value_counts().plot(kind="bar")
plt.title("Barplot of Seat_count")
car.manufacture_year.value_counts().plot(kind="bar")
plt.title("Barplot of Manufacture_year")



