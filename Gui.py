from tkinter import *
import time
import PIL
import sqlite3
import form # importando las varibables y funciones de otro codigo que ya habia hecho


# Base de Datos. Table de los datos de los ciclistas

conn = sqlite3.connect('Ciclistaslocos.db')
tablesCreation = conn.cursor()
# Nota: el nombre de la base de datos simplemente me quede sin ideas ;)
tablesCreation.execute (""" CREATE TABLE IF NOT EXISTS Ciclistas (
   
    cedula INT,
    nombre NVARCHAR(100),
    apellido NVARCHAR(100),
    Fecha_de_nacimiento NVARCHAR(100),
    Tipo_de_sangre NVARCHAR(100),
    Size_de_bicicleta NVARCHAR(100),
    Size_de_uniforme NVARCHAR(100),
    Telefono NVARCHAR(100),
    Celular NVARCHAR(100),
    Email NVARCHAR(100),
    Direccion NVARCHAR(100),
    Persona_de_contacto NVARCHAR(100),
    Telefono_de_contacto NVARCHAR(100),
    Fecha_de_registro DATE 
    
    )""")

conn.commit
conn.close





def hovering(hover):


    menus1.etiqueta1["image"] = menus1.C_gestions_icon_white

def hovering2(hover):

    menus1.etiqueta2["image"] = menus1.a_actividades_white



def unhovering(event):
    menus1.etiqueta1["image"] = menus1.C_gestions_icon

def unhovering2(event):
    menus1.etiqueta2["image"] = menus1.a_actividades_icon


def despliegue1():
    
    

    if menus1.menu_desplegable == False and menus1.animation == 0:
        menus1.menu_desplegable = True

        while menus1.animation < 0.2 :
            menus1.animation += 0.01
            if round(menus1.animation,2) == 0.19:
                menus1.animation = 0.2
                     
                   
            menus1.frame_3.place(relheight = 1, relwidth = menus1.animation, rely = 0, relx = 0.04)
            

            menus1.frame_3.update_idletasks()
            menus1.frame_3.update()

            time.sleep(.001)    
            
            


    elif menus1.menu_desplegable == True and menus1.animation == 0.2 :
        menus1.menu_desplegable = False
        
        #animation = 0.2

        while menus1.animation > 0:
            menus1.animation -= 0.01
            if round(menus1.animation,2) == 0.01:
                menus1.animation = 0
                
                

            menus1.frame_3.place(relheight = 1, relwidth = menus1.animation, rely = 0, relx = 0.04)
            

                

            menus1.frame_3.update_idletasks()
            menus1.frame_3.update()
            time.sleep(0.001)
            
            


class menus1 ():

    principal = Tk()
    principal.title("Ciclistas S X A")
    principal.geometry("1200x720")
    principal.configure(background = "#503A99")
    animation = 0

   


    
    #principal.attributes("-topmost", True)
    
    #color de los botones principal
    buttonColor = "#503A99"

    botonesSec = "#3B2A73"

    menu_desplegable = False

    despliegue = 0

    C_gestions_icon = PhotoImage(file=r"D:\Visual Studio Code\Python\Maplicacion5645\icons\grid32b.PNG")
    C_gestions_icon_white = PhotoImage(file=r"D:\Visual Studio Code\Python\Maplicacion5645\icons\grid32.PNG")
    
    reportes = PhotoImage(file =r"D:\Visual Studio Code\Python\Maplicacion5645\icons\bar-chart.PNG")

    about = PhotoImage(file = r"D:\Visual Studio Code\Python\Maplicacion5645\icons\about.PNG")

    salida = PhotoImage(file = r"D:\Visual Studio Code\Python\Maplicacion5645\icons\salida.PNG")


    a_actividades_icon = PhotoImage (file=r"D:\Visual Studio Code\Python\Maplicacion5645\icons\archive32.PNG")
    a_actividades_white = PhotoImage (file=r"D:\Visual Studio Code\Python\Maplicacion5645\icons\archive32W.PNG")

    frame_1 = Frame(principal, bg="#503A99")
    frame_2 = Frame(principal, bg="#281C4D")
    frame_3 = Frame(principal, bg= "#3B2A73")

    etiqueta1 = Button(frame_1, text= "Gestionar ciclista", bg = buttonColor, image = C_gestions_icon, command = despliegue1, relief = FLAT )
    etiqueta2 = Button(frame_1, text= "Gestionar Actividades",bg = buttonColor, image = a_actividades_icon, relief = FLAT )
    etiqueta3 = Button(frame_1, text= "Reporte",bg = buttonColor, image = reportes, relief = FLAT)
    etiqueta4 = Button(frame_1, text= "Acerca de",bg = buttonColor, image = about, relief = FLAT)
    etiqueta5 = Button(frame_1, text= "Salir",bg = buttonColor, image = salida, relief = FLAT)


    subMenu = Button(frame_3, text ="Ver listado de ciclistas", bg= botonesSec, relief = FLAT, )
    subMenu2 = Button(frame_3, text = "Agregar Ciclistas", bg = botonesSec, relief = FLAT, command = form.formulario)
    subMenu3 = Button(frame_3, text = "Editar Ciclistas", bg = botonesSec, relief = FLAT)
    subMenu4 = Button(frame_3, text = "Eliminar Ciclistas", bg = botonesSec, relief = FLAT)





def menu_update():

    menus1.frame_1.place(relheight = 1, relwidth = 0.04, rely = 0, relx = 0)

    menus1.frame_2.place(relheight = 1, relwidth = 1, rely = 0, relx = 0.04)
    
    # Frame del menu desplegable

    menus1.frame_3.place(relheight = 1, relwidth = menus1.despliegue, rely = 0, relx = 0.04)

    # ajustes de Menu Principal
    menus1.etiqueta1.place( rely = 0.1, relx = 0.1)
    menus1.etiqueta2.place( rely = 0.2, relx = 0.1)
    menus1.etiqueta3.place( rely = 0.3, relx = 0.1)
    menus1.etiqueta4.place( rely = 0.4, relx = 0.1)
    menus1.etiqueta5.place( rely = 0.5, relx = 0.1)
    
    # ajustes de sub-menu de ciclistas
    menus1.subMenu.place(rely = 0.1, relx = 0.1)
    menus1.subMenu2.place(rely = 0.2, relx = 0.1)
    menus1.subMenu3.place(rely = 0.3, relx = 0.1)
    menus1.subMenu4.place(rely = 0.4, relx = 0.1)
    
    menus1.etiqueta1.bind("<Enter>", hovering)
    menus1.etiqueta1.bind("<Leave>", unhovering)
    menus1.etiqueta2.bind("<Enter>", hovering2)
    menus1.etiqueta2.bind("<Leave>", unhovering2)

    menus1.principal.mainloop()







            

            













 
menu_update()













