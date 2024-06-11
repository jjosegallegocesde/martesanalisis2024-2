import pandas as pd
from data.generators.generadorCalidadAire import generarDatosCalidadAire
from helpers.generarTabla import crearTablaHTML

import matplotlib.pyplot as plt


#1. PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATFRAME

def construirDataFrameCalidadAire():
    #traigo los datos generados en el mock
    datosCalidadAire=generarDatosCalidadAire()

    #construyo el dataframe
    calidadAireDF=pd.DataFrame(datosCalidadAire, columns=['comuna','ttlpob','muestra','ICA','Fecha','nombre','id'])


    #Limpiando el dataframe

    #1. Limpiando (reemplazando valores)
    #calidadAireDF.replace('-',pd.NA,inplace=True)
    #calidadAireDF.replace('sin',pd.NA,inplace=True)

    #2. Limpiando (eliminando valores)
    calidadAireDF.replace('sin',pd.NA,inplace=True)
    calidadAireDF.dropna(inplace=True)

    #3. Filtrando datos para depurar la informacion
    #FILTRAR DTOS ES OBTENER NUEVOS DATFRAMES
    #AL APLICAR CONDICIONES LOGICAS

    #CONTAR DATOS

    #CONSULTAR DATOS ESPECIFICOS
    #filtroICAPositivo=calidadAireDF.query("(ICA>=20) and (ICA<50)")
    #filtroICAModerado=calidadAireDF.query("(ICA>=50) and (ICA<70)")
    #filtroICAPeligroso=calidadAireDF.query("(ICA>=70)").value_counts()

    #print(filtroICAPositivo)
    #print("\n")
    #print(filtroICAModerado)
    print("\n")
    #print(filtroICAPeligroso)

    #probando...
    
    #crearTablaHTML(calidadAireDF,"calidadAire")

    sumatoria=calidadAireDF.groupby("comuna")["ICA"].mean()
    print(sumatoria)

    # Graficar el promedio de ICA por comuna
    plt.figure(figsize=(20, 10))
    promedio_ICA = calidadAireDF.groupby('comuna')['ICA'].mean()
    promedio_ICA.plot(kind='bar', color='skyblue')
    plt.title('Promedio del Índice de Calidad del Aire por Comuna')
    plt.xlabel('Comuna')
    plt.ylabel('Promedio de ICA')
    plt.xticks(rotation=45)
    plt.grid(True)
    # Guardar la gráfica en un archivo
    plt.savefig('./assets/img/Promedio_ICA_por_Comuna.png', format='png', dpi=300)
    
   
construirDataFrameCalidadAire()