import numpy_financial as npf
"""
fv()	Compute the future value.	numpy.fv(rate, nper, pmt, pv, when='end')[source]
pv()	Compute the present value.	numpy.pv(rate, nper, pmt, fv=0.0, when='end')
npv()	Returns the NPV (Net Present Value) of a cash flow series.	numpy.npv(rate, values)
pmt()	Compute the payment against loan principal plus interest.	numpy.pmt(rate, nper, pv, fv=0, when='end')
ppmt()	Compute the payment against loan principal.	numpy.ppmt(rate, per, nper, pv, fv=0.0, when='end')
ipmt	Compute the interest portion of a payment.	numpy.ipmt(rate, per, nper, pv, fv=0.0, when='end')
irr	The (IRR) function return the Internal Rate of Return.	numpy.irr(values)
mirr	Modified internal rate of return.	numpy.mirr(values, finance_rate, reinvest_rate)
nper()	Compute the number of periodic payments.	numpy.nper(rate, pmt, pv, fv=0, when='end')
rate()	Compute the rate of interest per period.	numpy.rate(nper, pmt, pv, fv, when='end', guess=0.1, tol=1e-06, maxiter=100)
    
"""

# First we try to compute the Feture value
""" 
Let's assume you invest $1000 for 5 years at an annual return rate of 8%.
We need to calculate how much our investment will be worth after 5 years.
"""

# res = npf.fv(rate=0.08, nper=5, pmt=0, pv=-1000)
# print(res)

""" 
What is the future value after 10 years of saving $200 now, with an additional 
monthly savings of $200. Assume the interest rate is 6% (annually) compounded monthly?
"""
# res=npf.fv(rate=0.06/12,nper=10*12,pmt=-200,pv=-200)
# print(res)
import pandas as pd 
x = [4, 5, 2, 1]
s = pd.Series(x)
print(s[3])


