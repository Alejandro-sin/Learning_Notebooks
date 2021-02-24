-- Windows Function
-- Aquí wl ranking se comparte al tener n campos iguales.
-- Al saltarse RNAK() deja gaps al tener campos con el mismo valor, para eliminar eso usamos DENSE_RANK
SELECT *,
	RANK() OVER(PARTITION BY carrera_id ORDER BY colegiatura DESC) AS colegiatura_rank
	FROM public.alumnos
	ORDER BY carrera_id, colegiatura_rank;


-- Ideal para los rankis útiles.
SELECT *,
	DENSE_RANK() OVER(PARTITION BY carrera_id ORDER BY colegiatura DESC) AS colegiatura_rank
	FROM public.alumnos
	ORDER BY carrera_id, colegiatura_rank;


-- Percent categoriza mediante porcentajes, : (rank-1)/(total de filas -1) E slo que hace percent rank
SELECT *,
	PERCENT_RANK() OVER(PARTITION BY carrera_id ORDER BY colegiatura DESC) AS colegiatura_rank
	FROM public.alumnos
	ORDER BY carrera_id, colegiatura_rank;