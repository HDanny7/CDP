create TABLE products (
id int  not null AUTO_INCREMENT,
name varchar(50) not null,
created_by int not null,
marca VARCHAR(50),
PRIMARY KEY(id),
FOREIGN KEY(created_by) REFERENCES user(id)
);

rename table products to product; -- renombramos
USE holamundo;
INSERT INTO product (name, created_by, marca)
VALUES
	('ipad', 1, 'apple'),
	('iphone', 1, 'apple'),
	('watch', 2, 'apple'),
	('macbook', 1, 'apple'),
	('imac', 3, 'apple'),
	('ipad mini', 2, 'apple');

SELECT *FROM product;
SELECT u.id, u.email, p.name FROM user u left JOIN product p on u.id = p.created_by;
-- el comando left join trae la informacion de la tabla que ya habiamos hecho para que se relaciones con la tabla actual.
-- Aqui la realcion es de la tabla de usuarios a la tabla de productos
SELECT u.id, u.email, p.name FROM user u RIGHT JOIN product p on u.id = p.created_by;
-- es lo mismo pero desde la tabla de productos.
SELECT u.id, u.email, p.name FROM user u INNER JOIN product p on u.id = p.created_by;
-- Este te muestra todos los registros que tengan relacion entre las tablas, si hay valores entre las tablas que no se relacionan estos no se muestran
SELECT u.id, u.name, p.id, p.name FROM user u CROSS JOIN product p;
-- Este comando es usado para hacer combinaciones entre tablas, ya se probo y funciona muy bien apra ciertos casos donde se debe conocer todos las posibles combinaciones de registros posibles.
SELECT COUNT(id), marca FROM product GROUP BY marca;
SELECT COUNT(p.id), u.name from product p left join user u on u.id = p.created_by group by p.created_by;
-- de esta forma con group by podemos agrupar ciertas tablas para que los registros que se muestre tengan cierta relacion de imortancia para nosotros.
SELECT COUNT(p.id), u.name from product p left join user u 
on u.id = p.created_by group by p.created_by
HAVING COUNT(p.id) >= 2;
DROP TABLE product; -- Borrar tables.
drop table animales, user;
