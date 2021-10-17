# librerias
import sklearn 
import pandas as pd 
from sklearn.model_selection import train_test_split # Dividir los datos en train y test 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score 
import matplotlib.pyplot as plt 
from joblib import dump, load

# Dataset
dataframe = pd.read_csv("dato_r101.csv") 
df_x = dataframe[['x']] 
df_y = dataframe['y'] 

#Graficar Datos
plt.plot(df_x,df_y) 
plt.xlabel("X") 
plt.ylabel("Y") 
plt.title("Regresion lineal")
plt.savefig("rl.png") 
plt.show() 

# Separar dataset en train y test 
x_train, x_test, y_train, y_test = train_test_split(df_x,df_y, test_size=0.2, random_state=1234) 

#Entrenar el modelo de ML  
model = LinearRegression() 
model.fit(x_train,y_train) 

# Calcular la precisión 
y_hat = model.predict(x_test) 
acc = r2_score(y_test,y_hat) 
print("Accuracy: %.2f" % acc)

# Guardar el medelo 
dump(model,"model.joblib")