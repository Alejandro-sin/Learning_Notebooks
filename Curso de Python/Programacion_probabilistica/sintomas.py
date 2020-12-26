# Defino mi función de cálculo Bayseiano.
def teoremaBayes(prior_a, b_dado_a, probabilidad_b ):
    return(b_dado_a *prior_a) /probabilidad_b

# Calcular elementos que necesito para pasarselos como parametros a la función.
if __name__ =="__main__":
    prob_cancer = 1 / 100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10 / 99999
    prob_no_cancer = 1 - prob_cancer

    prob_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * prob_no_cancer)

    prob_cancer_dado_sintoma = teoremaBayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)

    print(prob_cancer_dado_sintoma)

# Mi prior cambia,  al 9 %.
# dETERMINAR IS MI HIPOTESIS ES CIERTA O NO Y CON QUÉ GRADO DE PROBABILDIAD. Aqui se actualiza nuevamente la información.
# Podemos hacer el ejercicio para el CODVID, ejemplo util:


