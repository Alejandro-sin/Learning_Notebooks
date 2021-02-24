-- El segundo mayor

-- Traigo solo lo que no se repite
SELECT DISTINCT colegiatura
FROM public.alumnos AS a1
-- Donde 2 es igual a al siguiente subquery
-- Lo que está seleccionando es un índice
WHERE  2 = (
	-- Selecciona y Hace un conteo de todas las colegiaturas
	SELECT COUNT(DISTINCT colegiatura)
	-- Que provienen de la tabla que se llamará a2
	FROM public.alumnos AS a2
	-- Aqui traerá solo lso que coincidan
	WHERE a1.colegiatura <= a2.colegiatura
);



-- Forma 2.
-- Selecciono lo único de colegiatura de manera decendente con un límite de 1 desde 1. Esto ordenara de mayro a menor 
-- por colegiatura y solo extraigo el segundo valor más grande.
SELECT DISTINCT colegiatura
FROM public.alumnos
ORDER BY colegiatura DESC
LIMIT 1 OFFSET 1


-- Seleccionar todos los estudiantes que Tuvieron un tutor de id 20 con la segunda legiatura más cara

SELECT *
FROM public.alumnos AS data_alumnos
INNER JOIN (
	SELECT DISTINCT colegiatura
	FROM public.alumnos
	WHERE tutor_id =20
	ORDER BY colegiatura DESC
	LIMIT 1 OFFSET 1
) AS segunda_mayor
ON data_alumnos.colegiatura = segunda_mayor.colegiatura;


-- Forma adicional de hacer lo anterior, traer la todos lso alumnos de la segunda tutoria más cara
SELECT *
FROM public.colegiaturas as data_alumnos
WHERE colegiatura =  (
SELECT DISTINCT colegiatura
	FROM public.alumnos
	WHERE tutor_id =20
	ORDER BY colegiatura DESC
	LIMIT 1 OFFSET 1
)


