#Q2.calculate total price per product
#input the data
prod_qty=[13,5,6,10,11]
prices=[1.2,6.5,1.0,4.8,5.0]

#calculate total price 
total_price_per_product=[prod_qty[i]*prices[i] for i in range (len(prod_qty))]
#total prices
total_price=sum(total_price_per_product)
#print the result
print(total_price)