import numpy as np
import matplotlib.pyplot as plt

# Tempo em segundos (valores fixos)
tempo_segundos = [0, 30]

# Porcentagem de bateria (valores aleatórios)
bateria = [100, 80]  

plt.figure(facecolor='lightgrey')

# Plotar o gráfico de linha
plt.plot(tempo_segundos, bateria, marker='o', linestyle='-.', color='blue', linewidth= 3, markersize=10, label='Porcentagem de Bateria')

# Adicionar título e rótulos aos eixos
plt.title('PORCENTAGEM DE BATERIA AO LONGO DO TEMPO', fontsize=16, fontweight="bold", fontfamily="arial")
plt.xlabel('TEMPO (SEGUNDOS)', fontsize=16, fontweight="bold" )
plt.ylabel('PORCENTAEM DE BATERIA', fontsize=16, fontweight="bold")

# Adicionar grade ao gráfico
plt.grid(True, linestyle='--', alpha=1)

# Adicionar legenda
plt.legend(loc='lower left')

# Exibir o gráfico
plt.tight_layout()       # Ajustar layout para evitar sobreposição de elementos
plt.show()
