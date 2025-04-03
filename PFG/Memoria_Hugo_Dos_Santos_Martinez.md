# Índice

- [1. Estudio del problema y análisis del sistema](#1-estudio-del-problema-y-análisis-del-sistema.-)  
  - [1.1 Introducción](#11-introducción)  
  - [1.2 Finalidad](#12-finalidad)  
  - [1.3 Requisitos](#13-requisitos)  

- [2. Recursos](#2-recursos)  
  - [2.1 Recursos hardware](#21-recursos-hardware)  
  - [2.2 Recursos software](#22-recursos-software)  

- [3. Planificación](#3-planificación)  
  - [3.1 Planificación temporal](#31-planificación-temporal)  
  - [3.2 Planificación económica](#32-planificación-económica)  

- [4. Desarrollo](#4-desarrollo)
      


- [5. Conclusiones finales](#5-conclusiones-finales)  
  - [5.1 Cumplimiento de los requisitos fijados](#51-cumplimiento-de-los-requisitos-fijados)  
  - [5.2 Propuestas de mejora](#52-propuestas-de-mejora)  

- [6. Guías](#6-guías)  
  - [6.1 Guía de uso](#61-guía-de-uso)
  - [6.2 Guía de instalación](#62-guía-de-instalación)  
  
- [7. Referencias bibliográficas](#7-referencias-bibliográficas)  

# 1. Estudio del problema y análisis del sistema

## 1.1 Introducción

## 1.2 Finalidad

## 1.3 Requisitos

# 2. Recursos

## 2.1 Recursos hardware

## 2.2 Recursos software

# 3. Planificación

## 3.1 Planificación temporal

## 3.2 Planificación económica

# 4. Desarrollo

Con las 3 aplicaciones ya instaladas empezaremos a desarrollar

La app web lo haremos de **Python Flask** que es un framework de Python para crear aplicaciones web con un número de líneas de código reducido basado en WSGI

```python
# Importamos al .py el Flask, para las templates y el conector a la BBDD
from flask import Flask, render_template, request
import re
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Datos de configuración de la base de datos
db_config = {
    'host': 'localhost',  # Dirección
    'user': 'root',            # Usuario
    'password': '*******',            # Contraseña
    'database': 'usuarios'     # Nombre de la base de datos
}

# Función para validar los datos del formulario
def validate_form(email, username, password, phone):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    phone_regex = r'^\d{10}$'
    if not re.match(email_regex, email):
        return "Correo electrónico no válido."
    if len(username) < 3:
        return "El nombre de usuario debe tener al menos 3 caracteres."
    if len(password) < 6:
        return "La contraseña debe tener al menos 6 caracteres."
    if not re.match(phone_regex, phone):
        return "El número de teléfono debe tener 10 dígitos."
    return None

# Función para insertar los datos del formulario en la base de datos
def insert_user(email, username, password, phone):
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**db_config)
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Consulta SQL para insertar el usuario
            insert_query = """INSERT INTO usuarios (email, usuario, pwd, phone)
                              VALUES (%s, %s, %s, %s)"""
            # Ejecutar la consulta
            cursor.execute(insert_query, (email, username, password, phone))
            connection.commit()
            cursor.close()
            return None
    except Error as e:
        return f"Error al insertar datos: {e}"
    finally:
        if connection.is_connected():
            connection.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        
        validation_error = validate_form(email, username, password, phone)
        if validation_error:
            message = validation_error
        else:
            insert_error = insert_user(email, username, password, phone)
            if insert_error:
                message = insert_error
            else:
                message = f"Registro exitoso para {username}!"
    # Aquí renderiza el HTML
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

```

Empezaremos con la parte de Podman y ahora explicaré unos conceptos

**¿Qué es Podman?**

Podman es un software de contenerización como Docker pero con la pequeña diferencia de que no te pide permisos de administrador y tampoco tiene un servicio en el sistema como si lo tiene docker (dockerd)

**¿Que es un contendor?**

Un contenedor es una versión light de una MV, mientras en la máquina virtual instalas todo un SO en el virtualizador y después las aplicaciones que necesites, en un contenedor solo instalarías el Kernel de Linux y la aplicación que necesites haciendo al contenedor portable, facil de arrancar y con mucho menos peso que una MV

Para crear un contenedor tienes que partir de una imagen que es una plantilla la cual contiene las instrucciones necesarias para hacer un contenedor

Lo que haremos será crear una pod con dos contenedores uno con la aplicación web de Python Flask y otro con la base de datos

La de la aplicación web será creada con un Dockerfile personalizado a partir de una imagen de Python3.13 metido en un Alpine Linux

La base de datos será una imagen de MySQL por defecto

**¿Que es una pod o cápsula?**

La pod es un grupo de uno o mas contenedores que comparten la misma red, PID y namespaces

**¿Que es un Dockerfile o Containerfile?**

Es un archivo que sirve como plantilla para crear una imagen

Este es el dockerfile

```dockerfile
FROM python:3.13-alpine

WORKDIR /app

COPY . /app

RUN apk update && apk upgrade
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["app.py"]
```

Vamos a explicar el dockerfile:

- **FROM** dicta la imagen base sobre la que se va a construir tu imagen personalizada en este caso un Linux Alpine sobre el cual está instalado Python

- **WORKDIR** crea un directorio si no existe y le hace un cd para entrar a el en este caso nos dirige a /app

- **COPY {fuente} {destino}** copia todo lo que le digas hacia donde le digas, si pones . copiará todo lo que esté en la carpeta del dockerfile y sus hijos y con un archivo .dockerignore funciona como un .gitignore, solo pones el archivo que quieras que ignore en este caso copia todo lo que tenga en el directorio del Dockerfile a la carpeta /app

- **RUN** Ejecuta un comando cuando se crea la imagen y se pasa a la shell del sistema (CMD, /bin/bash, /bin/sh) en este caso instala todas las dependencias de Python que hayamos puesto en el archivo requirements.txt, esto se hace porque así solo tendremos que añadir la dependencia al .txt y no habría que hacer nada mas y también actualizarán el Python

```txt
flask==3.1.0
```

- **ENTRYPOINT** Sirve para ejecutar un ejecutable en el contenedor cuando arranca, por ejemplo si quiero saber los servicios de windows que están corriendo puede servir en este caso te ejecuta Python

```pwsh
ENTRYPOINT [“Powershell”, “Get-Services”]
```

- **CMD** Pasa un argumento al comando del entrypoint, si pongo MYSQL me mostrará todos los servicios de MYSQL en este caso dentro de python me ejecuta la aplicación web

```pwsh
CMD [“MySQL”]
```

Para crear la imagen del Dockerfile es con el siguiente comando

```pwsh
PS D:\Projects> podman build -t flask_app .\PFG\
STEP 1/9: FROM python:3.13-alpine
STEP 2/9: WORKDIR /app
--> Using cache 3a2563be92ac47103c1bf59d5e4d5c329a2ea33ac0b4f2e8dfe6f9e5564e2552 
--> 3a2563be92ac
STEP 3/9: COPY . /app
--> a56b1e2e0ea1
STEP 4/9: RUN apk update && apk upgrade
fetch https://dl-cdn.alpinelinux.org/alpine/v3.21/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.21/community/x86_64/APKINDEX.tar.gz
v3.21.3-264-gb0ede8eacde [https://dl-cdn.alpinelinux.org/alpine/v3.21/main]
v3.21.3-267-gb1b14b7bf27 [https://dl-cdn.alpinelinux.org/alpine/v3.21/community] 
OK: 25398 distinct packages available
(1/2) Upgrading libffi (3.4.6-r0 -> 3.4.7-r0)
(2/2) Upgrading tzdata (2025a-r0 -> 2025b-r0)
OK: 10 MiB in 28 packages
--> d23610eda503
STEP 5/9: RUN pip install --no-cache-dir -r requirements.txt
Collecting flask==3.1.0 (from -r requirements.txt (line 1))
  Downloading flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting cryptography (from -r requirements.txt (line 2))
  Downloading cryptography-44.0.2-cp39-abi3-musllinux_1_2_x86_64.whl.metadata (5.7 kB)
Collecting mysql-connector-python (from -r requirements.txt (line 3))
  Downloading mysql_connector_python-9.2.0-py2.py3-none-any.whl.metadata (6.0 kB)Collecting Werkzeug>=3.1 (from flask==3.1.0->-r requirements.txt (line 1))
  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from flask==3.1.0->-r requirements.txt (line 1))
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting itsdangerous>=2.2 (from flask==3.1.0->-r requirements.txt (line 1))
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from flask==3.1.0->-r requirements.txt (line 1))
  Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from flask==3.1.0->-r requirements.txt (line 1))
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting cffi>=1.12 (from cryptography->-r requirements.txt (line 2))
  Downloading cffi-1.17.1-cp313-cp313-musllinux_1_1_x86_64.whl.metadata (1.5 kB)
Collecting pycparser (from cffi>=1.12->cryptography->-r requirements.txt (line 2))
  Downloading pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->flask==3.1.0->-r requirements.txt (line 1))
  Downloading MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_x86_64.whl.metadata (4.0 kB)
Downloading flask-3.1.0-py3-none-any.whl (102 kB)
Downloading cryptography-44.0.2-cp39-abi3-musllinux_1_2_x86_64.whl (4.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.3/4.3 MB 67.0 MB/s eta 0:00:00
Downloading mysql_connector_python-9.2.0-py2.py3-none-any.whl (398 kB)
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading cffi-1.17.1-cp313-cp313-musllinux_1_1_x86_64.whl (488 kB)
Downloading click-8.1.8-py3-none-any.whl (98 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
Downloading MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_x86_64.whl (23 kB)
Downloading pycparser-2.22-py3-none-any.whl (117 kB)
Installing collected packages: pycparser, mysql-connector-python, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, cffi, flask, cryptography
Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 cffi-1.17.1 click-8.1.8 cryptography-44.0.2 flask-3.1.0 itsdangerous-2.2.0 mysql-connector-python-9.2.0 pycparser-2.22
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable.It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.

[notice] A new release of pip is available: 24.3.1 -> 25.0.1
[notice] To update, run: pip install --upgrade pip
--> 683d5d11a78b
STEP 6/9: RUN pip install --upgrade pip
Requirement already satisfied: pip in /usr/local/lib/python3.13/site-packages (24.3.1)
Collecting pip
  Downloading pip-25.0.1-py3-none-any.whl.metadata (3.7 kB)
Downloading pip-25.0.1-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 50.9 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.3.1
    Uninstalling pip-24.3.1:
      Successfully uninstalled pip-24.3.1
Successfully installed pip-25.0.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your systema.io/warnings/venv. Use the --root-user-action option if you know what you are do--> 55da837126e7
STEP 7/9: EXPOSE 8080
--> d36295992f34
STEP 8/9: ENTRYPOINT ["python"]
--> bdd93767efda
STEP 9/9: CMD ["app.py"]
COMMIT flask_app
--> 18ee5d98cd04
18ee5d98cd042fcc2a63d27a6873e106aeacd01309b06b49d807f21ecf46ee21
```

Parámetros:

- -t le dará un nombre a la imagen

Como puedes ver va paso a paso, esto te ayuda para que veas que comando falla

Creamos la pod

```pwsh
PS D:\Projects> podman pod create -p 8080:8080
b3474e41f547662191e7cc88215b609f7a5b4e09458c50add9e7f9deef4fb538
PS D:\Projects> podman pod ps
POD ID        NAME             STATUS      CREATED        INFRA ID      # OF CONTAINERS
b3474e41f547  thirsty_babbage  Created     6 seconds ago  93258c27af2e  1
PS D:\Projects> podman pod start thirsty_babbage
thirsty_babbage
PS D:\Projects> podman pod ps
POD ID        NAME             STATUS      CREATED             INFRA ID      # OF CONTAINERS
b3474e41f547  thirsty_babbage  Running     About a minute ago  93258c27af2e  1
PS D:\Projects>
```

Lo que he hecho ha sido crearla mapeando el puerto 8080 y arrancarla

```pwsh
PS D:\Projects> podman run -d --pod thirsty_babbage localhost/flask_app
39c362a105e71de8282cce665fd783af3a4189046d99a21d9d8d68515d0c62b5
PS D:\Projects>
```

Parámetros:

- -d sirve para que no te agarre la shell desde donde lo has ejecutado

- --pod para meterlo en la pod que indicas

Para el contenedor de MYSQL usaremos la imagen base de MySQL:latest

Si queremos data consistente tenemos que crear un volumen

```pwsh
PS D:\Projects> podman volumen create mysqldata
mysqldata
PS D:\Projects>
```

Y al crear el siguiente contenedor le decimos que los datos los guarde en el volumen, esta imagen de MySQL es de docker.io/library/mysql

```pwsh
PS D:\Projects> podman run -d -v mysqldata:/var/lib/mysql mysql:latest
```

Parámetros:

-d para que no te agarre la shell

-v para meter los datos en el volumen

Si quieres ver como funciona solo tendrán ir a tu navegador en localhost:8080

```pwsh
PS D:\Projects> podman exec -it 40da mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 13
Server version: 9.2.0 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

Creamos la BBDD y la tabla usuarios con los campos del formulario además de un campo ID que será la PK y será autoincremental

```mysql
mysql> CREATE DATABASE usuarios;
Query OK, 0 rows affected, 1 warning (0.01 sec)
mysql> USE usuarios;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> CREATE TABLE usuarios (
  >> id INT AUTO_INCREMENT PRIMARY KEY,
  >> email VARCHAR(60),
  >> usuario VARCHAR(20),
  >> pwd VARCHAR(60),
  >> phone INT
  >> );
  Query OK, 0 rows affected (0.02 sec)
mysql>
```

Cuando metas datos en el formulario, si son correctos lo puedes ver en la BBDD

```mysql
mysql> SELECT * FROM usuarios
    -> ;
+----+---------+-----------+----------+------------+
| id | email   | usuario   | pwd      | phone      |
+----+---------+-----------+----------+------------+
|  1 | a@a.com | prueba123 | 13214123 | 3645645212 |
|  2 | a@a.com | {{7*7}}   | 1415414  | 3645645212 |
+----+---------+-----------+----------+------------+
2 rows in set (0.00 sec)
```

Y generamos un archivo .YAML para kubernetes de la pod

```pwsh
PS D:\Projects> podman generate kube -f flaskapp_bbdd.yaml thirsty_babbage
PS D:\Projects>
```

# 5. Conclusiones finales

## 5.1 Cumplimiento de los requisitos fijados

## 5.2 Propuestas de mejora

# 6. Guías

## 6.1 Guía de uso

## 6.2 Guía de instalación

Empezaremos con la instalación del software:

Instalaremos Podman.

Iremos a [https://podman.io/](https://podman.io/) y tenemos 2 opciones de descarga.

La Desktop y la CLI, yo descargaré la Desktop porque así instala la CLI también.

Cuando ejecutemos el .exe nos dará la opción de descargar 3 dependencias e instalaremos las 3.

Te pedirá que instales WSL o Windows HyperV, el motivo de esto es que para crear un contenedor de Linux el sistema de contenerización necesita acceso al Kernel de Linux y lo que hace el WSL es justamente instalarte un Kernel de Linux

Ahora instalaremos Kubernetes que serán 2 componentes: Minikube para hacer pruebas y Kubectl para la command line tool

Para kubectl nos dirigimos a (Kubernetes)[kubernetes.io] en el apartado de documentación a la derecha Tasks -> Install tools y ejecutamos el siguiente comando

```pwsh
curl.exe -LO "https://dl.k8s.io/release/v1.32.0/bin/windows/amd64/kubectl.exe"
```

El .exe que se nos ha descargado lo movemos a una carpeta en C: llamada kube

En Panel de Control -> Sistema y Seguridad -> Sistema -> Configuración avanzada de Sistema -> Variables de entorno -> Path -> Añades la ruta del .exe de kube que en mi caso es C:\kube

Y ahora instalaremos minikube con 2 comandos en Powershell

Este para descargarlo:

```pwsh
New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force
Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing
```

Y este para añadir el binario al PATH del sistema

```pwsh
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -inotcontains 'C:\minikube'){
  [Environment]::SetEnvironmentVariable('Path', $('{0};C:\minikube' -f $oldPath), [EnvironmentVariableTarget]::Machine)
}
```

Además tendremos que usar Hyper-V que es el hipervisor que mejor funciona con Kubernetes

```pwsh
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

# 7. Referencias bibliográficas

(Curso Podman)[https://www.youtube.com/watch?v=YXfA5O5Mr18]

(Instalación Kubernetes)[https://core.digit.org/guides/operations-guide/working-with-kubernetes/installation-of-kubectl]

(Documentación Python Flask)[https://flask.palletsprojects.com/en/stable/]

(Documentación Dockerfile)[https://docs.docker.com/reference/dockerfile/]