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
    - [Podman](#podman)  


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



# 5. Conclusiones finales

## 5.1 Cumplimiento de los requisitos fijados

## 5.2 Propuestas de mejora

# 6. Guías

## 6.1 Guía de uso

## Podman

Si quieres iniciar podman tendrás que escribir los 2 siguientes comandos en tu cmd

**podman machine init**
**podman machine start**

La salida tendría que ser algo parecida a esto

```batch
C:\Users\Duke>podman machine init
Looking up Podman Machine image at quay.io/podman/machine-os-wsl:5.4 to create VM
Getting image source signatures
Copying blob 84c333c351e9 done   |
Copying config 44136fa355 done   |
Writing manifest to image destination
84c333c351e97943d8bcea7229680735577d544076574a2726cbb7e4539c898b
Extracting compressed file: podman-machine-default-amd64: done
Importing operating system into WSL (this may take a few minutes on a new WSL install)...
La operación se completó correctamente.
Configuring system...
Machine init complete
To start your machine run:

        podman machine start
C:\Users\Duke>podman machine start
Starting machine "podman-machine-default"

This machine is currently configured in rootless mode. If your containers
require root permissions (e.g. ports < 1024), or if you run into compatibility
issues with non-podman clients, you can switch using the following command:

        podman machine set --rootful

API forwarding listening on: npipe:////./pipe/docker_engine

Docker API clients default to this address. You do not need to set DOCKER_HOST.
Machine "podman-machine-default" started successfully
```

Para que Podman consiga las imágenes de los contenedores trabaja con registros que son unos repositorios donde están todas las imágenes predefinidas

Por defecto te viene el registro de Docker Hub, Red Hat, GitHub y el de Google aunque también puedes quitar o añadir otro registro, incluso algún registro privado que tengas

Si deseas buscar una imagen con un servicio que quieras con el comando **podman search 'nombre de contendor'** te buscará en todos los registros una imagen con ese servicio

```batch
PS D:\Clase\ASO> podman search nginx
NAME                                              DESCRIPTION
docker.io/library/nginx                           Official build of Nginx.
docker.io/nginx/nginx-ingress                     NGINX and  NGINX Plus Ingress Controllers fo...
docker.io/nginx/nginx-prometheus-exporter         NGINX Prometheus Exporter for NGINX and NGIN...
docker.io/nginx/unit                              This repository is retired, use the Docker o...
docker.io/nginx/nginx-ingress-operator            NGINX Ingress Operator for NGINX and NGINX P...
docker.io/nginx/nginx-quic-qns                    NGINX QUIC interop
docker.io/nginx/nginxaas-loadbalancer-kubernetes
docker.io/nginx/unit-preview                      Unit preview features
docker.io/bitnami/nginx                           Bitnami container image for NGINX
docker.io/ubuntu/nginx                            Nginx, a high-performance reverse proxy & we...
docker.io/bitnamicharts/nginx                     Bitnami Helm chart for NGINX Open Source
docker.io/rancher/nginx
docker.io/kasmweb/nginx                           An Nginx image based off nginx:alpine and in...
docker.io/linuxserver/nginx                       An Nginx container, brought to you by LinuxS...
docker.io/redash/nginx                            Pre-configured nginx to proxy linked contain...
docker.io/dtagdevsec/nginx                        T-Pot Nginx
docker.io/vmware/nginx
docker.io/paketobuildpacks/nginx
docker.io/chainguard/nginx                        Build, ship and run secure software with Cha...
docker.io/gluufederation/nginx                    A customized NGINX image containing a consu...
docker.io/intel/nginx
docker.io/droidwiki/nginx
docker.io/circleci/nginx                          This image is for internal use
docker.io/corpusops/nginx                         https://github.com/corpusops/docker-images/
docker.io/antrea/nginx
```

Una vez que ya tengamos la imagen deseada vamos a descargarla con **podman pull**, yo usaré la docker.io/library/nginx

```batch
PS D:\Clase\ASO> podman pull docker.io/library/nginx
Trying to pull docker.io/library/nginx:latest...
Getting image source signatures
Copying blob sha256:97f5c0f51d43d499970597eef919f9170954289eff0c5d7b8f8afd73dbb57977
Copying blob sha256:417c4bccf5349be7cd4ba91b1a2077ecf0ab50b3831bb071ba31f2c8bac02ed1
Copying blob sha256:6e909acdb790c5a1989d9cfc795fda5a246ad6664bb27b5c688e2b734b2c5fad
Copying blob sha256:5eaa34f5b9c2a13ef2217ceb966953dfd5c3a21a990767da307be1f57e5a1e4f
Copying blob sha256:373fe654e9845b69587105e1b82833209521db456bdc5bc26ac7260e3eb2dd52
Copying blob sha256:e7e0ca015e553ccff5686ec2153c895313675686d3f6940144ce935c07554d85
Copying blob sha256:c22eb46e871ad1cda19691450312c6b5c25eb5e6836773821d8091cffb6327cc
Copying config sha256:53a18edff8091d5faff1e42b4d885bc5f0f897873b0b8f0ace236cd5930819b0
Writing manifest to image destination
53a18edff8091d5faff1e42b4d885bc5f0f897873b0b8f0ace236cd5930819b0
PS D:\Clase\ASO>
```

Con **podman image list** podremos ver todas las imagenes que tengamos descargadas

```batch
PS D:\Clase\ASO\Proyectos\ProyectoFinGrado> podman image list
REPOSITORY               TAG         IMAGE ID      CREATED      SIZE
docker.io/library/nginx  latest      53a18edff809  6 weeks ago  196 MB
PS D:\Clase\ASO\Proyectos\ProyectoFinGrado>
```

Para arrancar el contenedor usaremos **podman run "contenedor"** y usaremos algunos parámetros:

- El parámetro --name que le dará un nombre al contenedor
- El parámetro -d que hará que el proceso no agarre nuestro shell
- El parámetro --rm que no borrará el contenedor cuando lo cerremos para no llenar el sistema de archivos
- El parámetro -p que nos permitirá mapear puertos

```batch
C:\Users\Duke>podman run --name nginx -d --rm -p 8080:80 nginx
208c2abaf060a96970c9ef001ee435fa242e0b4fb22bbe665ebdf2d8082f32b6

C:\Users\Duke>
```
De salida te da el id del contenedor

**podman ps -a** nos servirá para ver los contenedores incluso aquellos que estén parados

```batch
C:\Users\Duke>podman ps -a
CONTAINER ID  IMAGE                           COMMAND               CREATED         STATUS         PORTS                 NAMES
208c2abaf060  docker.io/library/nginx:latest  nginx -g daemon o...  12 seconds ago  Up 12 seconds  0.0.0.0:8080->80/tcp  nginx
```
También podrás ver cosas como:

- El ID del contenedor
- De donde sale la imagen
- Comando que se ha ejecutado
- Cuándo se creó
- Cuánto tiempo llevan encendido
- Puertos que usa
- Nombre del contenedor

En caso de no poner el parámetro --rm a la hora de iniciar el contenedor si está parado tendrás que iniciarlo con **podman start "id o nombre de contenedor"** para pararlo es con **podman stop "id o nombre de contenedor"**

Si quieres ver información detallada del contenedor en formato JSON es con **podman inspect "id o nombre de contenedor"**

Y para ver el puerto que tiene abierto la máquina es con **podman port "id o nombre de contenedor"**

```batch
C:\Users\Duke>podman port nginx
80/tcp -> 0.0.0.0:8080
```

Ahora que ya hemos aprendido como hacer un contenedor empezaremos con las **Cápsulas** o **Pods**

¿Que son las Pods?

Es un grupo de uno o mas contenedores que comparten la misma red e id de procesos

Para ver la ayuda **podman pod --help**

La creamos con **podman pod create**

```pwsh
PS C:\Users\Duke> podman pod create
4ae37935941d44012605294e403f094595c73bd6f384927061bb10af6fe73019
PS C:\Users\Duke>
```
Para ver la pod creada con **podman pod ls**

```pwsh
PS C:\Users\Duke> podman pod ls
POD ID        NAME               STATUS      CREATED         INFRA ID      # OF CONTAINERS
4ae37935941d  gallant_mendeleev  Created     53 seconds ago  2d6ff7f2e1f8  1
PS C:\Users\Duke>
```
Ese contenedor que ya está en la Pod permite a Podman conectar todos los contenedores entre sí y permite parar y arranca contenedores que estén dentro de la Pod sin que la Pod deje de funcionar, ese contenedor tiene una imagen default que no se cambia a no ser q se especifique

Con el comando **podman pod -a --pod** podremos ver todos los contenedores

```pwsh
PS C:\Users\Duke> podman ps -a --pod
CONTAINER ID  IMAGE                                    COMMAND               CREATED        STATUS                    PORTS                 NAMES               POD ID        PODNAME
f03d383c2c79  docker.io/library/nginx:latest           nginx -g daemon o...  22 hours ago   Exited (0) 292 years ago  0.0.0.0:8080->80/tcp  nginx
2d6ff7f2e1f8  localhost/podman-pause:5.4.1-1741651200                        6 minutes ago  Created                                         4ae37935941d-infra  4ae37935941d  gallant_mendeleev
PS C:\Users\Duke>
```
Se puede ver al final el POD ID y la PODNAME

Ahora añadiremos contenedores a la Pod con **podman run -dt --pod gallant_mendeleev nginx** es importante que el contenedor esté parado

```pwsh
PS C:\Users\Duke> podman run -dt --pod gallant_mendeleev nginx  
6de0504781996c99d33076d8de466394a949222656e1593be4c00c6471d732ec
PS C:\Users\Duke> podman ps -a --pod
CONTAINER ID  IMAGE                                    COMMAND               CREATED         STATUS                    PORTS 
                NAMES                POD ID        PODNAME
f03d383c2c79  docker.io/library/nginx:latest           nginx -g daemon o...  22 hours ago    Exited (0) 292 years ago  0.0.0.0:8080->80/tcp  nginx
2d6ff7f2e1f8  localhost/podman-pause:5.4.1-1741651200                        19 minutes ago  Up 7 seconds
                4ae37935941d-infra   4ae37935941d  gallant_mendeleev
6de050478199  docker.io/library/nginx:latest           nginx -g daemon o...  6 seconds ago   Up 7 seconds              80/tcp                quizzical_sanderson  4ae37935941d  gallant_mendeleev
PS C:\Users\Duke
```
Como hemos usado podman run en base a la imagen de nginx me creará otro contenedor y el que tenía antes no se ha borrado, lo borraré con **podman rm nginx**

Aunque el contenedor esté en una Pod todos los comandos anteriormente mencionados seguirán funcionando

Con **podman pod ls** listaremos todas las pods

```pwsh
PS C:\Users\Duke> podman pod ls
POD ID        NAME               STATUS      CREATED         INFRA ID      # OF CONTAINERS
4ae37935941d  gallant_mendeleev  Running     26 minutes ago  2d6ff7f2e1f8  2
PS C:\Users\Duke>
```
Para parar la pod podrás usar **podman pod stop gallant_mendeleev**, para arrancarla de nuevo **podman pod start gallant_mendeleev** y para borrarla servirá con **podman pod rm gallant_mendeleev**

```pwsh
PS C:\Users\Duke> podman pod stop gallant_mendeleev
gallant_mendeleev
PS C:\Users\Duke> podman pod start gallant_mendeleev
gallant_mendeleev
PS C:\Users\Duke> podman pod rm --force gallant_mendeleev
4ae37935941d44012605294e403f094595c73bd6f384927061bb10af6fe73019
PS C:\Users\Duke> podman pod ls
POD ID      NAME        STATUS      CREATED     INFRA ID    # OF CONTAINERS
PS C:\Users\Duke
```
Los comándos básicos de contenedores funciona con las pods añadiendo simplemente un pod entre podman y el comando

Ahora aprenderemos a generar un archivo Kubernetes YAML que contiene información de como se ejecuta la Pod de la cual se haya creado el archivo .YAML

```pwsh
PS C:\Users\Duke> podman generate kube vigilant_fermat >> D:\Clase\ASO\Proyectos\ProyectoFinGrado\prueba.yaml
PS C:\Users\Duke>
```
Una vez teniendo el archivo si usamos el comando **podman play kube D:\Clase\ASO\Proyectos\ProyectoFinGrado\prueba.yaml** nos creará un pod con exactamente la misma configuración y contenedores que tenemos en el .YAML

## 6.2 Guía de instalación

Empezaremos con la instalación del software:

Instalaremos Podman.

Iremos a [https://podman.io/](https://podman.io/) y tenemos 2 opciones de descarga.

La Desktop y la CLI, yo descargaré la Desktop porque así instala la CLI también.

Cuando ejecutemos el .exe nos dará la opción de descargar 3 dependencias e instalaremos las 3.

Te pedirá que instales WSL o Windows HyperV, el motivo de esto es que para crear un contenedor de Linux el sistema de contenerización necesita acceso al Kernel de Linux y lo que hace el WSL es justamente instalarte un Kernel de Linux

Ahora con Kubernetes solo tendremos que hacer un Curl

```batch
curl.exe -LO "https://dl.k8s.io/release/v1.32.0/bin/windows/amd64/kubectl.exe"
```



# 7. Referencias bibliográficas ø