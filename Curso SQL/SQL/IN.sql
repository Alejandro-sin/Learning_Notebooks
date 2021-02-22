-- Quiero seleccionar los id 2,3,5,7,10 d ela tabla de alumnos

SELECT *
FROM public.alumnos
-- Si tengo un CSV o un string que ya tenga esta separación puedo copiar y pegar
WHERE id IN (2,3,5,7,10)



-- Quiero llamar los id , nombre y colegiatura de los estudiantes cuyo tutor es id=30
-- Esto genera un subquery dinámico para traer todo.

SELECT id, nombre,colegiatura
FROM public.alumnos
WHERE id IN(
	SELECT id FROM public.alumnos
	WHERE tutor_id =30
)

