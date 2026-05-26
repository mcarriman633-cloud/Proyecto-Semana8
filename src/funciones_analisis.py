import pandas as pd
import os

def cargar_datos(ruta):
    """Carga los datos detectando el formato por la extensión."""
    _, ext = os.path.splitext(ruta)
    if ext == '.csv':
        return pd.read_csv(ruta)
    else:
        return pd.read_excel(ruta)

def filtrar_reporte(df, area):
    """Genera reportes diferenciados según el área solicitada."""
    if area == 'operaciones':
        cols = ['fecha_registro', 'planta', 'caudal_entrada_m3_d', 'DBO_entrada_mg_L', 
                'DBO_salida_mg_L', 'energia_aeracion_kWh', 'lodos_generados_kg_d']
        return df[cols]
    elif area == 'ambiental':
        cols = ['fecha_registro', 'planta', 'DBO_salida_mg_L', 'cumplimiento_norma']
        return df[cols]
    return df