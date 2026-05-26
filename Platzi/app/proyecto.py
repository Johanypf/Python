import read_csv
import utils
import charts


def run():
    data = read_csv.read_csv_2('./data.csv')
    country = input("Type Country => ")

    population = utils.population_by_country(data, country)
    
    labels, values = utils.get_population(population[0])
    charts.generate_bar_chart(labels,values)

if __name__ == '__main__':
    run()