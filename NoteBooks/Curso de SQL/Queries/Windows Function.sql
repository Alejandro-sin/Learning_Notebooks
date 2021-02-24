-- Devuelve una sumatoria de toda la tabla de manera que toma los ID y suma las apariciones. 
-- EN otras palabras está multiplicando colegiaturas y apraciones.
SELECT *,
	SUM(colegiatura) OVER (PARTITION BY carrera_id ORDER BY colegiatura)
	from public.alumnos



-- Me devuelve el promedio de colegiaturas de os ID
SELECT *,
	AVG(colegiatura) OVER (PARTITION BY carrera_id)
	from public.alumnos


-- Me devuelve el promedio de toda la tabla
SELECT *,
	AVG(colegiatura) OVER ()
	from public.alumnos