--Para traer todas las ocurrencias entr dos tablas se usa FULL OUTER JOIN.
--Se relacionan mediante su id.


SELECT alumnos.nombre,
	   alumnos.apellido,
	   alumnos.carrera_id,
	   carrera.id,
	   carrera.carrera

FROM public.alumnos AS alumnos
	FULL OUTER JOIN public.carreras AS carrera
	ON alumnos.carrera_id = carrera.id
ORDER BY alumnos.carrera_id;
	 