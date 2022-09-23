# CEU - Universidad Cardenal Herrera

Diagrama **ER** (relación de entidades) con información de los modelos necesarios para la construcción de la web correspondiente a **UCH CEU**.  
El modelo actual, está pensado para poder ser utilizado por otra universidad del grupo, no solamente UCH.  

<br><br>

## Tabla: universidades 
Contiene información relacionada a cada universidad.  
Por ejemplo:  
- Cardenal Herrera
- San Pablo
- Abat Oliba

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT  
| nombre | VARCHAR(50)  
<br><br>  

---
## Tabla: campus 
Contiene las divisiones existentes en cada universidad. Por ejemplo: 
Valencia, Elche o Castellón para la universidad Cardenal Herrera.

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT
| universidad_id 🔍 | INT
| nombre | VARCHAR(50)
|

| Clave Foranea  
|---
| fk_campus_universidades ( universidad_id ) --> dbschema_ceu.universidades( id ) ON DELETE NO ACTION ON UPDATE CASCADE
<br><br>

---
## Tabla: tipos_titulaciones 
Contiene los distintos tipos de titulaciones. Por ejemplo:  
- Grado
- Doble Grado
- Máster

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT
| nombre | VARCHAR(50)
<br><br>

---
## Tabla: areas 
Contiene todas las área de conocimiento. Por ejemplo:
- Educación
- Comunicación
- Empresa y marketing
- Deporte
- Ciencias de la Salud
- Ingeniería
- Arquitectura
- Diseño
- Derecho y Política
- Veterinaria
- Gastronomía


| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT |  |
| nombre | VARCHAR(50)  |  |
<br><br>

---
## Tabla: titulaciones 
Contiene todas las titulaciones (carreras) agrupadas según su tipo.  

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT  
| tipo_titulacion_id 🔍 | INT  
| area_id 🔍 | INT  | area de conocimiento 
| nombre | VARCHAR(80)  
| nombre_largo | VARCHAR(160)  
| duracion | TINYINT  | cantidad de (año/mes/dia/hora)  
| duracion_tipo | CHAR(1) | medida de tiempo (**a**ño/**m**es/**d**ia/**h**ora)  
| creditos | SMALLINT  | sumatoria de créditos de todas las materias  
| idioma | VARCHAR(2) | idioma en el que se impartirá la titulación (es, en, fr)  
| insercion_laboral | DECIMAL(5,2) | tasa de inserción laboral según BBVA e IVIE
<br><br>

---
## Tabla: campus_titulaciones 
Contiene la relación entre los campus y las titulaciones. Cada una de estas relaciones debe ser única, sin embargo, por cada campus habrá varias titulaciones y cada titulación puede pertener a varios campus.

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT
| campus_id 🔍 | INT
| titulacion_id 🔍 | INT
| codigo | VARCHAR(5)
| guid | VARCHAR(36)
| plazas | SMALLINT  
<br><br>

---
## Tabla: competencias
| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT
| titulacion_id 🔍 | INT
| grupo | VARCHAR(30)
| texto | TEXT
<br><br>

---
## Tabla: salidas_profesionales
| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT
| titulacion_id 🔍 | INT
| grupo | VARCHAR(30)
| texto | TEXT
<br><br>

---
## Tabla: plan_estudios 
Contiene información referente a los planes de estudios existentes, los cuales estarán agrupados por *año lectivo* y *titulación*.

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑| INT AUTO_INCREMENT
| titulacion_id 🔍 | INT  
| ciclo_lectivo</a>| INT | año correspondiente al plan de estudio |  
<br><br>

---
## Tabla: cursos 
Contiene información referente a cada curso que se dicta en un plan de estudio específico.
| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT
| plan_estudio_id 🔍 | INT
| nombre | VARCHAR(50)
<br><br>

---
## Tabla: personas 
Contiene información relacionada con una persona. Cada profesor o alumno es a su vez una persona. Esta tabla existe para normalizar este tipo de modelo evitando redundancia de datos.

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑| INT AUTO_INCREMENT
| nombre | VARCHAR(50)
| apellidos | VARCHAR(50)
<br><br>

---

## Tabla: profesores 
Contiene información relacionada a cada profesor.

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑| INT AUTO_INCREMENT
| persona_id 🔍| INT  
| foto | VARCHAR(50) | ruta de la imagen  
<br><br>

---
## Tabla: asignaturas 
La tabla de **asignaturas** contiene todas las materias agrupadas por profesor.

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT  
| profesor_id 🔍| INT  
| codigo | VARCHAR(9)  
| nombre | VARCHAR(50)  
| creditos | SMALLINT  
| idioma | VARCHAR(2) | idioma en el que se impartirá la asignatura (es, en, fr)  
<br><br>

---
## Tabla: curso_asignatura 
Contiene la relación entre curso y asignatura, esta relación será única, pero cada curso tendrá varias asignaturas y cada asignatura puede pertenecer a varios cursos.

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT
| curso_id 🔍 | INT
| asignatura_id 🔍 | INT
| creditos | SMALLINT
| tipo | VARCHAR(2) | **OB**ligatoria, **OP**cional, etc.
<br><br>

---
## Tabla: funciones 
Contiene información de cargos y funciones para cada profesor.

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑| INT AUTO_INCREMENT
| profesor_id 🔍 | INT
| nombre | VARCHAR(80)
| principal | BOOLEAN | función o cargo principal |
<br><br>

---
## Tabla: diccionarios 
La tabla **diccionarios** se utiliza para los campos descriptivos de todas las tablas.  

| Campo | Tipo | Descripción |
|---|---|---|
| id 🔑 | INT AUTO_INCREMENT
| tabla | VARCHAR(30)
| texto | VARCHAR(50)
<br><br>

