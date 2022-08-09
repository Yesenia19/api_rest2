DROP TABLE IF EXISTS clientes;
CREATE TABLE clientes(
    id_cliente  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , 
    nombre      VARCHAR(50) NOT NULL,
    email       VARCHAR(50) NOT NULL
);
 
INSERT INTO clientes(nombre,email) VALUES("Yesenia","yesenia@email.com");
INSERT INTO clientes(nombre,email) VALUES("Lizbeth","lizbeth@email.com");
INSERT INTO clientes(nombre,email) VALUES("Veronica","veronica@email.com");

.headers ON
SELECT * FROM clientes;