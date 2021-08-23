# Singleton

> Patrón de creación

## Explicación

En algún momento de nuestra vida mientras creamos objetos de una clase nos podremos percatar de que realmente no hace falta crear instancias nuevas para cada uso porque, por ejemplo, con una sola conexión a la base de datos nos basta. Si creamos varios objetos y cada uno de ellos establece una conexión con la base de datos podemos llegar a saturarla.

En este punto es dónde el patrón __*singleton*__ entra en acción. Un patrón con el que cada vez que creamos una instancia nueva realmente no creamos nada y nos devuelve una referencia a la primera que se ha creado. De esta forma nos aseguramos que solamente existe una instancia de ese objeto.
