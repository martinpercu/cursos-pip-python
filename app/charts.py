import matplotlib.pyplot as plt

def generate_bar_chart(country_name, labels, values):  
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./images/{country_name}bar.png')
  plt.close()
  # plt.show()


def generate_pie_chart(labels, values):  
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()
  # plt.show()


if __name__ == '__main__':
  labels = ['a', 'b', 'c', 'sdf', 'etsp']
  values = [25, 50, 100, 123, 129]
  generate_bar_chart(labels, values)
  #generate_pie_chart(labels, values)

