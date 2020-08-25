CREATE DATABASE cafeteria;
USE cafeteria;
CREATE TABLE tipo_de_cafe(
	Id_tipo int auto_increment primary key,
	nombre varchar(50) not null,
	descripcion varchar(110) not null);

CREATE TABLE cafetera(
	Id_cafetera int auto_increment primary key,
	nombre_id varchar(50) not null,
	marca varchar(50) not null, 
	modelo varchar(50) not null,
	Id_tipo int not null,
	capacidad int, 
	cantidad int, 
	funcionando varchar(40) not null, 
	foreign key(Id_tipo) references tipo_de_Cafe(Id_tipo)
	);

