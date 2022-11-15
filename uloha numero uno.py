def vypis_typy(list):
    for i in range(len(list)):
        a=list[i]
        if type(a) == str:
            print(a,'Je retazec.')
        elif type(a) == int  or type(a) == float:
            print(a,'Je cislo.')
        else:
            print(a,'iny typ.')
vypis_typy([13,'lol',None,12.5,[],range(5),'123'])
