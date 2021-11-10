Neste projeto foram implementadas algumas técnicas de limpeza e tratamento de dados, usando como exemplo o dataset eBay Car que contém dados de vendas de carros.

Foi baseado no projeto final do *step 2* do tópico *Pandas and NumPy Fundamentals*, do curso *Data Scientist in Python* na plataforma Dataquest.io.

Além disso, foram utilizados os conceitos de código limpo e documentação de código para padronizar esse projeto, baseando-se nas aulas ministradas pelo professor
Ivanovitch Silva na disciplina DCA0305 - PROJETO DE SISTEMAS BASEADOS EM APRENDIZADO DE MÁQUINA.

Para isso, foi utilizada a biblioteca **pandas** para tratar os dados e a biblioteca **pylint** para analisar o padrão de código. 
Os seguintes comandos foram utilizados para instalar as bibliotecas:

```sh 
pip install pandas
```

```sh
pip install pylint
```

É importante ressaltar que foi utilizado o ambiente da ferramente Anaconda para rodar esses programas.

Além disso, o JupterLab foi utilizado para desenvolver o projeto final do curso citado inicialmente, mas em seguida foi necessário exportar 
no formato de script para então utilizar a ferramenta pylint. 

Assim, o seguinte comando foi usado para rodar o script com pylint

```sh
pylint <nome_arquivo.py>
```

Na primeira vez que o comando foi utilizado, não foi obtido um score aceitavel:

![image](https://user-images.githubusercontent.com/20773821/141049396-7fcaca18-836f-4df3-ae07-e9a04d9bb227.png)


No entando, após corrigir as sugestões citadas na imagem acima, obteve-se o score maximo:

![image](https://user-images.githubusercontent.com/20773821/141049223-2f1873e1-572b-4961-9d57-5490a484b2d1.png)
