#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLARIO - Módulo de Procesamiento de Datos
Autor: Tu Nombre
Fecha: 2024
Descripción: Módulo para procesar, limpiar y organizar datos recolectados
"""

# Importar módulos necesarios
import pandas as pd
import numpy as np
from datetime import datetime
import json

class ProcesadorDatos:
    """
    Clase para procesar y limpiar datos recolectados.
    
    ¿Qué hace esta clase? Es como un "limpiador profesional" que:
    1. Recibe datos "sucios" o desorganizados
    2. Los limpia y organiza
    3. Los devuelve listos para analizar
    """
    
    def __init__(self):
        """
        Constructor de la clase ProcesadorDatos.
        """
        self.nombre = "Procesador de Datos CLARIO"
        self.version = "1.0"
        self.tipos_datos_soportados = [
            "texto",
            "números",
            "fechas",
            "categorías"
        ]
    
    def crear_datos_ejemplo(self):
        """
        Función que crea datos de ejemplo para demostrar el procesamiento.
        
        ¿Por qué crear datos de ejemplo? Para poder probar las funciones
        sin tener que recolectar datos reales primero.
        """
        print("📊 Creando datos de ejemplo...")
        
        # Crear datos de ejemplo de tendencias de moda
        datos_moda = {
            'fecha': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
            'tendencia': ['Streetwear', 'Vintage', 'Minimalista', 'Colorido', 'Deportivo'],
            'popularidad': [85, 72, 91, 68, 79],
            'categoria': ['Ropa', 'Ropa', 'Ropa', 'Ropa', 'Ropa'],
            'fuente': ['Instagram', 'Twitter', 'Google Trends', 'Instagram', 'Twitter']
        }
        
        # Crear un DataFrame (tabla de datos) con pandas
        df_moda = pd.DataFrame(datos_moda)
        
        print("✅ Datos de ejemplo creados exitosamente")
        return df_moda
    
    def limpiar_datos(self, datos):
        """
        Función que limpia y organiza los datos.
        
        ¿Qué significa "limpiar"? Es como:
        - Eliminar filas vacías
        - Corregir formatos incorrectos
        - Organizar las columnas
        """
        print("�� Iniciando limpieza de datos...")
        
        # Hacer una copia para no modificar los datos originales
        datos_limpios = datos.copy()
        
        # Eliminar filas con datos faltantes
        filas_antes = len(datos_limpios)
        datos_limpios = datos_limpios.dropna()
        filas_despues = len(datos_limpios)
        
        print(f"�� Filas antes de limpiar: {filas_antes}")
        print(f"📊 Filas después de limpiar: {filas_despues}")
        print(f"��️ Filas eliminadas: {filas_antes - filas_despues}")
        
        # Convertir la columna fecha a formato datetime
        datos_limpios['fecha'] = pd.to_datetime(datos_limpios['fecha'])
        
        # Ordenar por fecha
        datos_limpios = datos_limpios.sort_values('fecha')
        
        print("✅ Limpieza de datos completada")
        return datos_limpios
    
    def analizar_datos_basicos(self, datos):
        """
        Función que hace análisis básicos de los datos.
        
        ¿Qué es "análisis básico"? Es como hacer un "resumen ejecutivo"
        de los datos: cuántos hay, cuáles son los más populares, etc.
        """
        print("�� Iniciando análisis básico de datos...")
        
        # Estadísticas básicas
        total_tendencias = len(datos)
        tendencia_mas_popular = datos.loc[datos['popularidad'].idxmax()]
        promedio_popularidad = datos['popularidad'].mean()
        
        print(f"📊 Total de tendencias: {total_tendencias}")
        print(f"🏆 Tendencia más popular: {tendencia_mas_popular['tendencia']} (Popularidad: {tendencia_mas_popular['popularidad']})")
        print(f"📊 Promedio de popularidad: {promedio_popularidad:.2f}")
        
        # Análisis por fuente
        print("\n📱 Análisis por fuente de datos:")
        analisis_fuente = datos.groupby('fuente')['popularidad'].mean()
        for fuente, popularidad in analisis_fuente.items():
            print(f"   {fuente}: {popularidad:.2f}")
        
        return {
            'total_tendencias': total_tendencias,
            'tendencia_mas_popular': tendencia_mas_popular['tendencia'],
            'popularidad_maxima': tendencia_mas_popular['popularidad'],
            'promedio_popularidad': promedio_popularidad
        }
    
    def guardar_datos_procesados(self, datos, nombre_archivo):
        """
        Función que guarda los datos procesados en un archivo.
        
        ¿Por qué guardar? Para poder usar los datos procesados más tarde
        sin tener que procesarlos de nuevo.
        """
        print(f"💾 Guardando datos procesados en: {nombre_archivo}")
        
        # Crear la ruta completa del archivo
        ruta_archivo = f"data/{nombre_archivo}"
        
        # Guardar como CSV (formato de tabla)
        datos.to_csv(ruta_archivo, index=False)
        
        print(f"✅ Datos guardados exitosamente en: {ruta_archivo}")
        return ruta_archivo

def probar_procesador():
    """
    Función para probar el procesador de datos.
    """
    print("🔧 Probando Procesador de Datos de CLARIO...")
    print("=" * 60)
    
    # Crear un objeto de la clase ProcesadorDatos
    procesador = ProcesadorDatos()
    
    # Mostrar información del procesador
    print(f"🛠️ {procesador.nombre}")
    print(f"📅 Versión: {procesador.version}")
    print(f"�� Tipos de datos soportados: {', '.join(procesador.tipos_datos_soportados)}")
    print()
    
    # Crear datos de ejemplo
    datos_ejemplo = procesador.crear_datos_ejemplo()
    print("📋 Datos de ejemplo:")
    print(datos_ejemplo)
    print()
    
    # Limpiar los datos
    datos_limpios = procesador.limpiar_datos(datos_ejemplo)
    print("📋 Datos después de la limpieza:")
    print(datos_limpios)
    print()
    
    # Analizar los datos
    analisis = procesador.analizar_datos_basicos(datos_limpios)
    print()
    
    # Guardar los datos procesados
    archivo_guardado = procesador.guardar_datos_procesados(datos_limpios, "tendencias_moda_procesadas.csv")
    print()
    
    print("🎯 Procesamiento de datos completado exitosamente!")

# Punto de entrada para pruebas
if __name__ == "__main__":
    probar_procesador()