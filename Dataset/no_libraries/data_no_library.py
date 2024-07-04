import csv
with open("Dataset\Online Sales Data.csv","r") as file:
    listaDatos = []
    reader = csv.reader(file)
    for row in reader:
        listaDatos.append(row)
    columnas_numericas = [columna[4:7] for columna in listaDatos[1:]]
    
    
    primera_columna = []
    segunda_columna = []
    tercera_columna = []
    for value in columnas_numericas:
        primera_columna.append(value[0])
        segunda_columna.append(value[1])
        tercera_columna.append(value[2])
          
    int_primera = []
    int_segunda = []
    int_tercera = []
        
        
    for valor in primera_columna:
        try:
            int_primera.append(float(valor))
        except ValueError:
           int_primera.append(None)
               
    mean = sum(valor for valor in int_primera if valor is not  None) / len([valor for valor in int_primera if valor is not None])
        
    processed_list = []
    for valor in int_primera:
        if valor is None:
            processed_list.append(mean)
        else:
            processed_list.append(str(valor))
                
    print(primera_columna)
    print(processed_list)
    print(listaDatos)
               
               
            #if v == "" or v == None or v == 0:  
            #else:
             #   v = int(v)
    
                    
                
        
        
    #for index,value in enumerate(listaDatos):
     #   print(listaDatos[index][0])    newRow = row.split(",")
        

        