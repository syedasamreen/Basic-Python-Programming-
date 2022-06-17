price = 2000
quantity = 5
if price > 1000:
    print("price is less then 1000")
    print("price = ", price)
    print("quantity = ", quantity)
 
 
 
if price*quantity < 500:
     print("price is less then 1000")
     print("price = ", price)
     print("quantity = ", quantity)
###


price = 100

if price > 100:
 print("price is greater than 100")

if price == 100:
  print("price is 100")

if price < 100:
    print("price is less than 100")   
    
###

if price >=100:
    print("price is GT 100")
else:
    print("price is = 100")
    
    
## 
if price >100:
    print("price is greater than 100")

elif price == 100:
    print("price is equal to 100")

elif price <100:
    print("price is less then 100")
    
##
if price >100:
    print("price is GT 100")
elif price == 100:
    print("price is equal to 150")
else:
    print("price is LT 150")
    
##
prc = 50
qt = 5
amt = prc * qt

if amt > 100:
    if amt >500:
        print("amount is GT 500")
    else:
        if amt <500 and amt >400:
            print("amt is")
        elif amt < 500 and amt >300:
            print("amt is between 300 and 500")
        else:
            print("amt is between 200 and 500")
elif amt ==100:
     print("amt is 100")
else:
    print("amount is less than 100")
