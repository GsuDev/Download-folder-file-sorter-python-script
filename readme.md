# Automatic File Organizer for Downloads Folder

This Python script automatically organizes files in your Downloads folder by moving them into subfolders based on their type (Documents, Images, Music, Videos, Executables, etc.). Any file that doesn't fit into the predefined categories will be moved to an "Others" folder.

## Features

- **Automatic Sorting**: Organizes files into subfolders within the Downloads folder based on their extensions.
- **Predefined Categories**:
  - **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`, etc.
  - **Images**: `.jpg`, `.png`, `.gif`, `.jpeg`, etc.
  - **Videos**: `.mp4`, `.avi`, `.mkv`, etc.
  - **Music**: `.mp3`, `.wav`, etc.
  - **Executables**: `.exe`, `.py`, `.kt`, etc.
  - **Others**: Files that don’t match the above categories will be moved to an "Others" folder.
- **Customizable**: You can easily add new file types or modify existing ones in the script.

## Installation

1. Ensure that you have Python installed. This script requires Python 3.8 or later.
2. Install the necessary dependencies with:

   ```bash
   pip install watchdog
   ```

3. Download the script and place it in a desired location, such as your `Documents/Scripts` folder.

## Usage

1. Simply run the script from the terminal or command line:

   ```bash
   python automatic_file_sorter.py
   ```

2. The script will monitor your Downloads folder and automatically sort files into the appropriate subfolders.

## Adding to Task Scheduler (Windows)

To run the script automatically when your computer starts:

1. Open **Task Scheduler** in Windows.
2. Create a new task with the trigger set to "At system startup."
3. Set the action to run the Python interpreter with the path to your script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Created by GsuDev