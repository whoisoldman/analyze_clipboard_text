# analyze_clipboard_text

## ABOUT CODE (PROGRAMM)
This program analyzes text either copied to the clipboard or contained within a `.txt` file.

If text is copied to the clipboard, the program outputs the number of lines, words, characters with spaces, and characters without spaces in the text.

If a path to a `.txt` file is provided, the program analyzes the content of the file. If the file is empty or does not contain text, the program notifies accordingly. Otherwise, the program outputs the number of lines, words, characters with and without spaces in the file, as well as the number of characters in the filename with and without extension, and the number of spaces in the filename without extension.

If the file format is not supported (not `.txt`), the program outputs a message indicating the unsupported file format.

In case of errors during execution, the program prints an error message.

Here are examples of using the program:

**Example 1: Analyzing text from the clipboard**

1. Copy the following text to the clipboard:
   ```
   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
   ```

2. Run the program.

3. The program will automatically analyze the text from the clipboard.

4. The analysis results will be displayed on the screen:
   ```
   IN YOUR TEXT:

   lines: 1
   words: 14
   characters with spaces: 97
   characters without spaces: 82
   ```

**Example 2: Analyzing text from a file**

1. Create a text file named `example.txt` and add the following text to it:
   ```
   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
   ```

2. Specify the path to the `example.txt` file in the program.

3. Run the program.

4. The program will analyze the contents of the `example.txt` file.

5. The analysis results will be displayed on the screen:
   ```
   IN YOUR FILE (.txt):

   lines: 1
   words: 10
   characters with spaces: 82
   characters without spaces: 76
   characters in the filename with extension: 11
   characters in the filename without extension: 7
   spaces in the filename without extension: 1
   ```

These examples demonstrate how to use the program to analyze text from the clipboard or from text files.
