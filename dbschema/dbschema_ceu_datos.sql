INSERT INTO `ceu_universidades` (`id`, `nombre`) VALUES
  (1, 'San Pablo'),
  (2, 'Cardenal Herrera'),
  (3, 'Abat Oliba');

INSERT INTO `ceu_campus` (`id`, `universidad_id`, `nombre`) VALUES
  (1, 1, 'Valencia'),
  (2, 1, 'Elche'),
  (3, 1, 'Castellón');

INSERT INTO `ceu_areas` (`id`, `nombre`) VALUES
  (1, 'Ciencias de la Salud'),
  (2, 'Comunicación'),
  (3, 'Derecho y Política'),
  (4, 'Diseño'),
  (5, 'Educación'),
  (6, 'Empresa y Marketing'),
  (7, 'Deporte'),
  (8, 'Ingeniería'),
  (9, 'Arquitectura'),
  (10, 'Veterinaria'),
  (11, 'Gastronomía');

INSERT INTO `ceu_tipos_titulaciones` (`id`, `nombre`) VALUES
  (4, 'Estudios Propios'),
  (5, 'Doble Grado'),
  (6, 'Máster Universitario');

INSERT INTO `ceu_titulaciones` (`id`, `tipo_titulacion_id`, `area_id`, `nombre`, `nombre_largo`, `duracion`, `duracion_tipo`, `creditos`, `idioma`, `insercion_laboral`) VALUES
  (1, 5, 1, 'Farmacia', 'Grado en Farmacia', 5, 'a', 300, 'es', '95.4');

INSERT INTO `ceu_competencias` (`id`, `titulacion_id`, `grupo`, `texto`) VALUES
  (1, 1, 'Generales', 'Desarrollar habilidades de comunicación e información, tanto orales como escritas, para tratar con pacientes y usuarios del centro donde desempeñe su actividad profesional. Promover las capacidades de trabajo y colaboración en equipos multidisciplinares y las relacionadas con otros profesionales sanitarios.'),
  (2, 1, 'Generales', 'Reconocer las propias limitaciones y la necesidad de mantener y actualizar la competencia profesional, prestando especial importancia al autoaprendizaje de nuevos conocimientos basándose en la evidencia científica disponible.'),
  (3, 1, 'Específicas', 'Identificar, diseñar, obtener, analizar, controlar y producir fármacos y medicamentos, así como otros productos y materias primas de interés sanitario de uso humano o veterinario.'),
  (4, 1, 'Específicas', 'Evaluar los efectos terapéuticos y tóxicos de sustancias con actividad farmacológica.'),
  (5, 1, 'Específicas', 'Saber aplicar el método científico y adquirir habilidades en el manejo de la legislación, fuentes de información, bibliografía, elaboración de protocolos y demás aspectos que se consideran necesarios para el diseño y evaluación crítica de ensayos preclínicos y clínicos.'),
  (6, 1, 'Específicas', 'Diseñar, preparar, suministrar y dispensar medicamentos y otros productos de interés sanitario.'),
  (7, 1, 'Específicas', 'Prestar consejo terapéutico en farmacoterapia y dietoterapia, así como en el ámbito nutricional y alimentario en los establecimientos en los que presten servicios.'),
  (8, 1, 'Específicas', 'Promover el uso racional de los medicamentos y productos sanitarios, así como adquirir conocimientos básicos en gestión clínica, economía de la salud y uso eficiente de los recursos sanitarios.'),
  (9, 1, 'Específicas', 'Identificar, evaluar y valorar los problemas relacionados con fármacos y medicamentos, así como participar en las actividades de farmacovigilancia.'),
  (10, 1, 'Específicas', 'Llevar a cabo las actividades de farmacia clínica y social, siguiendo el ciclo de atención farmacéutica.'),
  (11, 1, 'Específicas', 'Intervenir en las actividades de promoción de la salud, prevención de enfermedad, en el ámbito individual, familiar y comunitario; con una visión integral y multiprofesional del proceso salud-enfermedad.'),
  (12, 1, 'Específicas', 'Diseñar, aplicar y evaluar reactivos, métodos y técnicas analíticas clínicas, conociendo los fundamentos básicos de los análisis clínicos y las características y contenidos de los dictámenes de diagnóstico de laboratorio.'),
  (13, 1, 'Específicas', 'Evaluar los efectos toxicológicos de sustancias y diseñar y aplicar las pruebas y análisis correspondientes.'),
  (14, 1, 'Específicas', 'Desarrollar análisis higiénico-sanitarios, especialmente los relacionados con los alimentos y medioambiente.'),
  (15, 1, 'Específicas', 'Conocer los principios éticos y deontológicos según las disposiciones legislativas, reglamentarias y administrativas que rigen el ejercicio profesional, comprendiendo las implicaciones éticas de la salud en un contexto social en transformación.');

