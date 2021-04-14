#Funciones que usa armen
def extraerFecha_0(fech):
    o=fech.replace('-','/')
    o=o.split('/')
    fecha_final_0_aux=Logic(o)
    fecha_final_0='/'.join(fecha_final_0_aux)
    return fecha_final_0

def extraerFecha_1(fech): 
    a=fech.split('-')
    meses = {'ene': '01', 'feb' : '02', 'mar' : '03', "abr" : '04', 'may':'05', 'jun': '06', 'jul':'07', 'ago':'08', 'set':'09', 'oct':'10','nov':'11', 'dic':'12' }
    a[1]=meses[a[1]]
    fecha_final_aux=Logic(a)
    fecha_final='/'.join(fecha_final_aux)
    return fecha_final

def extraerFecha_2(fech):
    b=fech.split(' ')
    Meses = {'enero': '01', 'febrero' : '02', 'marzo' : '03', "abril" : '04', 'mayo':'05', 'junio': '06', 'julio':'07', 'agosto':'08', 'septiembre':'09', 'octubre':'10','noviembre':'11', 'diciembre':'12' }
    b[2]=Meses[b[2]]
    
    for i in range(2):      #Eliminar lo "de" 
     b.remove("de")
    fecha_final_2_aux=Logic(b)
    fecha_final_2='/'.join(fecha_final_2_aux)
    return fecha_final_2

def extraerFecha_3(fech):
    c=fech.split(' ')
    MESES = {'Enero': '01', 'Febrero' : '02', 'Marzo' : '03', "Abril" : '04', 'Mayo':'05', 'Junio': '06', 'Julio':'07', 'Agosto':'08', 'Septiembre':'09', 'Octubre':'10','Noviembre':'11', 'Diciembre':'12' }
    c[1]=MESES[c[1]]
    fecha_final_3_aux=Logic(c)
    fecha_final_3='/'.join(fecha_final_3_aux)
    return fecha_final_3

def Logic(dato): #Funcion para evitar resultados ilógicos.
    if float(dato[0])>31 or float(dato[1])>12 or  float(dato[2])>2025:
         vuelta=["error"]
    else:
        vuelta=dato
    return vuelta









if __name__ == "__main__":
    print(extraerFecha_0("12-08-2012"))
    print(extraerFecha_0("15/02/2020"))
   
