import read_csv
import charts
import utils


def run():
  data = read_csv.read_csv('data.csv')

  # data = list(filter(lambda item : item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  porcentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, porcentages)

  country = input('Elegite el pais ==> ')
  country_name = country 
  #use country to send to generate_bar_chart
  #send country_name just the string to generate_bar_chart to create the file name

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    print(labels, values) 
    charts.generate_bar_chart(country_name, labels, values)
  

if __name__ == '__main__':
  run()