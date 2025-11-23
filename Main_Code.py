print("------ Hostel Hygiene & Health Monitoring System ------")

complaints = []

# ----------- FUNCTIONS -----------
def show_menu():
    print("\n1. Report a Hygiene Problem")
    print("2. View All Reports")
    print("3. Hygiene Risk Analytics")
    print("4. Exit")

def add_complaint():
    print("\n--- Report a Hygiene Problem ---")
    category = input("Enter category (Water/Food/Washroom/Room/Mosquito/Other): ")
    description = input("Enter short description of the problem: ")

    complaint = {
        "category": category,
        "description": description
    }

    complaints.append(complaint)
    print("\n Congratulation Complaint Added Successfully!")

def view_complaints():
    print("\n--- All Hygiene Complaints ---")

    if not complaints:
        print("No complaints reported yet.")
        return

    
    for i in range(len(complaints)):
        c = complaints[i]
        print(f"\nComplaint #{i+1}")
        print("Category    :", c["category"])
        print("Description :", c["description"])


def show_analytics():
    print("\n--- Hygiene Risk Analytics ---")

    if len(complaints) == 0:
        print(" Sorry No data available. Please add complaints first.")
        return

    
    count = {}

    for c in complaints:
        category = c['category'].lower()
        if category in count:
            count[category] += 1
        else:
            count[category] = 1

    
    for category, total in count.items():
        print(f"\n {category.capitalize()} Issues Reported: {total}")

        
        if total >= 3:
            if category == "water":
                print(" High Risk of jaundice/typhoid due to water quality!")
            elif category == "food":
                print(" Risk of food poisoning!")
            elif category == "washroom":
                print(" Risk of fungal/skin infections!")
            elif category == "mosquito":
                print(" Risk of dengue or malaria!")
            else:
                print(" Health risk! Needs attention.")

# ----------- MAIN LOOP -----------
while True:
    show_menu()
    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        add_complaint()
    elif choice == "2":
        view_complaints()
    elif choice == "3":
        show_analytics()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid Choice! Please try again.")
