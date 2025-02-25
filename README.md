# Configurando a API do Google Sheets para o Cadastro de Alunos

Este guia passo a passo irá te ajudar a configurar a API do Google Sheets para que o software de cadastro de alunos possa acessar e modificar sua planilha.

## 1. Criando a Planilha do Google Sheets

1.  **Acesse o Google Sheets:** Abra seu navegador e vá para [Google Sheets](https://sheets.google.com/).
2.  **Crie uma nova planilha:** Clique no botão "+" para criar uma nova planilha em branco.
3.  **Defina as colunas:** Na primeira linha da planilha, insira os títulos das colunas: "Nome", "Endereço", "Matrícula", "Telefone" (ou as colunas que você definiu no seu software).
4.  **Obtenha a URL da planilha:** Copie a URL da planilha da barra de endereços do seu navegador. Você precisará dela mais tarde.

## 2. Criando um Projeto no Google Cloud Platform

1.  **Acesse o Google Cloud Console:** Vá para [Google Cloud Console](https://console.cloud.google.com/).
2.  **Crie um novo projeto:**
    * Clique em "Selecionar um projeto" no canto superior esquerdo.
    * Clique em "Novo projeto".
    * Dê um nome ao seu projeto (ex: "CadastroAlunos").
    * Clique em "Criar".

## 3. Ativando a API Google Sheets

1.  **Acesse o Painel de APIs e Serviços:** No menu lateral do Google Cloud Console, vá em "APIs e serviços" -> "Painel".
2.  **Ative a API:**
    * Clique em "+ ATIVAR APIS E SERVIÇOS".
    * Pesquise por "Google Sheets API".
    * Clique no resultado "Google Sheets API".
    * Clique em "ATIVAR".

## 4. Criando Credenciais de Conta de Serviço

1.  **Acesse as Credenciais:** No menu lateral do Google Cloud Console, vá em "APIs e serviços" -> "Credenciais".
2.  **Crie uma conta de serviço:**
    * Clique em "+ CRIAR CREDENCIAIS" e selecione "Conta de serviço".
    * Dê um nome à sua conta de serviço (ex: "cadastro-alunos-service-account").
    * Clique em "Criar e continuar".
    * Em "Conceder a esta conta de serviço acesso ao projeto (opcional)", você pode selecionar um papel (por exemplo, "Editor") ou deixar em branco. Clique em "Continuar".
    * Clique em "CONCLUÍDO".
3.  **Crie uma chave JSON:**
    * Na lista de contas de serviço, clique no nome da conta que você criou.
    * Vá na aba "Chaves".
    * Clique em "ADICIONAR CHAVE" e selecione "Criar nova chave".
    * Selecione "JSON" e clique em "Criar".
    * Um arquivo JSON será baixado. Guarde-o em um local seguro.

## 5. Compartilhando a Planilha com a Conta de Serviço

1.  **Obtenha o email da conta de serviço:** Abra o arquivo JSON baixado com um editor de texto. Procure pelo campo "client\_email". Copie o valor desse campo (ex: "cadastro-alunos-service-account@seu-projeto.iam.gserviceaccount.com").
2.  **Compartilhe a planilha:**
    * Abra a planilha do Google Sheets que você criou.
    * Clique no botão "Compartilhar" no canto superior direito.
    * No campo "Adicionar pessoas e grupos", cole o email da conta de serviço.
    * Conceda permissão de "Editor".
    * Clique em "Enviar".

## 6. Configurando o Software

1.  **Copie o arquivo JSON:** Coloque o arquivo JSON que você baixou no mesmo diretório do seu script Python ou em um local de fácil acesso.
2.  **Atualize o código:**
    * Abra o código do seu software de cadastro de alunos.
    * Substitua `'path/to/your/service_account.json'` pelo caminho real do seu arquivo JSON.
    * Substitua `'your_sheet_url'` pela URL da sua planilha do Google Sheets.

## 7. Executando o Software

1.  **Execute o script Python:** Abra um terminal ou prompt de comando, navegue até o diretório do seu script e execute-o com `python seu_script.py`.

Agora seu software deve ser capaz de acessar e modificar a planilha do Google Sheets!