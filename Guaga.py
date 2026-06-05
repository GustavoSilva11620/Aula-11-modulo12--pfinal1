import requests

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
    pergunta = dados["results"][x]["question"]
    resposta = dados["results"][x]["correct_answer"]
    incorreto = dados["results"][x]["incorrect_answers"]

    print(f"\n\n\npergunta={pergunta}\nresposta={resposta}\nincorretas={incorreto}")


