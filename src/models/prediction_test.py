#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import statsmodels.api as sm
from prediction import modelresult

def test_modelresult():

	dt = pd.DataFrame([{'mileage':5000,'engine_displacment':2000,'engine_power':150,'door_count':6,'seat_count':6}])

	pred=round(float(modelresult.predict(dt)),2)
	expected = 6102.52

	assert pred.equals(expected)

test_modelresult