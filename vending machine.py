changeStock = [["R$100", 0, 5, 100],
               ["R$50", 0, 5, 50],
               ["R$20", 0, 5, 20],
               ["R$10", 0, 5, 10],
               ["R$5", 0, 5, 5],
               ["R$2", 0, 5, 2],
               ["R$1", 0, 5, 1],
               ["R$0,50", 0, 5, 0.5],
               ["R$0,25", 0, 5, 0.25],
               ["R$0,10", 0, 5, 0.10],
               ["R$0,05", 0, 5, 0.05],
               ["R$0,01", 0, 5, 0.01]]

drinkStock = [[1, "Coca-Cola", 3.75, 2],
              [2, "Pepsi", 3.67, 5],
              [3, "Monster", 9.96, 1],
              [4, "Café", 1.25, 100],
              [5, "Red Bull", 13.99, 2]]


def mainMenu():
    while True:
        userType = int(input("\n================================================================================================================\n\
                                        MÁQUINA DE BEBIDAS                                                  \n\
================================================================================================================\n\
                                     SELECIONE O MODO DE USO                                                    \n\
================================================================================================================\n\
\n[ 1 ] CONSUMIDOR\n[ 2 ] ADMINISTRADOR\n\n[ 0 ] ENCERRAR MÁQUINA\n\nDigite o modo de uso desejado: "))
        if userType == 1:
            drinkSelection()
        elif userType == 2:
            password = input("Insira a senha: ")
            if password == "adm123":
                print("\n================================================================================================================\n\
                                        ACESSO PERMITIDO                                                         ")
                admMode()
            else:
                print("\nSENHA INCORRETA\nTente novamente.")
        elif userType == 0:
            print("\nENCERRANDO OPERAÇÕES...")
            exit()
        else:
            print("\nOPÇÃO INVÁLIDA\nTente novamente.")


def clientMode(drinkNum):
    while True:
        payDrink = float(input(f"Insira aqui o dinheiro: R$"))
        if payDrink < drinkStock[drinkNum][2]:
            print("\nDINHEIRO INSUFICIENTE\nEntre com um valor maior ou igual ao preço da bebida.\n")
        else:
            change(payDrink, drinkNum)


def drinkSelection():
    while True:
        print("\n================================================================================================================\n\
                                            OPÇÕES DE BEBIDA                                                   \n\
================================================================================================================\n")
        for i in range(len(drinkStock)):
            print("[", drinkStock[i][0], "] ", drinkStock[i][1])
        drinkNum = int(input("\nDigite o número da bebida que deseja comprar: "))
        drinkNum -= 1
        if drinkNum not in range(len(drinkStock)):
            print("\nOPÇÃO INVÁLIDA\nTente novamente.\n")
        elif drinkNum in range(len(drinkStock)):
            if drinkStock[drinkNum][3] > 0:
                print(f"\nO valor para comprar {drinkStock[drinkNum][1]} é R${drinkStock[drinkNum][2]}\n")
                clientMode(drinkNum)
            else:
                print("\nBebida indisponível.")
        else:
            break


def change(payDrink, drinkNum):
    change = payDrink - drinkStock[drinkNum][2]
    global changeStock
    changeTemp = [[item[0], 0, item[2], item[3]] for item in changeStock]
    for t in range(len(changeStock)):
        while round(change, 2) - changeTemp[t][3] >= 0 and changeTemp[t][2] > 0:
            change = round(change - changeTemp[t][3], 2)
            changeTemp[t][1] += 1
            changeTemp[t][2] -= 1
    if round(change, 2) >= 0.01:
        print("\nCOMPRA CANCELADA\nTroco insuficiente.\n\nRetornando R$", payDrink)
    else:
        changeStock = changeTemp
        print("\nDevolvendo troco...\n")
        for i in range(len(changeStock)):
            if changeStock[i][1] > 0:
                print(changeStock[i][0],': ', changeStock[i][1])
        drinkStock[drinkNum][3] -= 1
        print(f"\nA quantidade total de {drinkStock[drinkNum][1]} disponíveis é {drinkStock[drinkNum][3]}\n")
    buyAnother = int(input("\n[ 1 ] SIM\n[ 2 ] NÃO\n\nDeseja comprar outra bebida? "))
    if buyAnother == 1:
        drinkSelection()
    else:
        print("\nVolte sempre!\n")
        exit()


def admMode():
    while True:
        print("================================================================================================================\n\
                                       MENU ADMINISTRADOR                                                       \n\
================================================================================================================\n")
        admin = int(input(
            "[ 1 ] Remover itens\n[ 2 ] Adicionar itens\n[ 3 ] Editar itens\n[ 4 ] Voltar ao menu principal\n\nSelecione uma opção: "))
        if admin == 1:
            for i in range(len(drinkStock)):
                print("[", drinkStock[i][0], "] ", drinkStock[i][1])
            drinkNum = int(input("\nInsira o número da bebida que deseja remover: "))
            drinkStock.remove(drinkStock[drinkNum - 1])
            renumber = 1
            for i in range(len(drinkStock)):
                drinkStock[i][0] = renumber
                renumber += 1
            admMode()
        elif admin == 2:
            addProd = input("\nNOME, PREÇO, UNIDADES\nInsira as informações do produto seguindo o formato acima: ")
            lastDrink = int(len(drinkStock))
            addProd = addProd.split(", ")
            newDrink(addProd, lastDrink)
            admMode()
        elif admin == 3:
            print("\nAs bebidas disponíveis para edição são:\n")
            for i in range(len(drinkStock)):
                print("[", drinkStock[i][0], "] ", drinkStock[i][1])
            edit = int(input("\nInsira o número da bebida que deseja editar: "))
            editType = int(input(
                f"\n[ 1 ] {drinkStock[edit - 1][1]}\n[ 2 ] {drinkStock[edit - 1][2]}\n[ 3 ] {drinkStock[edit - 1][3]}\
                                \n\nQual informação você deseja editar? "))
            if editType == 1:
                mod = input(f"Insira o novo nome de {drinkStock[edit - 1][1]}: ")
                drinkStock[edit - 1][1] = mod
                admMode()
            elif editType == 2:
                mod = input(f"Insira o novo valor de {drinkStock[edit - 1][2]}: ")
                drinkStock[edit - 1][2] = mod
                admMode()
            elif editType == 3:
                mod = input(f"Insira a nova quantidade disponível de {drinkStock[edit - 1][1]}: ")
                drinkStock[edit - 1][3] = mod
                admMode()
            else:
                print("OPÇÃO INVÁLIDA!\nTente novamente: ")
        elif admin == 4:
            mainMenu()
        else:
            print("\nOPÇÃO INVÁLIDA!\nTente novamente.")


def newDrink(addProd, lastDrink):
    addProd[1] = float(addProd[1])
    addProd[2] = int(addProd[2])
    drinkStock.append([lastDrink + 1, addProd[0], addProd[1], addProd[2]])
    print("\nProduto adicionado com sucesso. Seu estoque está assim:\n")
    for j in range(len(drinkStock)):
        print("[", drinkStock[j][0], "] ", drinkStock[j][1])
    mainMenu()


mainMenu()