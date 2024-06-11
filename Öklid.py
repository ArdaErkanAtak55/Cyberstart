import math

# Noktalar
Noktalar = [(1, 2), (4, 6), (7, 8), (2, 1)]

# Noktalar arası mesafe 
def ÖklidMesafesi(Nokta1, Nokta2):
    return math.sqrt((Nokta2[0] - Nokta1[0])**2 + (Nokta2[1] - Nokta1[1])**2)

# Noktalar arasındaki measfeyi hesaplama
Mesafeler = []

for i in range(len(Noktalar)):
    for j in range(i + 1, len(Noktalar)):
        distance = ÖklidMesafesi(Noktalar[i], Noktalar[j])
        Mesafeler.append(distance)

# Minimum mesafe
min_distance = min(Mesafeler)

print("Minimum mesafe:", min_distance)