<!-- PROJECT LOGO -->
<br />
<div>
  <a href="https://github.com/virginiasacudato/PlanificacionHoraria">
   
  </a>

<h3 align="center">Legajo Digital</h3>






<!-- ABOUT THE PROJECT -->
## Acerca del proyecto

Con este proyecto se busca automatizar pruebas para el módulo Legajo Digital.

A continuación un detalle de los casos de prueba que realiza:

**1. Test Suite - Certificado Firma:**
- Caso 1 (Happy Path): Crear un certificado raiz. Verificación de leyenda exitosa. Verifica la existencia de elemento traído.
- Caso 2: Crear certificado raiz sin el campo contraseña. Verificación de leyenda de error.
- Caso 3: Eliminar certificado raiz.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Construido

* Python - Pytest
* Selenium


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Empezando

El proyecto está construido en base al patrón de diseño Page Object Model(POM).

### Prerequisitos

v.Python >= 3.10

### Instalación

1. Clonar el repositorio.
   ```sh
   git clone https://github.com/virginiasacudato/PlanificacionHoraria.git
   ```
2. Crear un archivo .env con las siguientes variables de entorno:
   ```sh
   USER=example@mail.com
   PASSWORD=password
   URL=http://urlexample.com
   ```
3. En línea de comandos ejecutar (*Aclaración: el segundo comando es opcional, sirve para ver los mensajes print*):
   ```sh
   python -m pytest
   ```
   ```sh
   python -m pytest -s
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contacto

Virginia Sacudato

Project Link: [https://github.com/virginiasacudato/PlanificacionHoraria](https://github.com/virginiasacudato/PlanificacionHoraria)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


 