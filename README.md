# __Eduardo Takeshi Voltareli Suzuki__ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[<img src="imgs/aws-cloud-quest-cloud-practitioner.png" width="" height="55">](https://www.credly.com/badges/b30c914f-127a-4ddd-9b57-124493b2f993/public_url) [<img src="imgs/aws-partner-sales-accreditation-business.png" width="" height="55">](https://www.credly.com/badges/1023f226-498d-42ac-a5b0-f96fb1574ef1/public_url)
[eduardo.suzuki.pb@compasso.com.br](mailto:eduardo.suzuki.pb@compasso.com.br)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[<img src="imgs/Linkedin-logo-icon.png" width="" height="27">](https://www.linkedin.com/in/eduardo-suzuki888/) 
[eduardo.suzuki8@hotmail.com](mailto:eduardo.suzuki8@hotmail.com) 
#

Saudações, sou estudante de Sistemas de Informação na UTFPR, sede de Curitiba, onde também moro, e atualmente estou no 6º período. Originalmente venho do interior de São Paulo, cidade de Presidente Prudente, onde cursei brevemente Ciência da Computação pela UNESP de lá.

Há algum tempo já venho tendo interesse na área de análise/ciência/engenharia de dados e à procura de uma oportunidade de estágio relacionado, inclusive cursando uma matéria optativa de introdução a ciência de dados ofertada pela universidade.

Já tive experiência com _python_ em um estágio anterior, onde era responsável tanto pelo desenvolvimento quanto a execução de testes automáticos(_robot framework, pywinauto, requests_, etc.). 

Gosto de jogar online, conversar com amigos no discord e ocasionalmente editar vídeos. [Aqui](https://www.youtube.com/watch?v=ewrH-qLSbXs) vai um exemplo de um vídeo que editei como um trabalho da faculdade.

## :runner: __Sprint 1__:

Durante esta primeira _sprint_ fui o líder da _squad_ 5. Procurei demonstrar iniciativa no quesito de discussão sobre o material passado, propus reunirmos antes das _dailies_ para tirarmos dúvidas de uns aos outros, acompanhar o progresso de cada um, e passar um pouco da experiência que tive pois já havia usado as tecnologias passadas em um estágio anterior.

#### :rugby_football: SCRUM:

Como mencionado, no estágio anterior já tive experiência com _scrum_, assim como nas _dailies_ desta primeira sprint, participando de reuniões diárias relatando o progresso e eventuais problemas que impediam ou postergavam a evolução das _tasks_ e/ou estudos. O curso ajudou a esclarecer melhor as responsabilidades do _**Product Owner**_ e _**Scrum Master**_.

1. **Product Owner**:

    1. Administrar e priorizar o _backlog_ do produto.
    2. Entender o mercado e as necessidades do cliente.
    3. Traduzir as estratégias do(s) _product manager(s)_ em _user stories_ para que possam se definir em _tasks_ para o time de desenvolvimento.
    4. Avaliação de testes e se os resultados atingem o objetivo esperado.
    <br>
    No geral, se responsabilizar pelo relacionamento entre produto e desenvolvimento.
    <br>

2. **Scrum Master**:

    1. Acompanhar e facilitar o progresso do time de desenvolvimento.
    2. Avaliar e adaptar aos impedimentos ou dificultadores no desenvolvimento do projeto.
    3. Organizar e avaliar as _tasks_ de maior prioridade.

    <br>

#### :octocat: **Git e Github**:

Como também mencionado, já estava familiarizado com o básico do _git_, e já o utilizo para armazenar arquivos _config_ e projetos da universidade. Aproveitei para dar uma revisada no conteúdo e aprender mais sobre a tecnologia, principalmente da seção 4 em diante, o conceito de _submodules_, _logs_ mais detalhados, _markdown_ e boas práticas em geral. 

Um exemplo de comandos utilizados para inicializar este repositório:

```
git init
git remote add compass_uol https://github.com/Z1g0t0/compass_uol
git add .
git commit -m "Primeiro commit"
git push
```

#### :penguin: **Linux**:

Também já estava familiarizado com os comandos de _linux_, conceitos relacionados a arquivos e diretórios, permissões, e comandos relacionados a rede. Possuo um _notebook_ com _ubuntu_ instalado e sempre gostei do editor _vim_ junto com _tmux_ desde o primeiro contato que tive e é o que eu sempre utilizo para programar. 

Um exemplo de comandos utilizados na criação deste repositório:
```
mkdir -p compass_uol
cd compass_uol
vim README.md
```

E caso não saibam _**:x**_ para salvar e sair do _vim_ :sweat_smile:

## :runner: __Sprint 2__:

#### :outbox_tray: **SQL**

_Structured Query Language_, ou _SQL_, é uma linguagem estruturada para realizar consultas aplicadas em base de dados, para a geração de tabelas as quais podem ser extraídas informações que podem agregar valor à diversas análises, como _trends_, padrões, estatisticas, visualizações, etc.

Um exemplo de _query_ realizada para extrair a tabela _Export_1_, encontrada na pasta _Export_ usando a base de dados _biblioteca.sqlite_:

```
with livros as(
    select cod, titulo, valor, nome, codeditora, autor
    from livro 
    left join editora on 
        livro.editora = editora.codeditora
)

select cod as CodLivro, titulo as Titulo, codautor as CodAutor, autor.nome as NomeAutor, valor as Valor, codeditora as CodEditora, livros.nome as NomeEditora
from livros 
left join autor on 
    livros.autor = autor.codautor
order by valor desc
limit 10
```

#### :bar_chart: **Big Data**

Com a geração de dados cada vez maior dia após dia, é necessário entender os conceitos usados para o armazenamento, os profissionais responsáveis por cada função de análise de dados e o funcionamento de computação em _cloud_.

Exemplo de conceitos vistos para armazenamento de dados:

##### _**Data Warehouse**_

Sistema de armazenamento de dados com um _schema_ predefinido, porém podendo receber dados de diferentes fontes, voltado para suportar decisões de negócio.

##### _**Data Lake**_

Armazenamento de dados estruturados e não estruturados, na sua forma bruta, sem um _schema_ predefinido, podendo receber qualquer tipo de dado.

##### _**Data Store**_

Armazenamento de dados com um fim especifico, podendo receber dados de formatos variados, relacionados a uma categoria determinada.

## :runner: __Sprint 3__:

#### :snake: **Python**

Como também mencionado, já estava familiarizado com _python_ devido a um estágio anterior, usei o conteúdo da udemy para revisar os conceitos de programação orientada a objetos, como classes, herança, herança múltipla, etc.

Um exemplo de herança múltipla usando classes:

```
class Azul:
    rgBLUE = '0000FF'

class Vermelho:
    REDgb = 'FF0000'

class Roxo( Azul, Vermelho ):
    REDgBLUE = 'FF00FF'

if __name__ == '__main__':
    roxo = Roxo()
    print(f'Azul: {roxo.rgBLUE}, Vermelho: {roxo.REDgb}, Roxo: {roxo.REDgBLUE}')
```

## :runner: __Sprint 4__:

#### :curly_loop: **Python Funcional**
Como continuação da _sprint_ anterior, foi visto o paradigma funcional e as ferramentas que o _python_ oferece sobre, sendo visto métodos como _map_, _filter_, _reduce_, entre outros, que possibilitam solucionar problemas de maneira enxuta, sofisticada e com outra maneira de se pensar/programar.

Como exempo, a solução do exercício 2 feito na _sprint_, implementando uma função que conta as vogais de uma _string_ ou texto:

```
def conta_vogais(texto:str)-> int:

    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    count = filter(lambda x: x in vogais, texto)
    
    return len(list(count))
```

#### :whale: **Docker**
Assim como _python_ funcional, pode-se dizer que docker também oferece um paradigma diferente de virtualização, com a execução de programas e/ou sistemas a partir da contrução de uma imagem, com as informações e instruções necessária pré-determinadas, onde estas são executadas em containers, que seriam ambientes isolados tendo o que for necessário para a execução da imagem.

Um exemplo de _Dockerfile_ usado no exercício da _sprint_, que executa um _script_ _python_ "_hash.py_":

```
FROM python

WORKDIR /test

COPY hash.py .
CMD ["python", "hash.py"]
```

E o comando para construir e executar a imagem:

```
docker build -t mascarar-dados .
docker run -it mascarar-dados
```

Vale lembrar em verificar se o serviço do _docker_ está rodando :sweat_smile:

#### :chart_with_downwards_trend: **Estatística Descritiva com Python**

Como já havia cursado a matéria de probabilidade e estatística com a didática muito parecida com a do curso, usei os vídeos como revisão dos conceitos gerais, como o de variância, desvio padrão, método de monte carlo, etc.

## :runner: __Sprint 5__:

Durante esta _sprint_ foi o primeiro contato com os princípios e conceitos que se baseiam a AWS(_Amazon Web Services_), assim como a execução de tarefas práticas com suas ferramentas e seus respectivos serviços. Componentes AWS fundamentais abordados durante esta _sprint_ foram:

#### :left_right_arrow: Elastic Compute Cloud (EC2):
...


#### :symbols: Simple Storage Service (S3):
...

#### :repeat: Relational Database Service (RDS):
...

#### :twisted_rightwards_arrows: Virtual Private Cloud (VPC):
...

#### :left_luggage: Identity Access Management (IAM):
...