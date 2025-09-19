Cómo ejecutar el programa:

Para poder realizar la ejecución del programa se debe tomar en cuenta que se tenga instalado Python además de contar con algún IDE el cual permita la interpretación del código al igual que acepte una 
visualización gráfica, ya que el programa a demás de mostrar el resultado en consola cuenta con una pantalla adicional para un mejor entendimiento de cuantas pruebas realizo antes de obtener el resultado 
al igual del tiempo en que se tardó en conseguirlo.
En este caso para la realización del trabajo se utilizó “Visual Studio Code” entonces para poder ejecutar el programa debemos abrir el archivo “bruteforce.py”, una vez abierto debemos darle en botón play 
que se encuentra en el lado derecho como se muestra en la imagen:

<img width="921" height="116" alt="image" src="https://github.com/user-attachments/assets/a7a30304-a9f5-4ef4-b0cf-6dfe069e0714" />



Ejemplos de salida:

El ejemplo de salida en el terminal usando una contraseña de 3 dígitos como es: “abc”

<img width="625" height="135" alt="image" src="https://github.com/user-attachments/assets/f8f9e246-75f3-40fe-b05a-2ae4b12afa27" />


Como se puede observar en la imagen nos muestra la contraseña que encontró que en este caso es “abc”, además de mostrarnos lofs intentos que realizo antes de encontrarla los cuales son “98”, y por ultimo
nos muestra el tiempo trascurrido desde que inicio el ataque de fuerza bruta hasta que lo termino

El ejemplo de salida en una pantalla grafica usando igual la contraseña de 3 dígitos la cual es: “abc”

<img width="921" height="478" alt="image" src="https://github.com/user-attachments/assets/05e0d76f-5681-4a98-92c5-599d949eeac5" />


Como se visualiza en la imagen se muestra los mismos datos de la terminal pero de una forma grafica en la cual se puede observar una línea “azul” la cual indica el recorrido de intentos hasta llegar al punto “rojo” el cual indica el ultimo intento que se realizo para obtener la contraseña junto con el tiempo en que se demoró, de igual manera se observa que en el eje “y” los datos de los intentos realizados y a su vez en el eje “x” se muestra el tiempo trascurrido

Reflexión: ¿qué pasa si la contraseña tiene 8+ caracteres y usa mayúsculas, números y símbolos?

El programa que se realizó tardaría mucho tiempo en poder descubrir una contraseña con 8 caracteres intercambiados entre mayúsculas, minúsculas, números y símbolos ya que existen billones de combinaciones antes
de encontrar la contraseña, por lo cual este programa solo serviría para encontrar contraseñas cortas que estén entre los 2 a 4 caracteres. Por lo tanto esto nos da un indicio de que se debe utilizar contraseñas
complejas para evitar ataques a nuestra información ya que si se utiliza contraseñas débiles o cortas se puede observar que un simple programa que no contiene tantas líneas de código lo puede encontrar de manera 
eficiente y en un corto tiempo 
