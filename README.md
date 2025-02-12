# Patagonia - Proyecto Django con Docker

![Patagonia](/img/patagonia.jpg)

## Descripción

Patagonia es un proyecto Django configurado para ejecutarse en contenedores Docker, utilizando PostgreSQL como base de datos.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Instalación y ejecución

Sigue estos pasos para configurar y ejecutar el proyecto:

### 1. Clonar el repositorio

```sh
 git clone https://github.com/Agujuarez/Patagonia.git
 cd Patagonia
```

### 2. Crear el archivo `.env`

Crea un archivo `.env` en la raíz del proyecto y define las variables de entorno necesarias para la configuración de la base de datos.

### 3. Construir y levantar los contenedores

```sh
docker compose up --build -d
```

Esto descargará las imágenes necesarias y levantará los servicios de Django y PostgreSQL.

### 4. Aplicar migraciones

Ejecuta las migraciones de la base de datos:

```sh
docker exec -it django_app python manage.py migrate
```

### 5. Crear un superusuario

```sh
docker exec -it django_app python manage.py createsuperuser
```

Sigue las instrucciones para crear un usuario administrador.

### 6. Acceder a la aplicación

Abre el navegador y ve a:

```
http://127.0.0.1:8000/
```

Para acceder al panel de administración de Django:

```
http://127.0.0.1:8000/admin/
```

## Comandos útiles

- **Ver logs de Django:**
  ```sh
  docker logs django_app
  ```
- **Acceder al contenedor de Django:**
  ```sh
  docker exec -it django_app bash
  ```
- **Apagar los contenedores:**
  ```sh
  docker compose down
  ```

---

📌 ¡Listo! Ahora tienes Patagonia corriendo con Docker y PostgreSQL. 🚀
