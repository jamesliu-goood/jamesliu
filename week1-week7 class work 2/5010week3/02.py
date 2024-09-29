def get_price(child, adult):
    child_price = 10
    adult_price = 25
    group_size = 14
    group_rate = 0.9

    cost = (child * child_price + adult * adult_price)

    if child + adult > group_size:
        cost = cost * group_size
    return cost 
def main():
    num_child = int(input("Enter the number of childern"))   
    num_adult = int(input("Enter the number of adults"))
    cost = get_price(num_child,num_adult)
    print("The cost of your tickets is : $ "+ str(cost)) 
