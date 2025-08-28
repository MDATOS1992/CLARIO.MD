#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLARIO - Plataforma de Análisis de Datos y Tendencias de Mercado
Autor: Tu Nombre
Fecha: 2024
Descripción: Herramienta para recolectar y analizar datos de marcas, moda, 
             consumo de alimentos y tendencias políticas.
"""

# Importar módulos del sistema
import os
import sys
from datetime import datetime

# Importar nuestros módulos personalizados
from src.scraper_basico import ScraperBasico
from src.procesador_datos import ProcesadorDatos
from src.analizador_tendencias import AnalizadorTendencias
from src.dashboard_simple import DashboardSimple

def mostrar_bienvenida():
    """
    Función que muestra un mensaje de bienvenida al usuario.
    """
    print("=" * 60)
    print("🚀 BIENVENIDO A CLARIO - SISTEMA COMPLETO ��")
    print("=" * 60)
    print("Plataforma de Análisis de Datos y Tendencias de Mercado")
    print(f"Fecha de inicio: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 60)

def verificar_estructura_proyecto():
    """
    Función que verifica que todas las carpetas necesarias existan.
    """
    carpetas_requeridas = ['src', 'data', 'config']
    carpetas_faltantes = []
    
    for carpeta in carpetas_requeridas:
        if not os.path.exists(carpeta):
            carpetas_faltantes.append(carpeta)
    
    if carpetas_faltantes:
        print(f"❌ Carpetas faltantes: {carpetas_faltantes}")
        return False
    else:
        print("✅ Todas las carpetas del proyecto están creadas")
        return True

def ejecutar_sistema_completo():
    """
    Función que ejecuta todo el sistema CLARIO.
    """
    print("🔄 Iniciando sistema CLARIO completo...")
    print()
    
    try:
        # PASO 1: Recolección de datos
        print("📡 PASO 1: Recolección de datos...")
        scraper = ScraperBasico()
        scraper.mostrar_info()
        print()
        
        # Simular recolección de datos
        datos_recolectados = []
        for fuente in scraper.fuentes_disponibles:
            datos = scraper.simular_recoleccion(fuente)
            datos_recolectados.append(datos)
        print()
        
        # PASO 2: Procesamiento de datos
        print("🔧 PASO 2: Procesamiento de datos...")
        procesador = ProcesadorDatos()
        datos_ejemplo = procesador.crear_datos_ejemplo()
        datos_limpios = procesador.limpiar_datos(datos_ejemplo)
        analisis_basico = procesador.analizar_datos_basicos(datos_limpios)
        print()
        
        # PASO 3: Análisis de tendencias
        print("📈 PASO 3: Análisis de tendencias...")
        analizador = AnalizadorTendencias()
        crecimiento = analizador.calcular_crecimiento_tendencia(datos_limpios)
        emergentes = analizador.identificar_tendencias_emergentes(datos_limpios)
        insights = analizador.generar_insights(datos_limpios)
        print()
        
        # PASO 4: Creación del dashboard
        print("📊 PASO 4: Creación del dashboard...")
        dashboard = DashboardSimple()
        datos_dashboard = dashboard.crear_datos_ejemplo_dashboard()
        resultado_dashboard = dashboard.crear_dashboard_completo(datos_dashboard)
        print()
        
        print("🎯 ¡SISTEMA CLARIO COMPLETADO EXITOSAMENTE!")
        print("📁 Revisa la carpeta 'data' para ver los archivos generados")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en el sistema: {e}")
        return False

def main():
    """
    Función principal que ejecuta todo el programa.
    """
    print("Iniciando CLARIO...")
    print()
    
    # Mostrar mensaje de bienvenida
    mostrar_bienvenida()
    print()
    
    # Verificar estructura del proyecto
    print("Verificando estructura del proyecto...")
    estructura_ok = verificar_estructura_proyecto()
    print()
    
    if estructura_ok:
        print("🎯 CLARIO está listo para funcionar!")
        print()
        
        # Ejecutar el sistema completo
        exito = ejecutar_sistema_completo()
        
        if exito:
            print()
            print("🚀 ¡FELICITACIONES! Has completado tu primera herramienta de análisis de datos")
            print("�� Próximos pasos:")
            print("   1. Personalizar las fuentes de datos")
            print("   2. Agregar más análisis")
            print("   3. Crear un dashboard web interactivo")
            print("   4. Conectar con APIs reales")
        else:
            print("❌ Hubo un problema en el sistema")
    else:
        print("❌ Hay problemas con la estructura del proyecto")
        print("Por favor, crea las carpetas faltantes")

# Punto de entrada del programa
if __name__ == "__main__":
    main()