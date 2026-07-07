# Integrantes del grupo:

**-Cuenca Danna**
**_Duarte Santiago**
**_Fernandez Eugenia**
**_Suárez Mauro**

**COMISION K1.3 C**


**Sistema de Reservas de Cine**

Descripción general

El sistema permite:
**.Consultar películas y horarios disponibles, junto con la cantidad de entradas restantes por función.**
**.Reservar una cantidad de entradas para una película y horario específicos, validando que haya disponibilidad.**
**.Aplicar automáticamente una promoción 2x1 sobre el importe a pagar.**
**.Registrar estadísticas globales: entradas vendidas por película, por horario y el total general.**

Toda la información (películas, horarios, capacidad, ventas y estadísticas) se guarda 
en memoria mientras el programa está corriendo, usando diccionarios de Python. No hay 
base de datos ni archivos externos: al cerrar el programa, los datos se pierden.


**Instrucciones de ejecución**


1.Guardar el archivo como ReservasCine.py.
2.Abrir una terminal en la carpeta donde está el archivo.
3.Ejecutar el siguiente comando:

**python ReservasCine.py**

4.Usar el menú interactivo:

1 --> Reservar entradas (elegir película, horario y cantidad, y confirmar con s).
2 --> Ver estadísticas de ventas: muestra un resumen con la cantidad de entradas vendidas por cada película
3 --> Salir del programa: imprime un mensaje de despedida ("Gracias por usar el sistema.").



4. Usar el menú interactivo:

   - **1** → Reservar entradas (elegir película, horario y cantidad, y confirmar con `s`).

   - **2** → Ver estadísticas de ventas: muestra un resumen con la cantidad de entradas vendidas por cada película, la demanda de cada horario (solo se listan los horarios que tuvieron al menos una venta) y el total general de entradas vendidas hasta el momento. Después de mostrarlo, vuelve automáticamente al menú principal.

   - **3** → Salir del programa: imprime un mensaje de despedida ("Gracias por usar el sistema.") y termina la ejecución, cerrando el bucle principal (`menu()`). No se guardan los datos: si se vuelve a ejecutar el programa, las ventas y estadísticas arrancan de cero.

