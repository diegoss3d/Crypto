def principal():
    #Método para limpar console
    import os, time, sys
    os.system('cls')
    clear = lambda: os.system('cls')
    barraLonga = '\n________________________________________________________\n'
    criptoLogo = ("""\033[35m
          .d8888b           d8b          888                
         d88P  Y88b         Y8P          888                
         888    888         888          888                
         888        888d888 888 88888b   888888   d88b      
         888        888P    888 888  88b 888    d88  88b    
         888    888 888     888 888  888 888    888  888    
         Y88b  d88P 888     888 888 d88P Y88b   Y88  88P    
           Y8888P   888     888 88888P   Y888     Y88P 
                                888                         
                                888                         
                                888
        \n\033[m""")

    for l in criptoLogo:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.001)
    nome = str(input('\nOlá, Vamos começar com o seu nome: \n'))
    while len(nome) == 0 or nome.isdigit():
        nome = str(input('Por favor, Digite pelo menos uma letra: '))
    clear()
    seEmail = str(input("Gostaria de receber a chave por e-mail [S/N]? ")).lower()
    while seEmail not in 'sn':
        seEmail = str(input('Favor, Apenas S ou N: ')).lower()
    if seEmail == 's':
        email = input(f'{criptoLogo}\nSeja bem vindo ao Cripto \033[1;31m{nome}\033[m, qual seu e-mail?\n')
        while len(email) == 0:
            email = input('Digite ao menos um caractere: ')
    print(f'Seja bem vindo {nome}')
    clear()
    print(criptoLogo, 'Ótimo! Pressione ENTER para entrar no menu principal.')
    input()
    clear()

    #Função Encriptar Mensagem
    def encriptar():
        clear()
        assunto = 'Codificada'
        print(f'{criptoLogo}  {barraLonga}\033[33m                 Codificar Mensagem \033[m{barraLonga}')
        print('   Escolha uma opção abaixo:\n \n   1. Importar a mensagem desde um arquivo (mensagem.txt) \n   2. Digitar a mensagem \n   3. Menu Inicial')
        opcao = input()
        #Ler mensagem de arquivo
        if opcao == '1':
            arquivo = 'mensagem.txt'
            try:
                mensagem = open(arquivo, "r", encoding="utf-8", errors='ignore')
                mensagem = mensagem.read()
                print(barraLonga, 'Mensagem Encontrada: \n', mensagem, barraLonga)
            except:
                print('Arquivo não encontrado. Nome do arquivo deve ser mensagem.txt \n')
                menuInicial()
                exit()
        elif opcao == '2':
            print(f'{barraLonga}')
            mensagem = input("   \033[33mDigite a mensagem:\033[m \n")
            print(barraLonga)
        elif opcao == '3':
            menu()
        else:
            print('Seleção Inválida. Presione ENTER para continuar')
            input()
            encriptar()
        #Inserir Chave
        print('\033[33m\n   Escolha uma opção abaixo para escolher a chave: \n\033[m')
        print('\n   1. Gerar a chave aleatória  \n   2. Digitar a chave: \n   3. Menu Inical')
        opcao = input()
        if opcao == '1':
            key = randomKey()
        elif opcao == '2':
            key = verificador()
        elif opcao == '3':
            menu()
        else:
            print('Seleção Inválida. Presione ENTER para continuar')
            input()
            menu()

        #Conversão ASCII
        mensagemAscii = [ord(c) for c in mensagem]
        keyAscii = [ord(c) for c in key]
        tamanhoKey = len(keyAscii)
        tamanhoMensagem = len(mensagemAscii)
        indicador = tamanhoKey - tamanhoMensagem
        if tamanhoKey == tamanhoMensagem:
            print('Tamanho da chave é incompativel com mensagem \n')
            menuInicial()
        #Selecção de Algoritmo de Encriptação de acordo ao tamanho
        elif tamanhoKey > tamanhoMensagem:
            #Expandir Mensagem ao mesmo tamanho da key
            for e in mensagemAscii:
                tamanhoMensagem = len(mensagemAscii)
                if tamanhoMensagem != tamanhoKey:
                    mensagemAscii.append(e)
            #Soma key & Mensagem e subtrai a media da key na Cripto
            mensagemCripto = []
            contador = 0
            soma = 0
            for e in keyAscii:
                soma += e
            media = soma / len(keyAscii)
            media = int(media)
            while contador < tamanhoMensagem:
                soma = keyAscii[contador] + mensagemAscii[contador]
                soma = soma-media
                mensagemCripto.append(soma)
                contador += 1
            mensagemTest = [chr(x) for x in mensagemCripto]
            mensagemString = "".join(mensagemTest)
            #Salvar Arquivo
            file = open("Mensagem Codificada.txt", "w",  encoding="utf-8", errors='ignore')
            file.write(mensagemString)
            file.close()
            keyExpandida = str(indicador) + key
            keyArquivo = open("Chave.txt", "w", errors="ignore")
            keyArquivo.write(keyExpandida)
            keyArquivo.close()
            clear()
            print(f" {criptoLogo} {barraLonga}\033[33mMensagem Codificada:\033[33m \n {mensagemString} {barraLonga}")
            print(f'Atento a sua chave: {keyExpandida} {barraLonga}')
            print(f"{criptoLogo}Sua mensagem foi codificada com sucesso. Mensagem codificada e chave armazenados no disco como arquivos. \n")
            enviarEmail(mensagemString, keyExpandida, nome, email, assunto)
            return menuInicial()
        else:
            #Expandir Key ao mesmo tamanho da mensagem
            for e in keyAscii:
                tamanhoKey = len(keyAscii)
                if tamanhoMensagem != tamanhoKey:
                    keyAscii.append(e)
            #Soma key & Mensagem e subtrai a media da key na Cripto
            mensagemCripto = []
            contador = 0
            soma = 0
            for e in keyAscii:
                soma += e
            media = soma / len(keyAscii)
            media = int(media)
            while contador < tamanhoMensagem:
                soma = keyAscii[contador] + mensagemAscii[contador]
                soma -= media
                mensagemCripto.append(soma)
                contador += 1
            mensagemTest = [chr(x) for x in mensagemCripto]
            mensagemString = "".join(mensagemTest)
            #Salvar Arquivo
            file = open("Mensagem Codificada.txt", "w",  encoding="utf-8", errors='ignore')
            file.write(mensagemString)
            file.close()
            keyArquivo = open("Chave.txt", "w", errors="ignore")
            keyArquivo.write(key)
            keyArquivo.close()
            clear()
            print(f"{criptoLogo} Sua mensagem foi codificada com sucesso e armazenada no arquivo Mensagem Codificada.txt. \n")
            print(f'{barraLonga} \033[33mMensagem Codificada:\033[m  {mensagemString} {barraLonga} \033[33mChave:\033[m {key} {barraLonga}')
            if seEmail == 's':
                enviarEmail(mensagemString, key, nome, email, assunto)
            return menuInicial()
    #Função Desencriptar Mensagem
    def desencriptar():
        assunto = 'Decodificada'
        clear()
        #Leitura da mensagem encriptada
        print(f'{criptoLogo} \n {barraLonga}\033[33m                Decodificar Mensagem\n\033[m {barraLonga}')
        print('\n   1. Importar Mensagem Codificada (Mensagem Codificada.txt) \n   2. Digitar mensagem Codificada \n   3. Menu Inical')
        opcao = input()
        if opcao == '1':
            clear()
            try:
                cripto = open("Mensagem Codificada.txt", "r", encoding="utf-8", errors='ignore')
                cripto = cripto.read()
                print(f'{criptoLogo} {barraLonga} \033[33mMensagem importada:\033[m \033[31m{cripto}\033[m {barraLonga}')
                key = input("Insira a respectiva chave: \n")
            except:
                print('Arquivo não encontrado')
                input()
                desencriptar()
                exit()
        elif opcao == '2':
            clear()
            cripto = input("Digite o Cripto: \n")
            key = input("Insira a respectiva chave: \n")
        elif opcao == '3':
            menu()
        else:
            print('Seleção Inválida')
            input()
            desencriptar()
        #Ler e retirar indicador
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        indicador = []
        keyExpandida = key
        for e in key:
            for i in numeros:
                if e == i:
                    indicador.append(e)
                    key = key.replace(e,'')
        if indicador != []:
            indicador = "".join(indicador)
            indicador = int(indicador)
        #Conversão ASCII
        mensagemAscii = [ord(c) for c in cripto]
        keyAscii = [ord(c) for c in key]
        tamanhoKey = len(keyAscii)
        tamanhoMensagem = len(mensagemAscii)
        if tamanhoKey == tamanhoMensagem:
            for e in mensagemAscii:
                tamanhoMensagem = len(mensagemAscii)
                if tamanhoMensagem != tamanhoKey:
                    mensagemAscii.append(e)
            #Somar key e mensagem
            mensagemCripto = []
            contador = 0
            soma = 0
            for e in keyAscii:
                soma += e
            media = soma / len(keyAscii)
            media = int(media)
            while contador < tamanhoMensagem - indicador:
                soma = mensagemAscii[contador] - keyAscii[contador]
                soma += media
                mensagemCripto.append(soma)
                contador += 1
            #Adicionar a cada elemento da mensagem ASCII
            try:
                mensagemTest = [chr(x) for x in mensagemCripto]
                mensagemDesencriptada = "".join(mensagemTest)
                #save the file
                file = open("Mensagem Decodificada.txt", "w", errors="ignore")
                file.write(mensagemDesencriptada)
                file.close()
                clear()
                print(f'{criptoLogo}{barraLonga} Mensagem Deodificada:  {mensagemDesencriptada} {barraLonga}')
                print("\033[33m   Confira sua mensagem decodificada!. Mensagem aramazenada no arquivo\033[m Mensagem Decodificada.txt \n")
                enviarEmail(mensagemDesencriptada, keyExpandida, nome, email, assunto)
                menuInicial()
            except:
                print('Chave é incompátivel.  \n')
                menu()
        else:
            #criar key do mesmo tamanho da mensagem
            for e in keyAscii:
                tamanhoKey = len(keyAscii)
                if tamanhoMensagem != tamanhoKey:
                    keyAscii.append(e)
            mensagemCripto = []
            contador = 0
            soma = 0
            for e in keyAscii:
                soma += e
            media = soma / len(keyAscii)
            media = int(media)
            while contador < tamanhoMensagem:
                soma = mensagemAscii[contador] - keyAscii[contador]
                soma += media
                mensagemCripto.append(soma)
                contador += 1
            #Adicionar a cada elemento da mensagem ASCII
            try:
                mensagemTest = [chr(x) for x in mensagemCripto]
                mensagemDesencriptada = "".join(mensagemTest)
                #save the file
                file = open("Mensagem Decodificada.txt", "w", errors="ignore")
                file.write(mensagemDesencriptada)
                file.close()
                clear()
                print(f'{criptoLogo} {barraLonga} \033[33mMensagem Decodificada:\033[m  {mensagemDesencriptada} {barraLonga}')
                print("Confira sua mensagem decodificada!. Mensagem aramazenada no arquivo Mensagem Decodificada.txt \n")
                enviarEmail(mensagemDesencriptada, key, nome, email, assunto)
                menuInicial()
            except:
                print('   Chave não corresponde.  \n')
                return menuInicial()

    #Função Voltar ao Menú Inicial
    def menuInicial():
        print('   Voltar ao menú incial S/N:')
        opcao = input()
        if opcao == 's' or opcao == 'S':
            clear()
            menu()
        elif opcao == 'n' or opcao == 'N':
            clear()
            print("Obrigado por utilizar Cripto!")
            input()
        else:
            menu()
    #Função gerador de chave aleatória
    def randomKey():
        import random
        list = []
        x = 0
        print('   Digite o tamanho da Key:')
        try:
            tamanhoKey = int(input())
        except:
            print('\nNúmero Inválido!')
            return randomKey()
        if 2 < tamanhoKey < 33:
            while x < tamanhoKey:
                item = random.randint(97, 122)
                list.append(item)
                x += 1
            keyAscci = [chr(x) for x in list]
            key = "".join(keyAscci)
            return key
        elif tamanhoKey <3 or tamanhoKey > 32:
            print("Tamanho da chave incompátivel.")
            return randomKey()
    #Função verificadora de segurança mínima
    def verificador():
        key = str(input("Insira uma chave: "))
        while len(key) <= 2:
            print("Chave deve ser maior a tres caracteres.")
            key = str(input("Insira uma chave: "))
        i = key[0]
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        keyAprovada = False
        keyAprovada2 = True
        for e in key:
            if e != i:
                keyAprovada = True
        for j in key:
            for k in numeros:
                if j == k:
                    keyAprovada2 = False
                    break
        if keyAprovada and keyAprovada2:
            return key
        else:
            print('\nChave não cumpre com os criterios mínimos de segurança. \n')
            print('1. A chave não pode ter todos os caracteres iguais \n2. A chave não pode ter números\n')
            return verificador()

    #Função de Informações Cripto
    def info():
        clear()
        print(f'{criptoLogo} \n {barraLonga} Atividades Praticas Supervisionadas | Universidade Paulista \n')
        print('\nCripto codifica e decodifica mensagems com foco na segurança da informação.')
        print('O nivel de segurança é proporcional ao tamanho da respectiva chave.')
        print('Mais Informações: https://github.com/AlfredoSh/Cripto ', barraLonga)
        menuInicial()
    #Função Enviar E-mail
    def enviarEmail(mensagemString, key, nome, email, assunto):
        try:
            import smtplib, ssl
            from email.mime.text import MIMEText as text
            assunto
            Chave = "Chave" + ":"
            if assunto == 'Decodificada':
                Chave = ''
                key = ''
            port = 587
            smtp_server = "smtp.gmail.com"
            sender_email = "cripto.projectunip@gmail.com"
            receiver_email = email
            print('   Enviando informações a ', email)
            password = 'criptoproject'
            message = f"""Subject:  Mensagem {assunto} - Cripto

            Olá {nome},

            Parabéns! Sua mensagem foi {assunto} com sucesso:

            Mensagem {assunto}: {mensagemString}			
            {Chave}{key}


            Abraços,

            Equipe Cripto
            https://github.com/AlfredoSh/Cripto

            """
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.encode('utf8'))
                message.encode("utf8")
            print('   Informações enviadas com sucesso')
        except:
            print('   Informações não enviadas!')
    #Função Menú Principal
    def menu ():
        clear()
        print(criptoLogo)
        print(barraLonga, '\033[33m       Codifica ou decodifica uma mensagem\033[m', barraLonga)
        print('   Escolha uma das opções abaixo: \n ')
        print("   1. Codificar \n   2. Decodificar \n   3. Informações\n   4. Sair")
        opcao = input()
        if opcao == "1":
            encriptar()
        elif opcao == "2":
            desencriptar()
        elif opcao == "3":
            info()
        elif opcao == "4":
            print("Obrigado por utilizar Cripto!")
            input()
            exit()
        else:
            print('Seleção Inválida. Presione ENTER para continuar')
            input()
            menu()
    menu()
principal()