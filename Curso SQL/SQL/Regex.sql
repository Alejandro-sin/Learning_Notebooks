SELECT email
FROM public.alumnos
-- En postgres ~* Dice que es un REGEX.
--WHERE email ~*'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'


-- Si quisiera filtrar forzozamente por palbra la añado
WHERE email ~*'[A-Z0-9._%+-]+@google[A-Z0-9.-]+\.[A-Z]{2,4}'