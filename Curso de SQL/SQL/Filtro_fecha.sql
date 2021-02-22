-- Query para filtar por fechas, donde el año de incorporación es 2018 en Mayo

SELECT *
FROM (
	SELECT *,
		DATE_PART('YEAR',fecha_incorporacion) AS anio_incorporacion,
		DATE_PART('MONTH',fecha_incorporacion) AS mes_incorporacion
	FROM public.alumnos
) AS alumnos_anio
WHERE anio_incorporacion = 2018
	AND mes_incorporacion = 5