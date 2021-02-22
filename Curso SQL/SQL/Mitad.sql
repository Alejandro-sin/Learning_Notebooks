-- Traer la segunda mitad de la tabla

SELECT *
FROM alumnos
LIMIT 500 OFFSET 500

-- Otra forma de seleccionar el reto.

SELECT *
FROM public.alumnos
OFFSET (
	SELECT COUNT(*)/2
	FROM public.alumnos
)