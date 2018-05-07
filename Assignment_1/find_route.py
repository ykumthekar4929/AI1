import pprint
from operator import itemgetter
# config
filepath = ('input1.txt')
end_of_file = 'END OF INPUT'
end_of_file_copy = 'END OF INPUT'
pp = pprint.PrettyPrinter(indent=2)
# declarations
input_file = open(filepath)
all_the_paths = []
sample_graph = {}
cities_corpus = []

class path_object(object):
    def __init__(self):
        self.city_one = None
        self.city_two = None
        self.distance = None
    def __unicode__(self):
        return self.city_one


def format_to_graph():
    for cnt, line in enumerate(input_file):
        if line.strip() != end_of_file.strip():
            all_the_paths.append(line.strip().split(" "))
    for each in all_the_paths:
        cities_corpus.append(each[0].strip())
        cities_corpus.append(each[1].strip())
    cities_corpus =  list(set(cities_corpus))
    for city in cities_corpus:
        paths_from_city = []
        for line in all_the_paths:
            if line[0] == city:
                paths_from_city.append({'destination':line[1], 'distance':int(line[2])})
            elif line [1] == city:
                paths_from_city.append({'destination':line[0], 'distance':int(line[2])})
            else:
                pass
        sample_graph.update({city:paths_from_city})


def check_for_goal_city(node_to_check_from):
    for each in current_city_nodes:
        print initial_city, each

def driver(initial_city, goal_city):

    if initial_city != goal_city and initial_city in cities_corpus and goal_city in cities_corpus:
        current_city_nodes = sample_graph.get(initial_city)
        current_city_nodes = sorted(current_city_nodes, key=itemgetter('distance'), reverse=False)
    else:
        print "No route for these cities"





def main():
    format_to_graph()
    initial_city = raw_input("What is your initial_city? ")
    goal_city = raw_input("What is your goal_city? ")
    driver('Luebeck', 'Bremen')

main()
