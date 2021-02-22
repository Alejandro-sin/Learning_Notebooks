"""

El proósito de este código es eliminar código repetido que posea patrones semejantes.

"""



def select_costumer():
    costumers_list = []
    for costumer in costumers_list:
        if costumer == "A":
            costumers_list.append(costumer)


def select_business():
    business_list = []
    for costumer in business_list:
        if costumer == "b":
            business_list.append(costumer)


""" El código anterior hace lo mismo,usando lambda functions puedo reificar el código"""

def selec_global(objects, conditions):
    selected =[]
    for x in objects:
        if conditions(x):
            selected.append(x)
    return selected

# selec_global(customers, lambda customer: customer =="A")