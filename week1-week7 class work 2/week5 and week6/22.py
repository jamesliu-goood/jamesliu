
ticket_counter = 1

def customerBooking():
    global ticket_counter  

    id_type = input("Type of ID (passport, driver's license): ").strip()
    id_number = input("ID Number: ").strip()
    passenger_name = input("Passenger Names: ").strip()

    ticket_id = 20000 + ticket_counter
    ticket_counter += 1  
    return {
        'ID Type': id_type,
        'ID Number': id_number,
        'Passenger Name': passenger_name,
        'Ticket ID': ticket_id
    }

def ferry_total():
   
    total_cost = 0

    print("\nEnter each service and its cost (type 'done' to finish):")
    while True:
        service = input("Enter service name with price (e.g., Food $50): ").strip()
        
        if service.lower() == 'done':
            break
    return total_cost

def display_booking():
   
    booking_info = customerBooking()
    
    total_cost = ferry_total()
    
   
    approval_reference = f"{booking_info['ID Number']}{booking_info['Ticket ID']}"


    print("\nPrinting booking:")
    print(f"From of ID (passport, driver's license): {booking_info['ID Type']}")
    print(f"ID Number: {booking_info['ID Number']}")
    print(f"Passenger Names: {booking_info['Passenger Name']}")
    print(f"Ticket ID: {booking_info['Ticket ID']}")
    print(f"Total: ${total_cost:.2f}")
    print("Status:")
    print("Approved")
    print(f"Approval Reference Number: {approval_reference}")

display_booking()
