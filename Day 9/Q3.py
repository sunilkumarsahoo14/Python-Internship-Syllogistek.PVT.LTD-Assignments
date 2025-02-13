#Q3.to calculate the discounted price of the product
original_price=float(input("enter the original price of the product:"))
discount_percent=int(input("enter the discount percentage:"))
def discount(original_price,discount_percent):
    #condition to calculate discounted price
    discounted_price=original_price-(original_price * discount_percent/100)
    return discounted_price
#print the result
print("the discounted price is:",discount(original_price,discount_percent))