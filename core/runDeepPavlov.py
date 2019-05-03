from deeppavlov import configs, train_model
from deeppavlov import evaluate_model, build_model

def train():
    faq = train_model("../data/faq.json")


#train()

def answerQuestion(text, model):
    #faq = build_model("../data/faq.json")
    #while True:
    #    s = input()
    #if s == "exit":
    #    break
    #print(faq([s])[0])
    return model([text])[0]