# Nombre de la Aplicación

## Descripción

Esta es una aplicación web construida con FastAPI, un moderno y rápido (de alto rendimiento) framework web para construir APIs con Python 3.6+ basado en estándares para APIs.

## Funciones

- **FastAPI**: Se utiliza para manejar todas las solicitudes HTTP (GET, POST, PUT, DELETE, etc.) y para definir todas las rutas de la aplicación.
- **SQLAlchemy**: Es un ORM (Object Relational Mapper) que permite interactuar con nuestra base de datos como si fueran objetos Python.
- **Hashing**: Esta biblioteca se utiliza para el manejo seguro de las contraseñas en nuestra aplicación.

## Rutas

La aplicación tiene las siguientes rutas:

- **Blog**: Las rutas relacionadas con las operaciones del blog están en este router.
- **User**: Las rutas relacionadas con las operaciones del usuario están en este router.
- **Authentication**: Las rutas relacionadas con la autenticación están en este router.

## Librerias

- **FastAPI**: Se utiliza para manejar todas las solicitudes HTTP (GET, POST, PUT, DELETE, etc.) y para definir todas las rutas de la aplicación.
- **Uvicorn**: Es un servidor ASGI que permite a nuestra aplicación FastAPI comunicarse con la web. Es compatible con HTTP/1.1 y WebSockets.
- **SQLAlchemy**: Es un ORM (Object Relational Mapper) que permite interactuar con nuestra base de datos como si fueran objetos Python.
- **Passlib**: Esta biblioteca se utiliza para el manejo seguro de las contraseñas en nuestra aplicación.
- **Bcrypt**: Es una biblioteca que nos ayuda a obtener un hash seguro para nuestras contraseñas.
- **python-jose**: Es una biblioteca que nos ayuda a codificar y decodificar objetos JSON Web Token (JWT). Esto es útil para mantener las sesiones de los usuarios y para la autenticación.