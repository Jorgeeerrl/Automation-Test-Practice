# Automation Test Practice

Este proyecto automatiza las pruebas del sitio web [Test Automation Practice](https://testautomationpractice.blogspot.com) utilizando Selenium WebDriver y Python.
El Test "test_00 - Automatización Completa.py" utiliza el archivo config.py para la configuración del driver. El resto de tests funcionan independientemente en este sentido.

## Estructura del Proyecto

```
├── chromedriver.exe
├── config.py
├── test_00 - Automatización Completa.py
├── test_01 - Formulario.py
├── test_02 - Checks.py
├── test_03 - Menú Desplegable.py
├── test_04 - Colors.py
├── test_05 - Calendario.py
├── test_06 - Navegación.py
├── test_07 - Oculto.py
├── test_08 - Web Table.py
├── test_09 - Pagination Table.py
├── test_10 - Wikipedia.py
├── test_11 - iFrame_Formulario.py
├── test_12 - Resizable.py
├── test_13 - Slider.py
├── test_14 - Abuse.py
├── test_15 - Drag_and_Drop.py
├── test_16 - Copytext.py
└── test_17 - Alertas.py
```

## Detalle de los Casos de Prueba

1. **`test_00 - AUTOMATIZACIÓN COMPLETA.py`**: <strong>Ejecuta una serie completa de pruebas automatizadas que incluyen formularios, checks, menús desplegables, colores, calendario, navegación, y más.</strong>
2. **`test_01 - Formulario.py`**: Prueba la funcionalidad de un formulario de entrada de datos.
3. **`test_02 - Checks.py`**: Prueba los elementos de tipo checkbox en el formulario.
4. **`test_03 - Menú Desplegable.py`**: Prueba la funcionalidad de un menú desplegable.
5. **`test_04 - Colors.py`**: Prueba la selección de opciones en un menú de colores.
6. **`test_05 - Calendario.py`**: Prueba la funcionalidad del calendario.
7. **`test_06 - Navegación.py`**: Prueba la navegación entre diferentes enlaces en la página.
8. **`test_07 - Oculto.py`**: Prueba la interacción con elementos ocultos en la página.
9. **`test_08 - Web Table.py`**: Prueba la manipulación y validación de datos dentro de una tabla web.
10. **`test_09 - Pagination Table.py`**: Prueba la funcionalidad de la paginación en una tabla.
11. **`test_10 - Wikipedia.py`**: Prueba la integración y búsqueda de datos en Wikipedia.
12. **`test_11 - iFrame_Formulario.py`**: Prueba la interacción dentro de un iFrame y el envío de formularios.
13. **`test_12 - Resizable.py`**: Prueba la funcionalidad de elementos redimensionables.
14. **`test_13 - Slider.py`**: Prueba la funcionalidad de un control deslizante (slider).
15. **`test_14 - Abuse.py`**: Prueba la funcionalidad de reporte de abuso.
16. **`test_15 - Drag_and_Drop.py`**: Prueba la funcionalidad de arrastrar y soltar (drag and drop).
17. **`test_16 - Copytext.py`**: Prueba la funcionalidad de copiar y pegar texto.
18. **`test_17 - Alertas.py`**: Prueba la interacción con diferentes tipos de alertas.


## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Jorgeeerrl/automation-test-practice.git
    cd automation-test-practice
    ```

## Uso

Para ejecutar las pruebas automatizadas, utiliza el siguiente comando:
```bash
pytest nombre-del-archivo-de-prueba.py
