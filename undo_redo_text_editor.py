class UndoRedoTextEditor:
    def _init_(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def write(self, new_text):
        """Append text and clear redo history"""
        self.undo_stack.append(self.text)
        self.text += new_text
        self.redo_stack.clear()

    def undo(self):
        """Undo last action"""
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()
        else:
            print("Nothing to undo!")

    def redo(self):
        """Redo last undone action"""
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()
        else:
            print("Nothing to redo!")

    def show_text(self):
        """Display current text"""
        print(f"Current Text: '{self.text}'")


def main():
    editor = UndoRedoTextEditor()

    while True:
        print("\n--- Undo/Redo Text Editor ---")
        print("1. Write Text")
        print("2. Undo")
        print("3. Redo")
        print("4. Show Text")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_text = input("Enter text to add: ")
            editor.write(new_text)
        elif choice == '2':
            editor.undo()
        elif choice == '3':
            editor.redo()
        elif choice == '4':
            editor.show_text()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if _name_ == "_main_":
    main()