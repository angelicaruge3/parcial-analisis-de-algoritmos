#Libreria
import json
#Creas diccionario
diccionario={}
#Diccionario con datos
raza ={
  "humanos":[
      { "guerrero":
          {
                "vida": "3",
                "id": "123", 
                "ataque": "40", 
                "defenza": "24", 
                "poder_magico": "volar" 
          }
      },
               
       {"jinete":
           {
                  "vida":"3", 
                  "id": "124", 
                  "ataque": "50", 
                  "defenza": "50", 
                  "poder_magico": "nadar" 
            }
        },        
        
        {"mago":
            {
                   "vida": "3", 
                   "id": "125", 
                   "ataque": "60", 
                   "defenza": "80", 
                   "poder_magico": "camuflaje"
            }
            
        },
        
        {"recolector":
            {
                   "vida": "3", 
                   "id": "126", 
                   "ataque": "90", 
                   "defenza": "70", 
                   "poder_magico": "camuflaje"
            }
        },
               
        {"observador":
            {
                   "vida": "3", 
                   "id": "127", 
                   "ataque": "30", 
                   "defenza": "80", 
                   "poder_magico": "volar"
            }
        }       
  ]
  
  "orcos"[
      { "guerrero":
          {
         "vida": "3", 
         "id": "128", 
         "ataque": "50", 
         "defenza": "90", 
         "poder_magico": "matar"
          }
      },
      
      { "chaman":
          {
                   "vida": "3", 
                   "id": "129", 
                   "ataque": "20", 
                   "defenza": "90", 
                   "poder_magico": "volar"
          }
       }  
  ]
}


#imprimir
print(raza)
#escribir
archivo =open("raza.json", "w")
#guardar json
json.dump(raza,archivo)
#cerrar archivo
archivo.close()

a=["a", "b", "c", "d", "e"]
b=["guerrero", "jinete", "mago","recolector", "observador"]
print(lista(zip(a,b)))

new_dict= {a:b for (a,b) in zip(a,b)}
print(new_dict)


















