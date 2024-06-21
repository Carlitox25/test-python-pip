import utils
import read_csv
import charts
import pandas

# En la clase de Pandas, reescribimos el código para ser utilizado con la librería Pandas

def run():
  '''
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  
  '''
  
  #Realizamos el ajuste de código con Pandas
  # En Pandas se utliza los "dataFrames" (df) 
  df = pandas.read_csv('data.csv')
  # Para filtrar:
  df = df[df['Continent'] == 'South America']
  #Para obtener la lista de paises y sus porcentajes:
  paises = df['Country'].values
  porcentajes = df['World Population Percentage'].values

  charts.generate_pie_chart(paises, porcentajes)

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    print(labels,values)
    charts.generate_bar_chart(labels, values)
  

if __name__ == '__main__':
  run()

