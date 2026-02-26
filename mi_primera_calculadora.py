print("==================================================")
print("                  CACULADORA                      ")
print("==================================================")

#bucle
while True:
    
    primer_numero = int(input('ingrese el primer numero:'))
    
    print('''
      operaciones.
      para x² segundo numero 0
      
      1) +
      2) -
      3) X
      4) /
      5) //
      6) x² 
    ''')

    operacion = int(input('operacion que desea realizar:\n'))
   
    segundo_numero = int(input('ingrese el segundo numero:\n'))
    
    if operacion ==1:
        print(f'resultado = {primer_numero + segundo_numero}')
        
    elif operacion ==2:
        print(f'resultado = {primer_numero - segundo_numero}')
        
    elif operacion ==3:
        print(f'resultado = {primer_numero * segundo_numero}')
        
    elif operacion ==4:
        print(f'resultado = {primer_numero / segundo_numero}')
        
    elif operacion ==5:
        print(f'resultado = {primer_numero // segundo_numero}')
       
    elif operacion ==6:
        print(f'resultado = { primer_numero * primer_numero}')
        
    salir =input('salir: y/n?\n').lower()
    
    if salir == 'y':
        print('CERRANDO...')
        break
        
    elif salir == 'n':
        print('siguiente operacion.')
    
    
        
        