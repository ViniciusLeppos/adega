npcgold = float(5000)
playergold = float(200)
potato = int(0)
rice = int(0)
meat = int(0)
potprice = int(10)
riceprice = int(80)
meatprice = int(50)
batataarroz = int(0)
arrozcarne = int(0)
carnebatata = int(0)
pratododia = int(0)
pricebatataarroz = int(120)
pricearrozcarne = int(180)
pricecarnebatata = int(90)
pricepratododia = int(250)

if npcgold >= 0:

    while True:

        if npcgold <= 50:
            print ('\n  V O C E  V E N C E U')
            break


        print(' X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X\n X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X \nNPC\nOuro:', npcgold, '\n\nBem-vindo à adega das delícias! Como posso te ajudar?\n\n\n1.Comprar\n2.Vender\n3.Cozinhar\n\n\nSeu saldo:', playergold, '\nCarne: ', meat, '   Arroz: ', rice, '   Batata: ', potato)

        input_menu = int(input())

        if input_menu == 1:

            print(' X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X\n X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X \nNPC\nOuro:', npcgold, '\n\nAgora me diga...qual ingrediente deseja comprar?\n1.Batata (10$)\n2.Arroz (80$)\n3.Carne (''50$)\n\n\nSeu saldo:', playergold)

            input_compra = int(input())

            if input_compra == 1:

                print('\n\nQuantas batatas deseja?\n\n\n')

                buypotato = int(input())

                potatofinal = int(buypotato * potprice)

                if playergold >= potatofinal:

                    potato += buypotato

                    playergold -= potatofinal

                    npcgold += potatofinal

                    print('Você adquiriu', buypotato, 'batatas\n\n\nSaldo:', playergold)

                    print('Saldo do NPC:', npcgold, '\n\n\n')

                    if buypotato == 1:

                        print('Você adquiriu uma batata\n\n\nSaldo:', playergold)

                else:

                    print('Você não tem saldo suficiente.\n\n\n')



            if input_compra == 2:
                print('\n\nQuantos quilos de arroz deseja?\n\n\n')
                buyrice = int(input())
                ricefinal = int(buyrice * riceprice)

                if playergold >= ricefinal:
                    rice += buyrice
                    playergold -= ricefinal
                    npcgold += ricefinal
                    print('Você adquiriu', buyrice, 'quilos de arroz\n\n\nSaldo:', playergold)
                    print('Saldo do NPC:', npcgold, '\n\n\n')
                    if buyrice == 1:
                        print('Você adquiriu um quilo de arroz\n\n\nSaldo:', playergold)


                else:
                    print('Você não tem saldo suficiente.\n\n\n')


            if input_compra == 3:
                print('\n\nQuantos pedaços de carne deseja?\n\n\n')
                buymeat = int(input())
                meatfinal = int(buymeat * meatprice)

                if playergold >= meatfinal:
                    meat += buymeat
                    playergold -= meatfinal
                    npcgold += meatfinal
                    print('Você adquiriu', buymeat, 'pedaços de carne\n\n\nSaldo:', playergold)
                    print('Saldo do NPC:', npcgold, '\n\n\n')
                    if buymeat == 1:
                        print('Você adquiriu um pedaço de carne\n\n\nSaldo:', playergold)


                else:
                    print('Você não tem saldo suficiente.\n\n\n')
            continue

        if input_menu == 2:
            print(' X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X\n X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X \nNPC\nOuro:', npcgold,'\n\nOque desejas vender?\n\n1.Arroz e carne (+180$)\n\n2.Arroz e batata (+120$)\n\n3.Carne e batata (+90$)\n\n4.Prato do dia (+250$)\n\nSeu saldo:', playergold, '\nArroz e batata:', batataarroz, '   Arroz e carne:', arrozcarne, '   Carne e batata:', carnebatata, '   Prato do dia:', pratododia)

            input_venda = input()

            input_venda = float(input_venda)

            if input_venda == 1:

                sell_ricemeat = input('Quantos pratos de arroz e carne deseja vender?')

                arrozcarne = float(arrozcarne)

                sell_ricemeat = float(sell_ricemeat)

                if arrozcarne >= sell_ricemeat and npcgold >= pricearrozcarne * sell_ricemeat:

                    arrozcarne -= sell_ricemeat

                    playergold += pricearrozcarne * sell_ricemeat

                    npcgold -= pricearrozcarne * sell_ricemeat

                    print('Você vendeu ', sell_ricemeat, ' pratos de arroz e carne (+', pricearrozcarne * sell_ricemeat, '$)')

                if npcgold <= pricearrozcarne * sell_ricemeat:

                    print('Sinto muito! Não tenho reservas suficientes!')



            if input_venda == 2:

                sell_ricepot = input('Quantos pratos de arroz e batata deseja vender?')

                batataarroz = float(batataarroz)

                sell_ricepot = float(sell_ricepot)

                if batataarroz >= sell_ricepot and npcgold >= pricebatataarroz * sell_ricepot:

                    batataarroz -= sell_ricepot

                    playergold += pricebatataarroz * sell_ricepot

                    npcgold -= pricebatataarroz * sell_ricepot

                    print('Você vendeu ', sell_ricepot, ' pratos de arroz e batata (+', pricebatataarroz * sell_ricepot, '$)')

                if npcgold <= pricebatataarroz * sell_ricepot:

                    print('Sinto muito! Não tenho reservas suficientes!')



            if input_venda == 3:

                sell_meatpot = input('Quantos pratos de carne e batata deseja vender?')

                carnebatata = float(carnebatata)

                sell_meatpot = float(sell_meatpot)

                if carnebatata >= sell_meatpot and npcgold >= pricecarnebatata * sell_meatpot:

                    carnebatata -= sell_meatpot

                    playergold += pricecarnebatata * sell_meatpot

                    npcgold -= pricecarnebatata * sell_meatpot

                    print('Você vendeu ', sell_meatpot, ' pratos de carne e batata (+', pricecarnebatata * sell_meatpot, '$)')

                if npcgold <= pricecarnebatata * sell_meatpot:

                    print('Sinto muito! Não tenho reservas suficientes!')



            if input_venda == 4:

                sell_plate = input('Quantos pratos do dia deseja vender?')

                pratododia = float(pratododia)

                sell_plate = float(sell_plate)

                if pratododia >= sell_plate and npcgold >= pricepratododia * sell_plate:

                    pratododia -= sell_plate

                    playergold += pricepratododia * sell_plate

                    npcgold -= pricepratododia * sell_plate

                    print('Você vendeu ', sell_plate, ' pratos do dia! (+', pricepratododia * sell_plate, '$)')

                if npcgold <= pricepratododia * sell_plate:

                    print('Sinto muito! Não tenho reservas suficientes!')

            continue
        if input_menu == 3:
            print(' X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X\n X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X \nÉ preciso pagar uma taxa especifica para cada receita que desejar fazer na panela! Capitalismo não é facil mesmo hahahaha \n\n\n1. Fazer Arroz e Carne (30)\n\n2.Fazer Arroz e Batata (8)\n\n3.Fazer Carne e batata (16)\n\n4.Prato do dia (35)\n\nSeu saldo:', playergold, '\nArroz:', rice, '  Carne:', meat, '  Batata:', potato, '\n')

            input_cozinha = input()
