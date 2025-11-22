import os
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "data", "consumoAgua.csv")

print("Lendo arquivo:", file_path)
df = pd.read_csv(file_path)
print(df.head())


# Corrigir valores negativos ou nulos
df["ConsumoLitros"] = df["ConsumoLitros"].apply(lambda x: abs(x))
df.dropna(inplace=True)

# Criar coluna de consumo per capita
df["ConsumoPorPessoa"] = (df["ConsumoLitros"] / df["Moradores"]).round(2)

# Exportar dados tratados
df.to_csv("consumoAguaTratado.csv", index=False)
