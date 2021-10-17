# Cargar el modelo 
 
import sklearn 
from joblib import load 
 
model = load("model.joblib") 
while True: 
    XS = [] 
    X = int(input("X:")) 
    XS.append([X]) 
    prediction = model.predict(XS) 
    print(prediction)