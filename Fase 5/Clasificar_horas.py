
#horas trabajadas durante la semana "matriz"
#nombre, lunes, martes, miercoles, jueves, viernes
recursos = [
    ["sebas", 8, 6, 8, 6, 9],
    ["carlos", 7, 5, 8, 5, 7],
    ["luis", 9, 9, 5, 9, 8],
    ["brayan", 8, 8, 8, 8, 8],
    ["marta", 5, 6, 9, 9, 9]
]
#funcion para clasificar las horas de trabajo 

def clasificarhoras (horastrabajadas):
    #aqui se clasifican y se calculan las horas trabajadas 
    totalhoras=0
    
    for hora in horastrabajadas:
        totalhoras = sum(horastrabajadas)
        
    if totalhoras >= 40:
        clasificacion = "sobretiempo"
    else:
        clasificacion = "horario estandar"
        
    return totalhoras, clasificacion 

#se suma las horas trabajadas y su clasificacion 

for recurso in recursos:
    nombre = recurso[0]
    horastrabajadas = recurso[1:]
    totalhoras, clasificacion = clasificarhoras(horastrabajadas)

# ya aqui es para imprimir 
    print(f"{nombre} trabajó un total de {totalhoras} horas ")
    print(f"su clasificación es: {clasificacion}")
    