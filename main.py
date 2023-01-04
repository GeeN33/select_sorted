import csv
"""
Сортировка выбором

"""

def parsing_csv(limit):
    """
    загрузка csv-файла
    """
    filename = 'all_stocks_5yr.csv'
    i = 0
    all_stocks = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',', skipinitialspace=True)
        for row in reader:
            all_stocks.append(row)
            i += 1
            if i > limit:
                break

    return  all_stocks

def save_csv(dicts, filename):
    """
     записывает в csv-файл данные из анализируемого файла
    """

    csv_columns = ['date', 'open', 'high','low','close','volume','Name']
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dicts:
                writer.writerow(data)
    except IOError:
         print("I/O error")

def find_max(arr, sort_columns):
    """
     поиск максимума в массиве
    """
    max_list = float(arr[0][sort_columns])
    max_index = 0
    for i in range(1,len(arr)):
        if float(arr[i][sort_columns]) > max_list:
            max_list = float(arr[i][sort_columns])
            max_index = i
    return max_index

def find_min(arr, sort_columns):
    """
    поиск минимума в массиве
    """
    min_list = float(arr[0][sort_columns])
    min_index = 0
    for i in range(1,len(arr)):
        if float(arr[i][sort_columns]) < min_list:
            min_list = float(arr[i][sort_columns])
            min_index = i
    return min_index

def select_sorted(sort_columns ='high',limit=30, order='asc', filename='dump.csv'):
    """
    основная функция где происходит сортировка
    """
    new_list = []
    all_stocks = parsing_csv(limit)
    for i in range(1,len(all_stocks)):
        index = 0
        if order == 'desc':
             index = find_max(all_stocks,sort_columns)
        else:
            index = find_min(all_stocks, sort_columns)
        new_list.append(all_stocks.pop(index))

    save_csv(new_list, filename)
    return  new_list

if __name__ == '__main__':

    sorted_list = select_sorted(sort_columns ='low', order='desc', filename='dump.csv')
    for list in sorted_list:
        print(list)
