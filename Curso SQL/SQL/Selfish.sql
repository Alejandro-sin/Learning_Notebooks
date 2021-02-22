-- SELFISH
-- Los self join es hacer join con la propia tabla.
-- Este query nos devuelve el nombre del alumnos y quien es su tutor.

SELECT a.nombre,
	   a.apellido,
	   t.nombre,
	   t.apellido

FROM public.alumnos AS a
	INNER JOIN public.alumnos AS t ON a.tutor_id = t.id;
	
-- Función CONCAT()

SELECT CONCAT(a.nombre, ' ', a.apellido) AS nombre_completo,
	   CONCAT(t.nombre,' ', t.apellido ) AS tutor_nombre_completo
FROM public.alumnos AS A
	INNER JOIN public.alumnos AS t ON a.tutor_id = t.id;
		
		
--Puedo agrupar por tutor para saber cual tiene más carga de trabajo al contar lso alumnos.
SELECT CONCAT(t.nombre, ' ', t.apellido) AS tutor,
--Cuento a partir de aquí
	   COUNT(*) AS alumnos_por_tutor
FROM public.alumnos AS a
	INNER JOIN public.alumnos AS t ON a.tutor_id = t.id
GROUP BY tutor
ORDER BY alumnos_por_tutor DESC
-- Si quisiera saber los 10 tutores con mas alumnos
--LIMIT 10;
;
		