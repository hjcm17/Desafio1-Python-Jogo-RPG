# Jogo RPG v1
# Autor: Hugo Mota
# Data: 03/11/2023

# SAÍDA
print('Bem vindo a grande Jornada!')
print('...')
# ENTRADA
nome = str(input('Digite o nome do seu personagem: '))
# SAÍDA
print()
print(f'Olá {nome}, escolha seu personagem: ')
print()
print('Número 1 para ser o Mago;')
print('Número 2 para ser o Guerreiro;')
print('Número 3 para ser o Artesão.')
print()
# ENTRADA
personagem = str(input("Digite um número conforme orientação acima:"))
# PROCESSAMENTO GRAU 1  - ESCOLHENDO O PERSONAGEM
if (personagem == '1' or personagem == '2' or personagem == '3'):
    if (personagem == "1"):
        personagem = "Mago"
        # SAÍDA
        print(f'Olá {nome}! Você escolheu o {personagem}. \n- Es-me aqui, pronto para a jornada que se inicia. A magia '
              f'que flui em minhas veias é uma herança dos meus antepassados, e eu sinto o chamado para moldar a '
              f'realidade com o meu poder.')
    elif (personagem == "2"):
        personagem = "Guerreiro"
        # SAÍDA
        print(
            f'Olá {nome}! Você escolheu o {personagem}. - Bora para batalha! - Cada nome dado em nome da justiça é '
            f'uma vitória.')
    elif (personagem == "3"):
        personagem = "Artesão"
        # SAÍDA
        print(f'Olá {nome}! Você escolheu o {personagem}. - Vai um gole? Forjar é minha paixão, e minha obra será '
              f'eterna.')
else:
    # SAÍDA
    print()
    print('Escolha errada. Por favor Leia as orientações.')
    print()
