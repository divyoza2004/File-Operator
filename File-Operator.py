from datetime import datetime
class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"
    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ")
            with open(self.filename, "a") as file:
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write("[" + time + "]\n")
                file.write(entry + "\n")
                file.write("-" * 40 + "\n")
            print("Entry added successfully.")
        except Exception as e:
            print("Error:", e)
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()
                if data == "":
                    print("No journal entries found.")
                else:
                    print("\n----- Journal Entries -----")
                    print(data)
        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")
    def search_entry(self):
        try:
            keyword = input("Enter keyword or date to search: ")

            with open(self.filename, "r") as file:
                found = False
                for line in file:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True
                if not found:
                    print("No matching entries found.")
        except FileNotFoundError:
            print("Journal file does not exist.")
    def delete_entries(self):
        try:
            choice = input("Are you sure you want to delete all entries? (yes/no): ")
            if choice.lower() == "yes":
                with open(self.filename, "w") as file:
                    file.write("")
                print("All journal entries deleted.")
            else:
                print("Delete cancelled.")
        except Exception as e:
            print("Error:", e)
obj = JournalManager()

print("\n========== Personal Journal Manager ==========")
while True:
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            obj.add_entry()
        case 2:
            obj.view_entries()
        case 3:
            obj.search_entry()
        case 4:
            obj.delete_entries()
        case 5:
            print("Thank You!")
            break
        case _:
            print("Invalid Choice!")
