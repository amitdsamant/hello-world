import json
import csv
import requests
import datetime

def load_dict_to_csv():

    #response = request.GET('https://jsonplaceholder.typicode.com/posts')
    #print(json.loads(response.text))


    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)
    print(todos)
    csv_columns =[]
    for key in todos[0].keys():
        csv_columns.append(key)
    print(csv_columns)
    with open('report_results.csv', "w", encoding="utf8", newline='') as csvfile:
        w = csv.DictWriter(csvfile, fieldnames=csv_columns)
        w.writeheader()
        for i in range(len(todos)):
            w.writerow(todos[i])




if __name__ == '__main__':
    #load_dict_to_csv()
    from_date = datetime.datetime(2019, 1, 1)
    to_date = datetime.datetime(2019, 1, 5)
    datediff=(to_date-from_date).days
    print(datediff)
    print('date diff'+str(datediff))
    print(from_date.timestamp())
    print(round(to_date.timestamp()))
    print(type(from_date))


    while datediff>0:
        print(datediff)
        datediff=datediff-1

    timestamp = datetime.datetime(2019, 3, 1, 0, 0).timestamp() * 1000
    print(round(timestamp))