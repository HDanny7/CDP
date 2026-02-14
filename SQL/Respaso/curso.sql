USE holamundo;
CREATE TABLE user (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
edad INT NOT NULL,
email VARCHAR(100) NOT NULL,
PRIMARY KEY (id)
);

INSERT INTO user (name, edad, email) VALUES ('Oscar', 25, 'oscar@gmail.com');
INSERT INTO user (name, edad, email) VALUES ('Layla', 15, 'laila@gmail.com');
INSERT INTO user (name, edad, email) VALUES ('Nicolas', 36, 'nicolas@gmail.com');
INSERT INTO user (name, edad, email) VALUES ('Chanchito', 7, 'chanchito@gmail.com');

SELECT *FROM user;
SELECT *FROM user LIMIT 1;
SELECT *from user where edad > 15;
SELECT *from user where edad >= 15;
SELECT *from user where edad > 20 and email = 'nicolas@gmail.com';
SELECT *from user where edad > 20 or email = 'laila@gmail.com';
SELECT *from user where email != 'laila@gmail.com'; -- '!=' este signo significa distinto.
SELECT *from user where edad BETWEEN 15 and 30;
SELECT *from user where email like '%gmail%'; -- El % sirve para indicarle que busque algun dato relacionado con la palabra y poner
-- el % al inicio indica que no importa el inicio del dato y pornerlo al final indica que el final. Ej: $gmail indica que no sabemos antes de gmail que hay.
-- gmail% indica que no sabemos despues de gmail que sigue, pero buscamos todos los datos que compartan esa similitud.
SELECT *from user ORDER BY edad asc; -- busca en orden ascendente
SELECT *from user ORDER BY edad DESC; -- Busca en orden descendente
SELECT max(edad) as mayor from user; -- pasan variias cosas, usamos max para determinar que queremos el valor maximo,
-- seleccionamos entre () la edad porque queremos el valor maximo de esa columna y le damos el alias de mayor con AS.
SELECT min(edad) as minimo from user; -- lo mismo pero ahora con el minimo.

SELECT id, name from user; -- solo seleccionamos 2 columnas con este modo
SELECT id, name as nombre from user; -- le damos un alias a una columna.



