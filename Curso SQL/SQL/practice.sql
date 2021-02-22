SELECT *
FROM alumnos WHERE nombre = 'Wanda'
	OR (nombre = 'Nedda' OR nombre = 'Kelvin'
	AND colegiatura > 4000);
	