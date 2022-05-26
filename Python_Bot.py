import webbrowser, os
from datetime import datetime

usado=False
num_options=0
exit=2
tentativas=0
created_keywords=0
created_links=0
while True:
    ask=str(input("O que você quer que eu faça?\n- Evite letras maiúsculas\n- Insira DICA para receber uma lista de comandos\nDigite aqui: ")).lower()
    if ask=="dica" or ask=="help":
        os.system('cls')
        print("--> Eu atendo diversos comandos básicos te direcionando para sites.")
        print("--> Sou, por padrão, compatível com a maioria dos sites de domínio do google disponíveis.")
        print("--> Também posso abrir um jogo, tente usar <Abrir Minecraft> ou <Abrir Akinator>")
        print("--> Você também pode me adicionar novas funções, se as minhas utilidades padrão não lhe servirem.")
        ask=str(input("O que você quer que eu faça?\nDigite aqui: "))
    if usado==True:
        for number_key in range(1,created_keywords+1):
            locals()[("keyword" + str(number_key))]
            if locals()[("keyword" + str(number_key))] in ask:
                for number_link in range(1,created_links+1):
                    if number_link==number_key:
                        webbrowser.open ((locals()[("link" + str(number_link))]))
                        break
    
    # Verificação de opções Default ------------------------------------------------------------------------------------------------------------------------------
    if "horas" in ask or "horário" in ask or "horario" in ask or "data" in ask or "dia" in ask:
        os.system('cls')
        print(datetime.today().strftime('%A, %B %d, %Y %H:%M:%S'))
        enter=input("Pressione <Enter> para continuar.")
    if "google" in ask or "Google" in ask or "navegador" in ask or "Navegador" in ask:
        webbrowser.open("https://www.google.com.br")
    if "classroom" in ask or "Classroom" in ask or "class" in ask or "Class" in ask:
        webbrowser.open("https://classroom.google.com/u/0/h")
    if "Drive" in ask or "drive" in ask:
        webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
    if "gmail" in ask or "email" in ask or "e-mail" in ask:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    if "google keep" in ask or "notes" in ask or "google notes" in ask:
        webbrowser.open("https://keep.google.com/u/1/#home")
    if "youtube" in ask or "videos" in ask or "vídeos" in ask or "video" in ask or "vídeo" in ask:
        webbrowser.open("https://www.youtube.com")
    if "whatsapp" in ask or "zap" in ask or "mensagem" in ask or "mensagens" in ask or "telefonar" in ask or "chamada" in ask:
        webbrowser.open("https://web.whatsapp.com")
    if "músicas" in ask or "musicas" in ask or "musica" in ask or "música" in ask or "spotify" in ask:
        webbrowser.open("https://www.spotify.com/br/")
    if "minecraft" in ask or "mine" in ask:
        webbrowser.open("https://classic.minecraft.net/?join=tLMPdMClAadnmPkV")
    if "akinator" in ask:
        webbrowser.open("https://pt.akinator.com")
    if "netflix" in ask or "filmes" in ask or "filme" in ask:
        webbrowser.open("https://www.netflix.com/browse")
    if "agenda" in ask or "agendar" in ask or "marcar" in ask:
        webbrowser.open("https://www.google.com/intl/pt-BR/calendar/about/")
    #------------------------------------------------------------------------------------------------------------------------------
    # Criação de novas opções
    os.system('cls')
    end=int(input("Você foi respondido corretamente?\n[1] - sim\n[2] - não\nInsira sua resposta: "))
    os.system('cls')
    if end==1:
        exit=input("Deseja finalizar?\n[1] - sim\n[2] - não\nInsira sua resposta: ")
        if exit==1:
            exit()
    elif end==2:
        newoption=int(input("Gostaria de me adicionar uma nova funcionalidade? É simples e rápido.\n[1] - Sim.\n[2] - Não.\nInsira sua resposta:"))
        if newoption==1:
            created_keywords+=1
            locals()[("keyword" + str(created_keywords))]=str(input("insira a palavra-chave 1: ")) # keyword0=str(input....)
            created_keywords+=1
            locals()[("keyword" + str(created_keywords))]=str(input("insira a palavra-chave 2: ")) # keyword1=str(input....)
            created_keywords+=1
            locals()[("keyword" + str(created_keywords))]=str(input("insira a palavra-chave 3: ")) # keyword2=str(input....)
            created_links+=1
            locals()[("link" + str(created_links))]=str(input("insira o link: "))
            created_links+=1
            locals()[("link" + str(created_links))]=locals()[("link" + str(created_links-1))]
            created_links+=1
            locals()[("link" + str(created_links))]=locals()[("link" + str(created_links-1))]
            usado=True
            print("Muito obrigado pela cooperação.")
            print("AVISO: Se o programa for finalizado, dados adicionados por usuários serão perdidos.")
    os.system('cls')
