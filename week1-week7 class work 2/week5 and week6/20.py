
ticket_counter = 1
def custumerBooking(self):
    global ticket_counter  
    id_type = input("Type of ID (passport, driver's license): ").strip()
    id_number = input("ID Number: ").strip()
    passenger_name = input("Passenger Names: ").strip()

   
    ticket_id = 20000 + ticket_counter
    ticket_counter += 1  

    print("\nBooking Confirmation:")
    print(f" ID Type:{id_type}")
    print(f"ID Number: {id_number}")
    print(f"Passenger Names: {passenger_name}")
    print(f"Ticket ID: {ticket_id}")


    return {
        'Ticket ID':20002,
        'Passenger Name':'Emily clark',
        'ID Number':'PAX123',
    }


booking_info = custumerBooking()
print("\nReturned Data:", booking_info)





