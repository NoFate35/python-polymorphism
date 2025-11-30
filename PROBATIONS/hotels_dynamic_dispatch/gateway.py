KOSTROVOK_FEE = 0.12
BOOKKING_CONVERT_RATE = 75

# BEGIN (write your solution here)
def find_all_matching(data, predicates):
    SERVISCES = {
        'kostrovok': KOSTROVOK_FEE,
        'book-king': BOOKKING_CONVERT_RATE,
        'airdnb': 1
    }
    if predicates:
        max = predicates['max']
        min = predicates['min']
    filter_data = {}
    print('data', data)
    for offer in data:
        for part in offer['hotels']:
            if min < (part['cost'] * SERVISCES[offer['service']]) < max:
                print('service', offer['service'], 'max', max, 'min', min, 'part.cost', part['cost'], 'SERVICEcount', SERVISCES[offer['service']], 'total', part['cost'] * SERVISCES[offer['service']])
                filter_data['hotel'] = part
                filter_data['service'] = offer['service']

    print('filter_data', filter_data)
# END
