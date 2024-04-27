from nltk.stem import SnowballStemmer
import re
from nltk import download
download("stopwords")
download('punkt')
from nltk.corpus import stopwords
from re import sub
import unidecode
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__, template_folder='template', static_folder='template')
CORS(app)

model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

#funcoes de limpeza    
def remove_accent_mark(data):
  return unidecode.unidecode(data)

sm = SnowballStemmer("portuguese")
stop_words = stopwords.words("portuguese")
#Adição de stop_words
stop_words.append('disciplina')
stop_words.append('aulas')
stop_words.append('aula')
stop_words.append('professor')
stop_words.append('professora')
stop_words.append('cadeira')
stop_words.append('cadeiras')
stop_words.append('semestre')
stop_words.append('período')
stop_words.append('dados')
stop_words.append('algoritmos')
stop_words.append('porém')
stop_words.append('pois')
stop_words.append('porque')
stop_words.append('todos')
stop_words.append('todas')
stop_words.append('toda')
stop_words.append('tudo')
stop_words.append('conteúdo')
stop_words.append('frontend')
stop_words.append('backend')
stop_words.append('design')
stop_words.append('tornaram')
stop_words.append('tornou')
stop_words.append('fez')
stop_words.append('faz')
stop_words.append('torna')
stop_words.append('usuário')
stop_words.append('user')
stop_words.append('alguns')
stop_words.append('algumas')
stop_words.append('algo')
stop_words.append('exercícios')
stop_words.append('provas')
stop_words.append('prova')
stop_words.append('user')
stop_words.append('pra')
stop_words.append('vai')
stop_words.append("ter")
stop_words.append("fazer")
stop_words.append("the")
stop_words.append("nada")
stop_words.append("dia")
stop_words.append("coisa")
stop_words.append("ficar")
stop_words.append("pode")
stop_words.append("vou")
stop_words.append("mim")
stop_words.append("todo")
stop_words.append("vida")
stop_words.append("ainda")
stop_words.append("quer")
stop_words.append("metodologia")
stop_words.append("didática")
stop_words.append("pra")
stop_words.append("-")

# removendo acentuacao de stop words
for i in range(len(stop_words)):
  stop_words[i] = remove_accent_mark(stop_words[i])

frequent_bad_word = "merda"
def check_alphanumeric(text):
  output = []
  for word in text.split(" "):
    if(not(word.isdigit() or word.isalpha()) and word != ''):
      output.append(frequent_bad_word)
    else:
      output.append(word)
  text = " ".join(w for w in output)
  return text

def stemmer(text):
  text = text.split(" ")
  text = [sm.stem(w) for w in text]
  text = " ".join(w for w in text)
  return text

def check_accent_mark(text):
  output = []
  for w in text:
    output.append(remove_accent_mark(w))
  text = " ".join(w for w in output)
  return text

def clean(text):
  text = text.lower()
  text = sub("^\d+\s|\s\d+\s|\s\d+$", "", text)
  text = sub('[,.!?;:/>@_#"(]', '', text)
  text = re.sub(r"http\S+", "", text).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','')
  text = check_alphanumeric(text),
  text = check_accent_mark(text)
  text = ' '.join(i for i in text.split() if not(i in stop_words) and len(i) >= 2 and (not any (c.isdigit() for c in i)))
  return text

@app.route('/analyse', methods=['POST'])
def analyse():
    data = request.json
    text = data['comment']
    text = [text]
    print("Comentario: {}".format(text))

    # Limpa dados de teste
    text = [clean(str(i)) for i in text]
    text = [stemmer(str(i)) for i in text]

    # Transforma os dados de teste em vetores de palavras.
    vector_testes = vectorizer.transform(text)

    healthy = -1
    # Fazendo a classificação com o modelo treinado.
    for t, c in zip (text,model.predict(vector_testes)):
        healthy = c

    print("Classe: {} ", healthy)
    result = { 'result' : str(healthy)}
    return jsonify(result)


# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 5500))
#     app.run(host='0.0.0.0', port=port)

