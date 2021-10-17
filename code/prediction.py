# Cargar el modelo 
 
import sklearn 
from joblib import load 
 
model = load("model.joblib") 
while True: 
    xs = [] 
    x = int(input("x:")) 
    xs.append([X]) 
    prediction = model.predict(xs) 
    print(prediction)