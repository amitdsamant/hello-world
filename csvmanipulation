import os
import csv

def get_csv_file_name():
    base_folder=os.path.dirname(__file__)
    return os.path.join(base_folder,'data','testdata.csv')

def parse_csv_file_data(filename):
    with open(filename,'r',encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        print(reader)
        for row in reader:
            print(row)

# def parse_csv_file_data_basic(filename):
#     with open(filename,'r',encoding='utf-8') as fin:
#         header = fin.readline()
#         print(header)
#         lines=[]
#         for line in fin:
#             lines.append(line.split(','))
#         print(lines)




def main():
    filename=get_csv_file_name()
    print(filename)
    parse_csv_file_data(filename)


if __name__=='__main__':
    main()