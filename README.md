# icts-chatbot
Chat bot for ICTS-LMS

# How to run
1. Clone the repository
2. In the root direcotry download following two files:

   a) glove.6B from https://nlp.stanford.edu/projects/glove/ and add glove.6B.300d.txt to the root directory.
   
   b) clone this repository in the root directory [https://github.com/facebookresearch/InferSent]. Go into InferSent/models.py and edit the function "build_vocab_k_words" on line 144. Comment the line "print('Vocab size : %s' % (K))".
   
   c) In your browser, [https://s3.amazonaws.com/senteval/infersent/infersent1.pkl] go to this link to download infersent1.pkl, then add the file in /InferSent/encoder/ 
   
3. run main.py 

4. Write any question on the console and wait for the answer by the chatbot. In case the answer given by chatbot is not good and satisfiable, "exit" the program and write the required question and answer respectively in the "questions.txt" and "answers.txt".

5. Then run again and test. Keep doing till good results come. Try different questions.

# To run and train DeepPavlov
1. Clone the repository
2. Install deeppeavlov -> pip install deeppavlov
3. Create an empty /models folder in the root directory
4. For any changes in question answer dataset, make them in /data/faq.csv
5. For any changes in the loss function and model changes, make them in /data/faq.json
6. First you will need to train the chatbot, for that uncomment line#8 in /core/runDeepPavlov.py and comment everything below that.
7. For testing the chatbot, comment line#8 in /core/runDeepPavlov.py and uncomment everything below it.
8. Type in a question in the console and press enter for the answer.
9. Type "exit" for quitting the chatbot.
