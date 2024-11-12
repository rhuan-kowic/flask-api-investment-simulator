# Investment Simulator

Este é um simulador de investimentos desenvolvido com Python e Flask, utilizando Bootstrap para o frontend e gerenciado pelo Poetry para dependências.

## Funcionalidades

- **Simulação de Investimentos:** Calcule o montante final com base no valor inicial, taxa de juros anual e período de tempo.
- **Interface Responsiva:** Criada com Bootstrap, garantindo uma boa experiência em dispositivos móveis e desktops.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Flask**: Framework web para backend e API.
- **Bootstrap**: Para a estilização da interface.
- **Poetry**: Gerenciador de dependências e ambiente virtual.

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/rhuan-kowic/flask-api-investment-simulator.git
    ```
2. Acesse o diretório do projeto:
    ```bash
    cd seu-repositorio
    ```
3. Instale o Poetry:
    ```bash
    pip install poetry
    ```
4. Instale as dependências do projeto:
    ```bash
    poetry install
    ```

## Execução

1. Ative o ambiente virtual gerenciado pelo Poetry:
    ```bash
    poetry shell
    ```
2. Inicie o servidor Flask:
    ```bash
    flask run
    ```
3. Acesse o aplicativo no navegador em `http://127.0.0.1:5000`.

## Rotas

- **Home (`/`)**: Exibe a página principal do simulador.
- **Simulação (`/simulate`)**: Processa os dados enviados pelo formulário e calcula o montante final.

## Exemplo de Uso

1. Insira o valor inicial, a taxa de juros e o tempo de investimento na página inicial.
2. Clique no botão de simular.
3. O montante final será exibido.

## Licença

Este projeto está licenciado sob a licença MIT.

--- 
