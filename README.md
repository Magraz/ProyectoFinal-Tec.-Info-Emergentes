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

Primeramente hay que instalar Anaconda https://www.anaconda.com/products/individual

En el directorio de su preferencia clonamos este repositorio. Para facilitar la explicación asumiremos que el repositorio se clonó dentro un folder llamado ```Repositorios```

Posteriormente hay que crear el ambiente de ejecución desde clasificadorWeb.yml en Anaconda para correr la aplicación web. En una terminal de Anaconda ejecutamos:

```
conda env create -f clasificadorWeb.yml
conda activate clasificadorWeb
```

Dentro del directorio ```Repositorios``` ejecutamos: 
```
cd ProyectoFinal-Tec.-Info-Emergentes/flask_apps
```
