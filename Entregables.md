# Entregables

## Tecnologías utilizadas

### Base de datos

Se utilizó el motor de base de datos relacional PostgreSQL para guardar la información. Dicha elección se tomó porque 
el modelo de datos se dedujo que era estable, es decir, que no sería necesario agregar nuevos atributos (columnas) para 
el micro-desarrollo de la prueba.

Así mismo, el guardo de datos estaría mejor controlado al hacer uso del ORM SQLAlquemy que ya cuenta con funciones 
seguras para la manipulación de datos que residen dentro una base de datos.

En caso de haberse realizado con una base de datos NoSQL, se habría elegido MongoDB debido a la gran flexibilidad que 
otorga su modelo orientado a archivos.

Para ello se habría creado la colección **'Jokes'** con una estructura base para el documento de la siguiente forma:

    {
        "id": (int),
        "joke": (string),
        "created_time": (int-timestamp),
        "updated_time": (int-timestamp),
        "dropped": (bool)
    }

### Librerías

Se utilizó **httpx** y **pytest** para realizar las pruebas unitarias debido a la facilidad de utilizar dichas 
herramientas en un entorno local, sumado a que son las librerías recomendadas por el propio framework FastAPI.

Por otro lado, se usó **request** para realizar las peticiones a los repositorios de chistes debido a la confiabilidad 
que tengo hacia esa librería; sobre todo porque no agrega bugs al código al momento de obtener las respuestas.

## Decisiones tomadas


La decisión más importante tomada durante el desarrollo que no tiene que ver con las tecnologías a utilizar, se 
considera que es la estructura que se eligió para el desarrollo del código.

Se tomó un modelo vista-controlador donde la vista la compone la carpeta **'routers'** la cual cuenta con los 
entrypoints del sistema.

Mientras que el controlador se encarga de la capa de negocio de la aplicación, por ende aquí es donde se realizan las 
operaciones con los datos. De igual manera, esta capa se encarga de solicitar los datos a los repositorios locales o 
remotos con los que cuenta el sistema.

Finalmente, la capa de datos se encarga de recolectar  y/o almacenar la información que es necesaria para dar solución 
al requerimiento del cliente. El directorio **'local'** se comunica con la base de datos, mientras que el directorio 
**'remote'** obtiene la información de los repositorios ChucK y Dad.
    