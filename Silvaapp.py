from tkinter   import *         
from tkinter import ttk       
from tkinter import messagebox           
import requests 
import json
from threading import Thread      
import queue
import os       
from tkinter import filedialog         
from clienteID import cliente_ID
  


       

class Frame_Inicial():   
   def __init__(self):       
      self.root=Tk()                
      self.root.title("Silvaap")     # Título de la ventana 
      self.root.iconbitmap('C:/escritorio/Python/proyectoaplicacion/creadororiginal.ico')  # Icono de la ventana, en ico o xbm en Linux

      self.mi_frame=Frame(self.root,width=600,height=400)         
          
      self.mi_frame.pack(fill="both",expand=True)            
      self.miImagen=PhotoImage(file="C:/escritorio/Python/proyectoaplicacion/cabezalea.png")    
      self.labelimagen=Label(self.mi_frame,image=self.miImagen).place(x=0,y=50)         

      
             
                 
      self.params = cliente_ID()     
      self.i=0       
      self.directorio=""      
      self.archivo_guardado=""           
   def guarda_archivo(self,carpeta,my_data):           
      f=open(carpeta,"w")        
      for x in range(0, len(my_data[2])):      
            try:
              f.write('[')
              f.write(str(my_data[2][x]))
              f.write(']')
              f.write(' ')
              f.write('<')
              f.write(str(my_data[0][x]))
              f.write('>')
              f.write(' ')       
              f.write(str(my_data[1][x]))    
               
              f.write("\n")    
            except UnicodeEncodeError:    
              f.write("codigo indefinido")    
              f.write("\n")    

            
      f.close()          


      

                  
   def restaura_frame_inicial(self):         
        self.mi_frame.destroy()          
        self.mi_frame=Frame(self.root,width=600,height=400)        
        self.mi_frame.pack()           
        self.miImagen=PhotoImage(file="C:/escritorio/Python/proyectoaplicacion/cabezalea.png")    
        self.labelimagen=Label(self.mi_frame,image=self.miImagen).place(x=0,y=50)          
        self.params=cliente_ID()       
        self.i=0      
    
   def modifica_frame(self):     
       self.miImagen=PhotoImage(file="C:/escritorio/Python/proyectoaplicacion/cabezaalan.png")          
       self.labelimagen=Label(self.mi_frame,image=self.miImagen).place(x=160,y=0)                    
               
   def crea_frame(self):        
        def muestra_chat(tupla):       
          mitupla=tupla          
          self.mi_frame.destroy()
          self.mi_frame=Frame(self.root,width=600,height=400)          
          self.mi_frame.pack(fill="both",expand=True)           
            
          texto = Text(self.mi_frame,width=100,height=30)        
          
          texto.grid(row=1,column=1,padx=10,pady=10)          
          scroll=Scrollbar(self.mi_frame,command=texto.yview)           
          scroll.grid(row=1,column=2,sticky="nsew")    
                   

          texto.config(yscrollcommand=scroll.set)             
          Button(self.mi_frame,text="volver",bg="light blue",command=volver).grid(row=2,column=2,padx=10,pady=10)  
          texto.insert(INSERT,".....................Silvaapp 1.0........................ ")      
          texto.insert(INSERT,"\n ") 
          texto.insert(INSERT,".........Esta es una aplicacion creada por Diego Enrique Silva.........  ")      
          texto.insert(INSERT,"\n ")       
          texto.insert(INSERT,"\n ")
          for i in range(0,len(mitupla[2])):       
            texto.insert(INSERT,"[")     
            texto.insert(INSERT,mitupla[2][i])       
            texto.insert(INSERT,"]")     
            texto.insert(INSERT," ")   
            texto.insert(INSERT,"<")      
            texto.insert(INSERT,mitupla[0][i])       
            texto.insert(INSERT,">")      
            texto.insert(INSERT," ")    
            texto.insert(INSERT,":")     
            texto.insert(INSERT,mitupla[1][i])      
            texto.insert(INSERT,"\n ")
  
          texto.config(state=DISABLED)        
        my_queue = queue.Queue()

        def storeInQueue(f):
          def wrapper(*args):
            my_queue.put(f(*args))
          return wrapper
              

        @storeInQueue
        def parsea_sever(numero):       
           chat = []
           time = []
           user = []          
           def doubleDigit(num):
            if num < 10 :
              return '0'+str(num)
            else:
              return str(num)       
           try :             

            while True:    
            
            
             if self.i == 0 :
               URL = 'https://api.twitch.tv/v5/videos/'+numero+'/comments?content_offset_seconds=0' 
               self.i += 1
             else:
               URL = 'https://api.twitch.tv/v5/videos/'+numero+'/comments?cursor=' 
               URL +=  nextCursor   
            
       
        
             response = requests.get(URL,params=self.params)     
             response.encoding="KOI8-U"
        
             j=json.loads(response.text)
        
             for k in range(0,len(j["comments"])):
              timer = j["comments"][k]["content_offset_seconds"]
            
              timeMinute = int(timer/60)
            
              if timeMinute >= 60 :
                  timeHour = int(timeMinute/60)
                  timeMinute %= 60
              else :
                  timeHour = int(timeMinute/60)
    
              timeSec = int(timer%60)
            
              time.append(doubleDigit(timeHour)+':'+doubleDigit(timeMinute)+':'+doubleDigit(timeSec))
              user.append(j["comments"][k]["commenter"]["display_name"])
              chat.append(j["comments"][k]["message"]["body"])
       
             if '_next' not in j:
                break
        
             nextCursor = j["_next"]            
            return user,chat,time          
           except   KeyError :           


              messagebox.showinfo(message="¡Numero ID invalido!,por favor, coloque un numero ID valido.", title="Alerta")   
           except requests.exceptions.ConnectionError :           
           	  messagebox.showinfo(message="Error de conexion a internet , por favor revise su conexion a internet e intentelo mas tarde.", title="Alerta")
                
                     
        def ventana_de_carga():     
                     

          self.mi_frame.destroy()         
          self.mi_frame=Frame(self.root,width=500,height=200)          
          self.mi_frame.pack()   
          laraiz.modifica_frame()
                 
          
          label=Label(self.mi_frame,text="Cargando el chat.....")       
          label.place(x=50,y=40)          
                              
          progressbar = ttk.Progressbar(self.mi_frame, mode="indeterminate")
          progressbar.place(x=30, y=60, width=200)
          progressbar.start()        
             
             
                  

                  
        def check_if_done(t):
    # Si el hilo ha finalizado.(parsea server ha finalizado) 
           if not t.is_alive():
             
        #  guarda la informacion obtenida de parsea server
             my_data = my_queue.get()           

             if my_data == None :          
                      
               laraiz.restaura_frame_inicial()
          
               laraiz.crea_frame()           
             else:  
               muestra_chat(my_data)       
               if self.archivo_guardado != "":           
                 laraiz.guarda_archivo(self.archivo_guardado,my_data)  

           else:
        # Si no, volver a chequear en unos momentos.
             schedule_check(t)         
        def schedule_check(t):

          self.root.after(1000, check_if_done, t)           

        
        def ejecuta_funciones(event = None):                   
          numero=cuadro_texto2.get()         
                
          try:          
            if isinstance(int(numero), int)== False :     
              messagebox.showinfo(message="Por favor, Introduzca un numero ID", title="Alerta")  
           
            else:
                       
              t = Thread(target=parsea_sever, args = (numero, ))
              t.start()          

              ventana_de_carga()
              schedule_check(t)
          except ValueError :             
             messagebox.showinfo(message="Por favor, Introduzca un numero ID entero sin comas y puntos ", title="Alerta")           
        
        
        def carpeta():      
          self.directorio=filedialog.askdirectory()     
          if self.directorio != "":   
            os.chdir(self.directorio)      
                   
        def guardar_archivo():     
          self.archivo_guardado=filedialog.asksaveasfilename(initialdir="/desktop",title="Select file",defaultextension=".txt")    
          if self.archivo_guardado == "":     
            pass       
          else:
            archivo=open(self.archivo_guardado,"w")     
              
            archivo.close()                   
        def volver():        
          laraiz.restaura_frame_inicial()            
          laraiz.crea_frame()   

         
 
          
          
 
        
              
             
        Label(self.mi_frame,text="¿ Desea guaradar una copia del chat ?").grid(row=1,column=1,padx=10,pady=10)       

        
        Button(self.mi_frame,text="Guardar archivo",bg="light blue",command=guardar_archivo).grid(row=1,column=2,padx=10,pady=10)   
        Button(self.mi_frame,text="Directorio",bg="salmon",command=carpeta).grid(row=1,column=3,padx=10,pady=10)    
                   

        cuadro_texto2=Entry(self.mi_frame)           
        cuadro_texto2.grid(row=2,column=2,padx=10,pady=10)  
        nombre_cuadro_texto=Label(self.mi_frame,text="ID").grid(row=2,column=1,padx=10,pady=10)              



        Boton_envio=Button(self.mi_frame,text="Enviar",command=ejecuta_funciones)        
        Boton_envio.grid(row=3,column=1,padx=10,pady=10)              
     


        self.root.mainloop()             
laraiz=Frame_Inicial()      
laraiz.crea_frame()        