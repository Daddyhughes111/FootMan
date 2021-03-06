import random

CITIES_BRITAIN = ['London', 'Cardiff', 'Dublin', 'Edinburgh', 'Manchester', 'Southampton', 'Liverpool', 'Bristol', 'Leeds', 'Cambridge', 'Glasgow']
CITIES_SCANDINAVIA = ['Copenhagen', 'Aarhus', 'Oslo' 'Bergen', 'Trondheim', 'Gothenburg', 'Malmö', 'Stockholm', 'Helsinki', 'Tampere', 'Jyväskylä', 'Reykjavík', 'Tórshavn']
CITIES_GERMAN = ['Berlin', 'Munich', 'Hamburg', 'Dortmund', 'Essen', 'Hanover', 'Bremen', 'Düsseldorf' 'Vienna', 'Salzburg', 'Graz', 'Bern', 'Zürich', 'Basel']

def team_picker():
    animals = ['Dragons', 'Lions', 'Cats', 'Lynxes', 'Tigers', 'Sharks', 'Jaguars', 'Panthers', 'Cobras', 'Bisons', 'Alligators', 'Scorpions', 'Honey-Badgers', 'Piranhas', 'Porcupines', 'Warthogs', 'Wolves', 'Zebras', 'Spiders', 'Vipers', 'Eagles', 'Gorillas']

    regions = ['britain', 'scandinavia', 'german']
    city = random.choice(regions)
    if city == 'britain':
        city = random.choice(CITIES_BRITAIN)
    elif city == 'scandinavia':
        city = random.choice(CITIES_SCANDINAVIA)
    else:
        city = random.choice(CITIES_GERMAN)

    teamname = city + ' ' + random.choice(animals)
    return teamname