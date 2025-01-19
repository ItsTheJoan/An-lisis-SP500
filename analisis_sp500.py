import yfinance as yf
import pandas as pd
import datetime as dt
import seaborn as sns
from matplotlib import pyplot as plt


# Descargar los precios de cierre del activo
data = yf.download(tickers='^GSPC', start='1999-12-31', end='2025-01-01', interval='1mo')['Close']
monthly_data = data['^GSPC'].resample('M').last()

data.to_excel('data.xlsx')

# Mover el índice a la columna de fecha
monthly_data = monthly_data.reset_index()  
monthly_data['Date'] = pd.to_datetime(monthly_data['Date'])

# Obtener los cambios porcentuales entre una observación y otra
monthly_data['Cambio (%)'] = monthly_data['^GSPC'].pct_change()*100

# Obtener una columna con el mes (número) para cada observación
monthly_data['Mes'] = monthly_data['Date'].dt.month.astype(int)

# Histograma de los retornos mensuales
monthly_data['Cambio (%)'].hist(bins= 20) # 20 columnas para entender mejor la distribución, sin exceder el limite de los datos
plt.title('Distribución de los retornos mensuales (%)')
plt.axvline(monthly_data['Cambio (%)'].mean(), color = 'red') # Linea en la media
plt.axvline(monthly_data['Cambio (%)'].mean() + monthly_data['Cambio (%)'].std(), color = 'purple') # Linea en la media más desviación estándar
plt.axvline(monthly_data['Cambio (%)'].mean() - monthly_data['Cambio (%)'].std(), color = 'purple') # Linea en la media menos desviación estándar
plt.xlabel('Cambio Mensual (%)')
plt.grid() # Eliminar los grids
plt.yticks([]) # Eliminar las etiquetas del eje Y
#Comentario sobre media y desviación
plt.text(0.98, 0.95, f'Media: 0.58% \n \nDesviación \nestándar: 4.41%', color='black', ha='right', va='top', fontsize=12, style='italic', transform=plt.gca().transAxes)
plt.savefig('total_histogram.PNG')

# Gráfica de barras por mes
monthly_mean = monthly_data.groupby('Mes')['Cambio (%)'].mean() # Nuevo DF con la media de retornos por mes
monthly_mean = monthly_mean.sort_index(ascending=True) # Organizar el Df por mes (cronologico)

plt.figure(figsize=(10, 6))
monthly_mean.plot(kind='bar')
plt.title('Retorno esperado por mes')
plt.xlabel('Mes')
plt.ylabel('Promedio de Cambio (%)')

## Loop para agregar las etiquetas de datos
for i, value in enumerate(monthly_mean):
    if value >= 0:
        plt.text(i, value + 0.05, f'{value:.2f}', ha='center', fontsize=10) # Si el valor es mayor a 0, se pone la etiqueta 5 básicos arriba en el eje Y
    else:
        plt.text(i, value - 0.15, f'{value:.2f}', ha='center', fontsize=10) # Si el valor es menor a 0, se pone la etiqueta 15 básicos abajo en el eje Y

plt.savefig('monthly_mean.png')



# Gráfico con la evolución para las últimas 13 observaciones (2024)
monthly_data.set_index('Date', inplace= True)
plt.figure(figsize=(10, 6))
monthly_data['^GSPC'][-12:].plot(kind='line') # Tomar solo las últimas 12 observaciones (1 año)
plt.title('Evolución del SP500 en 2024')
plt.xlabel('Fecha')
plt.savefig('evolution_2024.png')


###### Análisis de Correlación

# Descargar datos de otros futuros
tickers = ['^GSPC', 'CL=F', 'GC=F', 'NG=F', 'ZN=F'] # ['Petroleo', 'Oro', 'Gas Natural', 'USDCOP', 'Nasdaq', 'Tesoros 10 años']
data_corr = yf.download(tickers= tickers, start= '2000-01-01', end = dt.date.today(), interval= '1mo')['Close']


corr_change = data_corr.pct_change()

corr = corr_change.corr()
correlations = corr['^GSPC']
correlations = correlations[correlations != 1 ]
correlations


# Tabla de correlacion
names = ['Petroleo', 'Oro', 'Gas Natural', 'Tesoros \n10 años' ] # nombres para las etiquetas


plt.figure(figsize=(10, 6))  # Ajusta el tamaño de la figura si lo necesitas
plt.title('Correlaciones mensuales SP500')
sns.heatmap(correlations.to_frame(), annot=True, cmap='coolwarm', fmt=".2f") # Fomato del visual y los números (2 decimales)
plt.yticks(ticks= range(len(names)), labels= names, va = 'center', rotation = 0) # Nombres de los futuros en vez de los ticker de YF
plt.xticks([]) # Borra la etiquta del eje x
plt.savefig('correlations.png')
