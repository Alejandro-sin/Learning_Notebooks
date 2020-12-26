# La TRANSPUESTA de una matriz permite convertir filas a columnas

tiempo_matrix <- matrix(c(tiempo_estudio,tiempo_lecturas),nrow = 2, byrow = TRUE)

# Definiciònde los titulos de las filas y columnas
dias_aprendizaje <- c("Lunes","Martes","Miercoles", "Jueves", "Viernes","Sabado")
descripcion_tipo <- c("Tiempo estudio", "Tiempo lectura","Podcast")

# Asignaciónde los titulos
colnames(tiempo_matrix) <- dias_aprendizaje
rownames(tiempo_matrix) <- descripcion_tipo

# NOTA: Matriz es diferente a dataframe dado quela matriz debe tener todos sus elementos del mismo tipo

tiempo_matrix

# Obtener totales por columna

colSums (tiempo_matrix)

# Obtener totales por fila

rowSums (tiempo_matrix)

# Adicionar filas a la matriz:  Se crea una matriz nueva 

tiempo_matrix <- rbind(tiempo_matrix, c(10,15,30,5,0))

# Adicionar columnas enla matriz: Se adiciona el día sábado

tiempo_matrix <- cbind(tiempo_matrix, c(10,28,30))```