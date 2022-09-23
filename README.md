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

*Prerequisito: Tener creado una cantidad de empleados con los permisos necesarios*

**1. Test Suite - Certificado Firma**
- Caso 1 (Happy Path): Crear un certificado raiz. Verificación de leyenda exitosa. Verifica la existencia de elemento traído.
- Caso 2: Eliminación certificado.

**2. Test Suite - Documentación**
- Caso 1 (Happy Path): Subir documento. Chequeo de operación exitosa.
- Caso 2: Eliminación de documento. Chequeo de la desaparición del elemento.
- Caso 3: Firma de documentación subida. 
- Caso 4: Descarga de documento PDF. Chequeo de existencia de archivo en carpeta del sistema operativo.

**3. Test Suite - Recibos de Sueldo**
- Caso 1 (Happy Path): Subida de documento. Chequeo del elemento en tabla.
- Caso 2: Eliminación del documento.


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
3. Descargar ```chromedriver``` y ubicar en la raíz del proyecto. 
            https://chromedriver.chromium.org/downloads

   *Tener en cuenta la version del navegador web a la hora de descargar.*
4. En línea de comandos ejecutar (*El segundo comando es opcional, sirve para ver los mensajes print*):
   ```sh
   python -m pytest
   ```
   ```sh
   python -m pytest -s
   ```




## Contacto

Virginia Sacudato

Project Link: [https://github.com/virginiasacudato/PlanificacionHoraria](https://github.com/virginiasacudato/PlanificacionHoraria)




 