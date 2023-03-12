from pprint import pprint

# Задание №1

def files_recipes():
    with open("files.txt", "rt", encoding="utf-8") as f:
        cook_book = {}
        for i in f:
            dish_name = i.strip()
            number = int(f.readline())
            lst = []
            for t in range(number):
                ingredient_name, quantity, measure = f.readline().strip().split(" | ")
                lst.append({
                    "ingredient_name": ingredient_name,
                    "quantity": quantity,
                    "measure": measure
                })
            cook_book[dish_name] = lst
            f.readline()
    f.close()

    return cook_book

# Задание №2

def get_shop_list_by_dishes(dishes, person_count):
    ingradient = {}
    for dis in dishes:
        for _ in range(len(files_recipes()[dis])):
            name, suman, measure = files_recipes()[dis][_].values()
            if name not in ingradient:
                ingradient[name] = {"measure": measure, "suman": int(suman) * person_count}
            else:
                ingradient[name]["suman"] += int(suman) * person_count
    return ingradient

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задание №3

dikt = {}
for b in range(3):
    files = (f"{b + 1}.txt")
    with open(files, encoding="utf-8") as fis:
        dikt[files] = fis.readlines()
sort = sorted((dikt.items()), key=lambda i: len(i[1]))
with open("sort_files.txt", "a", encoding="utf-8") as t:
    for name_, text_ in sort:
        t.write(f"{name_}\n")
        t.write(f"{str(len(text_))}\n")
        for ln in text_:
            t.write(ln)
        t.write("\n")
