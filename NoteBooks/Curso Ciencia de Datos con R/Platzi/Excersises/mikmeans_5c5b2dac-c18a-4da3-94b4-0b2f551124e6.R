data<-res_limpio
#Elimina la clumna nombre
data<-data[, -1]

#Escalar: Para poder equilibrar todas las variables para que unas no tengan mayor influencia sobre otras,
#Restamos la media, y dividirla entre la varianza, para que no haya mucha desigualdad al comparar distribuciones.
#Si midieramos dos numeros en difernete escalas, va varaibildiad de x numero sería muy grande en un conjunto que en otro.
data<-scale(data)

# ntart  suele ser importante cin un volumen masivo de datos.
# Cuando vas disminuyendo el witrmmiss vas aumentando el numero de iteraciones máximas.
mycluster<-kmeans(data, 3, nstart=5, iter.max = 30)


wss<-(nrow(data)-1)*sum(apply(data,2,var))
#Iteramos, para cada numero de clusters calculamos el withins y lo guardamos en wss
for(i in 2:20) wss[i]<-sum(kmeans(data,centers=i)$withinss)
wss
plot(1:20, wss, type="b", xlab="Numero de clusters", ylab= "withinss groups")


mycluster<-kmeans(data, 8, nstart = 5, iter.max = 30)


#Caracterización y visualización de centros.
# LA que me permite graficar en radar. Graficaremos 8 graficos.
library(fmsb)
#par me permtie partir las cosas.
par(mfrow=c(2,4))

#centers[1, ] corresponde a los 8 clusters
dat<-as.data.frame(t(mycluster$centers[1, ]))
dat

dat<-rbind(rep(5,10), rep(-1.5,10), dat)
dat

radarchart(dat)
dat<-as.data.frame(t(mycluster$centers[2, ]))
dat

dat<-rbind(rep(5,10), rep(-1.5,10), dat)
dat

#Para  hacer los radar CHart reuerimos tener los maximos , lo smínimos y los valores.
radarchart(dat)
dat<-as.data.frame(t(mycluster$centers[3, ]))
dat
dat<-rbind(rep(5,10), rep(-1.5,10), dat)
dat
radarchart(dat)
dat<-as.data.frame(t(mycluster$centers[4, ]))
dat
dat<-rbind(rep(5,10), rep(-1.5,10), dat)
dat
radarchart(dat)
dat<-as.data.frame(t(mycluster$centers[5, ]))
dat
dat<-rbind(rep(5,10), rep(-1.5,10), dat)
dat
radarchart(dat)
dat<-as.data.frame(t(mycluster$centers[6, ]))
dat
dat<-rbind(rep(5,10), rep(-1.5,10), dat)
dat
radarchart(dat)
dat<-as.data.frame(t(mycluster$centers[7, ]))
dat
dat<-rbind(rep(5,10), rep(-1.5,10), dat)
dat
radarchart(dat)
dat<-as.data.frame(t(mycluster$centers[8, ]))
dat
dat<-rbind(rep(5,10), rep(-1.5,10), dat)
dat
radarchart(dat)