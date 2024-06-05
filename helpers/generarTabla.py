#Funcion generica para convertir un DF
#en HTML

def crearTablaHTML(dataFrame,nombreTabla):

    #convertimos el DF en HTML
    archivoHTML=dataFrame.to_html()

    #Abrimos un archivo HTML en una ruta especifica
    archivo=open(f"./tables/{nombreTabla}.html","w")

    #Escribimos la info en el archivo
    archivo.write(
        '''
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>

        ''')
    archivo.write(archivoHTML)
    archivo.write(
        
        '''
        </body>
        </html>  
        '''
    )
    archivo.close()
           

        