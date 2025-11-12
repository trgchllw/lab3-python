import os

def merge_files(directory_path):
    try:
        txt_files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]
        txt_files.sort()
        
        if not txt_files:
            print("В папке нет txt-файлов")
            return
        
        print(f"Найдено файлов: {len(txt_files)}")
        print("Файлы для объединения:", txt_files)
        
        with open('merged.txt', 'w', encoding='utf-8') as merged_file:
            merged_file.write("")
        
        for i, filename in enumerate(txt_files):
            file_path = os.path.join(directory_path, filename)
            
            print(f"Обрабатывается файл: {filename}")
            
            with open(file_path, 'r', encoding='utf-8') as source_file, \
                 open('merged.txt', 'a', encoding='utf-8') as merged_file:
                
                for line in source_file:
                    merged_file.write(line)
                
                if i < len(txt_files) - 1:
                    merged_file.write("\n==== конец файла ====\n")
        
        print("Файлы успешно объединены в merged.txt")
        
    except FileNotFoundError:
        print(f"Ошибка: Папка '{directory_path}' не найдена")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    
    merge_files('texts')