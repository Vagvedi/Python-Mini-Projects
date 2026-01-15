# Python Mini-Projects

A collection of fun and educational Python mini-projects for beginners. Each project demonstrates fundamental programming concepts and practical applications.

## 📋 Projects Overview

### 1. **Caterpillar Game** 🐛
A fun interactive game built with Python's `turtle` graphics module.

- **File:** [Caterpillar_Game/Caterpillar.py](Caterpillar_Game/Caterpillar.py)
- **Description:** Guide a caterpillar to eat leaves while avoiding walls. Press SPACE to start the game. Navigate the caterpillar using arrow keys to collect leaves and increase your score.
- **Features:**
  - Interactive turtle graphics visualization
  - Score tracking
  - Collision detection with window boundaries
  - Dynamic leaf generation
  - Real-time game state management
- **Requirements:** Python built-in `turtle` module
- **How to Run:** `python Caterpillar_Game/Caterpillar.py`

---

### 2. **Chess Game** ♟️
A fully functional chess game with graphical interface using Pygame.

- **Files:** 
  - [Chess_Game/ChessGame.py](Chess_Game/ChessGame.py)
  - [Chess_Game/ChessEngine.py](Chess_Game/ChessEngine.py)
- **Description:** A complete chess implementation with a graphical board interface. Play against another player with full chess rules support.
- **Features:**
  - 8x8 chessboard visualization
  - All standard chess piece movements
  - Move validation and legal move calculation
  - Game state tracking
  - Check and checkmate detection
  - Animated piece movements
  - Player click-based move selection
- **Requirements:** 
  - `pygame` - For graphics and game window management
  - Chess piece images (provided in `images/` folder)
- **Installation:** `pip install -r Chess_Game/requirements.txt`
- **How to Run:** `python Chess_Game/ChessGame.py`

---

### 3. **Dice Rolling Simulator** 🎲
A simple command-line dice rolling simulator with visual representation.

- **File:** [Dice_Rolling_Stimulator/dice_stimulator.py](Dice_Rolling_Stimulator/dice_stimulator.py)
- **Description:** Simulates rolling a six-sided dice and displays the result as ASCII art.
- **Features:**
  - Random dice roll generation (1-6)
  - ASCII art visualization of dice faces
  - Looping gameplay - roll as many times as you want
  - Interactive user input
- **Requirements:** None - uses only Python standard library (`random`)
- **How to Run:** `python Dice_Rolling_Stimulator/dice_stimulator.py`
- **Usage:** Follow the prompts to roll the dice and press 'y' to roll again

---

### 4. **Number Guessing Game** 🎯
An interactive guessing game with difficulty levels and colored output.

- **File:** [Number_Guessing_Game/guess.py](Number_Guessing_Game/guess.py)
- **Description:** Guess a randomly generated number within a range. Three difficulty levels determine the number range.
- **Features:**
  - Three difficulty levels:
    - Easy: 1-50
    - Medium: 1-100
    - Hard: 1-200
  - Intelligent hints (too high/too low)
  - Attempt counter
  - Colorized terminal output
  - Input validation
  - Performance scoring
- **Requirements:** `colorama` - For colored terminal output
- **Installation:** `pip install colorama`
- **How to Run:** `python Number_Guessing_Game/guess.py`

---

### 5. **Password Generator** 🔐
A secure password generation tool with customizable options.

- **File:** [Password_Generator/password.py](Password_Generator/password.py)
- **Description:** Generate strong, random passwords with customizable character sets and length.
- **Features:**
  - Customizable password length (minimum 6 characters)
  - Optional character types:
    - Lowercase letters (always included)
    - Uppercase letters
    - Numbers
    - Special symbols/punctuation
  - Randomized character selection
  - Input validation
  - User-friendly prompts
- **Requirements:** None - uses only Python standard library (`random`, `string`)
- **How to Run:** `python Password_Generator/password.py`
- **Usage:** Follow the interactive prompts to configure your password options

---

### 6. **Rock Paper Scissors PRO** 🎮
A classic command-line game where the user competes against the computer using strategy and luck.

- **File:** [Rock_Paper_Scissors_PRO/rock_paper_scissors.py](Rock_Paper_Scissors/rock.py)
- **Description:** Play the classic Rock–Paper–Scissors game against the computer with score tracking and multiple rounds.
- **Features:**
  - User vs Computer gameplay
  - Randomized computer choices
  - Multiple rounds of play
  - Live scoreboard display
  - Clear win/lose/draw logic
  - Beginner-friendly and clean code structure
- **Requirements:** None – uses only Python standard library (`random`)
- **How to Run:** `python Rock_Paper_Scissors_PRO/rock.py`
- **Usage:** Choose Rock, Paper, or Scissors each round and decide whether to continue playing

---

### 7. **File Organiser Automation** 📁
A simple command-line automation tool to organize files in a directory based on their file types.

