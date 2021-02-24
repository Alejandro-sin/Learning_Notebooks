-- Windows Function

-- First me devuelve el primer valor de una columna, me devuel que el campo generado será el primer valor de la columna.
-- Al usar OVER y partition a través de carrera id,  solo contará el primer registo pero por id
SELECT FIRST_VALUE(colegiatura) OVER (PARTITION BY carrera_id) AS primera_colegiatura, *
FROM public.alumnos;