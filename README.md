<div align="center">
  <h1> Modelo de Classificação de Comentários Tóxicos </h1>
</div>

## 📑 Sumário

- [Sobre](#about)
- [Base de Dados](#database)
- [Resultado](#results)
- [Licença](#license)

## 📝 Sobre <a name = "about"></a>

Este projeto está atrelado ao meu Trabalho de Conclusão de Curso (TCC), o qual se trata de um [sistema web](https://fubby.vercel.app) informativo e interativo de apoio para decisões acadêmicas para alunos do Curso de Ciência da Computação na UFCG. Nesse sistema, existe uma seção com comentários de caráter anônimo sobre disciplinas, o que pode dar brechas para pessoas mal intencionadas realizarem comentários ofensivos e inapropriados dentro da proposta de um ambiente colaborativo. Diante disso, foi criado um modelo de classificação de possíveis comentários tóxicos para evitar que esse tipo de conteúdo seja publicado.

## 🎲 Base de Dados <a name = "database"></a>

Como base para a implementação desse modelo foram utilizados os seguintes databases:

- [Comentários Tóxicos PT-BR](https://www.kaggle.com/datasets/gedorneto/comentrios-toxicos-ptbr?select=comentarios_toxicos_ptBR.csv)
- [Brazilian Portuguese Sentiment Analysis Datasets](https://www.kaggle.com/datasets/fredericods/ptbr-sentiment-analysis-datasets)

Contudo, para obter maior acurácia foram aplicadas algumas técnicas baseadas em Data Merging e Data Augmentation que são melhor descritas no documento oficial do meu TCC.

## ✅ Resultados <a name = "results"></a>

A partir dos dados de treinamento, foi possível obter uma acurácia de aproximadamente 99,2%. Contudo, ainda é importante aplicar mais técnicas de aumento de dados para evitar falsos indicadores em comentários reais.

## 📃 Licença <a name="license"></a>

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
