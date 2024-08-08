def total_salary(path):
    try:
        # Відкриваємо файл з правильним кодуванням
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            count_employes = 0
            
            # Проходимо по кожному рядку у файлі
            for line in file:
                # Розділяємо ім'я та зарплату
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue  # Пропускаємо некоректні рядки
                name, salary_str = parts
                try:
                    # Перетворюємо зарплату на число
                    salary = float(salary_str)
                    total_salary += salary
                    count_employes += 1
                except ValueError:
                    # Пропускаємо некоректні дані про зарплату
                    continue
            
            # Обчислюємо середню зарплату
            average = total_salary / count_employes 
            
            # Повертаємо загальну та середню зарплату
            return total_salary, average
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0
    

# Приклад використання функції
total_salary, average = total_salary("Homework2/salary_file.txt")
print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average}")