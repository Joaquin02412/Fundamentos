ancho_terreno=float(input("ingresar el ancho del terreno en metros"))
largodel_terreno=float(input("Ingresar el largo del terreno en metros"))\

#convertimos el ancho y el largo a centimetros

ancho_terrenoen_cm=ancho_terreno * 100
largo_terrenoen_cm=largodel_terreno * 100

#Procedemos a calcular el area del terreno en cm cuadrados

area_terrenocm2=ancho_terrenoen_cm * largo_terrenoen_cm

area_panel_pastocm2= 60 * 60

panel_necesarios=area_terrenocm2/area_panel_pastocm2

#Procedemos a imprimir el resultado
print(f"Se necesitan {int(panel_necesarios)} paneles de pasto de 60x60 cm para poder cubrir el terreno")
