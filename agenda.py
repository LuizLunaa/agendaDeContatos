

print ("----AGENDA ELETRÔNICA FEITA EM PYTHON----")
import time


# coding: utf-8                

#Define uma variável para a lista.
lista = [] 

#Lê os dados do arquivo e joga para a lista.

arq2 = open("lista.txt","a+")
lista = arq2.readlines()
arq2.close()


#Função que constrói o MENU.

def menu():
    print ("-----------------------------------------" )
    print (
             "Escolha uma opção a seguir: \n"
             "(1) Inserir contato \n"
             "(2) Deletar \n"
             "(3) Mostrar agenda \n"
             "(4) Finalizar programa e salvar alterações"
          )
    print ("-----------------------------------------")
    


#Função "lista_agenda" - Adiciona, Remove e Exibe a lista.
    
def lista_agenda(nome, telefone, opc):

    if( opc == 1):
        contato = nome + " | " + telefone + "\n" #Concatena o nome e a data.
        lista.append(contato)
        lista.sort() #Ordena a lista por prioridade.

    elif (opc == 2):
        print ("=" * 30)
        if ( lista == []): #Se a lista for vazia.
            print (" \n Lista Vazia \n ")
        else:
            lista.pop(0) #Remove o elemento de maior prioridade, ou seja, índice 0 da lista.
            print ("Removido o elemento de maior prioridade")
        print ("=" * 30)

    elif (opc == 3):
        print ("=" * 30)
        if (lista == []):
            print (" \n Lista Vazia \n ")
        else:
            print ("Nome:    Telefone:")
            for i in lista:
                print (i)
        print ("=" * 30)
    elif (opc == 4):
        arq = open("lista.txt","w") #Rescreve o arquivo antigo (atualiza lista).
        tam = len(lista) #Recebe o tamanho da lista.


#''For'' que insere os valores no arquivo separado por ';' sendo nome = índice par e data = impar.

        for i in range(tam):
            arq.write(lista[i])

        arq.close()



#Função principal/MENU.

telefone = 0
opc = 0 #Variável do MENU.

while (opc != 4 ):

    menu() #Chama o MENU.

    while True:
        try:
            opc = int(input('Digite a opção desejada:')) #Recebe a opção do MENU ( 1, 2, 3 OU 4).
            break
        except:
            print ("Digite só numeros válidos")

    if ( opc == 1 ):

        print ("\n Informe o nome do contato: \n")
        nome = input('Nome: ')

       
        print ("\n Informe o telefone do contato \n")
        telefone = input('Telefone: ')

        lista_agenda(nome, telefone, 1) #Chama a função "lista_agenda" para adicionar um contato na lista.

        time.sleep(1.0)
        print("--------------------------")
        print("Contato salvo com sucesso!")
        print("--------------------------")
        time.sleep(1.0)     


    elif ( opc == 2):
        lista_agenda(0,0,2) #Chama a função "lista_agenda" para deletar um contato da lista.

    elif (opc == 3): #Chama a função "lista_agenda" para exibir a lista de contatos na tela.
        print ("Lista de contatos: ")
        lista_agenda(0,0,3)
                

lista_agenda(0,0,4) #grava a lista na agenda


    
