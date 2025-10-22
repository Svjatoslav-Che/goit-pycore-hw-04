def get_cats_info(path):
    cats = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
 
                cat_id, name, age = line.strip().split(',')
  
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
 
                cats.append(cat_info)
        
        return cats
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено")
        return []
    
    except Exception as e:
        print(f"П Помилка: {e}")
        return []

cats_info = get_cats_info("goit_pycore_hw_04_002.txt")
print(cats_info)