import os

# Pergunta
retorno: int

# Style Menu
style = ["Trickster","Swordmaster","Gunslinger","Royalguard","Quicksilver","Dopplegengar"]
aux: int; sele_a: int; sele_b = 1

# Menu
chave_menu: int

# Red Orbs
red_orbs = 0; inserir: float

# Itens Menu
limite_itens = [30,30,30,3,20,10,3]
nome_itens = ["Vital Star S", "Vital Star L", "Devil Star", "Holy Water", "Blue Orb", "Purple Orb", "Golden Orb"]
custo_itens = [250, 1000, 700, 10000, 5000, 3000, 10000]
inventario = [0, 0, 0, 0, 13, 3, 0]

# Equip menu
guns_nome = ["Ebony&Ivory", "Shotgun", "Artemis", "Spiral","KalinaAnn"]
weapons_nome = ["Rebelion", "Cerberus", "Agni&Rudra", "Nevan","Beowulf"]
equip_guns = [0,1]
equip_weapons = [0,1]

# Guns Upgrades
guns_up_preco = [5000, 10000, 10000, 7500, 5000]
guns_up_limit = [3,3,3,3,3]
guns_up_base = [1,1,1,1,1]

# Action Menu
arms_up_base = [[0,0,0],[0,0],[0,0,0],[0,0,0,0],[0,0,0]]
arms_up_limit = [[2,1,1],[1,1],[2,1,1],[2,1,1,1],[2,1,1]]
arms_up_preco = [[2500, 10000, 20000],[15000, 7500],[10000, 7500, 20000],[7500, 10000, 10000, 20000],[7500, 10000, 20000]]
arms_up_two = [["Stinger","Stinger: Level 2", "Stinger: Level 2"],["0"],["Jet Stream: Level 2","Jet Stream: Level 3","Jet Stream: Level 3"],
               ["Reverb Shock","Reverb Shock: Level 2","Reverb Shock: Level 2"],["Beast-Uppercut","Rising-Dragon","Rising-Dragon"]]
arms_up_one = [["Drive","Air-Hike"],["Revolver: Level 2","Windmill"],["Whirlwing","Air-Hike"],["Bad Rift: Level 2","Air-Raid","Volume Up"],["Straight: Level 2", "Air Hike"]]
arms_stop = [2,2,2,3,2]


def pergunta():

    global retorno
    
    retorno = input(" | Deseja prosseguir? [1] - SIM [0] - NAO |\n :: ")
    retorno = int(retorno)
    
    return retorno

def style_menu():

    os.system('cls')
    global aux, sele_a, sele_b
    global style

    sele_b = int(sele_b)
    
    aux = 1
        
    print("  ---------\n | Estilos |\n  --------- ")
    for styles in style:
        print(" |",aux,"--", styles, end= "")
        if aux == sele_b:
            print(" == Selecionado")
            aux += 1
        else:
            print(" ")
            aux += 1

    sele_a = input("\n | Digite o número do estilo que deseja equipar ou 0 para sair para o menu :: ")
    sele_a = int(sele_a)
    
    if sele_a >= 7 or sele_a <= 0:
        menu()
    else:
        sele_b = sele_a
        style_menu()    

def equip_menu_guns():

    os.system('cls')
    global guns_nome; equip_guns

    print("  ---------------\n | Armas de Fogo |\n  ---------------")
    print(" | 1 --", guns_nome[equip_guns[0]])
    print(" | 2 --", guns_nome[equip_guns[1]])
    print(" | 3 == Ir no menu das Devil Arms\n ")
    chave_guns = input(" | Digite o numero do que deseja trocar, acessar ou 0 para sair :: ")
    chave_guns = int(chave_guns)
    chave_guns -= 1

    os.system('cls')
    if chave_guns > 2 or chave_guns < 0:
        menu()
    elif chave_guns == 2:
        equip_menu_weapons()
    else:
        for aux_guns in range(0, 5):
            aux_guns = int(aux_guns)
            print(" | ",aux_guns + 1,"--",guns_nome[aux_guns])

        chave_troca_guns = input(" \n | Digite o numero de que deseja trocar ou 0 para sair :: ")
        chave_troca_guns = int(chave_troca_guns)
        chave_troca_guns -= 1

        os.system('cls')
    if chave_troca_guns > 4 or chave_troca_guns < 0:
        equip_menu_guns()
    elif chave_troca_guns == equip_guns[1] or chave_troca_guns == equip_guns[0]:
        print(" | Voce já está equipado com está arma '-' | ")
        os.system('pause')
        equip_menu_guns()
    else:
        equip_guns[chave_guns] = chave_troca_guns
        equip_menu_guns()

