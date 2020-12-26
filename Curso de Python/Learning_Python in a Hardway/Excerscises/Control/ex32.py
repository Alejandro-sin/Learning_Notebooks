#Loop And lists

mixed =[1,"123", 3 ,"2345", 4, "Caña de azucar"]
fruits =["piña", "fresa","sandia","manzana","limón","perú","toronja",]


for fruit in fruits:
    print(f"El nombre de tu fruta es: {fruit}")


for fruit in fruits:
    for mix in mixed:
        print(f"{mix} y {fruit}")


element =[]

for i in range (0,100):
    print(i)
    element.append(i)

print(element)

for a in element:
    var = a/2
    print(var)
