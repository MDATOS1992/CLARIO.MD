#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLARIO - Módulo de Análisis de Tendencias
Autor: Tu Nombre
Fecha: 2024
Descripción: Módulo para analizar tendencias y patrones en los datos
"""

# Importar módulos necesarios
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

class AnalizadorTendencias:
    """
    Clase para analizar tendencias y patrones en los datos.
    
    ¿Qué hace esta clase? Es como un "científico de datos" que:
    1. Recibe datos procesados y limpios
    2. Los analiza para encontrar patrones
    3. Identifica tendencias importantes
    4. Genera insights (conocimientos) útiles
    """
    
    def __init__(self):
        """
        Constructor de la clase AnalizadorTendencias.
        """
        self.nombre = "Analizador de Tendencias CLARIO"
        self.version = "1.0"
        self.metricas_disponibles = [
            "crecimiento",
            "estacionalidad",
            "correlaciones",
            "predicciones_basicas"
        ]
    
    def calcular_crecimiento_tendencia(self, datos):
        """
        Función que calcula el crecimiento de una tendencia en el tiempo.
        
        ¿Qué es "crecimiento"? Es como medir si algo está aumentando,
        disminuyendo o se mantiene igual en el tiempo.
        """
        print("📈 Calculando crecimiento de tendencias...")
        
        # Agrupar datos por tendencia y calcular crecimiento
        resultados = {}
        
        for tendencia in datos['tendencia'].unique():
            # Obtener datos de esta tendencia específica
            datos_tendencia = datos[datos['tendencia'] == tendencia].sort_values('fecha')
            
            if len(datos_tendencia) > 1:
                # Calcular crecimiento (último valor - primer valor)
                primer_valor = datos_tendencia.iloc[0]['popularidad']
                ultimo_valor = datos_tendencia.iloc[-1]['popularidad']
                crecimiento = ultimo_valor - primer_valor
                porcentaje_crecimiento = (crecimiento / primer_valor) * 100
                
                resultados[tendencia] = {
                    'crecimiento_absoluto': crecimiento,
                    'crecimiento_porcentual': porcentaje_crecimiento,
                    'tendencia': 'creciente' if crecimiento > 0 else 'decreciente' if crecimiento < 0 else 'estable'
                }
        
        return resultados
    
    def identificar_tendencias_emergentes(self, datos, umbral_crecimiento=10):
        """
        Función que identifica tendencias que están creciendo rápidamente.
        
        ¿Qué es "emergente"? Es algo que está apareciendo o creciendo
        muy rápido, como una nueva moda que se vuelve popular.
        """
        print(f"�� Identificando tendencias emergentes (umbral: {umbral_crecimiento}%)...")
        
        # Calcular crecimiento de todas las tendencias
        crecimiento_tendencias = self.calcular_crecimiento_tendencia(datos)
        
        # Filtrar solo las que crecen más del umbral
        tendencias_emergentes = {}
        
        for tendencia, datos_crecimiento in crecimiento_tendencias.items():
            if datos_crecimiento['crecimiento_porcentual'] > umbral_crecimiento:
                tendencias_emergentes[tendencia] = datos_crecimiento
        
        return tendencias_emergentes
    
    def analizar_estacionalidad(self, datos):
        """
        Función que analiza si hay patrones que se repiten en el tiempo.
        
        ¿Qué es "estacionalidad"? Es como las estaciones del año:
        - Verano = más ropa ligera
        - Invierno = más ropa abrigada
        - Es algo que se repite cada año
        """
        print("🌍 Analizando patrones estacionales...")
        
        # Agregar mes a los datos
        datos_con_mes = datos.copy()
        datos_con_mes['mes'] = datos_con_mes['fecha'].dt.month
        
        # Calcular popularidad promedio por mes
        popularidad_por_mes = datos_con_mes.groupby('mes')['popularidad'].mean()
        
        # Identificar meses con mayor y menor popularidad
        mes_mas_popular = popularidad_por_mes.idxmax()
        mes_menos_popular = popularidad_por_mes.idxmin()
        
        # Nombres de los meses
        nombres_meses = {
            1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
            5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
            9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
        }
        
        print(f"📅 Mes con mayor popularidad: {nombres_meses[mes_mas_popular]} ({popularidad_por_mes[mes_mas_popular]:.2f})")
        print(f"📅 Mes con menor popularidad: {nombres_meses[mes_menos_popular]} ({popularidad_por_mes[mes_menos_popular]:.2f})")
        
        return {
            'mes_mas_popular': mes_mas_popular,
            'mes_menos_popular': mes_menos_popular,
            'popularidad_por_mes': popularidad_por_mes.to_dict()
        }
    
    def generar_insights(self, datos):
        """
        Función que genera insights (conocimientos) útiles de los datos.
        
        ¿Qué es un "insight"? Es como una "revelación" o "descubrimiento"
        que te ayuda a entender mejor lo que está pasando.
        """
        print("�� Generando insights de los datos...")
        
        insights = []
        
        # Insight 1: Tendencia más popular
        tendencia_mas_popular = datos.loc[datos['popularidad'].idxmax()]
        insights.append(f"🏆 La tendencia más popular es '{tendencia_mas_popular['tendencia']}' con una popularidad de {tendencia_mas_popular['popularidad']}")
        
        # Insight 2: Tendencia emergente
        tendencias_emergentes = self.identificar_tendencias_emergentes(datos)
        if tendencias_emergentes:
            tendencia_emergente = list(tendencias_emergentes.keys())[0]
            insights.append(f"🚀 '{tendencia_emergente}' es una tendencia emergente que está creciendo rápidamente")
        
        # Insight 3: Análisis de fuentes
        fuente_mas_confiable = datos.groupby('fuente')['popularidad'].mean().idxmax()
        insights.append(f"📱 '{fuente_mas_confiable}' es la fuente de datos más confiable")
        
        # Insight 4: Variabilidad de popularidad
        variabilidad = datos['popularidad'].std()
        if variabilidad < 10:
            insights.append("📊 Las tendencias tienen popularidad muy estable")
        elif variabilidad < 20:
            insights.append("📊 Las tendencias tienen popularidad moderadamente variable")
        else:
            insights.append("📊 Las tendencias tienen popularidad muy variable")
        
        return insights
    
    def crear_reporte_tendencias(self, datos):
        """
        Función que crea un reporte completo de tendencias.
        
        ¿Qué es un "reporte"? Es como un "resumen ejecutivo" que
        condensa toda la información importante en pocas páginas.
        """
        print("�� Creando reporte de tendencias...")
        
        # Generar todos los análisis
        crecimiento = self.calcular_crecimiento_tendencia(datos)
        estacionalidad = self.analizar_estacionalidad(datos)
        insights = self.generar_insights(datos)
        
        # Crear reporte
        reporte = {
            'fecha_generacion': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'resumen_ejecutivo': {
                'total_tendencias': len(datos['tendencia'].unique()),
                'periodo_analisis': f"{datos['fecha'].min().strftime('%d/%m/%Y')} - {datos['fecha'].max().strftime('%d/%m/%Y')}",
                'fuentes_analizadas': list(datos['fuente'].unique())
            },
            'analisis_crecimiento': crecimiento,
            'analisis_estacionalidad': estacionalidad,
            'insights': insights
        }
        
        # Guardar reporte en formato JSON
        nombre_archivo = f"data/reporte_tendencias_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(reporte, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"✅ Reporte guardado en: {nombre_archivo}")
        return reporte

def probar_analizador():
    """
    Función para probar el analizador de tendencias.
    """
    print("📈 Probando Analizador de Tendencias de CLARIO...")
    print("=" * 70)
    
    # Crear un objeto de la clase AnalizadorTendencias
    analizador = AnalizadorTendencias()
    
    # Mostrar información del analizador
    print(f"�� {analizador.nombre}")
    print(f"📅 Versión: {analizador.version}")
    print(f"📊 Métricas disponibles: {', '.join(analizador.metricas_disponibles)}")
    print()
    
    # Crear datos de ejemplo (simulando que vienen del procesador)
    datos_ejemplo = pd.DataFrame({
        'fecha': pd.date_range('2024-01-01', periods=30, freq='D'),
        'tendencia': ['Streetwear'] * 10 + ['Vintage'] * 10 + ['Minimalista'] * 10,
        'popularidad': np.random.randint(60, 95, 30),
        'categoria': ['Ropa'] * 30,
        'fuente': ['Instagram', 'Twitter'] * 15
    })
    
    print("📋 Datos de ejemplo para análisis:")
    print(datos_ejemplo.head())
    print()
    
    # Analizar crecimiento de tendencias
    crecimiento = analizador.calcular_crecimiento_tendencia(datos_ejemplo)
    print("📈 Análisis de crecimiento:")
    for tendencia, datos in crecimiento.items():
        print(f"   {tendencia}: {datos['crecimiento_porcentual']:.2f}% ({datos['tendencia']})")
    print()
    
    # Identificar tendencias emergentes
    emergentes = analizador.identificar_tendencias_emergentes(datos_ejemplo)
    print("🚀 Tendencias emergentes:")
    for tendencia in emergentes:
        print(f"   {tendencia}")
    print()
    
    # Analizar estacionalidad
    estacionalidad = analizador.analizar_estacionalidad(datos_ejemplo)
    print()
    
    # Generar insights
    insights = analizador.generar_insights(datos_ejemplo)
    print("�� Insights generados:")
    for i, insight in enumerate(insights, 1):
        print(f"   {i}. {insight}")
    print()
    
    # Crear reporte completo
    reporte = analizador.crear_reporte_tendencias(datos_ejemplo)
    print("🎯 Análisis de tendencias completado exitosamente!")

# Punto de entrada para pruebas
if __name__ == "__main__":
    probar_analizador()