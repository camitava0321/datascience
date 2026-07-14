import pandas as pd
import string
import re
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


stopwords = nltk.corpus.stopwords.words('english')

# Remove usernames starting with @
def remove_username(text):
    no_name = re.sub('@[^\s]+', '', text)
    return no_name

# Remove numbers
def remove_number(text):
    no_number = re.sub(r'[0-9]+', '', text)
    return no_number

# Remove punctuation
def remove_punctuation(text):
    no_punctuation=[letter for letter in text if letter not in string.punctuation]
    no_punctuation=''.join(no_punctuation)
    return no_punctuation

# Tokenize and lower case words
def tokenize_lower(text):
    token = re.split("\W+",text)
    token = [word.lower() for word in token]
    return token

# Remove stopwords
def remove_stopwords(text):
    no_stopword = [word for word in text if word not in stopwords and word != '']
    return no_stopword

# Lemmatize the words
def lemmatize_words(text):
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word, 'v') for word in text]
    return lemmatized

# Remove emoji
# def remove_emoji(text):
#     pattern = re.compile(
#         "["
#             u"\U0001F600-\U0001F64F"  # emoticons
#             u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#             u"\U0001F680-\U0001F6FF"  # transport & map symbols
#             u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#         "]+",
#         flags=re.UNICODE
#     )
#     no_emoji = pattern.sub(r'', text)
#     return no_emoji

# Clean text
def clean_text(text):
    result = remove_username(text)
    result = remove_number(result)
    result = remove_punctuation(result)
    result = tokenize_lower(result)
    result = remove_stopwords(result)
    result = lemmatize_words(result)
    # result = remove_emoji(result)
    result = ' '.join(result)
    return result

def prepare_input_text(input_text, tokenizer):
    input_text = pd.DataFrame({'input_text': [input_text]})
    input_text['input_text'] = input_text['input_text'].apply(clean_text)
    seq_input_text = tokenizer.texts_to_sequences(input_text['input_text'])
    pad_input_text = pad_sequences(seq_input_text)
    return pad_input_text

def invoke_prediction(input_text, model, classes: list):
    result = model.predict(input_text, verbose=False)
    result = result.tolist()[0]
    result = [round(r,2) for r in result]
    emotion = classes[result.index(max(result))]
    return emotion, result

def predict_text_emotion(input_text, tokenizer, model, classes: list, prepare_input=True):
    if prepare_input == True:
        input_text = prepare_input_text(input_text, tokenizer)
    emotion, result = invoke_prediction(input_text, model, classes)
    return emotion, result
