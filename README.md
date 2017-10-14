# Repositorio de Trazas de Transporte Público

Este repositorio es para almacenar trazas (archivos `gpx`) correspondientes a viajes específicos de servicios de transporte público. Las trazas será utilizadas posteriormente para estimar los horarios *reales* del servicio. 


Las trazas están en carpetas, una carpeta por cada servicio de transporte (por ejemplo: `bus_alajuela-targuases`). 

 * Nota para estudiantes asistentes: en cada carpeta de una ruta, se creará una subcarpeta con nombre `asistentes` donde colocarán sus trazas. 


# ¿Cómo colaborar con trazas?

**Se agradece de antemano cualquier colaboración**. Para recolectar trazas se sugiere la utilizar la herramienta `osm-tracker`.

Las trazas de viajes de un servicio de transporte público deben ser subidas por medio de un `pull request`, siguiendo el flujo de trabajo [*GitHub Flow*](https://guides.github.com/introduction/flow/). Los pasos a seguir son :

1. **Haga un [*fork*](https://guides.github.com/activities/forking/) del repositorio**.  En la [página de este repositorio](https://github.com/LabExperimental-SIUA/trazas-transporte-publico), arriba a la derecha ubique el botón *fork* y presione clic sobre el mismo. Luego de esto tendrá una copia del repositorio asociada a su usuario de GitHub. 


2. **Clone su repositorio local**. El comando para conseguirlo es: `git clone <URL.git>`, donde *<URL.git>* debe sustituirlo por la dirección a su repositorio. 


3. **Cree una rama (*branch*) en su repositorio**. Asumiendo que se encuentra en la rama `master` actualizada (revisar comando `$git status`), el comando para crear una rama con el nombre *viaje-alajuela-targuases* es: `$git checkout -b viaje-alajuela-targuases`.

4. **Agregue las trazas** a las carpetas que corresponda y súbalas a su repositorio. En esta parte deberá utilizar los comandos `git add` y `git commit`. Luego suba los cambios a su repositorio con el comando `git push`. 

5. **Cree un `Pull Request`** en el sitio web de su repositorio. Asegúrese que el `Pull Request` sea de la rama que creó antes (en el ejemplo: *viaje-alajuela-targuases*) a la rama `master` del repositorio `/LabExperimental-SIUA/trazas-transporte-publico`.


6. **Comentarios y revisión**. Algún colaborador del proyecto revisará la solicitud, en caso de requerir cambios se le indicarán y cuando todo esté en su lugar será agregado al la rama `master` del repositorio `/LabExperimental-SIUA/trazas-transporte-publico`.


Recuerde mantener actualizado su repositorio. Estos dos pasos pueden ser de utilidad:

A. **Agregue el *upstream* a su repo**. En este caso el repositorio *upstream* será llamado *labexp*, el comando para esto es: `git remote add labexp https://github.com/jamescr/trazas-transporte-publico.git`,

B. **Actualice su rama master**. Asumiendo que se encuentra en la rama `master` (revisar comando `$git status`), el comando para actualizar desde el *upstream* es: : `$git pull labexp master`. En caso que no se encuentre en la rama `master` use antes el comando `git checkout master`.