# PROCESSAMENTO 2 ESCOLHENDO O EQUIPAMENTO EM RELAÇÃO AO PERSONAGEM (GRAU 1)
if (personagem == "Mago" or personagem == "Guerreiro" or personagem == "Artesão"):
    # PROCESSAMENTO - GRAU 2
    if (personagem == "Mago"):
        # SAÍDA
        print('Escolha um equipamento: ')
        print()
        print('Número 1 para se equipar com a Arcana das Profundezas;')
        print('Número 2  para se equipar com o Livro das estrelas;')
        print('Número 3  para se equipar com o Manto Dimensional.')
        print()
        # ENTRADA
        equipamento = str(input("Digite um número para escolher seu equipamento: "))
        # PROCESSAMENTO - GRAU 3
        if equipamento == "1" and equipamento == "2" and equipamento == "3":
            # PROCESSAMENTO - GRAU 4
            if (equipamento == "1"):
                equipamento = "Arcana das Profundezas"
                # SAÍDA
                print(
                    f'Você escolheu a {equipamento}.\nEssa arcana é uma fonte infinita de conhecimento e concede ao '
                    f'mago a capacidade de aprender novos feitiços e aprimorar sua magia.')
            if (equipamento == "2"):
                equipamento = "Livro das estrelas"
                # SAÍDA
                print(
                    f'Você escolheu o {equipamento}.\nUm livro extraído de um orbe mágico que amplifica o poder do '
                    f'mago, permitindo-lhe lançar feitiços mais poderosos e precisos. Com runas lendárias gravadas, '
                    f'que aumentam sua conexão com o reino arcano')
            elif (equipamento == "3"):
                equipamento = "Manto Dimensional"
                # SAÍDA
                print(
                    f'Você escolheu o {equipamento}.\nUm manto feito de tecido especial, que parece pontilhado de '
                    f'pedras cintilantes. Este manto permite que o mago viaje entre as dimensões, '
                    f'bem como resistência a danos mágicos.')
            else:
                # SAÍDA
                print('Essa opção não existe. Digite um número de 1-3 conforme orientação.')
    # ESCOLHA DO EQUIPAMENTO DO EQUIPAMENTO DO GUERREIRO (PROCESSAMENTO GRAU 2)
    if (personagem == "Guerreiro"):
        # SAÍDA
        print('Escolha um equipamento: ')
        print()
        print('Número 1 para se equipar com a Espada Rúnica da Justiça;')
        print('Número 2  para se equipar com o Escudo do Defensor Impenetrável;')
        print('Número 3  para se equipar com o Elmo do Leão Valente.')
        print()
        # ENTRADA
        equipamento = str(input("Digite um número para escolher seu equipamento: "))
        # PROCESSAMENTO - GRAU 3
        if equipamento == "1" and equipamento == "2" and equipamento == "3":
            # PROCESSAMENTO - GRAU 4
            if (equipamento == "1"):
                equipamento = "Espada Rúnica da Justiça"
                # SAÍDA
                print(
                    f'Você escolheu a {equipamento}.\nUma espada de aço forjada com runas sagradas que concedem '
                    f'poderes especiais. Ela brilha com uma luz divina quando o guerreiro luta pela justiça, '
                    f'aumentando sua força e habilidades de combate. ')
            if (equipamento == "2"):
                equipamento = "Escudo do Defensor Impenetrável"
                # SAÍDA
                print(
                    f'Você escolheu o {equipamento}.\nUm grande escudo feito de um metal resistente e adornado com '
                    f'motivos heroicos. Este escudo não apenas fornece uma defesa impenetrável contra ataques '
                    f'físicos, mas também pode ser usado para criar uma barreira mágica temporária que protege o '
                    f'guerreiro e seus aliados de ataques mágicos.')
            elif (equipamento == "3"):
                equipamento = "Elmo do Leão Valente"
                # SAÍDA
                print(
                    f'Você escolheu o {equipamento}.\nUm elmo ornamentado com a imagem de um leão corajoso. Ele '
                    f'concede ao guerreiro uma aura de coragem e resistência. Quando usado em batalha, o Elmo do Leão '
                    f'Valente aumenta a moral do guerreiro e de seus companheiros, tornando-os mais resistentes a '
                    f'efeitos de medo e fornecendo um bônus de força.')
            else:
                print('Essa opção não existe. Digite um número de 1-3 conforme orientação.')

    elif (personagem == "Artesão"):
        # SAÍDA
        print('Escolha um equipamento: ')
        print()
        print('Número 1 para se equipar com a Espada Martelo do Mestre Ferreiro;')
        print('Número 2  para se equipar com o Escudo do Luvas do Tecelão de Encantamentos;')
        print('Número 3  para se equipar com o Estojo do Artesão Viajante.')
        print()
        # ENTRADA
        equipamento = str(input("Digite um número para escolher seu equipamento: "))
        # # PROCESSAMENTO - GRAU 3
        if equipamento == "1" and equipamento == "2" and equipamento == "3":
            if (equipamento == "1"):
                equipamento = "Martelo do Mestre Ferreiro"
                # SAÍDA
                print(
                    f'Você escolheu o {equipamento}.\nUm martelo forjado com habilidade lendária, perfeito para moldar metais e criar obras-primas. Este martelo torna o processo de forja mais eficiente e preciso, permitindo que o artesão crie armaduras e armas de qualidade excepcional.. ')
            if (equipamento == "2"):
                equipamento = "Luvas do Tecelão de Encantamentos"
                # SAÍDA
                print(
                    f'Você escolheu o {equipamento}.\nUm par de luvas finamente trabalhadas que aprimoram a habilidade do artesão em encantar itens com magia. Quando usadas durante o processo de encantamento, as Luvas do Tecelão de Encantamentos aumentam a potência e a precisão das magias inscritas em armas, armaduras e acessórios.')
            elif (equipamento == "3"):
                equipamento = "Estojo do Artesão Viajante"
                # SAÍDA
                print(
                    f'Você escolheu o {equipamento}.\nUm estojo de couro que contém ferramentas essenciais para a prática da arte. Ele inclui instrumentos de corte, medição e entalhe de alta qualidade, bem como materiais raros, como gemas preciosas e metais. O Estojo do Artesão Viajante permite ao artesão criar obras-primas em qualquer lugar que vá.')
            else:
                # SAÍDA
                print('Essa opção não existe. Digite um número de 1-3 conforme orientação.')
