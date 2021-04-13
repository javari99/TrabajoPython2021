#Funciones que usa armen
def extraerFecha_1(fech): 
    a=fech.split('-')
    meses = {'ene': '01', 'feb' : '02', 'mar' : '03', "abr" : '04', 'may':'05', 'jun': '06', 'jul':'07', 'ago':'08', 'set':'09', 'oct':'10','nov':'11', 'dic':'12' }
    a[1]=meses[a[1]]
    fecha_final='/'.join(a)
    return fecha_final

def extraerFecha_2(fech):
    b=fech.split(' ')
    Meses = {'enero': '01', 'febrero' : '02', 'marzo' : '03', "abril" : '04', 'mayo':'05', 'junio': '06', 'julio':'07', 'agosto':'08', 'septiembre':'09', 'octubre':'10','noviembre':'11', 'diciembre':'12' }
    b[2]=Meses[b[2]]
    b[1]='/'
    b[3]='/'
    fecha_final_2=''.join(b)
    return fecha_final_2

def extraerFecha_3(fech):
    c=fech.split(' ')
    MESES = {'Enero': '01', 'Febrero' : '02', 'Marzo' : '03', "Abril" : '04', 'Mayo':'05', 'Junio': '06', 'Julio':'07', 'Agosto':'08', 'Septiembre':'09', 'Octubre':'10','Noviembre':'11', 'Diciembre':'12' }
    c[1]=MESES[c[1]]
    fecha_final_3='/'.join(c)
    return fecha_final_3










if __name__ == "__main__":
    print(extraerFecha_3("15 Enero 2020"))