# Project: File Operator

## Overview

Design and develop a Python program that allows users to maintain a personal journal. The application uses text file handling for storing journal entries, provides options for managing these files, and handles potential errors gracefully using exception handling. The project demonstrates a strong understanding of Object-Oriented Programming (OOP), including class and object creation.

## Learning Objectives

- Understand and implement file handling operations (read, write, append, and more).
- Use different modes of opening a file (r, w, a, x) and explain their impact.
- Perform I/O operations (reading from and writing to files).
- Handle exceptions such as FileNotFoundError, PermissionError, and others.
- Apply OOP principles to structure the application.

## Project Requirements

### Main Menu Options

1. **Add a New Entry** — Users can write a new journal entry. The program will append the entry to a journal file, creating the file if it doesn't exist.
2. **View All Entries** — Display all journal entries from the file. Handle the case where the file does not exist.
3. **Search for an Entry** — Search the file for a specific keyword or date and display matching entries.
4. **Delete All Entries** — Clear the journal by deleting the file. Prompt the user for confirmation before deleting.

## OOP Structure

- A JournalManager class will encapsulate all functionality, such as file handling operations and exception handling.
- Use instance methods for adding, reading, searching, and deleting entries.

## Exception Handling

- Handle exceptions for invalid file operations, such as opening non-existent files or permission errors.
- Ensure the program does not crash due to unexpected user input or file handling issues.

## File Handling Modes

- Use appropriate modes (r, w, a, x) for specific operations.
- Demonstrate the difference between these modes through functionality.


**Quick reference:**

| Mode | Name | Behavior |
|------|------|----------|
| `r` | Read | Opens an existing file for reading. Raises FileNotFoundError if the file is missing. |
| `w` | Write | Creates a new file or overwrites an existing one. Previous content is lost. |
| `a` | Append | Opens a file for writing, adding new content to the end without erasing existing data. |
| `x` | Exclusive create | Creates a new file but fails with FileExistsError if the file already exists. |

## User Interface (UI)

- Create a menu-driven interface to let users choose from different options.
- Allow users to exit the program from the main menu.

## Technical Specifications

- The program should operate only on text files (.txt).
- Journal entries should be stored in a file named journal.txt.
- Entries must include a timestamp and user input.
- Display clear error messages and guidance for invalid actions.

## ▶ Demo Video

<a href="https://drive.google.com/file/d/1eXo-U_dYl1SX5KKZ7ATmyYQXQrp_Lxnh/view?usp=sharing" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/▶-Watch%20Demo%20Video-181717?style=for-the-badge&logo=github&logoColor=white" alt="Watch Demo Video" />
</a>

## Output of Code
<img width="1150" height="710" alt="image" src="https://github.com/user-attachments/assets/2dbce019-ed9a-4f17-b7c2-2f4acf38ea09" />
<img width="857" height="690" alt="image" src="https://github.com/user-attachments/assets/6e619f4c-c4e9-43c1-9fe1-7bca9834b648" />


## Conclusion

The File Operator project brings together three core Python skills — file I/O, exception handling, and object-oriented design — into a single, practical application. By encapsulating all journal operations inside a JournalManager class, the program stays organized and easy to extend, while the menu-driven interface keeps it approachable for end users. Careful use of file modes (r, w, a, x) teaches the real-world consequences of each mode, such as accidental data loss with 'w' versus safe additions with 'a'. Robust exception handling around FileNotFoundError and PermissionError ensures the program degrades gracefully instead of crashing, which is a key habit for writing production-quality code. Overall, completing this project builds a solid foundation for working with persistent data in Python and reinforces good software design practices that carry over into larger, more complex applications.
