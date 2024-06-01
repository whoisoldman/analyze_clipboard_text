import pyperclip
import os

def analyze_clipboard_text():
    try:
        # Getting text from the clipboard
        clipboard_content = pyperclip.paste()

        if os.path.isfile(clipboard_content):
            analyze_file(clipboard_content)
        else:
            analyze_text(clipboard_content)

    except Exception as e:
        print(f"This is neither text nor a file. Error: {e}")

def analyze_text(text):
    # Counting lines
    line_count = text.count('\n') + (not text.endswith('\n')) if text else 0

    # Counting words
    word_count = len(text.split())

    # Counting characters with spaces
    char_count_with_spaces = len(text)

    # Counting characters without spaces
    char_count_without_spaces = len(text.replace(" ", ""))

    # Printing results
    print("IN YOUR TEXT:\n")
    print(f"lines: {line_count}")
    print(f"words: {word_count}")
    print(f"characters with spaces: {char_count_with_spaces}")
    print(f"characters without spaces: {char_count_without_spaces}")

def analyze_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension != '.txt':
        print(f"Unsupported file format: {file_extension}")
        return

    file_name_with_extension = os.path.basename(file_path)
    file_name_without_extension = os.path.splitext(file_name_with_extension)[0]

    # Counting characters in the filename with extension
    file_name_char_count_with_extension = len(file_name_with_extension)

    # Counting characters in the filename without extension and spaces
    file_name_char_count_without_extension = len(file_name_without_extension.replace(" ", ""))

    # Counting spaces in the filename without extension
    spaces_count_in_filename = file_name_without_extension.count(" ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            if content.strip() == "":
                # File is empty
                print(f"IN YOUR FILE ({file_extension}) NO TEXT:\n")
                print(f"characters in the filename with extension: {file_name_char_count_with_extension}")
                print(f"characters in the filename without extension: {file_name_char_count_without_extension}")
                print(f"spaces in the filename: {spaces_count_in_filename}")
            else:
                # File contains text
                line_count = content.count('\n') + (not content.endswith('\n'))
                word_count = len(content.split())
                char_count_with_spaces = len(content)
                char_count_without_spaces = len(content.replace(" ", ""))

                print(f"IN YOUR FILE ({file_extension}):\n")
                print(f"lines: {line_count}")
                print(f"words: {word_count}")
                print(f"characters with spaces: {char_count_with_spaces}")
                print(f"characters without spaces: {char_count_without_spaces}")
                print(f"characters in the filename with extension: {file_name_char_count_with_extension}")
                print(f"characters in the filename without extension: {file_name_char_count_without_extension}")
                print(f"spaces in the filename: {spaces_count_in_filename}")

    except UnicodeDecodeError:
        # File is not in text format
        print(f"YOUR FILE ({file_extension}) CONTAINS TECHNICAL INFORMATION:\n")
        print(f"characters in the filename with extension: {file_name_char_count_with_extension}")
        print(f"characters in the filename without extension: {file_name_char_count_without_extension}")
        print(f"spaces in the filename: {spaces_count_in_filename}")

if __name__ == "__main__":
    analyze_clipboard_text()
