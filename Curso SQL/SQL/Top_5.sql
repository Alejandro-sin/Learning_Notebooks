-- Los 5 primeros registros

-- Forma 1.
SELECT *
FROM public.alumnos
WHERE id BETWEEN 1 AND 5



-- Forma 2.
SELECT *
FROM public.alumnos
LIMIT 5



-- Forma 3.

SELECT *
FROM public.alumnos
FETCH FIRST 5 ROWS ONLY;


-- Forma 4.
SELECT *
FROM (
	SELECT ROW_NUMBER() OVER() AS row_id, *
	FROM public.alumnos
) AS alumnos_rows
WHERE row_id <=5


-- Forma 5.

SELECT *
FROM public.alumnos
WHERE id <=5



