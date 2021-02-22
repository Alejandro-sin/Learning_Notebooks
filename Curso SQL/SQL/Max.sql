-- Sacar el máximo.


SELECT carrera_id, fecha_incorporacion
FROM public.alumnos
GROUP BY carrera_Id, fecha_incorporacion
ORDER BY fecha_incorporacion DESC;


SELECT carrera_id,
	MAX(fecha_incorporacion)
FROM public.alumnos
GROUP BY carrera_id
ORDER BY carrera_id; 


-- Quiero sacar el mínimo de toda la tabla
-- Quiero consultar el menor nomnre por el id del tutor.
-- Min organiza por orden alfabético.

SELECT tutor_id,
	MIN(nombre)
FROM public.alumnos
GROUP BY tutor_id
ORDER BY tutor_id;