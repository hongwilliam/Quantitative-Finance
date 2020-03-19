import cgitb
cgitb.enable()
import math
import numpy as np
import scipy

#sample Monte CArlo simulation of a European call option
#Basis is the Black-Scholes Model

#establish parameters
S0 = 100 #initial index level
K = 105 #strike price
T = 1.0 #time to maturity
r = 0.05 #risk free short interest rate
sigma = 0.2 #volatility
I = 100000 #number of simulations

#valuation algorithm
z = np.random.standard_normal(I)
ST = S0 * np.exp( (r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)
hT = np.maximum(ST - K, 0)
C0 = np.exp(-r * T) * np.sum(hT) / # IDEA:

print "Value of the European Call Option %5.3f" % C0
