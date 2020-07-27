'''
#Without using Function - Print Tuple
Stock_Price = [('APPl',300),('MSFT',200),('Google',500)]
for item in Stock_Price:
    print(item)
#Unpacking Tuple and print Stock Name
Stock_Price = [('APPl',300),('MSFT',200),('Google',500)]
for itemName,Price in Stock_Price:
    print(itemName)
    print(Price)
'''
#How to retrun max stock price and name as tuple
Stock_Details = [('APPl',300),('MSFT',200),('Google',500)]
def find_expensive_stock(Stock_Details):
    current_price = 0
    name = ''
    for stockname,stockprice in Stock_Details:
        if current_price < stockprice:
            current_price = stockprice
            name = stockname
        else:
            pass
    return(name,current_price)
stockname,stockprice = find_expensive_stock(Stock_Details)
print(f'Expensive Stock is {stockname}')
print(f'And the price is {stockprice}')