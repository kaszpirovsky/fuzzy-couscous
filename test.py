#!/usr/bin/python

import numpy as np

class CC(object):
	def __init__(self):
		pass

	def start(self):
		pass

# fast = 480
# slow = 1440

fast = 20
slow = 10

# prices_path = 'open_100_2.txt'
#prices = np.loadtxt(prices_path)

#output_path = 'output.csv'
#output      = np.loadtxt(output_path)

currencies_paths = {}
currencies_paths['IN'] = 'M5_USDJPY.csv'



def ma(n, path):
	prices = np.loadtxt(path)
	a = 2.0/(n+1)
	a_neg = 1.0 - a
	prev_ema = 0
	for i in xrange(0, len(prices)):
		ema = a*prices[i]+a_neg*prev_ema
		prev_ema = ema
		yield ema

		
def ema(n, s):
  #s = array(s)
  ema = []
  j = 1

  #get n sma first and calculate the next n period ema
  sma = sum(s[:n]) / n
  multiplier = 2 / float(1 + n)
  ema.append(sma)

  #EMA(current) = ( (Price(current) - EMA(prev) ) x Multiplier) + EMA(prev)
  ema.append(( (s[n] - sma) * multiplier) + sma)

  #now calculate the rest of the values
  for i in s[n+1:]:
      tmp = ( (i - ema[j]) * multiplier) + ema[j]
      j = j + 1
      ema.append(tmp)

  return ema


in_ma = ma(10, currencies_paths['IN'])

## in_test = ema(10, np.loadtxt(currencies_paths['IN']))

def start():
	limit = 70 #parameter
	arrUSD = []

	# double EURUSD_Fast = ma( StringConcatenate("EURUSD",endfx), Fast, MA_Method, Price, i);
	# double EURUSD_Slow = ma(StringConcatenate("EURUSD",endfx), Slow, MA_Method, Price, i);
	#MA_method = exponential
	# Price = OPEN
	# i = shift - przesuniecie wzgledem aktualnego numeru slupka (tzn ile wstecz)

	# fast_ema.next()
	# slow_ema.next()

	## if_fast = in_ma.next()


	for i in xrange(0, limit):

		in_fast = in_ma.next()

		

		print "%f,%f" % (np.loadtxt(currencies_paths['IN'])[i],in_fast)
		# arrUSD[i] = 0;
		# if(EUR) 
		#     arrUSD[i] += EURUSD_Slow - EURUSD_Fast;
		# eurusd_step = EURUSD_Slow - EURUSD_Fast
		# eurusd_step = EURUSD_Fast - EURUSD_Slow

    
start()
