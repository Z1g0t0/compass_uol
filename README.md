# __Eduardo Takeshi Voltareli Suzuki__

### [eduardo.suzuki8@hotmail.com](mailto:eduardo.suzuki8@hotmail.com) &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[<img src="imgs/linkedin-logo-icon.png" width="" height="33">](https://www.linkedin.com/in/eduardo-suzuki888/) [<img src="imgs/aws-cloud-quest-cloud-practitioner.png" width="" height="33">](https://www.credly.com/badges/b30c914f-127a-4ddd-9b57-124493b2f993/public_url)


<br>

saudações, sou estudante de sistemas de informação na utfpr, sede de curitiba, onde também moro, e atualmente estou no 6º período. originalmente venho do interior de são paulo, cidade de presidente prudente, onde cursei brevemente ciência da computação pela unesp de lá.

há algum tempo já venho tendo interesse na área de análise/ciência/engenharia de dados e à procura de uma oportunidade de estágio relacionado, inclusive cursando uma matéria optativa de introdução a ciência de dados ofertada pela universidade.

já tive experiência com _python_ em um estágio anterior, onde era responsável tanto pelo desenvolvimento quanto a execução de testes automáticos(_robot framework, pywinauto, requests_, etc.). 

gosto de jogar online, conversar com amigos no discord e ocasionalmente editar vídeos. [aqui](https://www.youtube.com/watch?v=ewrh-qlsbxs) vai um exemplo de um vídeo que editei como um trabalho da faculdade.

## :runner: __sprint 1__:

durante esta primeira _sprint_ fui o líder da _squad_ 5. procurei demonstrar iniciativa no quesito de discussão sobre o material passado, propus reunirmos antes das _dailies_ para tirarmos dúvidas de uns aos outros, acompanhar o progresso de cada um, e passar um pouco da experiência que tive pois já havia usado as tecnologias passadas em um estágio anterior.

#### :rugby_football: scrum:

como mencionado, no estágio anterior já tive experiência com _scrum_, assim como nas _dailies_ desta primeira sprint, participando de reuniões diárias relatando o progresso e eventuais problemas que impediam ou postergavam a evolução das _tasks_ e/ou estudos. o curso ajudou a esclarecer melhor as responsabilidades do _**product owner**_ e _**scrum master**_.

1. **product owner**:

    1. administrar e priorizar o _backlog_ do produto.
    2. entender o mercado e as necessidades do cliente.
    3. traduzir as estratégias do(s) _product manager(s)_ em _user stories_ para que possam se definir em _tasks_ para o time de desenvolvimento.
    4. avaliação de testes e se os resultados atingem o objetivo esperado.
    <br>
    no geral, se responsabilizar pelo relacionamento entre produto e desenvolvimento.
    <br>

2. **scrum master**:

    1. acompanhar e facilitar o progresso do time de desenvolvimento.
    2. avaliar e adaptar aos impedimentos ou dificultadores no desenvolvimento do projeto.
    3. organizar e avaliar as _tasks_ de maior prioridade.

    <br>

#### :octocat: **git e github**:

como também mencionado, já estava familiarizado com o básico do _git_, e já o utilizo para armazenar arquivos _config_ e projetos da universidade. aproveitei para dar uma revisada no conteúdo e aprender mais sobre a tecnologia, principalmente da seção 4 em diante, o conceito de _submodules_, _logs_ mais detalhados, _markdown_ e boas práticas em geral. 

um exemplo de comandos utilizados para inicializar este repositório:

```
git init
git remote add compass_uol https://github.com/z1g0t0/compass_uol
git add .
git commit -m "primeiro commit"
git push
```

#### :penguin: **linux**:

também já estava familiarizado com os comandos de _linux_, conceitos relacionados a arquivos e diretórios, permissões, e comandos relacionados a rede. possuo um _notebook_ com _ubuntu_ instalado e sempre gostei do editor _vim_ junto com _tmux_ desde o primeiro contato que tive e é o que eu sempre utilizo para programar. 

um exemplo de comandos utilizados na criação deste repositório:
```
mkdir -p compass_uol
cd compass_uol
vim readme.md
```

e caso não saibam _**:x**_ para salvar e sair do _vim_ :sweat_smile:

## :runner: __sprint 2__:

#### :outbox_tray: **sql**

_structured query language_, ou _sql_, é uma linguagem estruturada para realizar consultas aplicadas em base de dados, para a geração de tabelas as quais podem ser extraídas informações que podem agregar valor à diversas análises, como _trends_, padrões, estatisticas, visualizações, etc.

um exemplo de _query_ realizada para extrair a tabela _export_1_, encontrada na pasta _export_ usando a base de dados _biblioteca.sqlite_:

```
with livros as(
    select cod, titulo, valor, nome, codeditora, autor
    from livro 
    left join editora on 
        livro.editora = editora.codeditora
)

select cod as codlivro, titulo as titulo, codautor as codautor, autor.nome as nomeautor, valor as valor, codeditora as codeditora, livros.nome as nomeeditora
from livros 
left join autor on 
    livros.autor = autor.codautor
order by valor desc
limit 10
```

#### :bar_chart: **big data**

com a geração de dados cada vez maior dia após dia, é necessário entender os conceitos usados para o armazenamento, os profissionais responsáveis por cada função de análise de dados e o funcionamento de computação em _cloud_.

exemplo de conceitos vistos para armazenamento de dados:

##### _**data warehouse**_

sistema de armazenamento de dados com um _schema_ predefinido, porém podendo receber dados de diferentes fontes, voltado para suportar decisões de negócio.

##### _**data lake**_

armazenamento de dados estruturados e não estruturados, na sua forma bruta, sem um _schema_ predefinido, podendo receber qualquer tipo de dado.

##### _**data store**_

armazenamento de dados com um fim especifico, podendo receber dados de formatos variados, relacionados a uma categoria determinada.

## :runner: __sprint 3__:

#### :snake: **python**

como também mencionado, já estava familiarizado com _python_ devido a um estágio anterior, usei o conteúdo da udemy para revisar os conceitos de programação orientada a objetos, como classes, herança, herança múltipla, etc.

um exemplo de herança múltipla usando classes:

```
class azul:
    rgblue = '0000ff'

class vermelho:
    redgb = 'ff0000'

class roxo( azul, vermelho ):
    redgblue = 'ff00ff'

if __name__ == '__main__':
    roxo = roxo()
    print(f'azul: {roxo.rgblue}, vermelho: {roxo.redgb}, roxo: {roxo.redgblue}')
```

## :runner: __sprint 4__:

#### :curly_loop: **python funcional**
como continuação da _sprint_ anterior, foi visto o paradigma funcional e as ferramentas que o _python_ oferece sobre, sendo visto métodos como _map_, _filter_, _reduce_, entre outros, que possibilitam solucionar problemas de maneira enxuta, sofisticada e com outra maneira de se pensar/programar.

como exempo, a solução do exercício 2 feito na _sprint_, implementando uma função que conta as vogais de uma _string_ ou texto:

```
def conta_vogais(texto:str)-> int:

    vogais = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u']
    
    count = filter(lambda x: x in vogais, texto)
    
    return len(list(count))
```

#### :whale: **docker**
assim como _python_ funcional, pode-se dizer que docker também oferece um paradigma diferente de virtualização, com a execução de programas e/ou sistemas a partir da contrução de uma imagem, com as informações e instruções necessária pré-determinadas, onde estas são executadas em containers, que seriam ambientes isolados tendo o que for necessário para a execução da imagem.

um exemplo de _dockerfile_ usado no exercício da _sprint_, que executa um _script_ _python_ "_hash.py_":

```
from python

workdir /test

copy hash.py .
cmd ["python", "hash.py"]
```

e o comando para construir e executar a imagem:

```
docker build -t mascarar-dados .
docker run -it mascarar-dados
```

vale lembrar em verificar se o serviço do _docker_ está rodando :sweat_smile:

#### :chart_with_downwards_trend: **estatística descritiva com python**

como já havia cursado a matéria de probabilidade e estatística com a didática muito parecida com a do curso, usei os vídeos como revisão dos conceitos gerais, como o de variância, desvio padrão, método de monte carlo, etc.

## :runner: __sprint 5__:

durante esta _sprint_ foi o primeiro contato com os princípios e conceitos que se baseiam a aws(_amazon web services_), assim como a execução de tarefas práticas com suas ferramentas e seus respectivos serviços. principais tecnologias aws abordados durante esta _sprint_ foram:

#### :left_right_arrow: elastic compute cloud (ec2):
...


#### :symbols: simple storage service (s3):
...

#### :repeat: relational database service (rds):
...

#### :twisted_rightwards_arrows: virtual private cloud (vpc):
...

#### :left_luggage: identity access management (iam):
...