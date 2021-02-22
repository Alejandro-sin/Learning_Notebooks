-- Seleccionar la primera fila
SELECT *
FROM public.alumnos
--FETCH FIRST 1 ROWS ONLY;


-- Con limit sirve para traer el primer registro
SELECT *
FROM public.alumnos
LIMIT 1;

-- Window Functions
-- Dentro hacemos un subselect, usando la window function ROW_Number.¿ Cual es el numero de registro? con over indica que es de toda la tabla

SELECT *
FROM ( 
	SELECT ROW_NUMBER()OVER() AS row_id, *
	FROM public.alumnos
) AS alumnos_with_row_num
WHERE row_id = 1
;
