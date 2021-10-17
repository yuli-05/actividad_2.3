# Instrucciones

## Images
```bash
docker built -t regresion_lineal:v0.1 .
```

## Contenedor
```bash
docker run -it -p 8080:8080 -v "$PWD"/code/:/home/code/ --name gitpod_rl1 -h rl1 regresion_lineal:v0.1
```

## Volume
```bash
docker container run -it --name regresion2 -v "$PWD"/code/:/home/code/
```