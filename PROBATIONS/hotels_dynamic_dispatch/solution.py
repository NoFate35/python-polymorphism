from gateway import find_all_matching


def find_the_cheapest_service(data, predicates=None):
    # BEGIN (write your solution here)
    filter_data = find_all_matching(data, predicates)
    #print('data', data, 'predicates', predicates)
    # END
