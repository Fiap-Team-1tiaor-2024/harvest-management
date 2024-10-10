# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Gestão de Colheita do Agronegócio

Este é um projeto desenvolvido para gestão da colheita no agronegócio, proporcionando um sistema de simulação de custos e previsão de produção de colheitas, além de armazenar essas informações em um banco de dados Oracle. Este software visa facilitar o gerenciamento e a tomada de decisões para produtores rurais, de forma simples e interativa.

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="[https://www.linkedin.com/company/inova-fusca](https://www.linkedin.com/in/ribeirobrunno/)">Brunno Ribeiro de Oliveira - RM560453</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 2</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 3</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 4</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 5</a>

## 👩‍🏫 Professores:

### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Tutor</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Coordenador</a>

## 📜 Descrição
- **Cadastro de Informações**: Permitir o cadastro de informações sobre os campos e as colheitas, como área plantada, produtividade estimada, máquinas alocadas e custo fixo.
- **Persistência de Dados**: Salvar esses dados tanto em um banco de dados Oracle quanto em um arquivo JSON para persistência local.
- **Simulação e Previsão**: Simular custos de colheita e prever a produção estimada, oferecendo insights financeiros importantes.
- **Facilidade de Uso**: Tornar a interface acessível, com uma ferramenta que seja fácil de utilizar por produtores, mesmo sem grande conhecimento técnico.

## Requisitos Atendidos
Este projeto foi desenvolvido com base nos requisitos das disciplinas estudadas nos capítulos 3, 4, 5 e 6 de Python:
- **Subalgoritmos**: Funções e procedimentos para realizar operações como adicionar campos, simular colheita e calcular produções.
- **Estruturas de Dados**: Uso de listas para armazenar dados temporários dos campos, tuplas para armazenar máquinas alocadas e dicionários para salvar informações estruturadas.
- **Manipulação de Arquivos**: Implementação de manipulação de arquivos JSON para salvar e recuperar dados localmente.
- **Conexão com Banco de Dados Oracle**: Persistência dos dados em um banco de dados Oracle para facilitar a consulta e armazenamento seguro das informações.

## Como Utilizar
1. **Instalação dos Requisitos**
   - É necessário ter o [Oracle Database](https://www.oracle.com/database/) instalado e configurado.
   - Instale as dependências do Python, incluindo `oracledb` e `tkinter` para a interface gráfica:
     ```bash
     pip install oracledb
     ```

2. **Execução do Programa**
   - Ao iniciar o programa, uma janela será exibida com opções à esquerda e campos para preenchimento no lado direito.
   - Preencha os campos obrigatórios e clique em "Adicionar Campo" para salvar as informações no banco de dados.
   - Utilize o botão "Simular Colheita" para gerar uma previsão de produção e custo total.

3. **Armazenamento dos Dados**
   - Os dados serão armazenados tanto em um banco de dados Oracle quanto em um arquivo JSON (`dados_campos.json`) para garantir persistência e backup.

## 📁 Estrutura 
- **`app.py`**: Arquivo principal contendo a lógica do programa e a interface gráfica.
- **`dados_campos.json`**: Arquivo JSON gerado automaticamente para armazenar os dados inseridos.

## Tecnologias Utilizadas
- **Python 3.9+**: Linguagem principal utilizada para desenvolvimento do sistema.
- **Tkinter**: Biblioteca usada para a criação da interface gráfica do usuário.
- **Oracle Database**: Banco de dados utilizado para armazenamento persistente das informações.
- **JSON**: Formato para salvar os dados localmente, proporcionando backup e portabilidade.

## 🔧 Como executar o código
O script está dividido em várias partes importantes para que o funcionamento do programa seja fluido e atenda aos requisitos do agronegócio:

1. **Conexão ao Banco de Dados Oracle**: O script estabelece uma conexão segura com o banco de dados Oracle utilizando as configurações do DSN (Database Source Name). Caso não seja possível conectar, ele exibirá uma mensagem de erro.
2. **Função de Adicionar Campo**: O script oferece uma função para coletar informações inseridas pelo usuário e armazená-las no banco de dados e também em um arquivo JSON. As informações incluem nome do campo, área plantada, produtividade estimada, data de colheita e máquinas alocadas.
3. **Simulação de Custos e Previsão de Produção**: A função de simulação calcula os custos estimados da colheita e também a produção baseada nos dados de produtividade inseridos. Esses cálculos ajudam a estimar receitas e gastos.
4. **Função de Limpeza de Campos**: Ao adicionar um novo campo, todos os campos de entrada de dados são limpos automaticamente para evitar erros de repetição.
5. **Interface Gráfica com Tkinter**: O uso do Tkinter permite criar uma interface gráfica amigável, onde o usuário pode facilmente preencher os dados e visualizar os resultados. O layout está dividido em seções de "Ações" à esquerda e "Entrada de Dados e Resultados" à direita.
6. **Manipulação de Arquivos JSON**: Além de salvar os dados no banco Oracle, eles também são armazenados em um arquivo JSON, proporcionando backup local e portabilidade.

## Funcionalidades
- **Cadastro de Campos**: O usuário pode cadastrar campos preenchendo informações como nome, área plantada, produtividade, data de colheita e máquinas alocadas.
- **Simulação de Colheita**: A simulação fornece o custo estimado da colheita e a previsão de produção, permitindo melhor planejamento financeiro.
- **Armazenamento e Consulta de Dados**: Os dados são salvos no banco de dados Oracle e localmente em um arquivo JSON. É possível consultar os campos cadastrados diretamente na interface gráfica.

## Melhorias Futuras
- Implementar um sistema de relatórios para exportar os dados em formatos como PDF ou Excel.
- Adicionar mais análises financeiras, como comparações de custos entre campos e margens de lucro.
- Melhorar a segurança das credenciais de conexão ao banco de dados.

## Contribuição
Contribuições são bem-vindas! Caso deseje melhorar o projeto, sinta-se à vontade para abrir uma pull request ou enviar sugestões.

## Licença
Este projeto está sob a licença MIT. Para mais detalhes, consulte o arquivo LICENSE no repositório.

## 🗃 Histórico de lançamentos
* 0.1.0 - 10/10/2024
---

Espero que este README ajude a entender melhor o funcionamento do sistema e facilite a apresentação do projeto! Caso tenha dúvidas ou sugestões, sinta-se à vontade para entrar em contato.
