import pyperclip
import os

def analyze_clipboard_text():
    try:
        # Получение текста из буфера обмена
        clipboard_content = pyperclip.paste()

        if os.path.isfile(clipboard_content):
            analyze_file(clipboard_content)
        else:
            analyze_text(clipboard_content)

    except Exception as e:
        print(f"Это не текст и не файл. Ошибка: {e}")

def analyze_text(text):
    # Количество строк
    line_count = text.count('\n') + (not text.endswith('\n')) if text else 0
    
    # Количество слов
    word_count = len(text.split())
    
    # Количество знаков с пробелами
    char_count_with_spaces = len(text)
    
    # Количество знаков без пробелов
    char_count_without_spaces = len(text.replace(" ", ""))
    
    # Вывод результатов
    print("В ВАШЕМ ТЕКСТЕ:\n")
    print(f"строк: {line_count}")
    print(f"слов: {word_count}")
    print(f"знаков с пробелами: {char_count_with_spaces}")
    print(f"знаков без пробелов: {char_count_without_spaces}")

def analyze_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension != '.txt':
        print(f"Неподдерживаемый формат файла: {file_extension}")
        return

    file_name_with_extension = os.path.basename(file_path)
    file_name_without_extension = os.path.splitext(file_name_with_extension)[0]

    # Количество знаков в названии файла с расширением
    file_name_char_count_with_extension = len(file_name_with_extension)
    
    # Количество знаков в названии файла без расширения и пробелов
    file_name_char_count_without_extension = len(file_name_without_extension.replace(" ", ""))
    
    # Количество пробелов в названии файла без расширения
    spaces_count_in_filename = file_name_without_extension.count(" ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
                
            if content.strip() == "":
                # Файл пустой
                print(f"В ВАШЕМ ФАЙЛЕ ({file_extension}) НЕТ ТЕКСТА:\n")
                print(f"знаков в названии файла с расширением: {file_name_char_count_with_extension}")
                print(f"знаков в названии файла без расширения: {file_name_char_count_without_extension}")
                print(f"пробелов в названии файла: {spaces_count_in_filename}")
            else:
                # Файл содержит текст
                line_count = content.count('\n') + (not content.endswith('\n'))
                word_count = len(content.split())
                char_count_with_spaces = len(content)
                char_count_without_spaces = len(content.replace(" ", ""))
                
                print(f"В ВАШЕМ ФАЙЛЕ ({file_extension}):\n")
                print(f"строк: {line_count}")
                print(f"слов: {word_count}")
                print(f"знаков с пробелами: {char_count_with_spaces}")
                print(f"знаков без пробелов: {char_count_without_spaces}")
                print(f"знаков в названии файла с расширением: {file_name_char_count_with_extension}")
                print(f"знаков в названии файла без расширения: {file_name_char_count_without_extension}")
                print(f"пробелов в названии файла: {spaces_count_in_filename}")

    except UnicodeDecodeError:
        # Файл не является текстовым форматом
        print(f"ВАШ ФАЙЛ ({file_extension}) СОДЕРЖИТ ТЕХНИЧЕСКУЮ ИНФОРМАЦИЮ:\n")
        print(f"знаков в названии файла с расширением: {file_name_char_count_with_extension}")
        print(f"знаков в названии файла без расширения: {file_name_char_count_without_extension}")
        print(f"пробелов в названии файла: {spaces_count_in_filename}")

if __name__ == "__main__":
    analyze_clipboard_text()