def equip_menu_weapons():
    
    os.system('cls')
    global weapons_nome; equip_weapons

    print("  ------------\n | Devil Arms |\n  ------------")
    print(" | 1 --", weapons_nome[equip_weapons[0]])
    print(" | 2 --", weapons_nome[equip_weapons[1]])
    print(" | 3 == Ir no menu das Armas de Fogo\n ")
    
    chave_weapons = input(" | Digite o numero do que deseja trocar, acessar ou 0 para sair :: ")
    chave_weapons = int(chave_weapons)
    chave_weapons -= 1

    os.system('cls')
    if chave_weapons > 2 or chave_weapons < 0:
        menu()
    elif chave_weapons == 2:
        equip_menu_guns()
    else:
        for aux_weapons in range(0, 5):
            aux_weapons = int(aux_weapons)
            print(" | ",aux_weapons + 1,"-",weapons_nome[aux_weapons])

        chave_troca_weapons = input(" \n | Digite o numero de que deseja trocar ou 0 para sair :: ")
        chave_troca_weapons = int(chave_troca_weapons)
        chave_troca_weapons -= 1

        os.system('cls')
    if chave_troca_weapons > 4 or chave_troca_weapons < 0:
        equip_menu_weapons()
    elif chave_troca_weapons == equip_weapons[1] or chave_troca_weapons == equip_weapons[0]:
        print(" | Voce já está equipado com está arma '-' | ")
        os.system('pause')
        equip_menu_weapons()
    else:
        equip_weapons[chave_weapons] = chave_troca_weapons
        equip_menu_weapons()

def item_menu():

    os.system('cls')
    global nome_itens; inventario; limite_itens; custo_itens; inventario 
    global red_orbs
    
    print(" HP ", end="")
    for blue_p in range (0, inventario[4]):
        print("-", end="")
        if blue_p == 9:
            print("\n    ", end="")
    
    print("\n DT ", end="")
    for purple_p in range (0, inventario[5]):
        print("*", end="")

    red_orbs = float(red_orbs)

    print("\n ---------------\n| Loja de itens |		| ",red_orbs," Red Orbs |\n ---------------")

    for aux_item in range(0, 7):
        aux_item = int(aux_item)
        print(" |",aux_item + 1,"--",nome_itens[aux_item],"==",inventario[aux_item],"/",limite_itens[aux_item],"Inventario ==", custo_itens[aux_item],"Red Orbs")

    chave_item = input(" \n | Digite o numero de o item que deseja comprar ou 0 para sair para o menu :: ")
    chave_item = int(chave_item)
    chave_item -= 1
    
    os.system('cls')
    if chave_item >= 7 or chave_item < 0:
        menu()
    elif inventario[chave_item] == limite_itens[chave_item]:
        print(" | Voce já atingiu o máixmo de itens no inventário '-' |")
        os.system('pause')
        item_menu()
    elif red_orbs < custo_itens[chave_item]:
        print(" | Voce não tem Red Orbs o suficiente '-' |")
        os.system('pause')
        item_menu()
    else:
        if pergunta() == 1:
            custo_itens[chave_item] = float(custo_itens[chave_item])
            
            red_orbs -= custo_itens[chave_item]
            inventario[chave_item] += 1
            custo_itens[chave_item] *= 1.2

            print(" | Compra realizada com sucesso UwU |")
            os.system('pause')

            if inventario[chave_item] == limite_itens[chave_item]:
                custo_itens[chave_item] = 0
                
            item_menu()

def action_menu():

    os.system('cls')
    global weapons_nome; arms_stop; arms_up_base; arms_up_limit
    global red_orbs; arms_up_preco
    global arms_up_two; arms_up_one

    print(" -------------\n| Action Menu |      | ",red_orbs," Red Orbs |\n -------------")
    for aux_up_arms in range(0, 5):
        aux_up_arms = int(aux_up_arms)
        print(" |",aux_up_arms + 1,"--",weapons_nome[aux_up_arms],"")

    chave_weapon_up = input("\n | Digite o numero da Devil Arm que deseja melhorar ou 0 para sair menu :: ")
    chave_weapon_up = int(chave_weapon_up)
    chave_weapon_up -= 1

    os.system('cls')
    if chave_weapon_up > 5 or chave_weapon_up < 0:
        menu()
    else:
        suporte = 1
        gambiarra = 0

        suporte = int(suporte)
        print(" | ", weapons_nome[chave_weapon_up]," | ",red_orbs," Red Orbs |\n")
        if chave_weapon_up == 1:
            suporte = 0
            gambiarra = 1
        else:
            print(" | 1 --",arms_up_two[chave_weapon_up][arms_up_base[chave_weapon_up][0]], "==", arms_up_preco[chave_weapon_up][0],"Red Orbs") 
        for arms_aux_up in range(0, arms_stop[chave_weapon_up]):
            arms_aux_up = int(arms_aux_up)
            print(" |",arms_aux_up + 1 + suporte,"--",arms_up_one[chave_weapon_up][arms_aux_up], "==", arms_up_preco[chave_weapon_up][arms_aux_up + suporte],"Red Orbs") 
        
        chave_up = input( "\n | Digite qual habilidade deseja adqurir ou 0 para sair :: ")
        chave_up = int(chave_up)
        chave_up -= 1
        
        os.system('cls')
        if chave_up > arms_stop[chave_weapon_up] - gambiarra or chave_up < 0:
            action_menu()
        elif arms_up_base[chave_weapon_up][chave_up] == arms_up_limit[chave_weapon_up][chave_up]:
            print(" | Você já upgredeou essa arma ao maxímo '-' |")
            os.system('pause')
            action_menu()
        elif arms_up_preco[chave_weapon_up][chave_up] > red_orbs:
            print(" | Você não tem Red Orbs o suficiente '-' |")
            os.system('pause')
            action_menu()
        else:
            if pergunta() == 1:
                red_orbs -= arms_up_preco[chave_weapon_up][chave_up]
                arms_up_base[chave_weapon_up][chave_up] += 1
                
                if chave_weapon_up == 0 and chave_up == 0:
                    arms_up_preco[chave_weapon_up][chave_up] += 7500
                else:
                    arms_up_preco[chave_weapon_up][chave_up] *= 2
                
                print(" | Upgrade realizado com sucesso UwU |")
                os.system('pause')
                
                if arms_up_base[chave_weapon_up][chave_up] == arms_up_limit[chave_weapon_up][chave_up]:
                    arms_up_preco[chave_weapon_up][chave_up] = 0
            
                action_menu()
            else:
                action_menu()
        
