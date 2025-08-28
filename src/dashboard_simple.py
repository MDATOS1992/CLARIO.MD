#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLARIO - Módulo de Dashboard Simple
Autor: Tu Nombre
Fecha: 2024
Descripción: Módulo para crear visualizaciones y dashboards de datos
"""

# Importar módulos necesarios
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

class DashboardSimple:
    """
    Clase para crear visualizaciones y dashboards de datos.
    
    ¿Qué hace esta clase? Es como un "diseñador gráfico" que:
    1. Recibe datos procesados y analizados
    2. Los convierte en gráficos bonitos y útiles
    3. Crea un dashboard completo y profesional
    4. Permite al usuario explorar los datos fácilmente
    """
    
    def __init__(self):
        """
        Constructor de la clase DashboardSimple.
        """
        self.nombre = "Dashboard Simple CLARIO"
        self.version = "1.0"
        self.tipos_graficos = [
            "gráfico de barras",
            "gráfico de líneas",
            "gráfico circular",
            "gráfico de dispersión",
            "tabla de datos"
        ]
        
        # Configurar estilo de matplotlib para gráficos más bonitos
        plt.style.use('default')
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.rcParams['font.size'] = 12
    
    def crear_datos_ejemplo_dashboard(self):
        """
        Función que crea datos de ejemplo para demostrar el dashboard.
        """
        print("📊 Creando datos de ejemplo para el dashboard...")
        
        # Crear datos más complejos para visualizaciones
        fechas = pd.date_range('2024-01-01', periods=90, freq='D')
        
        # Datos de tendencias de moda con variación temporal
        datos_moda = {
            'fecha': fechas,
            'streetwear': np.random.normal(75, 15, 90) + np.sin(np.arange(90) * 2 * np.pi / 30) * 10,
            'vintage': np.random.normal(65, 12, 90) + np.cos(np.arange(90) * 2 * np.pi / 30) * 8,
            'minimalista': np.random.normal(80, 10, 90) + np.sin(np.arange(90) * 2 * np.pi / 45) * 12,
            'deportivo': np.random.normal(70, 18, 90) + np.cos(np.arange(90) * 2 * np.pi / 60) * 15
        }
        
        # Convertir a DataFrame
        df_moda = pd.DataFrame(datos_moda)
        
        # Asegurar que los valores estén entre 0 y 100
        for col in ['streetwear', 'vintage', 'minimalista', 'deportivo']:
            df_moda[col] = df_moda[col].clip(0, 100)
        
        print("✅ Datos de ejemplo creados exitosamente")
        return df_moda
    
    def crear_grafico_barras(self, datos, titulo="Gráfico de Barras"):
        """
        Función que crea un gráfico de barras.
        
        ¿Qué es un "gráfico de barras"? Es como un gráfico donde cada barra
        representa una categoría y su altura muestra la cantidad o valor.
        """
        print(f"�� Creando gráfico de barras: {titulo}")
        
        # Crear figura y ejes
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Preparar datos para el gráfico
        categorias = ['Streetwear', 'Vintage', 'Minimalista', 'Deportivo']
        valores = [
            datos['streetwear'].mean(),
            datos['vintage'].mean(),
            datos['minimalista'].mean(),
            datos['deportivo'].mean()
        ]
        
        # Crear el gráfico de barras
        barras = ax.bar(categorias, valores, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
        
        # Personalizar el gráfico
        ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)
        ax.set_ylabel('Popularidad Promedio', fontsize=12)
        ax.set_xlabel('Tendencias de Moda', fontsize=12)
        
        # Agregar valores en las barras
        for barra, valor in zip(barras, valores):
            altura = barra.get_height()
            ax.text(barra.get_x() + barra.get_width()/2., altura + 1,
                   f'{valor:.1f}', ha='center', va='bottom', fontweight='bold')
        
        # Mejorar la apariencia
        ax.grid(axis='y', alpha=0.3)
        ax.set_ylim(0, max(valores) * 1.1)
        
        # Guardar el gráfico
        nombre_archivo = f"data/grafico_barras_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        print(f"✅ Gráfico guardado en: {nombre_archivo}")
        
        # Mostrar el gráfico
        plt.show()
        
        return nombre_archivo
    
    def crear_grafico_lineas(self, datos, titulo="Evolución de Tendencias"):
        """
        Función que crea un gráfico de líneas.
        
        ¿Qué es un "gráfico de líneas"? Es como un gráfico que muestra
        cómo cambia algo en el tiempo, como la temperatura durante el día.
        """
        print(f"�� Creando gráfico de líneas: {titulo}")
        
        # Crear figura y ejes
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Crear el gráfico de líneas para cada tendencia
        ax.plot(datos['fecha'], datos['streetwear'], label='Streetwear', linewidth=2, color='#FF6B6B')
        ax.plot(datos['fecha'], datos['vintage'], label='Vintage', linewidth=2, color='#4ECDC4')
        ax.plot(datos['fecha'], datos['minimalista'], label='Minimalista', linewidth=2, color='#45B7D1')
        ax.plot(datos['fecha'], datos['deportivo'], label='Deportivo', linewidth=2, color='#96CEB4')
        
        # Personalizar el gráfico
        ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)
        ax.set_ylabel('Popularidad', fontsize=12)
        ax.set_xlabel('Fecha', fontsize=12)
        ax.legend(fontsize=12, loc='upper right')
        
        # Mejorar la apariencia
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 100)
        
        # Rotar etiquetas del eje X para mejor legibilidad
        plt.xticks(rotation=45)
        
        # Ajustar el diseño
        plt.tight_layout()
        
        # Guardar el gráfico
        nombre_archivo = f"data/grafico_lineas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        print(f"✅ Gráfico guardado en: {nombre_archivo}")
        
        # Mostrar el gráfico
        plt.show()
        
        return nombre_archivo
    
    def crear_grafico_circular(self, datos, titulo="Distribución de Tendencias"):
        """
        Función que crea un gráfico circular.
        
        ¿Qué es un "gráfico circular"? Es como una pizza donde cada
        rebanada representa una parte del total.
        """
        print(f"🥧 Creando gráfico circular: {titulo}")
        
        # Crear figura y ejes
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Preparar datos para el gráfico
        categorias = ['Streetwear', 'Vintage', 'Minimalista', 'Deportivo']
        valores = [
            datos['streetwear'].sum(),
            datos['vintage'].sum(),
            datos['minimalista'].sum(),
            datos['deportivo'].sum()
        ]
        
        # Colores para cada categoría
        colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        
        # Crear el gráfico circular
        wedges, texts, autotexts = ax.pie(valores, labels=categorias, colors=colores, 
                                         autopct='%1.1f%%', startangle=90)
        
        # Personalizar el gráfico
        ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)
        
        # Mejorar la apariencia del texto
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        # Agregar leyenda
        ax.legend(wedges, categorias, title="Tendencias", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        
        # Ajustar el diseño
        plt.tight_layout()
        
        # Guardar el gráfico
        nombre_archivo = f"data/grafico_circular_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        print(f"✅ Gráfico guardado en: {nombre_archivo}")
        
        # Mostrar el gráfico
        plt.show()
        
        return nombre_archivo
    
    def crear_tabla_resumen(self, datos):
        """
        Función que crea una tabla resumen de los datos.
        
        ¿Qué es una "tabla resumen"? Es como un "resumen ejecutivo"
        que muestra las estadísticas más importantes de los datos.
        """
        print("📋 Creando tabla resumen de datos...")
        
        # Calcular estadísticas para cada tendencia
        resumen = {
            'Tendencia': ['Streetwear', 'Vintage', 'Minimalista', 'Deportivo'],
            'Promedio': [
                datos['streetwear'].mean(),
                datos['vintage'].mean(),
                datos['minimalista'].mean(),
                datos['deportivo'].mean()
            ],
            'Máximo': [
                datos['streetwear'].max(),
                datos['vintage'].max(),
                datos['minimalista'].max(),
                datos['deportivo'].max()
            ],
            'Mínimo': [
                datos['streetwear'].min(),
                datos['vintage'].min(),
                datos['minimalista'].min(),
                datos['deportivo'].min()
            ],
            'Tendencia': [
                'Creciente' if datos['streetwear'].iloc[-1] > datos['streetwear'].iloc[0] else 'Decreciente',
                'Creciente' if datos['vintage'].iloc[-1] > datos['vintage'].iloc[0] else 'Decreciente',
                'Creciente' if datos['minimalista'].iloc[-1] > datos['minimalista'].iloc[0] else 'Decreciente',
                'Creciente' if datos['deportivo'].iloc[-1] > datos['deportivo'].iloc[0] else 'Decreciente'
            ]
        }
        
        # Crear DataFrame del resumen
        df_resumen = pd.DataFrame(resumen)
        
        # Redondear valores numéricos
        df_resumen['Promedio'] = df_resumen['Promedio'].round(2)
        df_resumen['Máximo'] = df_resumen['Máximo'].round(2)
        df_resumen['Mínimo'] = df_resumen['Mínimo'].round(2)
        
        print("📊 Tabla resumen creada:")
        print(df_resumen.to_string(index=False))
        
        # Guardar la tabla como CSV
        nombre_archivo = f"data/tabla_resumen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df_resumen.to_csv(nombre_archivo, index=False)
        print(f"✅ Tabla resumen guardada en: {nombre_archivo}")
        
        return df_resumen
    
    def crear_dashboard_completo(self, datos):
        """
        Función que crea un dashboard completo con todos los gráficos.
        
        ¿Qué es un "dashboard completo"? Es como un "centro de control"
        que muestra toda la información importante en un solo lugar.
        """
        print("��️ Creando dashboard completo...")
        
        # Crear todos los gráficos
        graficos_creados = []
        
        # 1. Gráfico de barras
        grafico_barras = self.crear_grafico_barras(datos, "Popularidad Promedio de Tendencias de Moda")
        graficos_creados.append(grafico_barras)
        
        # 2. Gráfico de líneas
        grafico_lineas = self.crear_grafico_lineas(datos, "Evolución Temporal de Tendencias de Moda")
        graficos_creados.append(grafico_lineas)
        
        # 3. Gráfico circular
        grafico_circular = self.crear_grafico_circular(datos, "Distribución Total de Tendencias de Moda")
        graficos_creados.append(grafico_circular)
        
        # 4. Tabla resumen
        tabla_resumen = self.crear_tabla_resumen(datos)
        
        print(f"�� Dashboard completo creado exitosamente!")
        print(f"�� Gráficos guardados en la carpeta 'data':")
        for grafico in graficos_creados:
            print(f"   - {os.path.basename(grafico)}")
        
        return {
            'graficos': graficos_creados,
            'tabla_resumen': tabla_resumen
        }

def probar_dashboard():
    """
    Función para probar el dashboard simple.
    """
    print("�� Probando Dashboard Simple de CLARIO...")
    print("=" * 70)
    
    # Crear un objeto de la clase DashboardSimple
    dashboard = DashboardSimple()
    
    # Mostrar información del dashboard
    print(f"��️ {dashboard.nombre}")
    print(f"📅 Versión: {dashboard.version}")
    print(f"📈 Tipos de gráficos disponibles: {', '.join(dashboard.tipos_graficos)}")
    print()
    
    # Crear datos de ejemplo
    datos_ejemplo = dashboard.crear_datos_ejemplo_dashboard()
    print("📋 Datos de ejemplo creados para visualización")
    print()
    
    # Crear dashboard completo
    resultado = dashboard.crear_dashboard_completo(datos_ejemplo)
    print()
    
    print("🎯 Dashboard completado exitosamente!")
    print("💡 Los gráficos se han guardado en la carpeta 'data'")
    print("�� Puedes abrir estos archivos para ver las visualizaciones")

# Punto de entrada para pruebas
if __name__ == "__main__":
    probar_dashboard()
    