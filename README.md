# Predicción con Scikit-Learn

Esta app es una tarea para la asignatura "Programación de inteligencia artificial" del curso de especialización en Inteligencia Artificial y Big Data. Esta tarea, se trata de una tarea de clasificación binaria. Tenemos un datasets donde el target es predecir el valor de la columna "Converted". Esta columna tiene dos valores: 1 para los clientes que se han convertido y 0 para los que no.
Dentro del proyecto, podemos encontrar varias carpetas:
* __dataset__: es donde se encuentra almacenado el dataset.
* __models__: es donde se encuentra almacenado el modelo, con el nombre de "practica_model.pck". De no hacer esto, habría que entrenar el modelo cada vez que queramos usarlo.
* __notebooks__: es donde se encuentra el archivo Jupyter Notebook con todos los pasos a seguir para la creación del modelo.
* __proyecto_scikitlearn__: Es donde se encuentra la app. Dentro, hay dos archivos python: uno monta un servidor, captura lo que le llega por post a http://localhost/predict y lo convierte en dataframe para pasarlo al archivo practica_predict_services.py, el cual hace la predicción y se la devuelve de nuevo. Por último, se responde con la predicción con un json con un contenido booleano, indicando con un True y se convierte y con un False si es que no.
* __test__: carpeta generada automáticamente por poetry donde se pueden almacenar todos los test.
* Los otros dos ficheros son propios de poetry, y tienen la configuración necesaria para que funcione el proyecto.

Para que este proyecto funcione, debes descargarlo en local, ejecutar con python el archivo "practica_predict_app.py" y pasarle con postman(o con cualquier otro método) con json con la información de la columnas menos la columna que deseas predecir. Recuerda que este json debe ir dentro de un array. Esta app está pensada para hacer predicciones de una en una, de tal forma que si lo que quieres es saber la predicción para un conjunto de golpe, deberá modificar el código.

