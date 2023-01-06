import csv

def parsing_csv(limit):
    """
    загрузка csv-файла
    """
    filename = 'all_stocks_5yr.csv'
    i = 0
    cache =  []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',', skipinitialspace=True)
        for row in reader:
            cache.append(row)
            i += 1
            if i > limit:
                break

    return  cache

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

def select_sorted(sort_columns,limit, order, filename):
    """
     функция где происходит сортировка
    """
    new_cache = []
    cache = parsing_csv(limit)
    for i in range(1,len(cache)):
        index = 0
        if order == 'desc':
             index = find_max(cache,sort_columns)
        else:
            index = find_min(cache, sort_columns)
        new_cache.append(cache.pop(index))

    save_csv(new_cache, filename)
    return  new_cache

def get_by_date(date, name, filename):
    """
    функция где происходит поиск
    """
    new_cache = []
    cache = parsing_csv(limit=2000000)
    for stock in cache:
        if date == stock['date'] and name == stock['Name']:
            new_cache.append(stock)

    save_csv(new_cache, filename)
    return new_cache
def uniqs(inputstring):
    """
    Количество уникальных подстрок
    """
    substrings = [""]
    for i in range(0, len(inputstring) + 1):
        for j in range(i + 1, len(inputstring) + 1):
            substr = inputstring[i:j]
            substrings.append(substr)
    uniq = set()
    for ss in substrings:
        uniq.add(ss)
    return uniq


if __name__ == '__main__':

    # sorted_list = select_sorted(sort_columns ='high',limit=10, order='asc', filename='dump_select_sorted1.csv')
    # sorted_list = select_sorted(sort_columns ='close',limit=10, order='asc', filename='dump_select_sorted2.csv')
    sorted_list = select_sorted(sort_columns ='low',limit=10, order='desc', filename='dump_select_sorted3.csv')

    # sorted_list = get_by_date(date='2017-08-08', name='PCLN', filename='dump_get_by_date.csv')

    # sorted_list =  uniqs("gfg")
    # sorted_list = uniqs("ggg")

    for list in sorted_list:
        print(list)
