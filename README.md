# API-EAS24

### Esta é uma API simples construída em Python utilizando o framework Flask para fornecer informações sobre jogadores de futebol do jogo Ea Sports FC 24.
### Criei ele para estudar um pouco mais sobre o framework Flask e entender melhor como ele trabalha, para a construção dela utilizei o SQLite como banco de dados e, para obter os dados da API, utilizei um dataset com os dados dos jogadores que esta na plataforma kaggle, disponivel em: https://www.kaggle.com/datasets/nyagami/fc-24-players-database-and-stats-from-easports

## Instalação

Para executar este projeto localmente, siga as instruções abaixo:

1. Clone o repositório:

```bash
git clone https://github.com/MarceloBuch/API-EAS24.git
```

2. Entre na pasta do projeto localmente;

3. Instale as depedências do projeto:
```bash
pip install -r requirements.txt
```

4. Execute o arquivo:
```bash
python main.py
```

A aplicação estará disponível em http://localhost:5000.

## Endpoints ##
### 1. Obter Dados de um Jogador por ID ###

- **Método:** GET
- **Rota:** `/players/<int:player_id>`
- **Descrição:** Retorna os dados de um jogador com base no seu ID.

### 2. Obter Jogadores por Nacionalidade ###

- **Método:** GET
- **Rota:** `/players/nation/<string:nation>`
- **Descrição:** Retorna uma lista de jogadores com uma determinada nacionalidade.

### 3. Obter Jogadores por Clube ###

- **Método:** GET
- **Rota:** `/players/club/<string:club_name>`
- **Descrição:** Retorna uma lista de jogadores que pertencem a um determinado clube.

### 4. Obter Jogadores por Posição ###

- **Método:** GET
- **Rota:** `/players/position/<string:position>`
- **Descrição:** Retorna uma lista de jogadores com uma determinada posição.

### 5. Obter 50 Melhores Jogadores (por Overall) ###

- **Método:** GET
- **Rota:** `/players/best`
- **Descrição:** Retorna uma lista ordenada (maior para o menor) de 50 jogadores com o maior Overall.



<br>
<br>
Fique à vontade para contribuir com melhorias ou novos recursos. =)
