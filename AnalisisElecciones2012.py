import json
sabanas=list()
lista=list()
file_nombre_archivos = open('nombre_archivos.txt')
count = 0
votos_totales = {}
for archivo in file_nombre_archivos:    #Abrir cada archivo
    archivo = archivo.rstrip()
    data = json.load(open(archivo))
    
    for sabana in data['sabanas']:      #Abrir cada sabana
        for partido in sabana['resultados'].keys():       #Contar los votos por partido
            votos_totales[partido] = votos_totales.get(partido, 0) + int(sabana['resultados'][partido])

#         count += 1
#         print(count, sabana['id'], ' '.join([str(i) for i in votos_totales.values()]))

# Separar los votos por partidos de los de coalision
votos_partidos = {p: v for p, v in votos_totales.items() if '_' not in p}
votos_coalision = {c: v for c, v in votos_totales.items() if '_' in c}
# Imprimir resultados
print('Partido - Votos')
for k, v in votos_totales.items():
    print(k, v)

print('Votos por partidos:', sum(votos_partidos.values()))
print('Votos por coalisión:', sum(votos_coalision.values()))
print('Total de votos:', sum(votos_totales.values()))
