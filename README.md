# Proyecto de Monitoreo: AquaLimpia S.A.

## 1. Objetivos
Desarrollar un flujo de datos eficiente para monitorear el desempeño operativo y ambiental de las plantas de tratamiento de AquaLimpia S.A., asegurando la calidad y el cumplimiento de la normativa.

## 2. Proceso Analítico
El proyecto se organiza bajo una estructura modular para garantizar la reproducibilidad:
- `/data`: Almacena los archivos fuente (.csv, .xlsx).
- `/src`: Contiene los scripts con funciones modulares (`funciones_analisis.py`).
- `/notebooks`: Notebook principal para la ejecución y exploración de los datos.
- `/outputs`: Carpeta donde se guardan los resultados gráficos.

## 3. Resultados
- **Automatización**: Pipeline de carga que detecta automáticamente el formato del archivo de entrada.
- **Visualización**: Dashboard exploratorio (`dashboard_aguas.png`) que grafica el DBO de salida por planta, permitiendo una detección temprana de anomalías.
- **Trazabilidad**: Uso de Git para el control de versiones y gestión de cambios.

## 4. Consideraciones Éticas
Como profesional, me he asegurado de que el análisis sea transparente y verificable. La reproducibilidad de este repositorio evita interpretaciones sesgadas de los datos, contribuyendo a una gestión ambiental responsable que prioriza la salud pública y el cumplimiento normativo sobre cualquier otro interés.