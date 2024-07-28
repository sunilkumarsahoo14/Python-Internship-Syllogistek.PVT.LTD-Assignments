#Q1.print name of all the products with price higher than 10
products=[{'name':'orange','price':20},{'name':'apple','price':8},
          {'name':'banana','price':10},{'name':'kiwi','price':30}]
#condition to print products with price higher than 10
for p in products:
    if p['price']>10:
        #print result
        print(p['name'])