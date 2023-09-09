nombre=input("Introduzca su nombre")
apellido=input("Introduzca su apellido")
numeroalumno=input("Introduzca su numero de alumno: ")
comision=input("Introduzca la comision que quiere inscribirse: ")

#Ahora haremos el mensaje de confirmacion una vez obtenido los datos
mensaje=f"La solicitud de inscripcion a la comision{comision} solicitdada por el alumno{apellido}, {nombre} esta siendo procesada."
print(mensaje)
