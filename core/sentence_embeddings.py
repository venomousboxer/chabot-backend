from InferSent.models import InferSent
import torch
import numpy as np

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

def Start_chatbot():
    model_version = 1
    MODEL_PATH = "../InferSent/encoder/infersent%s.pkl" % model_version
    params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                    'pool_type': 'max', 'dpout_model': 0.0, 'version': model_version}
    model = InferSent(params_model)
    model.load_state_dict(torch.load(MODEL_PATH))

    use_cuda = False
    model = model.cuda() if use_cuda else model

    W2V_PATH = '../data/glove.6B.300d.txt' if model_version == 1 else '../dataset/fastText/crawl-300d-2M.vec'
    model.set_w2v_path(W2V_PATH)

    model.build_vocab_k_words(K=570000)

    dict = {}
    embeddings = {}
    questions = []
    answers = []

    with open('../data/questions.txt') as f:
        content = f.readlines()
    questions = [x.strip() for x in content]

    with open('../data/answers.txt') as f:
        content = f.readlines()
    answers = [x.strip() for x in content]

    for i in range(len(questions)):
        dict[questions[i]] = answers[i]
        embeddings[questions[i]] = model.encode([questions[i]])[0]

    return model, dict, embeddings

def give_similarity_score(u, v, model, embeddings):
    return cosine(embeddings[u], model.encode([v])[0])

#print(give_similarity_score('how are you today?', 'would you tell me how you are today?'))