class RequestSystem:
    def __init__(self):
        self.requests = [] 
        self.counter = 1    
    
    def user_info(self):
        name = input("Enter your name: ").strip()
        age = input("Enter your age: ").strip()
        email = input("Enter your email: ").strip()
        user_details = {"Name": name, "Age": age, "Email": email}
        return user_details

   
    def request_details(self):
        total_amount = 0
        items = []

        while True:
            item = input("Enter the service/item name (or type 'done' to finish): ").strip()
            if item.lower() == 'done':
                break
            cost = float(input(f"Enter the cost for {item}: ").strip())
            items.append({"Item": item, "Cost": cost})
            total_amount += cost

        return total_amount, items

  
    def request_approval(self, total_amount):
        if total_amount < 150:
            return "Approved"
        else:
            return "Pending"

   
    def respond_request(self, request_id):
        for request in self.requests:
            if request["ID"] == request_id and request["Status"] == "Pending":
                response = input(f"Do you want to approve request ID {request_id}? (yes/no): ").strip().lower()
                if response == 'yes':
                    request["Status"] = "Approved"
                else:
                    request["Status"] = "Not Approved"
                print(f"Request ID {request_id} has been updated to {request['Status']}.")
                return
        print("Request not found or already processed.")

   
    def display_request(self):
        print("\nDisplaying All Requests:")
        for request in self.requests:
            print(f"Name: {request['User']['Name']}, ID: {request['ID']}, Total: ${request['Total']}, Status: {request['Status']}")

    
    def request_statistic(self):
        total_requests = len(self.requests)
        approved_requests = sum(1 for req in self.requests if req["Status"] == "Approved")
        pending_requests = sum(1 for req in self.requests if req["Status"] == "Pending")
        not_approved_requests = sum(1 for req in self.requests if req["Status"] == "Not Approved")

        print("\nRequest Statistics:")
        print(f"Total number of requests submitted: {total_requests}")
        print(f"Total number of approved requests: {approved_requests}")
        print(f"Total number of pending requests: {pending_requests}")
        print(f"Total number of not approved requests: {not_approved_requests}")

    
    def create_request(self):
        user = self.user_info()
        total_amount, items = self.request_details()
        status = self.request_approval(total_amount)

        request = {
            "ID": self.counter,
            "User": user,
            "Items": items,
            "Total": total_amount,
            "Status": status
        }
        self.requests.append(request)
        self.counter += 1

        print(f"Request ID {request['ID']} has been submitted with status: {request['Status']}.")


request_system = RequestSystem()

while True:
    print("\nMenu:")
    print("1. Submit a New Request")
    print("2. Respond to a Request")
    print("3. Display All Requests")
    print("4. Display Request Statistics")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == '1':
        request_system.create_request()
    elif choice == '2':
        request_id = int(input("Enter the Request ID to respond to: ").strip())
        request_system.respond_request(request_id)
    elif choice == '3':
        request_system.display_request()
    elif choice == '4':
        request_system.request_statistic()
    elif choice == '5':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
