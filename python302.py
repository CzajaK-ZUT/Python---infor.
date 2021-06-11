def przeczytaj_miasta(nazwa_pliku):
	lista_miast = []
	with open(nazwa_pliku, encoding = 'utf-8') as plik:
		for linia in plik:
			miasto = linia.strip().upper()
			lista_miast.append(miasto)
	return lista_miast

def zbior_polaczen(miasta):
	s = set()
	for m1 in miasta:
		for m2 in miasta:
			if m1 < m2:
				s.add((m1, m2))
	return s


miasta_a = przeczytaj_miasta("a.txt")
print("a.txt : ", miasta_a)
miasta_b = przeczytaj_miasta("b.txt")
print("b.txt : ", miasta_b)
miasta_c = przeczytaj_miasta("c.txt")
print("c.txt : ", miasta_c)

s1 = zbior_polaczen(miasta_a)
print("s1 : ", s1)
s2 = zbior_polaczen(miasta_b)
print("s2 : ", s2)
s3 = zbior_polaczen(miasta_c)
print("s3 : ", s3)

brak1 = s1 - s2 - s3
brak2 = s2 - s1 - s3
brak3 = s3 - s1 - s2

brak = brak1 | brak2 | brak3

print("braki : ", brak)