import json
sabanas=list()
lista=list()
file_nombre_archivos = open('nombre_archivos.txt')
count = 0
votos_totales = {}
votos_totales_revisados = {}
porcentaje={}
votos_entidad = {str(i):{} for i in range(1, 33)}
for archivo in file_nombre_archivos:    #Abrir cada archivo
    archivo = archivo.rstrip()
    data = json.load(open(archivo))
    
    for sabana in data['sabanas']:      #Abrir cada sabana
        if int(sabana['revision']) >= 2:
            for partido in sabana['resultados'].keys():
                votos_totales_revisados[partido]=votos_totales_revisados.get(partido, 0)+int(sabana['resultados'][partido])
        for partido in sabana['resultados'].keys():       #Contar los votos por Entidad
            votos_entidad[sabana['entidad']][partido] = votos_entidad[sabana['entidad']].get(partido, 0) + int(sabana['resultados'][partido])
        for partido in sabana['resultados'].keys():       #Contar los votos por partido
            votos_totales[partido] = votos_totales.get(partido, 0) + int(sabana['resultados'][partido])

#         count += 1
#         print(count, sabana['id'], ' '.join([str(i) for i in votos_totales.values()]))

# Separar los votos por partidos de los de coalicion
votos_partidos = {p: v for p, v in votos_totales.items() if '_' not in p}
votos_coalicion = {c: v for c, v in votos_totales.items() if '_' in c}

votos_partidos_revisados = {p: v for p, v in votos_totales_revisados.items() if '_' not in p}
votos_coalicion_revisados = {c: v for c, v in votos_totales_revisados.items() if '_' in c}
# Imprimir resultados
print("----------------------")
print("Votos explícitos")
print('Partido \t\t Votos')
for k, v in votos_totales.items():
    print(k,"\t\t\t", v)
print('Votos por partidos:\t', sum(votos_partidos.values()))
print('Votos por coalición:\t', sum(votos_coalicion.values()))
print('Total de votos:\t\t', sum(votos_totales.values()))
print("-----------------------")
print("Votos revisados")
print("Partido \t\t Votos")
for k, v in votos_totales_revisados.items():
    print(k,"\t\t\t",v)
print('Votos por partidos:\t', sum(votos_partidos_revisados.values()))
print('Votos por coalición:\t', sum(votos_coalicion_revisados.values()))
print('Total de votos:\t\t', sum(votos_totales_revisados.values()))
print("-----------------------")
for k in votos_totales.keys():
    porcentaje[k]=votos_totales_revisados[k]*100/votos_totales[k]
print("porcentaje de revision")
print("partido \t\t corrupcion")
for k,v in porcentaje.items():
    print(k,"\t\t","{0:.2f}".format(v),"%")
print('Votos por partidos:\t', "{0:.2f}".format(100*sum(votos_partidos_revisados.values())/sum(votos_partidos.values())),"%")
print('Votos por coalición:\t', "{0:.2f}".format(100*sum(votos_coalicion_revisados.values())/sum(votos_coalicion.values())),"%")
print('Total de votos:\t\t', "{0:.2f}".format(100*sum(votos_totales_revisados.values())/sum(votos_totales.values())),"%")
print("-------------------------")
for k, v in votos_entidad.items():
    print(k)
    for i, j in v.items():
        print(i, j)
    print('-'*10)
# Resultados de la gráfica de Votos por Candidatos "NACIONAL"
resultados_candidato = {}
# Agregar las  etiquetas de los coaliciones completas (las que no son subconjuntos de otras)
for coal_1 in votos_coalicion:
    for coal_2 in votos_coalicion:
        if coal_1 != coal_2 and not set(coal_1.split('_')) - set(coal_2.split('_')):
            break
    else:
        resultados_candidato[coal_1] = 0
        
print('votos totales')
for k, v in votos_totales.items():
    print(f"{k:25}{v}")
print(f"{'Suma':25}{sum(votos_totales.values())}")
print('-' * 25)

# Agragar los votos de las coaliciones a los candidatos
for subcoalicion, subvotos in votos_coalicion.items():
    for coalicion in resultados_candidato.keys():
        if subcoalicion[:subcoalicion.find('_')] in coalicion:
            resultados_candidato[coalicion] = resultados_candidato.get(coalicion, 0) + subvotos

print('Contar votos de las coaliciones para los candidatos')
for k, v in resultados_candidato.items():
    print(f"{k:25}{v}")
print('-' * 25)

# Agragar los votos de los partidos a los candidatos
tmp_resultados_candidato = [i for i in resultados_candidato.keys()]
for partido, votos in votos_partidos.items(): 
    print('partido:', partido)  
    for coalicion in tmp_resultados_candidato:
        if partido in coalicion:
            resultados_candidato[coalicion] = resultados_candidato.get(coalicion, 0) + votos
            print(f'Sumar {votos} votos de "{partido}" al candidato "{coalicion}"')
            break
    else:
        resultados_candidato[partido] =  votos
        print(f'Agregar "{partido}" con {votos} votos a los Resultados por Candidatos')  

# Imprimir información        
    for k, v in resultados_candidato.items():
        print(f"-{k:24}{v}")
    print(f"{'Suma acumulada:':25}{sum(resultados_candidato.values())}")
    print('-' * 25)

print('Resultado Final por Candidato')
for k, v in resultados_candidato.items():
    print(f"-{k:24}{v}")
print(f"{'Suma':25}{sum(resultados_candidato.values())}")
