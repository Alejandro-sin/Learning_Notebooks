
SELECT alumnos.nombre,
	   alumnos.apellido,
	   alumnos.carrera_id,
	   carrera.id,
	   carrera.carrera
FROM public.alumnos AS alumnos
	--JOIN LEFT EXCLUSIVE
	LEFT JOIN public.carreras AS carrera
	ON alumnos.carrera_id = carrera.id
-- CONDICIÓN
--WHERE carrera.id IS NULL