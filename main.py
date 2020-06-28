from bot_whatsapp import pd, WhatsappBot, date, time
from tkinter import Tk
from tkinter.filedialog import askopenfile
def enviarmsg(nomes, filepath=None):
    bot = WhatsappBot()
    bot.enviarMensagensLojasImagem(nomes, filepath)
    bot.driver.quit()
    with open("text_stored.txt", "a") as myfile:
        myfile.write(f"Número de contatos enviados ({date.today()}) : {bot.count_mensagens}\n")

def fazer_dados():
    print('Escolha o arquivo CSV')
    filepath_global = askopenfile()
    filepath_name = filepath_global.name
    df = pd.read_csv(filepath_name ,encoding='latin-1', sep=';')

    nomes_completos = df['NOME E SOBRENOME'].tolist()

    nomes_completos = sorted(nomes_completos, key = str.lower)

    return nomes_completos

#LEMBRA DE COLOCAR O ÍNDICE DO PRIMEIRO NOME COMO 2
def pedir_informacoes():
    flag = False
    flag2 =False
    opcao = 0
    opcao_mensagem = 0

    while ( (opcao != 1 and opcao != 2) or (flag == False) ):
        opcao = int(input('Digite o número da opção escolhida para quem mandar os opcao:\n1 - Arquivo CSV\n2 - Digitar os nomes\n'))

        if opcao == 1:
            contatos = fazer_dados()
            flag = True
        elif opcao == 2:
            contatos = input("Digite os nomes exatamente como estão salvos nos contatos separados por uma /\nExemplo: Arthur Brito Medeiros/Pedro Medeiros/Isabela Campelo\n")
            contatos = contatos.split('/')
            flag = True
        else:
            print('Opção inválida, escolha novamente')
        #nomes = fazer_dados()

    while ( (opcao != 1 and opcao != 2 and opcao != 3) or (flag2 == False) ):
        opcao_mensagem = int(input('O que você deseja fazer:\n1 - Enviar mensagem e arquivo\n2 - Enviar só mensagem\n3 - Enviar só arquivo\n'))

        if opcao_mensagem == 1:
            mensagem = input('Escreva a mensagem:\nDica: Escreva no bloco de notas depois cole aqui\n')
            print('Escolha o arquivo\n')
            filepath = askopenfile()
            filepath_send = filepath.name
            bot2 = WhatsappBot()
            bot2.enviarMensagemImagem(contatos, mensagem, filepath_send)
            flag2 =True
            bot2.driver.quit()

        elif opcao_mensagem == 2:
            mensagem = input('Escreva a mensagem:\nDica: Escreva no bloco de notas depois cole aqui\n')
            bot2 = WhatsappBot()
            bot2.enviarMensagens(contatos, mensagem)
            flag2 = True
            bot2.driver.quit()

        elif opcao_mensagem == 3:
            print('Escolha o arquivo')
            filepath = askopenfile()
            filepath_send_2 = filepath.name
            bot2 = WhatsappBot()
            bot2.enviarImagem(contatos, filepath_send_2)
            flag2 = True
            bot2.driver.quit()
        else:
            print('Opção inválida, escolha novamente')

if __name__ == '__main__':
    pedir_informacoes()