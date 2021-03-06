Neste projeto foram implementadas algumas técnicas de limpeza e tratamento de dados no dataset que contém valores da variação de todas as moedas com relação ao euro,
dos anos de 1999 a 2020. Foi usada também a biblioteca matplotlib, com o estilo do **FiveThirtyEight** para gerar alguns gráficos que apresentam a relação de variação do dólar americano e do real com o euro.

Foi baseado no projeto final do *step 2* do tópico *Storytelling Data Visualization and Information Design*, do curso *Data Scientist in Python* na plataforma Dataquest.io.

Além disso, foram utilizados os conceitos de código limpo e documentação de código para padronizar esse projeto, bem como foi aplicado o conhecimento sobre testes e tratamento de erros, baseando-se nas aulas ministradas pelo professor Ivanovitch Silva na disciplina DCA0305 - PROJETO DE SISTEMAS BASEADOS EM APRENDIZADO DE MÁQUINA.

Para isso, foi utilizada a biblioteca **pandas** para tratar os dados, a biblioteca **pylint** para analisar o padrão de código, a biblioteca **logging** para tratar
erros e a biblioteca **pytest** para realizar testes do código.

Os seguintes comandos foram utilizados para instalar as bibliotecas:

```sh 
pip install pandas
```

```sh
pip install pylint
```

```sh
pip install python3 pytest pytest-sugar
```

É importante ressaltar que foi utilizado o ambiente da ferramente Anaconda para rodar esses programas.

Além disso, o JupterLab foi utilizado para desenvolver o projeto final do curso citado inicialmente, mas em seguida foi necessário exportar 
no formato de script para então utilizar a ferramenta pylint. 

Assim, o seguinte comando foi usado para rodar o script com pylint

```sh
pylint nome_arquivo.py
```
Para rodar o teste, foi utilizado o comando

```sh
python3 -m pytest nome_arquivo.py
```
O código obteve score 10/10 como resultado do pylint, e passou nos 2 testes desenvolvidos. 

Como resultado, os seguintes gráficos foram gerados:

![euro-real](https://user-images.githubusercontent.com/20773821/142852162-454b9c71-fe3f-437e-b4ac-0b6598b3c50b.png)
![euro-dolar](https://user-images.githubusercontent.com/20773821/142852180-1d4a7939-1840-4e05-8adf-006cff698d83.png)
![euro-dolar-real](https://user-images.githubusercontent.com/20773821/142852186-93258009-1ab1-4383-8d92-83af1293bfcf.png)




