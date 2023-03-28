def keycalcul(code):
    resultat = 0
    facteur = (7, 3, 1)
    for (position, car) in enumerate(code):
        if car == "<":
            valeur = 0
        elif "0" <= car <= "9":
            valeur = int(car)
        elif "A" <= car <= "Z":
            valeur = ord(car)-55
        else:
            print("Caractère hors bornes")
            break

        resultat += valeur * facteur[position % 3]
    return str(resultat % 10)

# ALL INFOS
names = str(input("Nom : "))
names = names.upper()
names = names.split(" ")
surnames = str(input("Prénom(s) : "))
surnames = surnames.upper()
surnames = surnames.replace("-", "<")
surnames = surnames.replace("é", "e")
surnames = surnames.replace("É", "E")
surnames = surnames.split(" ")
naissance = str(input("Date de naissance : "))
naissance = naissance.split(".")[2][-2:] + naissance.split(".")[1] + naissance.split(".")[0]
sexe = str(input("Sexe (M/F) : "))
dep = str(input("Département : "))
dep1 = "0" + dep
delivrance = str(input("Date de délivrance : "))
delivrance = delivrance.split(".")[1][-2:] + delivrance.split(".")[0]
agent = str(input("Numéro de l'agent : "))
ordre = str(input("Chiffre d'ordre : "))
service = str(input("Numéro de service : "))
key1 = keycalcul(delivrance + dep + service + ordre)
key2 = keycalcul(naissance)

# GENERATION
part1_1 = "IDFRA"
part1_2 = ""
for name in names:
    part1_2 = part1_2 + name + "<"
part1 = part1_1 + part1_2
part2 = dep1 + agent

if len(part1 + part2) <= 36:
    diff1 = 36 - len(part1 + part2)
    mrz1 = str(part1 + "<" * diff1 + part2)
else:
    diff1 = len(part1 + part2) - 36
    mrz1 = str(part1[:36 - diff1 + 1] + "<" + part2)

part3_1 = delivrance + dep + service + ordre + key1
part3_2 = ""
for surname in surnames:
    part3_2 = part3_2 + surname + "<<"
part_3 = part3_1 + part3_2
part_4 = naissance + key2 + sexe

if len(part_3 + part_4) <= 35:
    diff2 = 35 - len(part_3 + part_4)
    mrz2 = str(part_3 + "<" * diff2 + part_4)
else:
    diff2 = len(part_3 + part_4) - 35
    mrz2 = str(part_3[:len(part_3) - diff2] + part_4)


mrz2 = mrz2 + keycalcul(mrz1 + mrz2)

print("")
print("MRZ : \n")
print(mrz1 + "\n" + mrz2)

print("")
print("N De Carte : \n")
print(delivrance + dep + service + ordre)
print("")

