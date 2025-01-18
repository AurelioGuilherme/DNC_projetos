import numpy as np

def outlier(df):
  ''' A função retornara os valores considerados outliers inferiores e superiores
    x = valor que deseja descobrir
    quartil_75 = retorna o quartil 75%
    quartil_25 = retorna o quartil 25%
    outlier é a diferença de 1,5 vezes a diferença do amplitude
    interquantil
    C = constante
      ''' 
  quartil_75 = np.quantile(df,0.75)
  quartil_25 = np.quantile(df,0.25)
  c = 1.5
  intervalo_Interquartil =  quartil_75 - quartil_25
  outlier_Sup = quartil_75 + (c * intervalo_Interquartil)
  outlier_Inf = quartil_25 - (c * intervalo_Interquartil)
  return outlier_Inf, outlier_Sup