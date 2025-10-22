def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
        
        if count == 0:
            average = 0

        else:
            average = total / count
        
        return total, average
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено")
        return None, None
    
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None

total, average = total_salary("goit_pycore_hw_04_001.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")