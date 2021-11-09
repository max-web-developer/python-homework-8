print('Здравствуйте вас приветствует афтомат продуктов!')
print('Меню \n1-Snicers \n2- Pepsi \n3- Fanta')
chouse=int(input('Выберити один номер из этих продуктов:'))
def ProductSnicers(Sprise,Ssum):
    return Sprise-Ssum
if chouse == 1:
    print('Вы выбрали продукт Сникерс,Сумма продукта 6000: ')
    prisesnikers=6000
    ss=int(input('ВВедите сумму продукта: '))
    if ss > prisesnikers: 
        print(ss-prisesnikers)
    elif prisesnikers > ss:
        print('Нехвотает денежных средств: ')

def ProductPepsi(Pprise,Ssum):
    return Pprise-Ssum
if chouse == 2:
    print('Вы выбрали продукт пепси,Сумма продукта 5000: ')
    prisepepsi=5000
    sp=int(input('ВВедите сумму продукта: '))
    if sp > prisepepsi:
        print(sp-prisepepsi)
    elif prisepepsi > sp:
        print('Нехвотает денежных средств: ')

def ProductFanta(Fprise,Fsum):
    return Fprise-Fsum
if chouse == 3:
    print('Вы выбрали продукт фанта,Сумма продукта 5000: ')
    prisefanta=5000
    sf=int(input('ВВедите сумму продукта: '))
    if sf > prisefanta:
        print(sf-prisefanta)
    elif prisefanta > sf:
        print('Нехвотает денежных средств: ')




        



  
