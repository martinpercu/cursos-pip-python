import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    #print(header)
    for row in reader:
      iterable = zip(header, row)
      #print(list(iterable))
      #print('***' * 5)
      country_dict = {key: value for key, value in iterable}
      #print(country_dict)
      data.append(country_dict)
    return data
      #print(row)



if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[8])