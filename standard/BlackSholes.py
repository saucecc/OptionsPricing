import numpy as np 
from scipy.stats import norm 

from PricingModel import PricingModel

class BlackSholes(PricingModel): 
    def init(self, underlying_spot, strike, to_maturity, rf, vol): 

