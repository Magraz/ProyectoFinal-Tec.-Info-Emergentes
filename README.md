# ProyectoFinal-Tec.-Info-Emergentes
Repositorio del proyecto final de la materia de Tecnologías de Información Emergentes

Este repositorio contiene código e instrucciones para poder ejecutar una aplicación web
que clasifica imágenes en 5 clases:
<ul>
  <li> Camiones</li>
  <li> Carros</li>
  <li> Trenes</li>
  <li> Patinetas</li>
  <li> Bicicletas</li>
</ul>

## Instrucciones de ejecución

Primeramente hay que instalar Anaconda https://www.anaconda.com/products/individual

En el directorio de su preferencia clonamos este repositorio. Para facilitar la explicación asumiremos que el repositorio se clonó dentro un folder llamado ```Repositorios```

Posteriormente hay que crear el ambiente de ejecución de Anaconda con ayuda del archivo ```clasificadorWeb.yml``` para poder correr la aplicación web. En una terminal de Anaconda con permisos de administrador ejecutamos:

```
conda env create -f clasificadorWeb.yml
conda activate clasificadorWeb
```

Dentro de la misma terminal nos movemos al directorio ```Repositorios```  y ejecutamos: 
```
cd ProyectoFinal-Tec.-Info-Emergentes/flask_apps
set FLASK_APP=predict_app.py
flask run --host=0.0.0.0
```

Estos comandos realizan la configuración necesaria para habilitar nuestro clasificador web. Para poder utilizar la aplicación web hay que accessar a cualquiera de las siguientes páginas locales:
⋅⋅* http://localhost:5000/static/predict_with_visuals.html Clasificador que los resultados a través de gráficas
⋅⋅* http://localhost:5000/static/predict.html Clasificador que muestra las probabilidaes de cada clase 
