#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLARIO - Módulo de Recolección Básica de Datos
Autor: Tu Nombre
Fecha: 2024
Descripción: Módulo para recolectar datos básicos de diferentes fuentes
"""

# Importar módulos necesarios
import requests
import time
from datetime import datetime

class ScraperBasico:
    """
    Clase para recolectar datos básicos de diferentes fuentes.
    
    ¿Qué es una "Clase"? Es como un "molde" que define cómo debe ser algo.
    Por ejemplo: "Auto" es una clase que define que todos los autos tienen
    ruedas, motor, volante, etc.
    """
    
    def __init__(self):
        """
        Constructor de la clase. Se ejecuta cuando creas un objeto de esta clase.
        
        ¿Qué es "__init__"? Es como el "plan de construcción" de la clase.
        """
        self.nombre = "Scraper Básico de CLARIO"
        self.version = "1.0"
        self.fuentes_disponibles = [
            "Google Trends",
            "Twitter",
            "Instagram",
            "Noticias"
        ]
    
    def obtener_fecha_actual(self):
        """
        Función que obtiene la fecha y hora actual.
        
        ¿Qué es "self"? Es como decir "yo mismo" - se refiere al objeto
        que estás usando de esta clase.
        """
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    def mostrar_info(self):
        """
        Función que muestra información sobre el scraper.
        """
        print(f"🕷️ {self.nombre}")
        print(f"📅 Versión: {self.version}")
        print(f"🕐 Última actualización: {self.obtener_fecha_actual()}")
        print(f"📊 Fuentes disponibles: {len(self.fuentes_disponibles)}")
        print("📋 Lista de fuentes:")
        for i, fuente in enumerate(self.fuentes_disponibles, 1):
            print(f"   {i}. {fuente}")
    
    def simular_recoleccion(self, fuente):
        """
        Función que simula la recolección de datos (por ahora).
        
        ¿Qué significa "simular"? Es como "hacer de cuenta que" - no recolecta
        datos reales todavía, pero muestra cómo funcionará.
        """
        print(f"🔄 Simulando recolección de datos de: {fuente}")
        print("⏳ Esperando 2 segundos...")
        time.sleep(2)  # Espera 2 segundos
        print(f"✅ Datos recolectados exitosamente de: {fuente}")
        return f"Datos de {fuente} - {self.obtener_fecha_actual()}"

def probar_scraper():
    """
    Función para probar el scraper básico.
    """
    print("�� Probando Scraper Básico de CLARIO...")
    print("=" * 50)
    
    # Crear un objeto de la clase ScraperBasico
    scraper = ScraperBasico()
    
    # Mostrar información del scraper
    scraper.mostrar_info()
    print()
    
    # Simular recolección de datos
    print("🔄 Iniciando simulación de recolección...")
    for fuente in scraper.fuentes_disponibles:
        datos = scraper.simular_recoleccion(fuente)
        print(f"📊 {datos}")
        print()
    
    print("�� Simulación completada exitosamente!")

# Punto de entrada para pruebas
if __name__ == "__main__":
    probar_scraper()