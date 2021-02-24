-- Generar rangos

SELECT *
-- FROM generate_series(1,4);
--Empieza en 5 y deciende en -2 unidades
--FROM generate_series(5,1, -2);
--FROM generate_series(3.1,4.9, 0.1);

--Current_date
-- Genero una tabla s con una sola columa a Uso la fecha actual para sumarle el numero de días. al sumar.
SELECT current_date + s.a AS dates
FROM generate_series(0,14,7) AS s(a)

-- Creo un rango de fechas
-- Los dobles dos puntos significa un casteo.
-- El paso lo quiero de 10 horas, Postegres intuye 10 hours como 10 horas
SELECT *
FROM generate_series('2020-09-01 00:00:00' ::timestamp,'2020-09-04 12:00:00','10 hours');


-- Un caso de generate series con datos reales.
SELECT  alumnos.id,
		alumnos.nombre,
		alumnos.apellido,
		alumnos.carrera_id,
		series.alumnos
FROM public.alumnos AS alumnos
	INNER JOIN generate_series(0,10) AS series(alumnos)
	ON series.alumnos = alumnos.carrera_id
ORDER BY alumnos.carrera_id	
		
		