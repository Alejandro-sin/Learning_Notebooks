-- Windows Function

-- Row number: Da el numero de la tupla que ocupamos, independiente del id
-- Para visualizrlo mejor podemos ordenar por fecha de incorporación, sin importar el orden que le demso el row number devuelve
-- el número de tupla o fila de manera consecutiva.
SELECT ROW_NUMBER() OVER (ORDER BY fecha_incorporacion) AS row_id, *
FROM public.alumnos;