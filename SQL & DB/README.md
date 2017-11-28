## Informacion sobre esta carpeta y como cruzar los datos

Aqui se contienen las consultas de SQL usadas para obtencion de datos para predicición y nálisis de damanda. Tambien hay copias de los output files.

El arhivo AccQuality tiene los datos de las calidades de las cuentas, este es el que cruzamos con los datos de opp30d.csv para realizar la predicción.


Para hacer el cruce, es necesario hacer un join.

los pasos a seguir son.

* 1. Abrir una terminal
* 2. navegar hasta el directorio en que se encuenten las tablas
* 3. ejecutar los siguientes comandos

Abrimos Sqlite3

	>> sqlite3

Creamos las tablas

	>>  create table QUALITY(Id varchar,Name varchar, 
	Quality_of_Location__c varchar, 
	Partner_Website__c varchar, 
	Research_Ranking__c varchar, 
	Google_Streetview_Rating__c varchar,
	 CreatedDate DATE);
	 
	>> create table 'op30d' ('country' varchar(45) DEFAULT NULL, 
	'Tercera' varchar(45) DEFAULT NULL,
	'Account_Name' varchar(100) DEFAULT NULL,
	 'Account_ID_18' varchar(45) DEFAULT NULL,
	'accCreatedDate' varchar(45) DEFAULT NULL,
	'Opp_18' 	varchar(45) DEFAULT NULL,
	'oppPrimary_Deal_Services__c' varchar(45) DEFAULT NULL,
	'cupones' varchar(45) DEFAULT NULL,
	'Cash_in_USD' varchar(45) DEFAULT NULL);

Importamos las tablas, para esto primero definir el separador de los datos

	>> .separator ;

Importamos las calidades

	>> .import Acc_Quality.csv QUALITY

Y los datos de las oportunidades

	>> .import opp30d.csv op30d

Hacemos el JOIN y exportamos la consulta a un csv

	>> .mode csv
	>> .output opp_q30_v4.csv
	>> SELECT * FROM op30d as acc , quality as q
	where acc.Account_ID_18 = q.Id;
	>> .output stdout

Notar que por la naturaleza del problema no nos sirve un outer join pues perderiamos el label o la informacion requerida para predecir