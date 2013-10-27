import sys

def ebay(paid,sale):
	# input total amount spent
	paid2 = float(paid)

	# input the final sale price
	sale2 = float(sale)

	# find difference between amount price and final sale price

	totalprofit = sale2 - paid2

	# find out what archie's percentage is with 30% of the profit

	archiescut = sale2 * .30 

	# find out what my total sold amount is after archie takes his cut

	mytotal = sale2 - archiescut

	# find out what my total profit is after archie takes his cut (30 % of total sale price)

	myprofit = mytotal - paid2

	# find out what archie gets if he takes 30 % of the profit MARGIN

	archiescut2 = totalprofit * .30

	# find out what my total profit is if archie takes 30 % of the profit MARGIN

	myprofit2 = totalprofit - archiescut2

	print('you paid: %r' %paid2)
	print('-' * 50)
	print('it sold for: %r' %sale2)
	print('-' * 50)
	print('the difference between the purchase and sale price is: %r' %totalprofit)
	print('-' * 50)
	print('archies cut if he takes 30 percent of the TOTAL sale amount: %r' %archiescut)
	print('-' * 50)
	print('whats left over after archie takes his cut (30 percent of TOTAL PROFIT): %r' %mytotal)
	print('-' * 50)
	print('how much money i make when its all said and done (if archie keeps 30 percent of TOTAL): %r' %myprofit)
	print('-' * 50)
	print('how much money i make if archie keeps 30 percent of the profit MARGIN: %r' %myprofit2)
	print('-' * 50)
	if myprofit <= 50 or myprofit2 <= 50:
		print('you\'re not making any money if archie keeps 30 percent of the TOTAL profit')
	