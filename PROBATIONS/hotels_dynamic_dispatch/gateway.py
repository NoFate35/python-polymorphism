KOSTROVOK_FEE = 0.12
BOOKKING_CONVERT_RATE = 75

# BEGIN (write your solution here)
import copy
class Calculator:
	def __init__(self, service):
		self.service = service()
	def calculate(self, cost):
		return self.service.calculate(cost)

class Kostrovok:
		def calculate(self, cost):
			#print('cost', cost, 'cost+', cost + cost * KOSTROVOK_FEE)
			return cost + cost * KOSTROVOK_FEE

class Booking:
		def calculate(self, cost):
			return cost * BOOKKING_CONVERT_RATE

class Airdnb:
		def calculate(self, cost):
			return cost * 1
			
		
def find_all_matching(data, predicates):
    SERVISCES = {
        'kostrovok': Kostrovok,
        'book-king': Booking,
        'airdnb': Airdnb
    }
    print('predicates.gateway', predicates)
    max = predicates['max']
    min = predicates['min']
        
    filter_data = []
    for offer in data:
        for part in offer['hotels']:
            #print('service', offer['service'], 'max', max, 'min', min, 'part.cost', part['cost'], 'SERVICEcount', SERVISCES[offer['service']], 'total', Calculator(SERVISCES[offer['service']]).calculate(part['cost']))
            normalize_cost = Calculator(SERVISCES[offer['service']]).calculate(part['cost'])
            if min <= normalize_cost <= max:
                hotel = {}
                hotel['hotel'] = copy.deepcopy(part)
                hotel['hotel']['cost'] = normalize_cost
                hotel['service'] = offer['service']
                filter_data.append(hotel)
    #print('max', max, 'min', min, 'filter_data', sorted(filter_data, key=lambda hotel:hotel['hotel']['cost'] )[0])
    return sorted(filter_data, key=lambda hotel:hotel['hotel']['cost'] )[0]
# END
