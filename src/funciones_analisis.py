import pandas as pd
import numpy as np
from scipy import stats
import joblib
import os

def cargar_datos(ruta):
    """Carga datos de forma flexible (detecta .csv o .xlsx)."""
    _, ext = os.path.splitext(ruta)
    return pd.read_csv(ruta) if ext == '.csv' else pd.read_excel(ruta)

def filtrar_reporte(df, area):
    """Filtra columnas según necesidad operativa o ambiental."""
    if area == 'operaciones':
        return df[['fecha_registro', 'planta', 'DBO_salida_mg_L', 'caudal_entrada_m3_d']]
    return df[['fecha_registro', 'planta', 'DBO_salida_mg_L', 'cumplimiento_norma']]

def analizar_calidad(df, columna):
    """Detecta anomalías usando Z-Score (SciPy) y maneja robustez con NumPy."""
    datos_limpios = df[columna].replace([np.inf, -np.inf], np.nan).dropna()
    return stats.zscore(datos_limpios)

def guardar_modelo(objeto, nombre_archivo):
    """Persiste objetos complejos usando Joblib."""
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    joblib.dump(objeto, f'outputs/{nombre_archivo}.pkl')