import json

# JSON con la información de las casas
data = '''
{
  "casa_stark": {
    "padre": "Rickard",
    "hijos": [
      "Benjen",
      "Brandon",
      "Lyanna",
      "Wylla",
      "Eddard"
    ],
    "pareja_wylla": "Jon Snow",
    "perros": {
      "Wylla": "Ghost"
    }
  },
  "casa_tully": {
    "padre": "Hoster",
    "hijos": [
      "Catelyn",
      "Lysa",
      "Edmure"
    ],
    "pareja_catelyn": "Eddard",
    "pareja_lysa": "Robb",
    "perros": {
      "Robb": "Grey Wind",
      "Sansa": "Lady",
      "Arya": "Nymeria",
      "Bran": "Summer",
      "Rickon": "Shaggydog"
    }
  }
}
'''

# Cargar el JSON en un diccionario
casas = json.loads(data)

# Acceder a los datos de la casa Stark
casa_stark = casas["casa_stark"]
padre_stark = casa_stark["padre"]
hijos_stark = casa_stark["hijos"]
pareja_wylla = casa_stark["pareja_wylla"]
perros_stark = casa_stark["perros"]

print("Casa Stark:")
print("Padre:", padre_stark)
print("Hijos:", hijos_stark)
print("Pareja de Wylla:", pareja_wylla)
print("Perros:")
for nombre, perro in perros_stark.items():
    print(nombre, "-", perro)

print()

# Acceder a los datos de la casa Tully
casa_tully = casas["casa_tully"]
padre_tully = casa_tully["padre"]
hijos_tully = casa_tully["hijos"]
pareja_catelyn = casa_tully["pareja_catelyn"]
pareja_lysa = casa_tully["pareja_lysa"]
perros_tully = casa_tully["perros"]

print("Casa Tully:")
print("Padre:", padre_tully)
print("Hijos:", hijos_tully)
print("Pareja de Catelyn:", pareja_catelyn)
print("Pareja de Lysa:", pareja_lysa)
print("Perros:")
for nombre, perro in perros_tully.items():
    print(nombre, "-", perro)
