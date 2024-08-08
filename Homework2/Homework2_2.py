def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    continue  # Пропустити некоректні рядки
                cat_id, name, age = parts
                cat_dict = {              # Створення словника для кота
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat_dict)
    except FileNotFoundError: 
        print(f"Файл за шляхом {path} не знайдено.")
    return cats_info

# Приклад використання функції
cats_info = get_cats_info("Homework2/cats_file.txt")
print(cats_info)