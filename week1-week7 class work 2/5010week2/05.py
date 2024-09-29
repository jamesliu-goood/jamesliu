
cover_price = 24.95 
discount = 0.40  
shipping_first_copy = 3.00  
shipping_additional_copy = 0.75  
num_copies = 60  

discounted_price = cover_price * (1 - discount)

total_book_price = discounted_price * num_copies

total_shipping_cost = shipping_first_copy + shipping_additional_copy * (num_copies - 1)

total_wholesale_cost = total_book_price + total_shipping_cost

print(f"The total wholesale cost for {num_copies} copies is: ${total_wholesale_cost}")
