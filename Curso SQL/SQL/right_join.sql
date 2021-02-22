-- RIGTH JOIN

SELECT alumnos.nombre,
	   alumnos.apellido,
	   alumnos.carrera_id,
	   carrera.id,
	   carrera.carrera

FROM public.alumnos AS alumnos
	RIGHT JOIN public.carreras AS carrera
	ON alumnos.carrera_id = carrera.id
-- EXLUYENDO CARRERAS SIN ALUMNOS
WHERE alumnos.id IS NULL