def guns_menu():

    os.system('cls')
    global guns_nome; guns_up_limit; guns_up_base; guns_up_preco;
    global red_orbs

    print("  --------------\n | Upgrade Guns |      | Red Orbs: ",red_orbs," |\n  --------------")

    for aux_guns_up in range(0, 5):
            aux_guns_up = int(aux_guns_up)
            if guns_up_base[aux_guns_up] == guns_up_limit[aux_guns_up]:
                print(" | ",aux_guns_up + 1,"--",guns_nome[aux_guns_up],"== Level",guns_up_base[aux_guns_up])
            else:
                print(" | ",aux_guns_up + 1,"--",guns_nome[aux_guns_up],"== Level",guns_up_base[aux_guns_up], ">> Level",guns_up_base[aux_guns_up] + 1,"==",guns_up_preco[aux_guns_up],"Red Obrs")

    chave_guns_menu = input(" \n | Digite o numero da arma que deseja melhor ou 0 para sair para o menu :: ")
    chave_guns_menu = int(chave_guns_menu)
    chave_guns_menu -= 1

    os.system('cls')
    if chave_guns_menu >= 5 or chave_guns_menu < 0:
        menu()
    elif guns_up_base[chave_guns_menu] == guns_up_limit[chave_guns_menu]:
        print(" | Você já upgredeou essa arma ao maxímo '-' |")
        os.system('pause')
        guns_menu()
    elif guns_up_preco[chave_guns_menu] > red_orbs:
        print(" | Você não tem Red Orbs o suficiente '-' |")
        os.system('pause')
        guns_menu()
    else:
        if pergunta() == 1:
            red_orbs -= guns_up_preco[chave_guns_menu]
            guns_up_base[chave_guns_menu] += 1
            guns_up_preco[chave_guns_menu] *= 2

            print(" | Upgrade realizado com sucesso UwU |")
            os.system('pause')

            if guns_up_base[chave_guns_menu] == guns_up_limit[chave_guns_menu]:
                guns_up_preco[chave_guns_menu] = 0
                
            guns_menu()
        else:
            guns_menu()

def inserir_orbs():

    os.system('cls')
    global red_orbs, inserir

    print("  ------------------\n | Inserir Red Obrs |      | Red Orbs: ",red_orbs," |\n  ------------------")
    inserir = input(" | Digite a quantidade que deseja inserir ou 0 para sair :: ")
    inserir = float(inserir)
    
    os.system('cls')
    if inserir <= 0:
        menu()
    else:
        if pergunta() == 1:
            red_orbs += inserir
            print(" | Red orbs inseridas com sucesso UwU |")
            os.system('pause')
            inserir_orbs()
        else:
            menu()

def menu():

    os.system('cls')
    global chave_menu, inventario
    
    print(" HP ", end="")
    for blue_p in range (0, inventario[4]):
        print("-", end="")
        if blue_p == 9:
            print("\n    ", end="")
    
    print("\n DT ", end="")
    for purple_p in range (0, inventario[5]):
        print("*", end="")

    print(" \n -------------------------\n| Loja do Devil May Cry 3 |      | Red Orbs: ",red_orbs," |\n -------------------------")
    print(" | 1 -- Style\n | 2 -- Equip\n | 3 -- Item\n | 4 -- Action\n | 5 -- Guns\n | 6 -- Inserir Red Orbs\n | 7 == Exit\n")
    chave_menu = input(" | Digite o numero do menu que deseja entrar ou 0 para fechar o programa :: ")
    chave_menu = int(chave_menu)
    
    os.system('cls')
    match chave_menu:
        case 1:
            style_menu()
        case 2:
            equip_menu_weapons()
        case 3:
            item_menu()
        case 4:
            action_menu()
        case 5:
            guns_menu()
        case 6:
            inserir_orbs()
        case default:
            print(" Falou AMEGAN")
            exit()
menu()