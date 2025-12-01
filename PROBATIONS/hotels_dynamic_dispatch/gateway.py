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
    max = predicates['max']
    min = predicates['min']
    filter_data = []
    for offer in data:
        for part in offer['hotels']:
            normalize_cost = Calculator(SERVISCES[offer['service']]).calculate(part['cost'])
            if min <= normalize_cost <= max:
                hotel = {}
                hotel['hotel'] = copy.deepcopy(part)
                hotel['hotel']['cost'] = normalize_cost
                hotel['service'] = offer['service']
                filter_data.append(hotel)
    return sorted(filter_data, key=lambda hotel:hotel['hotel']['cost'] )[0]
# END
