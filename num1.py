def count_lines_and_chars(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        total_lines = len(lines)
        total_chars = 0
        
        for line in lines:
            line_without_newline = line.rstrip('\n')
            total_chars += len(line_without_newline)
        
        if total_lines > 0:
            avg_length = total_chars // total_lines
        else:
            avg_length = 0
        
        print(f"Строк: {total_lines}")
        print(f"Символов: {total_chars}")
        print(f"Средняя длина строки: {avg_length}")
        
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    file_path = input("Введите путь к файлу .txt: ")
    count_lines_and_chars(file_path)