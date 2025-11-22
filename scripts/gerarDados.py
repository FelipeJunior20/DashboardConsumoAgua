import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Criar período de 1 ano
dataInicial = datetime(2024, 1, 1)
datas = [dataInicial + timedelta(days=i) for i in range(365)]

# Simular consumo diário (litros)
np.random.seed(42)
consumo = np.random.normal(250, 50, size=len(datas))  # média 250L, desvio 50L

# Simular moradores e temperatura média
moradores = np.random.choice([2, 3, 4, 5], size=len(datas))
temperatura = np.random.normal(28, 4, size=len(datas))

# Montar DataFrame
df = pd.DataFrame({
    "Data": datas,
    "ConsumoLitros": consumo.round(2),
    "Moradores": moradores,
    "Temperatura_C": temperatura.round(1)
})

# Adicionar coluna de mês e dia da semana
df["Mes"] = df["Data"].dt.month_name()
df["DiaSemana"] = df["Data"].dt.day_name()

# Salvar em CSV
df.to_csv("consumoAgua.csv", index=False)
print(df.head())
