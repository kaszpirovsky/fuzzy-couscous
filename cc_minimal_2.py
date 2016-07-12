
#!/bin/bash/python

import numpy as np

class CC(object):
	def __init__(self):
		pass

	def start(self):
		pass

# fast = 480
# slow = 1440

fast = 100
slow = 500

# prices_path = 'open_100_2.txt'
#prices = np.loadtxt(prices_path)

output_path = 'M5_CC_USD.csv'
output      = np.loadtxt(output_path)



USD=1
EUR=1
GBP=1
CHF=1
JPY=1
AUD=1
CAD=1
NZD=1
calcUSD=1
calcEUR=1
calcGBP=1
calcCHF=1
calcJPY=1
calcAUD=1
calcCAD=1
calcNZD=1

currencies_paths = {}
currencies_paths['AUDUSD'] = 'M5_AUDUSD.csv'
currencies_paths['EURUSD'] = 'M5_EURUSD.csv'
currencies_paths['GBPUSD'] = 'M5_GBPUSD.csv'
currencies_paths['NZDUSD'] = 'M5_NZDUSD.csv'
currencies_paths['USDCAD'] = 'M5_USDCAD.csv'
currencies_paths['USDCHF'] = 'M5_USDCHF.csv'
currencies_paths['USDJPY'] = 'M5_USDJPY.csv'


def ma(n, path):
	prices = np.loadtxt(path)
	a = 2.0/(n+1)
	a_neg = 1.0 - a
	prev_ema = 0
	for i in xrange(0, len(prices)):
		ema = a*prices[i]+a_neg*prev_ema
		prev_ema = ema
		yield ema
		

def cc(ma=1,price=0,fast=100,slow=200,USD=1,EUR=1,GBP=1,CHF=1,JPY=1,AUD=1,CAD=1,NZD=1,calcUSD=1,calcEUR=1,calcGBP=1,
        calcCHF=1,calcJPY=1,calcAUD=1,calcCAD=1,calcNZD=1,bar=0):
	print x
	
	

