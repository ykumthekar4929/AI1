# config
end_of_file = 'END OF INPUT'

# initialisations
dataset_raw = []
dataset_tree = {}
initial_city =''
goal_city = ''
cities_corpus = []
fringe = []

def format_to_graph():
    global cities_corpus
    filepath = raw_input('Give path of the input file: ')
    input_file = open(filepath)
    for cnt, line in enumerate(input_file):
        if line.strip() != end_of_file.strip():
            dataset_raw.append(line.strip().split(" "))
    for each in dataset_raw:
        cities_corpus.append(each[0].strip())
        cities_corpus.append(each[1].strip())
    cities_corpus =  list(set(cities_corpus))
    for city in cities_corpus:
        paths_from_city = []
        for line in dataset_raw:
            if line[0] == city:
                paths_from_city.append({'destination':line[1], 'distance':int(line[2])})
            elif line [1] == city:
                paths_from_city.append({'destination':line[0], 'distance':int(line[2])})
            else:
                pass
        dataset_tree.update({city:paths_from_city})


def uc_search(current_city):
    global fringe
    while fringe:
        if goal_city == fringe[0][0][-1]:
            break
        else:
            dequed_element = fringe[0]
            del fringe[0]
            dequed_element_children = dataset_tree[dequed_element[0][-1]]
            for item in dequed_element_children:
                if set((item['destination'],)).issubset(dequed_element[0]):
                    pass
                else:
                    record_to_append = [(dequed_element[0] + (item['destination'],)), dequed_element[1] + item['distance']]
                    fringe.append(record_to_append)
            fringe = sorted(fringe, key = lambda x: (int(x[1]), x[0][-1]))
    else:
        fringe = None
    return fringe


def print_input_error(initial_city, goal_city):
    if initial_city == goal_city:
        print "Cities are same"
    elif initial_city not in cities_corpus or goal_city not in cities_corpus:
        print "Either or both of the cities not in dataset"
    show_prompt()


def driver(initial_city):
    global fringe
    if initial_city != goal_city and initial_city in cities_corpus and goal_city in cities_corpus:
        fringe.append([(initial_city,), 0])
        search_result = uc_search(initial_city)
        if search_result is None:
            print "Distance: infinity \nRoute: \nNone"
        else:
            search_result = search_result[0]
            print "Distance: %s"%search_result[1]
            route_points = search_result[0]
            print "Route: "
            for x in range(0,len(route_points) - 1):
                print "%s  %s  %s"%(route_points[x], route_points[x + 1], [item for item in dataset_tree[route_points[x]] if item['destination'] == route_points[x+1]][0]['distance'])
        show_prompt()
    else:
        print_input_error(initial_city, goal_city)


def show_prompt():
    global goal_city
    global fringe
    initial_city = raw_input("Initial city : ")
    goal_city = raw_input("Goal city : ")
    fringe = []
    driver(initial_city)


def main():
    format_to_graph()
    show_prompt()

if __name__ == "__main__":
    main()
