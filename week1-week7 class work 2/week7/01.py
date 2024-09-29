         membership_counter = 1


class MembershipRegistrationSystem:
    def __init__(self):
        self.registered_members = []  
        self.withdrawn_members = []   

    def register_member(self):
        global membership_counter

   
        student_id = input("Enter Student ID: ").strip()
        last_name = input("Enter Student Last Name: ").strip()
        programme = input("Enter Student Programme (Diploma/Bachelor): ").strip().capitalize()

       
        membership_id = membership_counter
        membership_counter += 1


        member = {
            "Student ID": student_id,
            "Last Name": last_name,
            "Programme": programme,
            "Membership ID": membership_id
        }
        self.registered_members.append(member)
        print(f"Student {last_name} has been successfully registered with Membership ID: {membership_id}.")

    
    def withdraw_member(self):
       
        membership_id = int(input("Enter Membership ID: ").strip())
        last_name = input("Enter Student Last Name: ").strip()

        
        for member in self.registered_members:
            if member["Membership ID"] == membership_id and member["Last Name"].lower() == last_name.lower():
               
                self.registered_members.remove(member)
                self.withdrawn_members.append(member)
                print(f"Student {last_name} has been successfully withdrawn.")
                return
        
        
        print("Member not found. Please check the Membership ID and Last Name.")

    
    def display_members(self):
        
        num_registered = len(self.registered_members)
        num_withdrawn = len(self.withdrawn_members)

        
        num_diploma = sum(1 for member in self.registered_members if member["Programme"] == "Diploma")
        num_bachelor = sum(1 for member in self.registered_members if member["Programme"] == "Bachelor")

        
        print("\nMembership Statistics:")
        print(f"Number of registered members: {num_registered}")
        print(f"Number of students in the Diploma programme: {num_diploma}")
        print(f"Number of students in the Bachelor programme: {num_bachelor}")
        print(f"Number of students who have withdrawn their membership: {num_withdrawn}")

club_system = MembershipRegistrationSystem()


while True:
    print("\nMenu:")
    print("1. Register a Member")
    print("2. Withdraw a Member")
    print("3. Display Members Statistics")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == '1':
        club_system.register_member()
    elif choice == '2':
        club_system.withdraw_member()
    elif choice == '3':
        club_system.display_members()
    elif choice == '4':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
