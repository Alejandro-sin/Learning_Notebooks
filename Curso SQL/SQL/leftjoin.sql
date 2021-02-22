-- Con esto devuelvo la cantidad de alumnos por carrera
SELECT carrera_id, COUNT(*) AS cuenta
FROM public.alumnos
GROUP BY carrera_id
ORDER BY cuenta DESC;

--Para encontrar las diferencias borraremos elementos 
--DELETE FROM public.carreras
--WHERE id BETWEEN 30 and 50;


--Deuvel todos los alumnos cuya carrera no existe.
SELECT a.nombre,
	   a.apellido,
	   a.carrera_id,
	   c.id,
	   c.carrera
FROM public.alumnos AS a
	LEFT JOIN public.carreras as c
	ON carrera_id = c.id
WHERE c.id IS NULL;

