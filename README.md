<div align="center">
  <h1> Modelo de Classificação de Comentários Tóxicos </h1>
</div>

## 📑 Sumário

- [Sobre](#about)
- [Acesso](#access)
- [Base de Dados](#database)
- [Resultados](#results)
- [Tecnologias](#tech)
- [Projeto Associado](#projects)
- [Licença](#license)

## 📝 Sobre <a name = "about"></a>

Este projeto está atrelado ao meu Trabalho de Conclusão de Curso (TCC), o qual se trata de um [sistema web](https://fubby.vercel.app) informativo e interativo de apoio para decisões acadêmicas para alunos do Curso de Ciência da Computação na UFCG. Nesse sistema, existe uma seção com comentários de caráter anônimo sobre disciplinas, o que pode dar brechas para pessoas mal intencionadas realizarem comentários ofensivos e inapropriados dentro da proposta de um ambiente colaborativo. Diante disso, foi criado um modelo de classificação de possíveis comentários tóxicos para evitar que esse tipo de conteúdo seja publicado.

## 🛜 Acesso <a name = "access"></a>

A API pode receber requisições por meio do endereço: [nlp-toxic-detection.onrender.com/analyse](https://nlp-toxic-detection.onrender.com/analyse)

## 🎲 Base de Dados <a name = "database"></a>

Como base para a implementação desse modelo foram utilizados os seguintes databases:

- [Comentários Tóxicos PT-BR](https://www.kaggle.com/datasets/gedorneto/comentrios-toxicos-ptbr?select=comentarios_toxicos_ptBR.csv)
- [Brazilian Portuguese Sentiment Analysis Datasets](https://www.kaggle.com/datasets/fredericods/ptbr-sentiment-analysis-datasets)

Contudo, para obter maior acurácia foram aplicadas algumas técnicas baseadas em Data Merging e Data Augmentation que são melhor descritas no documento oficial do meu TCC.

## ✅ Resultados <a name = "results"></a>

A partir dos dados de treinamento, foi possível obter uma acurácia de aproximadamente 99,2%. Contudo, ainda é importante aplicar mais técnicas de aumento de dados para evitar falsos indicadores em comentários reais.

## 🚀 Tecnologias <a name = "tech"></a>

As principais tecnologias utilizadas no desenvolvimento do projeto foram:
- [Python](https://docs.python.org/3/)
- [NLTK](https://www.nltk.org)
- [Scikit-learn](https://scikit-learn.org/0.21/documentation.html)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)

## 🔍 Projeto Associado <a name = "projects"></a>

Este modelo faz parte do sistema web Fubby.
O repositório com o site criado pode ser acessado em: [github.com/emannuellymelo/FubbyUFCG](https://github.com/emannuellymelo/FubbyUFCG)

## 📃 Licença <a name="license"></a>

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
