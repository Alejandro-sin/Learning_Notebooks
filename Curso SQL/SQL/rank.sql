SELECT *
FROM (
	SELECT *,
	RANK() OVER (PARTITION BY carrera_id ORDER BY colegiatura DESC) brand_rank
	FROM public.alumnos
	
) AS rank_colegiaturas_por_carrera
WHERE brand_rank <3
ORDER BY carrera_id, brand_rank;
