1. Encapsulation

The class BookingSystem has encapsulated attributes (e.g., id_type, id_number, passenger_name, etc.), ensuring that the booking's details are grouped and stored inside each instance of the class.
Methods like customer_info(), ferry_service_details(), and booking_approval() allow controlled access to the object's data and operations without exposing them directly to external code.

Use getter and setter methods instead of directly accessing class attributes (like all_bookings, approved_bookings, etc.) at the class level. This provides better encapsulation and more control over how data is manipulated.
2. Abstraction
The BookingSystem class hides the complex logic of handling bookings and approvals inside methods. Consumers of the class only need to interact with simple method calls (like booking_approval() or ferry_service_details()), without needing to know the underlying details.
Further abstraction could be achieved by creating specialized classes for related concepts like a FerryService class. This would make the system more modular.

3. Single Responsibility Principle (SRP)
The BookingSystem class is responsible for too many things. It's handling:
Booking details and approval statuses.
Displaying customer information.
Managing ferry service details.
Handling booking statistics.
This violates the SRP because one class should ideally have only one responsibility.

Split responsibilities into multiple classes. For example:
A Booking class to handle individual bookings.
A BookingManager class for overall booking system statistics and management.
A Service or FerryService class to handle ferry service details separately.

4. Open/Closed Principle (OCP)
The class design is not easily extendable without modifying existing code. For example, adding a new type of booking or different services might require significant changes to the BookingSystem class.\
The system can be refactored to be open for extension but closed for modification by using inheritance or interfaces. For instance, a base Service class can be extended by multiple specific services like FerryService, FlightService, etc.

5. Liskov Substitution Principle (LSP)
Since no inheritance is used, this principle is not applicable at this point. However, in case of future subclasses (e.g., FerryBooking, FlightBooking), they should ensure that they can replace BookingSystem without altering the program’s correctness.

6. Interface Segregation Principle (ISP)

The current BookingSystem class exposes many methods (customer_info(), ferry_service_details(), booking_approval()) that are not always relevant to every context.

Consider splitting the interface into smaller, more focused interfaces (e.g., CustomerInfoProvider, ServiceDetailsHandler, etc.), which clients can implement according to their needs.
7. Dependency Inversion Principle (DIP)

The BookingSystem class directly handles input (e.g., ferry_service_details() takes user input), which can make the class harder to test and more tightly coupled to the user interface.

Introduce dependency injection or separate UI/input handling from the logic by passing inputs to methods via parameters instead of requesting them from within the class.
8. DRY Principle (Don’t Repeat Yourself)

The class minimizes repeated code for handling multiple bookings and approvals by using class variables and methods.

Some methods like ferry_service_details() could benefit from modularizing input validation, so the error handling for invalid price entries can be reused elsewhere.
9. Cohesion

The class lacks cohesion since it handles too many responsibilities, from managing bookings to calculating costs and processing user inputs.

Split responsibilities into smaller, highly cohesive classes that only do one thing.
10. Coupling

The methods inside BookingSystem are tightly coupled to one another. For example, booking_approval() modifies class-level counters (approved_bookings, pending_bookings), which leads to global state management.

Reduce coupling by managing such state transitions inside specialized classes that can track booking statistics independently.
Refactoring Suggestions
A better design could involve splitting this class into the following:


