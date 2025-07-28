# University Club Management System

clubs = {}
students = {}
events = {}

def load_sample_clubs():
    sample = {
        1: {"name": "Coding Club", "members": [], "events": []},
        2: {"name": "Music Club", "members": [], "events": []},
        3: {"name": "Robotics Club", "members": [], "events": []},
        4: {"name": "Art Club", "members": [], "events": []},
        5: {"name": "Drama Club", "members": [], "events": []},
    }
    clubs.update(sample)

def display_menu():
    print("\n--- University Club Management System ---")
    print("1. Add Club (Admin)")
    print("2. View Clubs")
    print("3. Register Student")
    print("4. Join Club")
    print("5. View My Clubs")
    print("6. Add Event")
    print("7. View Events")
    print("8. Dashboard")
    print("0. Exit")

def add_club():
    club_id = int(input("Enter Club ID: "))
    name = input("Enter Club Name: ")
    if club_id in clubs:
        print("Club ID already exists.")
    else:
        clubs[club_id] = {"name": name, "members": [], "events": []}
        print("Club added successfully.")

def view_clubs():
    print("\n--- Clubs ---")
    for cid, data in clubs.items():
        print(f"ID: {cid}, Name: {data['name']}")

def register_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    if sid in students:
        print("Student already registered.")
    else:
        students[sid] = {"name": name, "clubs": []}
        print("Student registered successfully.")

def join_club():
    sid = input("Enter Student ID: ")
    cid = int(input("Enter Club ID to join: "))
    if sid in students and cid in clubs:
        if sid not in clubs[cid]["members"]:
            clubs[cid]["members"].append(sid)
            students[sid]["clubs"].append(cid)
            print(f"{students[sid]['name']} joined {clubs[cid]['name']}")
        else:
            print("Already a member.")
    else:
        print("Invalid student or club ID.")

def view_my_clubs():
    sid = input("Enter Student ID: ")
    if sid in students:
        print(f"\n{students[sid]['name']}'s Clubs:")
        for cid in students[sid]["clubs"]:
            print(f"- {clubs[cid]['name']}")
    else:
        print("Student not found.")

def add_event():
    cid = int(input("Enter Club ID for the event: "))
    event_name = input("Enter Event Name: ")
    if cid in clubs:
        clubs[cid]["events"].append(event_name)
        print("Event added successfully.")
    else:
        print("Invalid Club ID.")

def view_events():
    cid = int(input("Enter Club ID to view events: "))
    if cid in clubs:
        print(f"\nEvents in {clubs[cid]['name']}:")
        for e in clubs[cid]["events"]:
            print(f"- {e}")
    else:
        print("Invalid Club ID.")

def dashboard():
    print("\n--- Dashboard ---")
    print(f"Total Clubs: {len(clubs)}")
    print(f"Total Students: {len(students)}")

    total_events = sum(len(c["events"]) for c in clubs.values())
    print(f"Total Events: {total_events}")

    most_active = max(clubs.items(), key=lambda x: len(x[1]["members"]), default=(None, None))
    if most_active[0]:
        print(f"Most Active Club: {most_active[1]['name']} with {len(most_active[1]['members'])} members")
    
    print("\nAll Clubs:")
    for cid, data in clubs.items():
        print(f"ID: {cid}, Name: {data['name']}, Members: {len(data['members'])}, Events: {len(data['events'])}")

# Main Execution
load_sample_clubs()
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_club()
    elif choice == '2':
        view_clubs()
    elif choice == '3':
        register_student()
    elif choice == '4':
        join_club()
    elif choice == '5':
        view_my_clubs()
    elif choice == '6':
        add_event()
    elif choice == '7':
        view_events()
    elif choice == '8':
        dashboard()
    elif choice == '0':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
