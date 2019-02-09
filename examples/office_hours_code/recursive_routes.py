'''
Using recursion to find the shortest route
'''
NON_STOPS = {
    "San Francisco" : ["Portland", "Seattle", "New York", "Austin", "Boston"],
    "Portland" : ["San Francisco", "Seattle", "Austin"],
    "Seattle" : ["San Francisco", "New York", "Austin", "Boston", "Portland"],
    "New York" : ["San Francisco", "Portland", "Seattle", "Boston", "Miami", "Buffalo"],
    "Buffalo" : ["New York", "Boston"],
    "Austin" : ["Portland", "San Francisco", "Seattle"],
    "Boston" : ["San Francisco", "Seattle", "New York", "Miami", "Buffalo"],
    "Miami" : ["New York", "Boston", "Tampa", "Fort Lauderdale"],
    "Tampa" : ["Miami", "Fort Lauderdale"],
    "Fort Lauderdale" : ["Tampa", "Miami"]
}

def find_routes(route_dict, origin, destination, current_route=[]):
    '''
    Returns a list of possible routes
    '''
    current_route.append(origin)
    if origin == destination:
        print(current_route)
        return
    # Use set to make sure we don't repeat cities
    if len(set(current_route)) < len(current_route):
        return
    # Go over the list of cities reachable from the current origin
    for city in route_dict[origin]:
        # Here is the recursion, note that a copy of current_route is passed, not a pointer
        find_routes(route_dict, city, destination, current_route[:])

def main():
    '''
    Main flow execution
    '''
    find_routes(NON_STOPS, "Buffalo", "New York")

if __name__ == '__main__':
    main()
    