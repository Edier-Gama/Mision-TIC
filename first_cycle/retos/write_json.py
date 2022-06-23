import json

def run():
    
    
 icr_file = open("_icr.json", "w", encoding="utf-8")
            
 usuarios = [
     
            {
             "nombre":"FELIPE MUNOZ",
             "identificacion":526684,
             "correo":"felipe@ucaldas.edu.co",
             "coordenadas":[{"lat":45},{"lon":52}],
             "zona":"SUR"
            },
            
            {
             "nombre":"CLAUDIA RAMIREZ",
             "identificacion": 95847,
             "correo":"claudia@ucaldas.edu.co",
             "coordenadas":[{"lat":36},{"lon":62}],
             "zona":"NORTE"
            },
            
            {
             "nombre":"ALEJANDRA SIERRA",
             "identificacion": 547215,
             "correo":"alejandra@ucaldas.edu.co",
             "coordenadas":[{"lat":25},{"lon":48}],
             "zona":"ORIENTE"
            }
            
    ]
      
 cadena = json.dumps(usuarios, sort_keys=True, indent=4)
           
 icr_file.write(cadena)
 
 icr_file.close()
 
   
if __name__ == "__main__":
    run()    