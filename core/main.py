from sentence_embeddings import give_similarity_score, Start_chatbot


def find_best_response(s, model, dict, embeddings):
    """
    :param s: Input string
    :return: Outputs string
    """
    response = ''
    max_dist = -1

    for x in dict:
        val = give_similarity_score(x, s, model, embeddings)
        if val > max_dist:
            max_dist = val
            response = dict[x]

    return response


flag = 1
model, dict, embeddings = Start_chatbot()
print("Hey! How can I help you today? What do you want to know?")
while flag:
    s = input()
    if s == 'exit':
        break
    print(find_best_response(s, model, dict, embeddings))