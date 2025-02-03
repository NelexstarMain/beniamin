# Hacking Beniamin Bot

**Disclaimer:**  
This project is provided for educational and entertainment purposes only. The code simply creates a short black screen flash on your monitor at precise minute intervals. It is **not** designed to compromise or damage any system, network, or individual. Always ensure that you have permission before running any software that may affect someone else's device or experience.

## Overview

The "Hacking Beniamin Bot" is a Python script that simulates a hacking prank by briefly flashing a full-screen black window at the exact moment a new minute begins (when seconds equal 00). The flash duration is very short (default is 50 ms) to minimize disruption while still achieving the desired effect.

## Features

- **Precise Timing:**  
  The bot waits until the start of the next full minute and then repeats every 60 seconds, regardless of when it was started.

- **Full-Screen Prank:**  
  When triggered, the script displays a full-screen, borderless, and always-on-top window with a black background for a very short period.

- **Customizable Duration:**  
  You can adjust the flash duration by modifying the `duration_ms` parameter in the script.

## Requirements

- **Python 3.x**  
  The script is written in Python and requires Python 3.x to run.

- **tkinter module**  
  The tkinter module is used for creating the full-screen window. It is typically included with Python installations.

## Installation

1. **Download or Copy the Script:**  
   Save the provided Python code into a file named, for example, `src.pyw`. The `.pyw` extension is recommended on Windows to run the script without opening a console window.

2. **Ensure Python is Installed:**  
   Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. **Run the Script:**  
   - On Windows, double-click the `src.pyw` file to execute it without a console.
   - Alternatively, run it from the command line using:
     ```bash
     pythonw src.pyw
     ```

2. **Watch the Prank:**  
   The bot will wait until the next full minute (when the seconds equal 00) and then flash a full-screen black window for a brief moment (default 50 ms). This process will repeat every 60 seconds.

3. **Adjust Flash Duration:**  
   If you want to modify how long the flash lasts, change the `duration_ms` parameter in the `flash_black_screen` function:
   ```python
   def flash_black_screen(duration_ms=50):
   ```
   For example, to set the duration to 30 milliseconds, change it to:
   ```python
   def flash_black_screen(duration_ms=30):
   ```

## Important Notes

- **Intended Use:**  
  This script is intended solely for pranks or demonstrations with the explicit consent of the target (Beniamin in this case). Misusing this tool on systems without permission may violate laws and result in legal consequences.

- **Safety and Consent:**  
  Always use such tools responsibly. Ensure that any prank or demonstration is done in a safe environment and with the full awareness of everyone involved.

- **Modification and Distribution:**  
  You are free to modify and redistribute this project as long as you respect the above disclaimer and intended purpose.

---

By using this tool, you agree to take full responsibility for any actions that may result from its use. Enjoy responsibly!