def split_into_paragraphs(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        paragraphs = content.split('\n\n')
        
        paragraphs = [p.strip() for p in paragraphs if p.strip()]
        
        print(f"Найдено абзацев: {len(paragraphs)}")

        for i, paragraph in enumerate(paragraphs, 1):
            output_filename = f"part_{i}.txt"
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(paragraph)
            print(f"Создан файл: {output_filename}")
        
        print(f"Всего создано файлов: {len(paragraphs)}")
        
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    
    split_into_paragraphs('article.txt')