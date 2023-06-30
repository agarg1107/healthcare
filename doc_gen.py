import subprocess

def print_file(file_path):
    try:
        subprocess.run(['lpr', file_path])  # Use 'lpr' for macOS or Linux, use 'print' for Windows
        print("File sent to printer successfully.")
    except FileNotFoundError:
        print("Printing command not found or printer not available.")
    except subprocess.SubprocessError:
        print("Error occurred while printing.")

# Specify the file path
file_path = 'path/to/file.pdf'  # Replace with the actual path to your file

# Print the file
print_file(file_path)
