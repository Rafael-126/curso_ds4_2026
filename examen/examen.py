"""
Nombre: Rafael Justiniani Uriarte
Fecha: 24/09/2026
IA usada: Claude
Modelo: Sonnet 5
"""

import csv

class Frase:
    def __init__(self, frase, autor):
        self.frase = frase
        self.autor = autor

    def __str__(self):
        return f'"{self.frase}" - {self.autor}'

    def leer_csv(ruta):
        frases = []
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                nueva = Frase(fila["Frase"], fila["Película"])
                frases.append(nueva)
        return frases

    def guardar_csv(ruta, frases):
        with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
            campos = ["frase", "Película"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for frase in frases:
                escritor.writerow({"frase": frase.frase, "Película": frase.autor})

if __name__ == "__main__":
    ruta_csv = "C:\\Users\\rafa_\\Desktop\\curso_python\\curso_ds4_2026\\examen\\frases_consolidadas_ampliadas.csv"
    frases = Frase.leer_csv(ruta_csv)
    for frase in frases:
        print(frase)