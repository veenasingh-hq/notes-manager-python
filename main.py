# ==============================
# Project 05 - Notes Manager
# ==============================

FILE_NAME = "notes.txt"

while True:
    print("\n===== Notes Manager =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Note")
    print("4. Delete All Notes")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # -------------------------
    # Add Note
    # -------------------------
    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")

        with open(FILE_NAME, "a") as file:
            file.write(f"Title   : {title}\n")
            file.write(f"Content : {content}\n")
            file.write("-" * 40 + "\n")

        print("✅ Note added successfully!")

    # -------------------------
    # View Notes
    # -------------------------
    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                notes = file.read()

            if notes.strip() == "":
                print("No notes found.")
            else:
                print("\n===== Your Notes =====")
                print(notes)

        except FileNotFoundError:
            print("No notes found.")

    # -------------------------
    # Search Note
    # -------------------------
    elif choice == "3":
        keyword = input("Enter title or keyword to search: ").lower()

        try:
            with open(FILE_NAME, "r") as file:
                data = file.read()

            if keyword in data.lower():
                print("\n===== Matching Notes =====")
                print(data)
            else:
                print("No matching note found.")

        except FileNotFoundError:
            print("No notes found.")

    # -------------------------
    # Delete All Notes
    # -------------------------
    elif choice == "4":
        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() == "y":
            with open(FILE_NAME, "w") as file:
                pass

            print("✅ All notes deleted.")

        else:
            print("Operation cancelled.")

    # -------------------------
    # Exit
    # -------------------------
    elif choice == "5":
        print("👋 Exiting Notes Manager...")
        break

    # -------------------------
    # Invalid Choice
    # -------------------------
    else:
        print("❌ Invalid choice! Please enter a number between 1 and 5.")