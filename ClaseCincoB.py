def Arch():
    
    print "Introduzca la opcion deseada: "
    print "a) leer "
    print "b) escribir "
    print "\n"
    opcion = raw_input("> ")
    print "Introduzca su nombre de archivo:"
    nombre_archivo = raw_input("> ")


    if opcion == "a":
        leer_archivo = open(nombre_archivo)
        print leer_archivo.read()
        leer_archivo.close()
        return

    elif opcion == "b":
        escribir_archivo = open(nombre_archivo,"a")
        print "Introduzca caracter(es) a escribir:"
        caracter = raw_input("> ")
        escribir_archivo.write(caracter)
        escribir_archivo.close()
        print ("Desea leer los cambios escritos en su archivo?")
        print "a) no "
        print "b) si "

        opcion = raw_input("> ")
        if opcion == "a":
            return
        elif opcion == "b":
            escribir_archivo = open(nombre_archivo)
            print escribir_archivo.read()
            escribir_archivo.close()
        return
