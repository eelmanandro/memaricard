# MemariCard

A PyQt5-based flashcard quiz application for learning questions and answers with progress tracking.

## Features

- **Quiz Mode**: Answer multiple-choice questions with 4 options
- **Menu System**: Add custom questions with wrong answer options
- **Statistics Tracking**: Monitor correct answers and success rate per question
- **Rest Timer**: Take timed breaks with optional YouTube entertainment
- **Question Management**: Add unlimited custom questions to your quiz set

## Project Structure

- `main.py` - Core application logic, question management, and event handlers
- `main_window.py` - Quiz interface UI layout and components
- `menu_window.py` - Menu interface for adding questions and viewing stats

## Usage

1. Run `main.py` to start the application
2. Answer questions by selecting one of four options and click "Answer"
3. Click "Menu" to add new questions or view statistics
4. Use "Rest" button for a timed break

## Requirements

- PyQt5
- Python 3.x

## Installation

```bash
pip install PyQt5
python main.py
```

## How It Works

Questions are stored as `Question` objects with tracking for:
- Total times asked
- Times answered correctly
- Success percentage
