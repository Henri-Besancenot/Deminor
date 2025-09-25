# Deminor
A simple Minesweeper game implemented in Python.

## Overview
Deminor is a desktop version of the classic Minesweeper puzzle game. The objective is to clear a rectangular board containing hidden "mines" without detonating any of them, using clues about the number of neighboring mines in each field.

## How to Use

1. **Download or Clone the Repository**
    - Download the project files or clone the repository to your local machine.

2. **Install Requirements**
    - Ensure you have Python 3.11 or later installed.
    - (Optional) Install any dependencies listed in `requirements.txt` using:
      ```
      pip install -r requirements.txt
      ```

3. **Run the Game**
    - Open a terminal and navigate to the project directory (e.g., `~/Démineur/`).
    - Start the game with:
      ```
      python main.py
      ```
      or
      ```
      python3 main.py
      ```

## Features

- **Classic Minesweeper Gameplay:** Enjoy the familiar logic puzzle experience.
- **Intuitive Controls:**
  - **Left Click:** Reveal a cell.
  - **Right Click:** Place or remove a flag to mark suspected mines.
  - **Click on Revealed Cell:** If the number of adjacent flags matches the number on the cell, clicking will reveal all adjacent unrevealed cells.
- **Automatic Reveal:** When a zero (no adjacent mines) is uncovered, all surrounding cells are automatically revealed.
- **Game Over Detection:** Uncovering a mine ends the game and reveals the entire grid.
- **User-Friendly Interface:** Simple and clear UI for easy gameplay.

## Acknowledgements

Inspired by the classic Minesweeper game found on many operating systems.
