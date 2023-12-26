import os
import datetime

class NoteTakingApp:
    def __init__(self, notes_file="notes.txt"):
        self.notes_file = notes_file
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as file:
                return file.readlines()
        else:
            return []

    def save_notes(self):
        with open(self.notes_file, 'w') as file:
            file.writelines(self.notes)

    def display_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            for idx, note in enumerate(self.notes, start=1):
                print(f"{idx}. {note.strip()}")

    def add_note(self, note):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.notes.append(f"{timestamp}: {note}\n")
        self.save_notes()
        print("Note added successfully.")

    def delete_note(self, note_index):
        if 1 <= note_index <= len(self.notes):
            deleted_note = self.notes.pop(note_index - 1)
            self.save_notes()
            print(f"Note deleted: {deleted_note.strip()}")
        else:
            print("Invalid note index.")

def main():
    app = NoteTakingApp()

    while True:
        print("\n1. Display Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            app.display_notes()
        elif choice == '2':
            note_text = input("Enter your note: ")
            app.add_note(note_text)
        elif choice == '3':
            app.display_notes()
            note_index = int(input("Enter the index of the note to delete: "))
            app.delete_note(note_index)
        elif choice == '4':
            print("Exiting the note-taking app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

