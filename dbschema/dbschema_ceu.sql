---------------------------------------
-- dev_marketing2 --
-- reemplazar dbschema_ceu. por ceu_ --
---------------------------------------
CREATE SCHEMA dbschema_ceu;


CREATE  TABLE ceu_areas ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	nombre               VARCHAR(50)  NOT NULL    
 ) engine=InnoDB;

CREATE  TABLE ceu_asignaturas ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	codigo               VARCHAR(8)      ,
	nombre               VARCHAR(160)      ,
	creditos             SMALLINT      
 );

CREATE  TABLE ceu_diccionarios ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	tabla                VARCHAR(30)  NOT NULL    ,
	texto                VARCHAR(50)  NOT NULL    
 ) engine=InnoDB;

CREATE  TABLE ceu_funciones ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	nombre               VARCHAR(80)      ,
	principal            BOOLEAN      
 ) engine=InnoDB;

CREATE  TABLE ceu_personas ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	nombre               VARCHAR(50)      ,
	apellidos            VARCHAR(50)      
 ) engine=InnoDB;

CREATE  TABLE ceu_profesores ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	persona_id           INT  NOT NULL    ,
	foto                 VARCHAR(50)      ,
	CONSTRAINT unq_profesores UNIQUE ( persona_id ) 
 ) engine=InnoDB;

CREATE  TABLE ceu_profesores_funciones ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	profesor_id          INT      ,
	funcion_id           INT      
 ) engine=InnoDB;

CREATE  TABLE ceu_tipos_titulaciones ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	nombre               VARCHAR(50)      
 ) engine=InnoDB;

CREATE  TABLE ceu_titulaciones ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	tipo_titulacion_id   INT      ,
	area_id              INT      ,
	codigo               VARCHAR(8)      ,
	nombre               VARCHAR(160)      ,
	duracion             TINYINT      ,
	duracion_tipo        CHAR(1)      ,
	creditos             SMALLINT      ,
	insercion_laboral    DECIMAL(5,1)      
 ) engine=InnoDB;

CREATE  TABLE ceu_universidades ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	nombre               VARCHAR(50)  NOT NULL    
 ) engine=InnoDB;

CREATE  TABLE ceu_asignatura_idiomas ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	asignatura_id        INT      ,
	nombre               VARCHAR(160)  NOT NULL    ,
	idioma               CHAR(2)   DEFAULT ('es')   
 ) engine=InnoDB;

CREATE  TABLE ceu_campus ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	universidad_id       INT      ,
	nombre               VARCHAR(50)  NOT NULL    
 ) engine=InnoDB;

CREATE  TABLE ceu_campus_titulaciones ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	campus_id            INT      ,
	titulacion_id        INT      ,
	codigo               VARCHAR(5)  NOT NULL    ,
	guid                 VARCHAR(36)  NOT NULL    ,
	plazas               SMALLINT      
 ) engine=InnoDB;

CREATE  TABLE ceu_competencias ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	titulacion_id        INT      ,
	grupo                VARCHAR(30)      ,
	texto                TEXT      
 ) engine=InnoDB;

CREATE  TABLE ceu_planes_estudios ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	titulacion_id        INT      ,
	ciclo_lectivo        INT      
 ) engine=InnoDB;

CREATE  TABLE ceu_salidas_profesionales ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	titulacion_id        INT      ,
	grupo                VARCHAR(60)      ,
	texto                VARCHAR(250)      
 ) engine=InnoDB;

CREATE  TABLE ceu_titulacion_idiomas ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	titulacion_id        INT      ,
	nombre               VARCHAR(160)      ,
	idioma               CHAR(2)   DEFAULT ('es')   
 ) engine=InnoDB;

CREATE  TABLE ceu_cursos ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	plan_estudio_id      INT      ,
	codigo               VARCHAR(8)      ,
	nombre               VARCHAR(50)  NOT NULL    
 );

CREATE  TABLE ceu_cursos_asignaturas ( 
	id                   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
	curso_id             INT      ,
	asignatura_id        INT      ,
	profesor_id          INT      ,
	periodo              CHAR(2)      ,
	creditos             SMALLINT      ,
	tipo                 CHAR(3)      
 ) engine=InnoDB;

