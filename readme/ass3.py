unique_booking_id = 20000

class BookingSystem:
  
    all_bookings = []
    approved_bookings = 0
    pending_bookings = 0
    not_approved_bookings = 0

    def __init__(self, id_number, passenger_name, id_type):
       
        global unique_booking_id
        self.id_type = id_type
        self.id_number = id_number
        self.passenger_name = passenger_name
        self.ticket_id = unique_booking_id
        unique_booking_id += 1
        self.total_cost = 0
        self.status = "pending"
        self.approval_reference_number = None
        BookingSystem.all_bookings.append(self)

    def customer_info(self):
        
        print(f"Customer Info Submitted:\nID Type: {self.id_type}\nID Number: {self.id_number}\nPassenger Name: {self.passenger_name}")

    def ferry_service_details(self):
      
        service_name = input("Enter the ferry service name: ")
        try:
            service_price = float(input(f"Enter the price for {service_name}: $"))
        except ValueError:
            print("Invalid price entered. Please enter a numeric value.")
            return

        self.total_cost = service_price
        print(f"Service Requested: {service_name}\nTotal Cost: ${self.total_cost}")
        return self.total_cost

    def booking_approval(self, approval_reference_number, decision):
       
        if decision.lower() == "approved":
            self.status = "approved"
            BookingSystem.approved_bookings += 1
        elif decision.lower() == "not approved":
            self.status = "not approved"
            BookingSystem.not_approved_bookings += 1
        else:
            self.status = "pending"
            BookingSystem.pending_bookings += 1

        self.approval_reference_number = approval_reference_number
        print(f"Booking {self.ticket_id} Status: {self.status}\nApproval Reference: {self.approval_reference_number}")

    @classmethod
    def display_booking_info(cls):
     
        print("\n--- Displaying Booking Information ---")
        for booking in cls.all_bookings:
            print(f"""
            ID Type: {booking.id_type}
            ID Number: {booking.id_number}
            Passenger Name: {booking.passenger_name}
            Ticket ID: {booking.ticket_id}
            Total Cost: ${booking.total_cost}
            Status: {booking.status}
            Approval Reference Number: {booking.approval_reference_number}
            """)

    @classmethod
    def booking_statistics(cls):
     
        print("\n--- Booking Statistics ---")
        print(f"Total number of bookings submitted: {len(cls.all_bookings)}")
        print(f"Total number of approved bookings: {cls.approved_bookings}")
        print(f"Total number of pending bookings: {cls.pending_bookings}")
        print(f"Total number of not approved bookings: {cls.not_approved_bookings}")


booking1 = BookingSystem("PAX123", "Emily Clark", "Driver's License")
booking1.customer_info()
booking1.ferry_service_details()
booking1.booking_approval("P20KF", "pending")

booking2 = BookingSystem("PAX124", "John Doe", "Passport")
booking2.customer_info()
booking2.ferry_service_details()
booking2.booking_approval("P21KF", "approved")


BookingSystem.display_booking_info()

BookingSystem.booking_statistics()
