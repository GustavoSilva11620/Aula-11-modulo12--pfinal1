import requests
import html
amount=int(input("n de perguntas"))
category=22
difficulty="medium"
type="multiple"

url = (
    f'https://opentdb.com/api.php?'
    f'amount={amount}&category={category}&difficulty={difficulty}&type={type}'
)

dados = requests.get(url).json()

for x in range(0,amount):
    pergunta = html.unescape(dados["results"][x]["question"])
    resposta = html.unescape(dados["results"][x]["correct_answer"])
    incorreto = [html.unescape(opt)for opt in dados["results"][x]["incorrect_answers"]]
    opcoes= incorreto+[resposta]
    opcoes.shuffle
    print(f"\n\n\npergunta={pergunta}\nresposta={resposta}\nincorretas={incorreto}")

