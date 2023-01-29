El procedimiento tiene como objetivo obtener de forma automática una capa de ríos, a través de los procesos de la librería Arcpy, los resultados del mismo dependen en última instancia del modelo que se utilice como parámetro de entrada. Alcanza resultados interesantes en modelos que se encuentran en zonas de montaña, no así en zonas llanas.

Tener en cuenta que para mejores resultados el modelo debe abarcar una superficie acotada, para que los procesos se lleven a cabo en áreas con cierta constancia de similitud.

Se presentan dos procedimientos, por si se desea generar los ríos de un solo modelo o en cambio se desea obtener los ríos de varios modelos a la vez. Teniendo en cuenta en esta última opción que los modelos deben estar todos contenidos dentro de un mismo directorio de trabajo.
Nota: En caso de requerirse modelos para utilizar este procedimiento se puede ver el siguiente enlace https://github.com/pmatiasn/Descarga-de-modelo

Algunos ejemplos de resultados obtenidos a partir de MDE de 30 metros descargados de la página del IGN. Se puede observar que en zonas de fuerte pendiente se obtiene mejor calidad de los datos que en zonas donde la pendientes es menos abrupta o se observan cuerpos de agua.

<img width="583" alt="image" src="https://user-images.githubusercontent.com/83612209/215350377-2bef0e9f-725b-49a1-9359-a3787ee33428.png">
<img width="593" alt="image" src="https://user-images.githubusercontent.com/83612209/215350587-194e825d-07b0-4a2e-ad61-948cc9c6cad2.png">


