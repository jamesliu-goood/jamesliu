item1 = 10
item2 = 20
item3 = 30
item1 = float(input("Enter the price for item1:"))
item2 = float(input("Enter the price for item2:"))
item3 = float(input("Enter the price for item3:"))


subTotal= item1 + item2 +item3
salesGST = subTotal * 0.15
total = subTotal + salesGST
print ("you purchase total is $", total,sep=)
