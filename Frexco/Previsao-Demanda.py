print("Previsão de Demanda")

periodo = int(input("1 - Informe o período: "))
parar = ""
demandas = 0

while parar.upper() != "S":

    qtdDemandas = float(input("2 - Informe a quantidade de demanda: "))

    parar = input("Deseja encerrar? S/N ")

    demandas = float(demandas + qtdDemandas / periodo)

print("3 - Previsão de demanda é de: {}".format(demandas))