#Rever a questão do caso do jogador que não tem dinheiro para taixa. Pensar num mecanismo melhor
            input_cozinha = int(input_cozinha)

            if input_cozinha == 1:

                print('Quantos pratos de arroz e carne gostaria de fazer?')

                input_arrozecarne = input()

                input_arrozecarne = int(input_arrozecarne)

                tx1 = input_arrozecarne * 30

                tx1 = int(tx1)

                if rice - input_arrozecarne << 0 and meat - input_arrozecarne << 0:

                    print('Você não tem ingredientes suficientes')

                if playergold < tx1:
                    print('Você não tem saldos suficientes')

                if rice - input_arrozecarne >= 0 and meat - input_arrozecarne >= 0 and playergold >= tx1:

                    npcgold += tx1

                    playergold -= tx1

                    print('Você adquiriu ', input_arrozecarne, 'pratos de arroz e carne.', ' Você pagou ', tx1, '$ de taxa! Muito obrigado!')

                    arrozcarne += input_arrozecarne

                    rice -= input_arrozecarne

                    meat -= input_arrozecarne





            if input_cozinha == 2:

                print('Quantos pratos de arroz e batata gostaria de fazer?')

                input_arrozbatata = input()

                input_arrozbatata = int(input_arrozbatata)

                tx2 = input_arrozbatata * 8

                tx2 = int(tx2)

                if rice - input_arrozbatata << 0 and potato - input_arrozbatata << 0:

                    print('Você não tem ingredientes suficientes')

                if playergold < tx2:
                    print('Você não tem saldos suficientes')

                if rice - input_arrozbatata >= 0 and potato - input_arrozbatata >= 0 and playergold >= tx2:

                    npcgold += tx2

                    playergold -= tx2


                    print('Você adquiriu ', input_arrozbatata, 'pratos de arroz e batata.', ' Você pagou ', tx2,
                          '$ de taxa! Muito obrigado!')

                    batataarroz += input_arrozbatata

                    rice -= input_arrozbatata

                    potato -= input_arrozbatata



            if input_cozinha == 3:

                print('Quantos pratos de carne e batata gostaria de fazer?')

                input_batatacarne = input()

                input_batatacarne = int(input_batatacarne)

                tx3 = input_batatacarne * 16

                tx3 = int(tx3)

                if potato - input_batatacarne < 0 and meat - input_batatacarne < 0:

                    print('Você não tem ingredientes suficientes')

                if playergold < tx3:
                    print('Você não tem saldos suficientes')

                if potato - input_batatacarne >= 0 and meat - input_batatacarne >= 0 and playergold >= tx3:

                    npcgold += tx3

                    playergold -= tx3


                    print('Você adquiriu ', input_batatacarne, 'pratos de carne e batata.', ' Você pagou ', tx3,
                          '$ de taxa! Muito obrigado!')

                    carnebatata += input_batatacarne

                    potato -= input_batatacarne

                    meat -= input_batatacarne





            if input_cozinha == 4:
            # prato do dia!
                print('Quantos pratos do dia gostaria de fazer?')

                input_plate = input()

                input_plate = int(input_plate)

                tx4 = input_plate * 35

                tx4 = int(tx4)

                if potato - input_plate << 0 and meat - input_plate << 0 and rice - input_plate << 0:

                    print('Você não tem ingredientes suficientes')

                if playergold < tx4:
                    print('Você não tem saldos suficientes')

                if potato - input_plate >= 0 and meat - input_plate >= 0 and rice - input_plate >= 0 and playergold >= tx4:
                    npcgold += tx4
                    playergold -= tx4

                    print('Você adquiriu ', input_plate, 'pratos do dia.', ' Você pagou ', tx4, '$ de taxa! Muito obrigado!')
                    pratododia += input_plate
                    potato -= input_plate
                    meat -= input_plate
                    rice -= input_plate



            continue


