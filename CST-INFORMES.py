# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:45:17 2024

@author: Jesús Garcia Valverde 
"""

import pandas as pd
import os

# Definir el directorio donde están los archivos CSV
directorio_csv = './'
# Listar todos los archivos CSV en el directorio
archivos_csv = [f for f in os.listdir(directorio_csv) if f.endswith('.csv')]

for archivo in archivos_csv:
    ruta_archivo = os.path.join(directorio_csv, archivo)
    
    # Leer el CSV
    df = pd.read_csv(ruta_archivo, sep=',',encoding='utf-8')

    # Asegurarse de que la columna 'Cola' tiene el formato esperado y crear la columna 'Numero_Cola'
    df['Numero_Cola'] = df['Cola'].str.split(' - ').str[0]
    
    # Crear columnas 'Fecha_solo' y 'Hora' basadas en 'Fecha'
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d-%m-%Y %H:%M:%S', dayfirst=True)
    df['Fecha_solo'] = df['Fecha'].dt.date
    df['Hora'] = df['Fecha'].dt.time
    
    incluir_tiempo_espera = df['Numero_Cola'].iloc[0] in ['9120', '9121'] and 'Tiempo Espera' in df.columns
    
    if incluir_tiempo_espera:
        columnas_necesarias = ['Fecha_solo', 'Hora', 'Cola', 'Número', 'DID', 'Evento', 'Tiempo al Habla', 'Numero_Cola', 'Tiempo Espera']
    else:
        columnas_necesarias = ['Fecha_solo', 'Hora', 'Cola', 'Número', 'DID', 'Evento', 'Tiempo al Habla', 'Numero_Cola']
        
    # Guardar el nuevo CSV filtrado en el mismo directorio
    df_filtrado=df[columnas_necesarias]
    nombre_archivo_filtrado = f"filtrado_{df['Cola'].iloc[0]}.csv"
    ruta_archivo_filtrado = os.path.join(directorio_csv, nombre_archivo_filtrado)
    df_filtrado.to_csv(ruta_archivo_filtrado, index=False)

    print(f"Archivo creado: {ruta_archivo_filtrado}")