def start():
	limit = len(output) ##1000  #parameter
	
	arrUSD = []
	arrEUR = []
	arrGBP = []
	arrJPY = []	
	arrCHF = []
	arrAUD = []
	arrCAD = []
	arrNZD = []
		
	if(EUR):
		EURUSD_Fast_ma = ma(fast, currencies_paths['EURUSD'])
		EURUSD_Slow_ma = ma(slow, currencies_paths['EURUSD'])

	if(GBP):
		GBPUSD_Fast_ma = ma(fast, currencies_paths['GBPUSD'])
		GBPUSD_Slow_ma = ma(slow, currencies_paths['GBPUSD'])

	if(CHF):
		USDCHF_Fast_ma = ma(fast, currencies_paths['USDCHF'])
		USDCHF_Slow_ma = ma(slow, currencies_paths['USDCHF'])
	
	if(JPY):
		USDJPY_Fast_ma = ma(fast, currencies_paths['USDJPY'])
		USDJPY_Slow_ma = ma(slow, currencies_paths['USDJPY'])
  
	if(AUD):
		AUDUSD_Fast_ma = ma(fast, currencies_paths['AUDUSD'])
		AUDUSD_Slow_ma = ma(slow, currencies_paths['AUDUSD'])

	if(CAD):
		USDCAD_Fast_ma = ma(fast, currencies_paths['USDCAD'])
		USDCAD_Slow_ma = ma(slow, currencies_paths['USDCAD'])

	if(NZD):
		NZDUSD_Fast_ma = ma(fast, currencies_paths['NZDUSD'])
		NZDUSD_Slow_ma = ma(slow, currencies_paths['NZDUSD'])

  
	for i in xrange(0, limit):
		if(EUR):
			EURUSD_Fast = EURUSD_Fast_ma.next()
			EURUSD_Slow = EURUSD_Slow_ma.next()

		if(GBP):
			GBPUSD_Fast = GBPUSD_Fast_ma.next()
			GBPUSD_Slow = GBPUSD_Slow_ma.next()

		if(AUD):
			AUDUSD_Fast = AUDUSD_Fast_ma.next()
			AUDUSD_Slow = AUDUSD_Slow_ma.next()
			
		if(NZD):
			NZDUSD_Fast = NZDUSD_Fast_ma.next()
			NZDUSD_Slow = NZDUSD_Slow_ma.next()
			
		if(CHF):
			USDCHF_Fast = USDCHF_Fast_ma.next()
			USDCHF_Slow = USDCHF_Slow_ma.next()
			
		if(CAD):
			USDCAD_Fast = USDCAD_Fast_ma.next()
			USDCAD_Slow = USDCAD_Slow_ma.next()
			
		if(JPY):
			USDJPY_Fast = USDJPY_Fast_ma.next()/100.0
			USDJPY_Slow = USDJPY_Slow_ma.next()/100.0
   

		if(calcUSD):
			arrUSD_tmp = 0
			if(EUR): arrUSD_tmp += EURUSD_Slow-EURUSD_Fast
			if(GBP): arrUSD_tmp += GBPUSD_Slow-GBPUSD_Fast
			if(CHF): arrUSD_tmp += USDCHF_Fast-USDCHF_Slow
			if(JPY): arrUSD_tmp += USDJPY_Fast-USDJPY_Slow	      
			if(AUD): arrUSD_tmp += AUDUSD_Slow-AUDUSD_Fast
			if(CAD): arrUSD_tmp += USDCAD_Fast-USDCAD_Slow
			if(NZD): arrUSD_tmp += NZDUSD_Slow-NZDUSD_Fast
			arrUSD.append(arrUSD_tmp)
			
			
		if(calcEUR):
			arrEUR_tmp = 0
			if(USD): arrEUR_tmp += EURUSD_Fast-EURUSD_Slow
			if(GBP): arrEUR_tmp += EURUSD_Fast/GBPUSD_Fast-EURUSD_Slow/GBPUSD_Slow
			if(CHF): arrEUR_tmp += EURUSD_Fast*USDCHF_Fast-EURUSD_Slow*USDCHF_Slow
			if(JPY): arrEUR_tmp += EURUSD_Fast*USDJPY_Fast-EURUSD_Slow*USDJPY_Slow
			if(AUD): arrEUR_tmp += EURUSD_Fast/AUDUSD_Fast-EURUSD_Slow/AUDUSD_Slow		  
			if(CAD): arrEUR_tmp += EURUSD_Fast*USDCAD_Fast-EURUSD_Slow*USDCAD_Slow
			if(NZD): arrEUR_tmp += EURUSD_Fast/NZDUSD_Fast-EURUSD_Slow/NZDUSD_Slow
			arrEUR.append(arrEUR_tmp)

		if(calcGBP):
			arrGBP_tmp = 0
			if(USD): arrGBP_tmp += GBPUSD_Fast - GBPUSD_Slow
			if(EUR): arrGBP_tmp += EURUSD_Slow / GBPUSD_Slow - EURUSD_Fast / GBPUSD_Fast
			if(CHF): arrGBP_tmp += GBPUSD_Fast*USDCHF_Fast - GBPUSD_Slow*USDCHF_Slow
			if(JPY): arrGBP_tmp += GBPUSD_Fast*USDJPY_Fast - GBPUSD_Slow*USDJPY_Slow
			if(AUD): arrGBP_tmp += GBPUSD_Fast / AUDUSD_Fast - GBPUSD_Slow / AUDUSD_Slow	  
			if(CAD): arrGBP_tmp += GBPUSD_Fast*USDCAD_Fast - GBPUSD_Slow*USDCAD_Slow
			if(NZD): arrGBP_tmp += GBPUSD_Fast / NZDUSD_Fast - GBPUSD_Slow / NZDUSD_Slow
			arrGBP.append(arrGBP_tmp)	

		if(calcCHF):
			arrCHF_tmp = 0
			if(USD): arrCHF_tmp += USDCHF_Slow - USDCHF_Fast
			if(EUR): arrCHF_tmp += EURUSD_Slow*USDCHF_Slow - EURUSD_Fast*USDCHF_Fast
			if(GBP): arrCHF_tmp += GBPUSD_Slow*USDCHF_Slow - GBPUSD_Fast*USDCHF_Fast
			if(JPY): arrCHF_tmp += USDJPY_Fast / USDCHF_Fast - USDJPY_Slow / USDCHF_Slow
			if(AUD): arrCHF_tmp += AUDUSD_Slow*USDCHF_Slow - AUDUSD_Fast*USDCHF_Fast
			if(CAD): arrCHF_tmp += USDCHF_Slow / USDCAD_Slow - USDCHF_Fast / USDCAD_Fast
			if(NZD): arrCHF_tmp += NZDUSD_Slow*USDCHF_Slow - NZDUSD_Fast*USDCHF_Fast
			arrCHF.append(arrCHF_tmp)

		if(calcJPY):
			arrJPY_tmp = 0
			if(USD): arrJPY_tmp += USDJPY_Slow - USDJPY_Fast
			if(EUR): arrJPY_tmp += EURUSD_Slow*USDJPY_Slow - EURUSD_Fast*USDJPY_Fast
			if(GBP): arrJPY_tmp += GBPUSD_Slow*USDJPY_Slow - GBPUSD_Fast*USDJPY_Fast
			if(CHF): arrJPY_tmp += USDJPY_Slow / USDCHF_Slow - USDJPY_Fast / USDCHF_Fast
			if(AUD): arrJPY_tmp += AUDUSD_Slow*USDJPY_Slow - AUDUSD_Fast*USDJPY_Fast
			if(CAD): arrJPY_tmp += USDJPY_Slow / USDCAD_Slow - USDJPY_Fast / USDCAD_Fast
			if(NZD): arrJPY_tmp += NZDUSD_Slow*USDJPY_Slow - NZDUSD_Fast*USDJPY_Fast
			arrJPY.append(arrJPY_tmp)
	
		if(calcAUD):
			arrAUD_tmp = 0
			if(USD): arrAUD_tmp += AUDUSD_Fast - AUDUSD_Slow
			if(EUR): arrAUD_tmp += EURUSD_Slow / AUDUSD_Slow - EURUSD_Fast / AUDUSD_Fast
			if(GBP): arrAUD_tmp += GBPUSD_Slow / AUDUSD_Slow - GBPUSD_Fast / AUDUSD_Fast
			if(CHF): arrAUD_tmp += AUDUSD_Fast*USDCHF_Fast - AUDUSD_Slow*USDCHF_Slow
			if(JPY): arrAUD_tmp += AUDUSD_Fast*USDJPY_Fast - AUDUSD_Slow*USDJPY_Slow
			if(CAD): arrAUD_tmp += AUDUSD_Fast*USDCAD_Fast - AUDUSD_Slow*USDCAD_Slow
			if(NZD): arrAUD_tmp += AUDUSD_Fast / NZDUSD_Fast - AUDUSD_Slow / NZDUSD_Slow
			arrAUD.append(arrAUD_tmp)

		if(calcCAD):
			arrCAD_tmp = 0
			if(USD): arrCAD_tmp += USDCAD_Slow - USDCAD_Fast;
			if(EUR): arrCAD_tmp += EURUSD_Slow*USDCAD_Slow - EURUSD_Fast*USDCAD_Fast;
			if(GBP): arrCAD_tmp += GBPUSD_Slow*USDCAD_Slow - GBPUSD_Fast*USDCAD_Fast
			if(CHF): arrCAD_tmp += USDCHF_Fast / USDCAD_Fast - USDCHF_Slow / USDCAD_Slow
			if(JPY): arrCAD_tmp += USDJPY_Fast / USDCAD_Fast - USDJPY_Slow / USDCAD_Slow
			if(AUD): arrCAD_tmp += AUDUSD_Slow*USDCAD_Slow - AUDUSD_Fast*USDCAD_Fast 
			if(NZD): arrCAD_tmp += NZDUSD_Slow*USDCAD_Slow - NZDUSD_Fast*USDCAD_Fast
			arrCAD.append(arrCAD_tmp)
  
                            			
		if(calcNZD):
			arrNZD_tmp = 0
			if(USD): arrNZD_tmp += NZDUSD_Fast - NZDUSD_Slow
			if(EUR): arrNZD_tmp += EURUSD_Slow / NZDUSD_Slow - EURUSD_Fast / NZDUSD_Fast
			if(GBP): arrNZD_tmp += GBPUSD_Slow / NZDUSD_Slow - GBPUSD_Fast / NZDUSD_Fast
			if(CHF): arrNZD_tmp += NZDUSD_Fast*USDCHF_Fast - NZDUSD_Slow*USDCHF_Slow
			if(JPY): arrNZD_tmp += NZDUSD_Fast*USDJPY_Fast - NZDUSD_Slow*USDJPY_Slow
			if(AUD): arrNZD_tmp += AUDUSD_Slow / NZDUSD_Slow - AUDUSD_Fast / NZDUSD_Fast
			if(CAD): arrNZD_tmp += NZDUSD_Fast*USDCAD_Fast - NZDUSD_Slow*USDCAD_Slow
			arrNZD.append(arrNZD_tmp)		
			
		print "%i : %f : %f \n "%(i, arrUSD[i], output[i])
	print "U=%f, E=%f, G=%f, C=%f, J=%f, A=%f, D=%f, N=%f \n "%(arrUSD[-1],arrEUR[-1],arrGBP[-1],arrCHF[-1],arrJPY[-1],arrAUD[-1],arrCAD[-1],arrNZD[-1])
		
		
	

start()

