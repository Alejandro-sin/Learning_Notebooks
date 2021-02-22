-- SELECTORES DE RANGO
SELECT*
FROM public.alumnos
WHERE tutor_id IN(1,2,3,4);

-- Puedo usar los rango de diversas maneras

SELECT int4range(10,20) @>3;

-- Si hay valores que se solapen entre ambos rangos me devuelve, es&& es una interseccion.
SELECT numrange(11.1, 22.2) && numrange(20.9,30.1);


-- Traer el valro más alto de un rango.

SELECT UPPER(int8range(15,25));

-- Traer el menor
SELECT LOWER(int8range(15,25));


-- Devuelve la intersección entre ambos rangos
SELECT int4range(10,20) * int4range(15,25);


-- Para saber si el rango es vacío.
SELECT ISEMPTY(numrange(1,5));


-- Usando rangos

SELECT *
FROM public.alumnos
WHERE int4range(10, 20) @> tutor_id;

