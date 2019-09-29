import json
sabanas=list()
lista=list()
file_nombre_archivos = open('nombre_archivos.txt')
count = 0
votos_totales = {}
votos_totales_revisados = {}
porcentaje={}
for archivo in file_nombre_archivos:    #Abrir cada archivo
    archivo = archivo.rstrip()
    data = json.load(open(archivo))
    
    for sabana in data['sabanas']:      #Abrir cada sabana
        if int(sabana['revision']) >= 2:
            for partido in sabana['resultados'].keys():
                votos_totales_revisados[partido]=votos_totales_revisados.get(partido, 0)+int(sabana['resultados'][partido])
        for partido in sabana['resultados'].keys():       #Contar los votos por partido
            votos_totales[partido] = votos_totales.get(partido, 0) + int(sabana['resultados'][partido])

#         count += 1
#         print(count, sabana['id'], ' '.join([str(i) for i in votos_totales.values()]))

# Separar los votos por partidos de los de coalision
votos_partidos = {p: v for p, v in votos_totales.items() if '_' not in p}
votos_coalision = {c: v for c, v in votos_totales.items() if '_' in c}

votos_partidos_revisados = {p: v for p, v in votos_totales_revisados.items() if '_' not in p}
votos_coalision_revisados = {c: v for c, v in votos_totales_revisados.items() if '_' in c}
# Imprimir resultados
print("----------------------")
print("Votos explícitos")
print('Partido \t\t Votos')
for k, v in votos_totales.items():
    print(k,"\t\t\t", v)
print('Votos por partidos:\t', sum(votos_partidos.values()))
print('Votos por coalisión:\t', sum(votos_coalision.values()))
print('Total de votos:\t\t', sum(votos_totales.values()))
print("-----------------------")
print("Votos revisados")
print("Partido \t\t Votos")
for k, v in votos_totales_revisados.items():
    print(k,"\t\t\t",v)
print('Votos por partidos:\t', sum(votos_partidos_revisados.values()))
print('Votos por coalisión:\t', sum(votos_coalision_revisados.values()))
print('Total de votos:\t\t', sum(votos_totales_revisados.values()))
print("-----------------------")
for k in votos_totales.keys():
    porcentaje[k]=votos_totales_revisados[k]*100/votos_totales[k]
print("porcentaje de revision")
print("partido \t\t corrupcion")
for k,v in porcentaje.items():
    print(k,"\t\t","{0:.2f}".format(v),"%")
print('Votos por partidos:\t', "{0:.2f}".format(100*sum(votos_partidos_revisados.values())/sum(votos_partidos.values())),"%")
print('Votos por coalisión:\t', "{0:.2f}".format(100*sum(votos_coalision_revisados.values())/sum(votos_coalision.values())),"%")
print('Total de votos:\t\t', "{0:.2f}".format(100*sum(votos_totales_revisados.values())/sum(votos_totales.values())),"%")
