--  JOIN la parte en comun entre ambas partes

SELECT alumnos.nombre,
	   alumnos.apellido,
	   alumnos.carrera_id,
	   carrera.id,
	   carrera.carrera

FROM public.alumnos AS alumnos
	JOIN public.carreras AS carrera
	ON alumnos.carrera_id = carrera.id
