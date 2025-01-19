Puedes instalar las librerías necesarias ejecutando:

```bash
pip install yfinance pandas seaborn matplotlib
```

## Descripción del Código

1. **Descarga de datos históricos del indice**:
   - Se descarga la serie histórica mensual de precios de cierre del S&P 500 (`^GSPC`) desde el 31 de diciembre de 1999 hasta el 01 de enero de 2025.

2. **Cálculo de cambios porcentuales mensuales**:
   - Se calculan los retornos mensuales como el cambio porcentual entre precios consecutivos.

3. **Visualización de la distribución de retornos**:
   - Se genera un histograma de los cambios porcentuales con la media y la desviación estándar resaltadas.

4. **Análisis de retornos promedio por mes**:
   - Se calcula y visualiza el retorno mensual promedio de cada mes del año.

5. **Evolución del S&P 500 en 2024**:
   - Se genera una gráfica de línea mostrando la evolución del S&P 500 en los últimos 12 meses.

6. **Análisis de correlación con otros activos**:
   - Se descargan datos históricos de otros activos (Petróleo, Oro, Gas Natural, Nasdaq, Tesoros 10 años) y se calcula la correlación mensual entre estos activos y el S&P 500.
   - Se visualiza la matriz de correlación mediante un heatmap.

## Archivos Generados

El script genera los siguientes archivos de imagen con los resultados del análisis:

1. `total_histogram.PNG`: Histograma de los retornos mensuales de ^GSPC.
2. `monthly_mean.png`: Gráfico de barras mostrando el retorno mensual promedio de cada mes.
3. `evolution_2024.png`: Gráfico de línea de la evolución de ^GSPC en 2024.
4. `correlations.png`: Heatmap de las correlaciones mensuales entre ES=F y otros activos.

## Cómo Ejecutar el Script

Para ejecutar el script, solo necesitas tener instalado Python y las librerías mencionadas. A continuación, ejecuta el archivo en tu terminal o entorno de desarrollo:

```bash
python nombre_del_archivo.py
```

Este script descargará los datos, realizará el análisis, y generará los gráficos en el directorio donde se ejecute.

## Notas

- El script utiliza datos históricos de Yahoo Finance a través de la librería `yfinance`.
- Los resultados pueden variar según los cambios en los datos históricos disponibles.
- Las visualizaciones generadas por el script ayudan a obtener una visión general de la volatilidad mensual y la correlación de los activos analizados.
