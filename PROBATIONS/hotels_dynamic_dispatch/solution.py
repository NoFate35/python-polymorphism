from gateway import find_all_matching


def find_the_cheapest_service(data, predicates=None):
    # BEGIN (write your solution here)
    if not predicates:
    	predicates = {}
    default = {'max': float('inf'), 'min': -float('inf')}
    new_predicates = {**default, **predicates}
    print('predicates', predicates, 'new_predicates', new_predicates)
    filter_data = find_all_matching(data, new_predicates)
    return filter_data
    #print('data', data, 'predicates', predicates)
    # END
