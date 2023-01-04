
def findNemo01(frase):

    n = 0
    o = 4

    frase_lower = frase.lower()
    tamanho_frase = len(frase)

    while o <= tamanho_frase :
        if frase_lower[n:o] == 'nemo':
            print(f'achou o nemo')
            achou_nemo_ = True
            break
        else:
            n += 1
            o += 1
    else: print('a frase não é grande o suficiente para conter o "nemo"')
    if achou_nemo_ != True: print('não foi possivel achar nemo')



def findNemo02(frase):
    frase_split = frase.split(' ')
    frase_split_len = len(frase_split)
    palavras = 0
    achou_nemo = False

    while palavras <=  frase_split_len -1:
       if len(frase) < 4:
           print("isn't big enough for contain nemo")
           break
       if  frase_split[palavras] == 'Nemo':
            print(f'I found Nemo at {palavras+1}')
            achou_nemo = True
            break
       else:
            palavras += 1
    if achou_nemo != True: print("can't find Nemo :(")

kk = input('write something to i find nemo')
findNemo01(kk)