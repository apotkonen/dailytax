#!/usr/bin/env python3

# Distribution Fitting Python file: difi.py

# If all needed packages are't available for your host nor you haven't rights,
# consider using virtual environment setup with "python3-virtualenv"-package
# and then install needed extra components to virtual python3 setup.

# Import python packages, modules and functions
import numpy as np # python3-numpy
import pandas as pd # python3-pandas
import seaborn as sns # python3-seaborn
import matplotlib as mpl # python3-matplotlib
import matplotlib.pyplot as plt # plt.subplots() plt.figure() plt.show()
from scipy import stats # python3-scipy
# install python3-all, python3-virtualenv and then fitter and distfit under it.
from fitter import Fitter, get_common_distributions, get_distributions
from distfit import distfit #dfit.plot() dfit.lineplot() dfit.qqplot(X) dfit.plot_summary()
# Be sure that you explicitly call virtual environment python3 if you had to use virtual.
# See also python3-venv and pipx as another way to create needed componet configuration.

# Read dataset using pandas package
df = pd.read_csv("data_cut.csv")
#df = pd.read_csv("datafull.csv")
X = df["Eur/d"].values
Y = df["1k/Eur"].values
#df.info()

# Print fitter package supported distributions
#print(get_distributions())

# References to distributions documentation to limit fitted distributions
# to data and current problem area nature matching distributions by hand:
#http://wikipedia.org/wiki/Probability_density_function
#http://wikipedia.org/wiki/List_of_probability_distributions
#http://wikipedia.org/wiki/List_of_probability_distributions#Supported_on_semi-infinite_intervals,_usually_[0,%E2%88%9E)
#http://wikipedia.org/wiki/Gini_coefficient#Continuous_probability_distribution
#http://stats.stackexchange.com/questions/595964/fisk-distribution-in-scipy
#'fisk'     http://wikipedia.org/wiki/Log-logistic_distribution
#'johnsonsu'http://wikipedia.org/wiki/Johnson%27s_SU-distribution
#'burr'     http://wikipedia.org/wiki/Burr_distribution
# Limit tested distributions to few well behaving candidates:
#dists=['burr','fisk','johnsonsu']
#dists=['fisk','johnsonsu']
dists=['fisk']

# Due that both distribution fitting packages utilize same distribution names
# Let both packages Fitter and Distfit to do they work for distributions list
# "dists" and utilize results then by hand as you wish.

# Fitter package fitting
#f = Fitter(df)
f = Fitter(df, distributions=dists)
f.fit()
print(f.summary(Nbest=33))
print(f.fitted_param)

# Distfit package fitting
#dfit = distfit(stats='RSS')
dfit = distfit(stats='RSS', distr=dists)
dfit.fit_transform(X)
#dfit.predict(y)
dfit.plot_summary()
fig, ax = dfit.plot(chart='pdf')
fig, ax = dfit.plot(chart='cdf')
plt.show()

# References to documentation:
#http://fitter.readthedocs.io
#http://pypi.org/project/fitter
#http://wasyresearch.com/tutorial-python-for-fitting-gaussian-distribution-on-data
#http://stackoverflow.com/questions/37559470/what-do-all-the-distributions-available-in-scipy-stats-look-like
#http://medium.com/the-researchers-guide/finding-the-best-distribution-that-fits-your-data-using-pythons-fitter-library-319a5a0972e9
#http://github.com/erdogant/distfit/blob/master/distfit/examples.py
#http://erdogant.github.io/distfit/pages/html/Abstract.html
#http://erdogant.github.io/distfit/pages/html/Plots.html
#http://erdogant.github.io/distfit
#http://seaborn.pydata.org
