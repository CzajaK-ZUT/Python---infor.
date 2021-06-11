#Wczytanie plików
file_a = open('a.txt', 'r', encoding="utf8")
file_b = open('b.txt', 'r', encoding="utf8")
file_c = open('c.txt', 'r', encoding="utf8")

cities_a = []
cities_b = []
cities_c = []

all_cities = {}

def get_all_combination(cities):
    cities_name = [key for key in cities.keys()]
    combinations = []

    for i in range(len(cities_name)):
        for j in range(i+1, len(cities_name)):
            combinations.append((cities_name[i], cities_name[j]))

    return combinations

def get_combination_bellow(cities, minimum=2):
    city_combinations = get_all_combination(cities)
    combination_bellow = []
    for combination in city_combinations:
        counter = 0

        company1 = cities[combination[0]]
        company2 = cities[combination[1]]

        for company in company1:
            if company in company2:
                counter += 1

        if counter < minimum:
            combination_bellow.append(combination)

    return combination_bellow

#Pobranie z każdego pliku nazw miast i dodanie ich do słownika,
# lub jeżeli już w nim występują dodanie do nich informacji o firmie
for line in file_a:
    city = line.strip().lower()

    if not city:
        continue

    cities_a.append(city)
    all_cities[city] = ['a']
    
for line in file_b:
    city = line.strip().lower()

    if not city:
        continue

    if city in all_cities:
        all_cities[city].append('b')
    else:
        all_cities[city] = ['b']

for line in file_c:
    city = line.strip().lower()

    if not city:
        continue

    if city in all_cities:
        all_cities[city].append('c')
    else:
        all_cities[city] = ['c']

#Pobranie par miast które nie są obsługiwane przez conajmniej dwie firmy
combinations_bellow = get_combination_bellow(all_cities)

#Jeżeli w tablicy są jakieś elementy niektóre pary miast nie są obsługiwane przez conajmniej dwie firm
# i zostają wypisane w przeciwnym razie wiadomo że wszystkie są obsługiwane
if combinations_bellow:
    print('Poniższe pary miast są obsługiwane przez jedną lub mniej firm')
    for combination in combinations_bellow:
        print(f'{combination[0]} - {combination[1]}')
else:
    print('Wszystkie pary miast są obsługiwane przez przynajmniej dwie firmy')