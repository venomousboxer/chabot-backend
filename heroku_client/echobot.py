"""from deeppavlov import configs, train_model
    from deeppavlov import evaluate_model, build_model
    
    def train():
    faq = train_model("../data/faq.json")
    
    
    #train()
    
    def answerQuestion():
    faq = build_model("../data/faq.json")
    #faq = train_model("../data/faq.json")
    while True:
    s = input()
    if s == "exit":
    break
    print(faq([s])[0])
    #return model([text])[0]
    
    answerQuestion()"""

from deeppavlov.models.tokenizers.spacy_tokenizer import StreamSpacyTokenizer
from deeppavlov.models.sklearn import SklearnComponent
from deeppavlov.dataset_readers.faq_reader import FaqDatasetReader
from deeppavlov.core.data.data_learning_iterator import DataLearningIterator

FAQ_DATASET_URL = "../data/faq.csv"

"""
    List containing all the questions
    """
def answerQuestion(question):
    
    reader = FaqDatasetReader()
    faq_data = reader.read(data_url=FAQ_DATASET_URL, x_col_name='Question', y_col_name='Answer')
    iterator = DataLearningIterator(data=faq_data)
    
    x, y = iterator.get_instances()
    
    tokenizer = StreamSpacyTokenizer(lemmas=True)
    x_tokenized = tokenizer(x)
    
    x_tokens_joined = tokenizer(x_tokenized)
    # fit TF-IDF vectorizer on train FAQ dataset
    vectorizer = SklearnComponent(model_class="sklearn.feature_extraction.text:TfidfVectorizer",
                                  save_path='../model/tfidf.pkl',
                                  infer_method='transform')
    vectorizer.fit(x_tokens_joined)
                                  
                                  # Now collect (x,y) pairs: x_train - vectorized question, y_train - answer from FAQ
    x_train = vectorizer(x_tokens_joined)
    y_train = y
                                  
                                  # Let's use top 2 answers for each incoming questions (top_n param)
    clf = SklearnComponent(model_class="sklearn.linear_model:LogisticRegression",
                                                         top_n=2,
                                                         c=1000,
                                                         penalty='l2',
                                                         save_path='../model/tfidf.pkl',
                                                         infer_method='predict')
    clf.fit(x_train, y_train)
                                  
    test_questions = question
    tokenized_test_questions = tokenizer(test_questions)
    joined_test_q_tokens = tokenizer(tokenized_test_questions)
    test_q_vectorized = vectorizer(joined_test_q_tokens)
    answers = clf(test_q_vectorized)
                                  
    return answers
