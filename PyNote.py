notes = []


def add_note():
    note = input("Enter your note: ")

    notes.append(note)

    print("Note added successfully!\n")


def view_notes():
    if len(notes) == 0:
        print("No notes found.\n")
        return

    print("\n===== Your Notes =====")

    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")

    print()


def delete_note():
    view_notes()

    if len(notes) == 0:
        return

    try:
        number = int(input("Enter note number to delete: "))

        if 1 <= number <= len(notes):
            removed = notes.pop(number - 1)

            print(f"Deleted note: {removed}\n")

        else:
            print("Invalid note number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def menu():
    while True:
        print("===== Simple Notes App =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            delete_note()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


menu()