- **File:** [File_Organiser/file_organizer.py](File_Organiser/file_organizer.py)
- **Description:** Automatically sorts files in a selected folder into categorized subfolders such as Images, Documents, Videos, Music, Archives, and Others.
- **Features:**
  - Automatic file organization by extension
  - Creates folders if they do not exist
  - Supports common file categories
  - Works on any directory (Downloads, Desktop, etc.)
  - Simple and user-friendly CLI
- **Requirements:** None – uses only Python standard library (`os`, `shutil`)
- **How to Run:** `python File_Organiser/file_organizer.py`
- **Usage:** Enter the path of the folder you want to organize and let the script sort the files automatically

 ---
### 8. **Calculator GUI (Tkinter)** 🧮
A simple graphical calculator application built using Python’s Tkinter library.

- **File:** [Calculator_GUI/calculator.py](Calculator_GUI/calculator.py)
- **Description:** A GUI-based calculator that performs basic arithmetic operations using clickable buttons.
- **Features:**
  - Graphical user interface using Tkinter
  - Button-based input system
  - Supports addition, subtraction, multiplication, and division
  - Error handling for invalid expressions
  - Clean and responsive layout
- **Requirements:** None – uses built-in Python library (`tkinter`)
- **How to Run:** `python Calculator_GUI/calculator.py`
- **Usage:** Click the calculator buttons to enter numbers and operations, then press `=` to view the result
---

### 9. **Digital Clock GUI** ⏰
A real-time digital clock application built using Python Tkinter.

- **File:** [Digital_Clock_GUI/digital_clock.py](Digital_Clock_GUI/digital_clock.py)
- **Description:** Displays the current system time and updates every second.
- **Features:**
  - Real-time clock display
  - Automatic refresh every second
  - Minimal and clean UI
- **Requirements:** None – uses built-in Python libraries (`tkinter`, `time`)
- **How to Run:** `python Digital_Clock_GUI/digital_clock.py`
- **Usage:** Launch the app to view the live digital clock
 
 ---

### 10. **To-Do List GUI (Tkinter)** 📝
A simple graphical task manager built using Python Tkinter.

- **File:** [Todo_List_GUI/todo_app.py](Todo_List_GUI/todo_app.py)
- **Description:** Manage daily tasks with options to add, mark complete, and delete tasks.
- **Features:**
  - Add and remove tasks
  - Mark tasks as completed
  - Clean graphical interface
- **Requirements:** None – uses built-in Python library (`tkinter`)
- **How to Run:** `python Todo_List_GUI/todo_app.py`
- **Usage:** Type a task, add it to the list, and manage tasks using buttons

  ---

### 11. **Stopwatch GUI (Tkinter)** ⏱️
A graphical stopwatch application built using Python Tkinter.

- **File:** [Stopwatch_GUI/stopwatch.py](Stopwatch_GUI/stopwatch.py)
- **Description:** Measure elapsed time with start, stop, and reset functionality.
- **Features:**
  - Real-time stopwatch
  - Millisecond precision
  - Start/Stop/Reset controls
- **Requirements:** None – uses built-in Python libraries (`tkinter`, `time`)
- **How to Run:** `python Stopwatch_GUI/stopwatch.py`
- **Usage:** Click Start to begin timing, Stop to pause, and Reset to clear the timer

---

### 12. **Weather App GUI (Tkinter + API)** 🌦️
A graphical weather application that fetches real-time weather data using an external API.

- **File:** [Weather_App_GUI/weather_app.py](Weather_App_GUI/weather_app.py)
- **Description:** Search any city to view temperature, humidity, and weather conditions.
- **Features:**
  - Real-time weather data
  - City-based search
  - Clean Tkinter interface
- **Requirements:** `requests` library, OpenWeatherMap API
- **How to Run:** `python Weather_App_GUI/weather_app.py`
- **Usage:** Enter a city name and click “Get Weather”

---

### 13. **Notes App GUI (Tkinter)** 🗒️
A graphical notes application built using Python Tkinter.

- **File:** [Notes_App_GUI/notes_app.py](Notes_App_GUI/notes_app.py)
- **Description:** Create, open, edit, and save text notes using a simple GUI.
- **Features:**
  - New, Open, and Save notes
  - Text editing area
  - File-based storage
- **Requirements:** None – uses built-in Python library (`tkinter`)
- **How to Run:** `python Notes_App_GUI/notes_app.py`
- **Usage:** Write notes and save them as text files on your system

---

### 14. **Mini Paint App (Tkinter)** 🎨
A simple drawing application built using Python Tkinter.

- **File:** [Paint_App_GUI/paint_app.py](Paint_App_GUI/paint_app.py)
- **Description:** Draw freely on a canvas, change brush color, and clear the canvas.
- **Features:**
  - Mouse-based drawing
  - Color picker
  - Clear canvas functionality
- **Requirements:** None – uses built-in Python library (`tkinter`)
- **How to Run:** `python Paint_App_GUI/paint_app.py`
- **Usage:** Click and drag on the canvas to draw

---

### 17. **File Search Tool (Tkinter)** 🔍
A graphical file search utility built using Python Tkinter.

- **File:** [File_Search_GUI/file_search.py](File_Search_GUI/file_search.py)
- **Description:** Search for files inside a directory and view their full paths.
- **Features:**
  - Directory browsing
  - File name search
  - Clean GUI output
