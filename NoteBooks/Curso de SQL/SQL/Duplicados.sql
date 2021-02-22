-- Cuenta los valores dupplicados por id,
-- las bases de datos automaticamente gestionana esto, por lo que hay otra forma de hacerl0

SELECT *
FROM public.alumnos AS ou
WHERE(
	SELECT *
	FROM public.alumnos AS inr
	WHERE ou.id = inr.id
) > 1:


-- Vamos a hacer un select a la tabla, quiero seleccioanr todos los campos de la tabla public.alumnos
-- Los dos dos puntos, es un cast para convertir los campos en un texto.
-- Agrupo y selecciono todo menos el id.

SELECT (public.alumnos.nombre,
		public.alumnos.apellido,
		public.alumnos.email,
		public.alumnos.colegiatura,
	   	public.alumnos.fecha_incorporacion
	   )::text, COUNT(*)
FROM public.alumnos
GROUP BY public.alumnos.nombre,
		public.alumnos.apellido,
		public.alumnos.email,
		public.alumnos.colegiatura,
	   	public.alumnos.fecha_incorporacion

-- HAVING, se ejecuta después del WHERE, HAVING se ejecut ala final de todo.
HAVING COUNT(*)>1;


-- Otra forma de encontrar duplicados, usamos over y partition
SELECT *
FROM (
	SELECT id,
	ROW_NUMBER()OVER(
		PARTITION BY nombre, apellido, email, colegiatura
		ORDER BY id ASC
	) AS row,
	*
	FROM public.alumnos
) AS duplicados
WHERE duplicados.row > 1;


-- Borro los duplicados
DELETE
    FROM public.alumnos
    WHERE id IN (SELECT id FROM (
        SELECT *
            FROM (SELECT id, ROW_NUMBER() OVER(
            PARTITION BY 
                nombre, apellido, 
                email, colegiatura,
                fecha_incorporacion, 
				carrera_id,
                tutor_id
            ORDER BY id ASC) AS row
            FROM public.alumnos
    ) AS duplicados
    WHERE duplicados.row > 1) AS duplicados_id);

