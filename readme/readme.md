

The `BookingSystem` class is designed to manage bookings for ferry services. It stores booking details, customer information, service costs, and allows for approval or rejection of bookings. The class also provides statistics and allows viewing all booking information.

- **Customer Information**: Store passenger's name, ID type, and ID number.
- **Ferry Service Details**: Accept ferry service name and cost, and calculate the total cost for the booking.
- **Booking Approval**: Set the status of a booking as 'approved', 'not approved', or 'pending'.
- **Display Bookings**: Display all bookings and their details.
- **Statistics**: Show total number of bookings, including approved, pending, and not approved bookings.

- **Class Attributes**:
  - `all_bookings`: List containing all the bookings created.
  - `approved_bookings`: Count of bookings with an 'approved' status.
  - `pending_bookings`: Count of bookings with a 'pending' status.
  - `not_approved_bookings`: Count of bookings with a 'not approved' status.

- **Instance Attributes**:
  - `id_type`: Type of ID used for the booking (e.g., Passport, Driver's License).
  - `id_number`: Unique identification number.
  - `passenger_name`: Name of the passenger.
  - `ticket_id`: Unique ticket ID generated for the booking.
  - `total_cost`: Total cost of the ferry service.
  - `status`: Current status of the booking (approved, not approved, or pending).
  - `approval_reference_number`: Reference number provided when the booking is approved.


Initializes a new booking with customer information.


Prints the customer information that has been submitted.

Accepts ferry service name and its price as input and calculates the total cost for the booking. Returns the total cost.


Changes the booking status to either 'approved', 'not approved', or 'pending' based on the decision provided. Increments the appropriate class-level booking count.


Displays all bookings with their details including ID type, ID number, passenger name, ticket ID, total cost, booking status, and approval reference number.


Displays statistics about the bookings, including total number of bookings, number of approved bookings, pending bookings, and not approved bookings.


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