- **Requirements:** None – uses Python standard library only
- **How to Run:** `python File_Search_GUI/file_search.py`
- **Usage:** Enter file name, select folder, and search

---


## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the repository:**
   ```bash
   git clone <repository-url>
   cd Python-Mini-Projects-main
   ```

2. **Install required packages:**
   ```bash
   pip install pygame colorama
   ```

3. **Run any project:**
   ```bash
   python <project_folder>/<file>.py
   ```

---

## 📦 Project Dependencies

| Project | Dependencies | Installation |
|--------|--------------|--------------|
| Caterpillar Game | Built-in `turtle` | No installation needed |
| Chess Game | `pygame` | `pip install pygame` |
| Dice Simulator | Built-in `random` | No installation needed |
| Number Guessing Game | `colorama` | `pip install colorama` |
| Password Generator | Built-in `random`, `string` | No installation needed |
| Rock Paper Scissors | Built-in `random` | No installation needed |
| File Organiser Automation | Built-in `os`, `shutil` | No installation needed |
| Calculator GUI | Built-in `tkinter` | No installation needed |
| Digital Clock GUI | Built-in `tkinter`, `time` | No installation needed |
| To-Do List GUI | Built-in `tkinter` | No installation needed |
| Stopwatch GUI | Built-in `tkinter`, `time` | No installation needed |
| Weather App GUI | `requests`, OpenWeatherMap API | `pip install requests` |
| Notes App GUI | Built-in `tkinter` | No installation needed |
| Mini Paint App GUI | Built-in `tkinter` | No installation needed |

---

## 💡 Learning Outcomes

These projects teach:
- **Variables and Data Types:** Numbers, strings, lists
- **Control Flow:** Loops, conditionals
- **Functions:** Creating and calling functions
- **Object-Oriented Programming:** Classes (Chess Game)
- **Game Development:** Graphics, user input, game loops
- **Data Structures:** Lists, dictionaries (Chess board state)
- **Module Usage:** Importing and using libraries
- **Input Validation:** Error handling and user input checks

---

## 📂 Project Structure

```
Python-Mini-Projects-main/
├── Caterpillar_Game/
│   ├── Caterpillar.py
│   └── README.md
├── Chess_Game/
│   ├── ChessEngine.py
│   ├── ChessGame.py
│   ├── requirements.txt
│   ├── README.md
│   └── images/
├── Calculator_GUI/
│   ├── calculator.py
│   └── README.md
├── Digital_Clock_GUI/
│   ├── digital_clock.py
│   └── README.md
├── Stopwatch_GUI/
│   ├── stopwatch.py
│   └── README.md
├── Dice_Rolling_Stimulator/
│   ├── dice_stimulator.py
│   └── README.md
├── Number_Guessing_Game/
│   ├── guess.py
│   └── README.md
├── Password_Generator/
│   ├── password.py
│   └── README.md
├── Rock_Paper_Scissors/
│   ├── rock.py
│   └── README.md
├── File_Organiser/
│   ├── file_organizer.py
│   └── README.md
├── Todo_List_GUI/
│   ├── todo_app.py
│   └── README.md
├── Weather_App_GUI/
│   ├── weather_app.py
│   └── README.md
├── Notes_App_GUI/
│   ├── notes_app.py
│   └── README.md
├── Paint_App_GUI/
│   ├── paint_app.py
│   └── README.md
├── LICENSE
└── README.md


```

---

## 🎮 Quick Start Examples

**Caterpillar Game:**
```bash
python Caterpillar_Game/Caterpillar.py
```
Press SPACE to start, use arrow keys to move the caterpillar.

**Chess Game:**
```bash
python Chess_Game/ChessGame.py
```
Click on a piece to select it, then click the destination square to move.

**Dice Roller:**
```bash
python Dice_Rolling_Stimulator/dice_stimulator.py
```
Press 'y' to roll the dice, any other key to exit.

**Number Guessing:**
```bash
python Number_Guessing_Game/guess.py
```
Select difficulty and guess the number based on hints.

**Password Generator:**
```bash
python Password_Generator/password.py
```

**Calculator GUI:**
```bash
python Calculator_GUI/calculator.py
```
Answer prompts to customize your password, then get a secure random password.

---

## 🔧 Customization

Feel free to modify and enhance these projects:
- Add new features to games (difficulty levels, high scores, etc.)
- Change visual styles and colors
- Add sound effects
- Create AI opponents
- Implement additional password generator options

---

## 📝 License

This project is licensed under the terms specified in the LICENSE file.

---

## 🤝 Contributing

Feel free to fork, modify, and improve these projects. Contributions are welcome!

---

## ❓ Troubleshooting

**Chess Game images not found:**
- Ensure chess piece PNG files are in the `Chess_Game/images/` folder

**Turtle graphics window doesn't appear:**
- Make sure you have a graphical display environment
- On WSL, you may need to configure an X server

**Module not found errors:**
- Install missing packages using pip: `pip install <package-name>`

---

Happy coding! 🐍✨
