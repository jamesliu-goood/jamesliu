def what_to_do_now():
    messge = "Time to"
    prompt = "Enter selection(1,2 or 3):"
    user_choice = int(input(prompt))

    if user_choice == 1:
        print(messge, "meat")
    elif user_choice == 2:
        print(messge, "Play")
    elif user_choice == 3:
        print(messge,"sleep")
    else:
        print("incorrect selection!")    

what_to_do_now()