INSERT INTO `ceu_salidas_profesionales` (`id`, `titulacion_id`, `grupo`, `texto`) VALUES
  (1, 1, 'Análisis Clínicos', 'Sector Público: Laboratorios de la Administración, Hospitales, Ayuntamientos y Facultades'),
  (2, 1, 'Análisis Clínicos', 'Privado: Laboratorios, Clínicas, Hospitales y Oficinas de Farmacia'),
  (3, 1, 'Farmacia Comunicataria', 'Director Técnico propietario'),
  (4, 1, 'Farmacia Comunicataria', 'Director Técnico copropietario'),
  (5, 1, 'Farmacia Comunicataria', 'Adjunto, sustituto, regente'),
  (6, 1, 'Colegios y Consejo General de Colegios', 'Técnicos de la Administración'),
  (7, 1, 'Colegios y Consejo General de Colegios', 'Técnicos de Laboratorio'),
  (8, 1, 'Colegios y Consejo General de Colegios', 'Centro de Información del Medicamento'),
  (9, 1, 'Colegios y Consejo General de Colegios', 'Técnicos de Atención Farmacéutica'),
  (10, 1, 'Óptica y Audiometría', 'Sector privado: cuenta propia o ajena'),
  (11, 1, 'Plantas Medicinales', 'Sector privado: cuenta propia o ajena'),
  (12, 1, 'Dermofarmacia', 'Laboratorios'),
  (13, 1, 'Dermofarmacia', 'Oficinas de Farmacia'),
  (14, 1, 'Prensa Profesional', 'Directores y redactores'),
  (15, 1, 'Farmacia Hospitalaria', 'Sector Público: Hospitales y Centros de Atención Primaria'),
  (16, 1, 'Farmacia Hospitalaria', 'Sector Privado: Hospitales, Clínicas e Industria Farmacéutica'),
  (17, 1, 'Toxicología', 'Sector público: Ministerio de Justicia, de Sanidad y Consumo'),
  (18, 1, 'Toxicología', 'Ayuntamientos'),
  (19, 1, 'Toxicología', 'Sector privado: Laboratorios'),
  (20, 1, 'Industria', 'Director Técnico'),
  (21, 1, 'Industria', 'Director y Técnico en control'),
  (22, 1, 'Industria', 'Director y Técnico en control de calidad'),
  (23, 1, 'Industria', 'Director y Técnico de producción'),
  (24, 1, 'Industria', 'Técnico en investigación y desarrollo'),
  (25, 1, 'Industria', 'Técnico en Registro'),
  (26, 1, 'Industria', 'Técnico en planificación de compras'),
  (27, 1, 'Industria', 'Marketing (Análisis de mercado, jefe de producto, delegado de ventas o Informador técnico de medicamentos)'),
  (28, 1, 'Medio Ambiente', 'Laboratorios'),
  (29, 1, 'Medio Ambiente', 'Administración'),
  (30, 1, 'Medio Ambiente', 'Empresas (ecotoxicología)');

INSERT INTO `ceu_planes_estudios` (`id`, `titulacion_id`, `ciclo_lectivo`) VALUES
  (1, 1, 2021);

INSERT INTO `ceu_cursos` (`id`, `plan_estudio_id`, `nombre`) VALUES
  (1, 1, 'Curso 1'),
  (2, 1, 'Curso 2'),
  (3, 1, 'Curso 3'),
  (4, 1, 'Curso 4'),
  (5, 1, 'Curso 5');

INSERT INTO `ceu_asignaturas` (`id`, `codigo`, `nombre`, `creditos`, `idioma`) VALUES
  (1, '1661001B', 'Matemáticas y Estadísticas', 6, 'es'),
  (2, '1661002B', 'Química', 6, 'es'),
  (3, '1661003B', 'Biología', 6, 'es'),
  (4, '1661004B', 'Estructura y Función del Cuerpo Humano I', 6, 'es'),
  (5, '1661N05U', 'Introducción a la Farmacia', 6, 'es'),
  (6, '1661007B', 'Bioquímica', 8, 'es'),
  (7, '1661008B', 'Física', 6, 'es'),
  (8, '1661009B', 'Estructura y Función del Cuerpo Humano II', 10, 'es'),
  (9, '1661N06U', 'Historia de la Ciencia', 6, 'es');

INSERT INTO `ceu_personas` (`id`, `nombre`, `apellidos`) VALUES
  (1, 'John Forbes', 'Nash');

INSERT INTO `ceu_profesores` (`id`, `persona_id`, `foto`) VALUES
  (1, 1, NULL);

INSERT INTO `ceu_funciones` (`id`, `profesor_id`, `nombre`, `principal`) VALUES
  (1, 1, 'Profesor Titular de Matemáticas', 1);

INSERT INTO `ceu_campus_titulaciones` (`id`, `campus_id`, `titulacion_id`, `codigo`, `guid`, `plazas`) VALUES
  (1, 1, 1, '', '', 75);

INSERT INTO `ceu_cursos_asignaturas` (`id`, `curso_id`, `asignatura_id`, `profesor_id`, `creditos`, `tipo`) VALUES
  (1, 1, 1, 1, 6, 'fb'),
  (2, 1, 2, 1, 6, 'fb'),
  (3, 1, 3, 1, 6, 'fb'),
  (4, 1, 4, 1, 6, 'fb'),
  (5, 1, 5, 1, 6, 'ob'),
  (6, 1, 6, 1, 8, 'fb'),
  (7, 1, 7, 1, 6, 'fb'),
  (8, 1, 8, 1, 10, 'fb'),
  (9, 1, 9, 1, 6, 'ob');