ALTER TABLE ceu_asignatura_idiomas ADD CONSTRAINT fk_asignatura_idiomas_asignaturas FOREIGN KEY ( asignatura_id ) REFERENCES ceu_asignaturas( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_campus ADD CONSTRAINT fk_campus_universidades FOREIGN KEY ( universidad_id ) REFERENCES ceu_universidades( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_campus_titulaciones ADD CONSTRAINT fk_campus_titulaciones_campus FOREIGN KEY ( campus_id ) REFERENCES ceu_campus( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_campus_titulaciones ADD CONSTRAINT fk_campus_titulaciones_titulaciones FOREIGN KEY ( titulacion_id ) REFERENCES ceu_titulaciones( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_competencias ADD CONSTRAINT fk_competencias_titulaciones FOREIGN KEY ( titulacion_id ) REFERENCES ceu_titulaciones( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_cursos ADD CONSTRAINT fk_cursos_plan_estudios FOREIGN KEY ( plan_estudio_id ) REFERENCES ceu_planes_estudios( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_cursos_asignaturas ADD CONSTRAINT fk_curso_asignatura_asignaturas FOREIGN KEY ( asignatura_id ) REFERENCES ceu_asignaturas( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_cursos_asignaturas ADD CONSTRAINT fk_curso_asignatura_cursos FOREIGN KEY ( curso_id ) REFERENCES ceu_cursos( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_cursos_asignaturas ADD CONSTRAINT fk_cursos_asignaturas_profesores FOREIGN KEY ( profesor_id ) REFERENCES ceu_profesores( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_planes_estudios ADD CONSTRAINT fk_plan_estudios_titulaciones FOREIGN KEY ( titulacion_id ) REFERENCES ceu_titulaciones( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_profesores ADD CONSTRAINT fk_profesores_personas FOREIGN KEY ( persona_id ) REFERENCES ceu_personas( id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE ceu_profesores_funciones ADD CONSTRAINT fk_profesores_funciones_profesores FOREIGN KEY ( profesor_id ) REFERENCES ceu_profesores( id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE ceu_profesores_funciones ADD CONSTRAINT fk_profesores_funciones_funciones FOREIGN KEY ( funcion_id ) REFERENCES ceu_funciones( id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE ceu_salidas_profesionales ADD CONSTRAINT fk_salidas_profesionales_titulaciones FOREIGN KEY ( titulacion_id ) REFERENCES ceu_titulaciones( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_titulacion_idiomas ADD CONSTRAINT fk_titulacion_idiomas_titulaciones FOREIGN KEY ( titulacion_id ) REFERENCES ceu_titulaciones( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_titulaciones ADD CONSTRAINT fk_titulaciones_tipos_titulacion FOREIGN KEY ( tipo_titulacion_id ) REFERENCES ceu_tipos_titulaciones( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_titulaciones ADD CONSTRAINT fk_titulaciones_areas FOREIGN KEY ( area_id ) REFERENCES ceu_areas( id ) ON DELETE NO ACTION ON UPDATE CASCADE;

ALTER TABLE ceu_areas COMMENT 'area de cnocimiento';

ALTER TABLE ceu_asignaturas MODIFY codigo VARCHAR(8)     COMMENT 'código original de referencia';

ALTER TABLE ceu_asignaturas MODIFY nombre VARCHAR(160)     COMMENT 'solo para referencia, utilizar asignatura_idiomas.nombre';

ALTER TABLE ceu_diccionarios COMMENT 'tabla utilizada como diccionario para los campos descriptivos';

ALTER TABLE ceu_funciones COMMENT 'funciones y cargos de los docentes';

ALTER TABLE ceu_funciones MODIFY principal BOOLEAN     COMMENT 'función o cargo principal';

ALTER TABLE ceu_profesores MODIFY foto VARCHAR(50)     COMMENT 'ruta de la imagen';

ALTER TABLE ceu_titulaciones MODIFY area_id INT     COMMENT 'area de conocimiento';

ALTER TABLE ceu_titulaciones MODIFY codigo VARCHAR(8)     COMMENT 'código original de referencia';

ALTER TABLE ceu_titulaciones MODIFY nombre VARCHAR(160)     COMMENT 'solo para referencia, utilizar asignatura_idiomas.nombre';

ALTER TABLE ceu_titulaciones MODIFY duracion TINYINT     COMMENT 'cantidad de (año/mes/dia/hora)';

ALTER TABLE ceu_titulaciones MODIFY duracion_tipo CHAR(1)     COMMENT 'medida de tiempo (año/mes/dia/hora)';

ALTER TABLE ceu_titulaciones MODIFY creditos SMALLINT     COMMENT 'sumatoria de créditos de todas las materias';

ALTER TABLE ceu_titulaciones MODIFY insercion_laboral DECIMAL(5,1)     COMMENT 'tasa de inserción laboral según ranking BBVA e IVIE';

ALTER TABLE ceu_asignatura_idiomas MODIFY idioma CHAR(2)   DEFAULT ('es')  COMMENT 'idioma en el que se impartirá la asignatura (es, en, fr)';

ALTER TABLE ceu_planes_estudios MODIFY ciclo_lectivo INT     COMMENT 'año correspondiente al plan de estudio';

ALTER TABLE ceu_titulacion_idiomas MODIFY idioma CHAR(2)   DEFAULT ('es')  COMMENT 'idioma en el que se impartirá la titulación (es, en, fr)';

ALTER TABLE ceu_cursos MODIFY codigo VARCHAR(8)     COMMENT 'código original de referencia';

ALTER TABLE ceu_cursos_asignaturas MODIFY periodo CHAR(2)     COMMENT 'Trimestre / Cuatrimestre / Semestre';

ALTER TABLE ceu_cursos_asignaturas MODIFY tipo CHAR(3)     COMMENT 'Formación Básica / OBligatoria / OPtativa / PRáctica / Trabajo Fin Grado';





---------------------------
-- vistas personalizadas --
---------------------------
CREATE VIEW titulacion_asignaturas_view AS 
SELECT t.nombre AS titulacion, pe.ciclo_lectivo, c.nombre AS curso, a.codigo, a.nombre AS asignatura, a.idioma, ca.creditos, ca.tipo
FROM titulaciones t
INNER JOIN planes_estudios pe ON pe.titulacion_id = t.id
INNER JOIN cursos c ON c.plan_estudio_id = pe.id
INNER JOIN cursos_asignaturas ca ON ca.curso_id = c.id
INNER JOIN asignaturas a ON a.id = ca.asignatura_id;;


CREATE VIEW titulacion_profesores_view AS 
SELECT grupo.area, grupo.titulacion, grupo.ciclo_lectivo, pe.nombre, pe.apellidos
FROM (
    SELECT distinct a.nombre AS area, t.nombre AS titulacion, pe.ciclo_lectivo, ca.profesor_id
    FROM titulaciones t
    INNER JOIN areas a on a.id = t.area_id
    INNER JOIN planes_estudios pe ON pe.titulacion_id = t.id    
    INNER JOIN cursos c ON c.plan_estudio_id = pe.id
    INNER JOIN cursos_asignaturas ca ON ca.curso_id = c.id
) AS grupo
INNER JOIN profesores p ON p.id = grupo.profesor_id
INNER JOIN personas pe ON pe.id = p.persona_id;


create view planes_estudios_view as
select pe.titulacion_id, pe.ciclo_lectivo, c.nombre plan, ai.nombre asignatura, ai.idioma, ca.periodo, ca.creditos, ca.tipo
from ceu_planes_estudios pe
inner join ceu_cursos c on c.plan_estudio_id = pe.id
inner join ceu_cursos_asignaturas ca on ca.curso_id = c.id
inner join ceu_asignaturas a on a.id = ca.asignatura_id
inner join ceu_asignatura_idiomas ai on ai.asignatura_id = a.id
-- where ai.idioma = 'es'


create view titulaciones_cursos_view as
select t.id, t.codigo, ti.nombre titulacion, tt.nombre tipo, 
       pe.titulacion_id, pe.ciclo_lectivo, pe.plan, pe.asignatura, pe.idioma, pe.periodo, pe.creditos, pe.tipo tipo_asig
from ceu_titulaciones t
inner join ceu_titulacion_idiomas ti on ti.titulacion_id = t.id
inner join ceu_tipos_titulaciones tt on tt.id = t.tipo_titulacion_id
left join planes_estudios_view pe on pe.titulacion_id = t.id
-- where t.codigo = '112' and ti.idioma = 'es' and pe.idioma = 'es'


Create View ceu_titulaciones_view As
Select 
    tt.id tipo_id, tt.nombre tipo, 
    c.id campus_id, c.nombre campus,
    a.id area_id, a.nombre area, 
	t.id titulacion_id, t.codigo, t.nombre titulacion, t.duracion, t.duracion_tipo, t.creditos
From ceu_titulaciones t
Inner Join ceu_tipos_titulaciones tt On tt.id = t.tipo_titulacion_id
Inner Join ceu_areas a On a.id = t.area_id
Inner Join ceu_campus_titulaciones ct On ct.titulacion_id = t.id
Inner Join ceu_campus c On c.id = ct.campus_id
