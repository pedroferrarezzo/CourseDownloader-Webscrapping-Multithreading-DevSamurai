# DEV SAMURAI COURSE DOWNLOADER
https://class.devsamurai.com.br

## Descrição
Este repositório contém um script em Python que permite baixar todos os cursos disponibilizados pela plataforma Dev Samurai, após a notícia do seu encerramento. O script utiliza multithreading para realizar downloads simultâneos, facilitando e agilizando o processo de obtenção dos conteúdos.<br>
O objetivo é divulgar a boa ação da plataforma, que disponibilizou todos os seus cursos para download, garantindo acesso vitalício ao material.


## Aviso da plataforma - IMPORTANTE
Queridos(as) estudantes,

Com muita gratidão e respeito, nos dirigimos a vocês para compartilhar uma importante atualização sobre a nossa jornada na Dev Samurai.

Após anos dedicados ao ensino de programação, ajudando milhares de alunos a desenvolverem habilidades e alcançarem seus objetivos profissionais, decidimos encerrar os serviços da nossa plataforma de ensino. Esta decisão foi tomada com muito cuidado e consideração por todos vocês, que são a razão de termos chegado tão longe.

Entendemos que a continuidade do acesso ao conhecimento é essencial para o sucesso de todos. Por isso, disponibilizamos todo o conteúdo dos nossos cursos para download logo abaixo neste mesmo site com um tamanho total de aproximadamente 100GB (o que pode ser armazenado em um simples pendrive de 128GB). Isso garante que vocês mantenham acesso vitalício a todo o material e possam seguir estudando no seu ritmo.

**IMPORTANTE:** Os arquivos estarão disponíveis para download até dezembro de 2025. Não deixem para a última hora!

Para facilitar, orientamos que todos os interessados realizem o download dos cursos o mais breve possível. Em caso de dúvidas ou dificuldades, nossa equipe está à disposição para ajudar. Vocês podem entrar em contato através do e-mail: suporte@devsamurai.com.br.

Agradecemos imensamente pela confiança depositada na Dev Samurai ao longo dessa jornada. O aprendizado e o sucesso de cada um de vocês sempre foram o que nos motivou a continuar criando conteúdo de qualidade.

Desejamos a todos muito sucesso e evolução em suas carreiras e projetos. Que essa despedida seja apenas um novo começo na trilha do aprendizado.

Com gratidão,
Equipe Dev Samurai

## Lista de Cursos
- Aulas ao Vivo
- Backend - Dominando o NodeJS
- Backend - Dominando o Postgres
- Carreira de Programador
- Flutter - Calculadora IMC
- Flutter - Cardápio online
- Flutter - Fluck Noris
- Flutter - Lista de Leituras
- Flutter Avançado
- Flutter Básico
- Flutter Snippets
- Frontend - Bootstrap
- Frontend - CSS Grid
- Frontend - Criando seu currículo
- Frontend - Criando seu portfólio
- Frontend - Curriculum HTML
- Frontend - Entendo o HTML com o CSS
- Frontend - Flexbox
- Frontend - Formulário de Cadastro
- Frontend - HTML Básico
- Frontend - Loja de Café
- Frontend - Mobile First
- Frontend - Preprocessadores (Sass)
- Frontend - Sua primeira página Web
- Full Stack - Food Commerce
- Ionic
- JavaScript - Gerador Senhas
- JavaScript Básico ao Avançado
- Kapi Academy - API Supreme
- Linux para Programadores
- Lógica de Programação Avançada
- Lógica de Programação Básica
- Master Classes
- Minha Primeira Oportunidade
- Minicurso Programar do Zero
- Monitoria Aberta
- Montando o ambiente Dev
- Primeira Oportunidade
- Programar do Zero - HTML
- Programar do Zero - Jokenpo
- Programar do Zero - Ping-Pong
- Programar do Zero
- Python - Forca
- Python - Jogo Adivinha
- Python - Jogo Cobrinha
- Python - Juros Compostos
- Python - Tabela Fipe
- Python Avançado
- Python Básico
- React - API Github
- React - Fundamentos
- React - Lista de Leitura
- React Native - Calculadora IMC
- React Native - Publicando o Aplicativo
- React Native - Smart Money - Firebase
- React Native - Smart Money - Navigation V5
- React Native - SmartMoney - Login
- React Native - SmartMoney
- React Native - TODO
- React Native
- Renda Extra 10x - Entrevistas
- Renda Extra 10x - Mente Inabalável
- Renda Extra 10x - Precificação de Sistemas
- Renda Extra 10x - Treinamento extra
- Renda Extra 10x
- TypeScript - TODO List
- TypeScript Básico

## COMO USAR

1. Clone este repositório:
   ```sh
    git clone https://github.com/seu-usuario/dev-samurai-course-downloader.git
   
2. Inicialize um Venv e instale as dependências:
   ```sh
    # Crie o Venv
    python -m venv venv
   
    # Ative o Venv - Windows
    .\venv\Scripts\activate

    # Ative o Venv -Linux/macOS:
    source venv/bin/activate

    # Instale o BS4
    pip install requests beautifulsoup4

3. Altere a variável referente ao diretório de download:
    ```sh
    # ATENÇÃO: o conteúdo possui aproximadamente 100GB. Certifique-se de ter espaço disponível em disco/unidade USB.
    ...
    if __name__ == '__main__':
      url = 'https://class.devsamurai.com.br'
      download_folder = r'C:\Users\User\Downloads' # Exemplo
    ...
    
4. OPCIONAL: aumente a quantidade de Threads utilizadas para download:
    ```sh

    # ATENÇÃO: aumentar a quantidade de Threads resulta em mais downloads simultâneos. Isso pode acelerar o processo de download, mas também aumentará o consumo de largura de banda e a carga sobre o servidor. Use com cautela para evitar sobrecarregar sua conexão ou a plataforma.
    # Múltiplas conexões simultâneas de um mesmo cliente, podem também ser interpretadas como um comportamento suspeito, podendo levar a restrições de acesso ou bloqueios temporários. Recomendo ajustar a quantidade de threads com moderação para evitar problemas de conectividade.

    ...
    threads = []
    for _ in range(x):  # x -> Número de threads
        ...
        threads.append(thread)
    ...

5. Execute o Projeto:
    ```sh
    python DownloadDevSamuraiCourses.py

6. O download começará. Acompanhe pela saída no terminal que curso está sendo baixado e se foi concluído com sucesso:
   ![image](https://github.com/user-attachments/assets/8e627c82-d9d5-4f4c-bbb9-7752eaf7aea9)


    


