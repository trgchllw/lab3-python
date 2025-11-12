def search_log_file(file_path, search_word):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        print(f"Строки с '{search_word}':")
        found = False
        
        for line_num, line in enumerate(lines, 1):
            if search_word in line:
                print(f"[{line_num}] {line.rstrip()}")
                found = True
        
        if not found:
            print(f"Строк с '{search_word}' не найдено")
            
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден")

search_log_file("log.txt", "ERROR")