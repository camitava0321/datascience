from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import csv
import re
import itertools
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC, LinearSVC
from sklearn.pipeline import Pipeline
import pickle as cPickle
import os
import sys
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split,GridSearchCV
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix


# https://stackoverflow.com/questions/18395952/how-to-load-csv-data-in-scikit-and-using-it-for-naive-bayes-classification

#mdlFile= '../../model/test_model.pkl'
mdlFile= 'test_model.pkl'
#catVarfile = open('../../data/Category_variation.csv',errors="backslashreplace")
catVarfile = open('Category_variation.csv')
catVarfileDf = pd.read_csv(catVarfile, sep=',', quoting=csv.QUOTE_MINIMAL)
catVarfileDf = catVarfileDf.fillna('')  

#dicfile = open('../../data/Element_dictionary.csv',errors="backslashreplace")
dicfile = open('Element_dictionary.csv')
dicfileData = pd.read_csv(dicfile, sep=',', quoting=csv.QUOTE_MINIMAL)
dicfileData = dicfileData.fillna('')



def get_msg_lable_train(train_df):
    data1=[]
    data2=[]
    for index, row in train_df.iterrows():
        for i in range(len(row)):
            i=i+1
            if i < len(row):
                v = row[i]
                if isBlank(v) == False:
                    data1.append(row[0])
                    data2.append(v)
                    
    print("lable_train="+str(data1))
    print("msg_train="+str(data2))
    return data1, data2
#query_element


def train_model(csvTrainFile):
#    file_train = open(csvTrainFile,errors="backslashreplace")
    file_train = open(csvTrainFile)
    train_df = pd.read_csv(file_train, sep=',', quoting=csv.QUOTE_MINIMAL)
    train_df=train_df.fillna('')
    
    #msg_train=text_varient(train_df)
    label_train,msg_train=get_msg_lable_train(train_df)
    
    df = pd.DataFrame()
    df['msg'] = msg_train
    df['label'] = label_train
    
    train_df_temp, test_df_temp = train_test_split(df, test_size=0.2)
    
    msg_train_temp = train_df_temp['msg'] #Text varient
    #print(len(msg_train_temp))
    msg_test_temp = test_df_temp['msg'] #Text varient
    
    
    label_train_temp = train_df_temp['label'] #Query Element
    label_test_temp = test_df_temp['label'] #Query Element

    
    #print (len(msg_train_temp), len(msg_test_temp), len(msg_train_temp) + len(msg_test_temp))
    vectorizer = TfidfVectorizer(sublinear_tf=True,stop_words=None, ngram_range=(1,3))
    clf=SVC(C=1000,kernel='rbf',gamma=1,probability=True)
    #print(clf)
    pipeline_svm = Pipeline([
    ('tfidf', vectorizer),
    ('classifier', clf)  # <== change here
    ])
    
    #svm_detector = pipeline_svm.fit(msg_train, label_train)
    
    svm_detector = pipeline_svm.fit(msg_train_temp, label_train_temp)
    svm_predictions = svm_detector.predict(msg_test_temp)
    score1 = accuracy_score(label_test_temp, svm_predictions)
    print("accuracy:   %0.3f" % score1)
    print (confusion_matrix(label_test_temp, svm_predictions))
    print (classification_report(label_test_temp, svm_predictions))
    svm_detector = pipeline_svm.fit(msg_train, label_train)
    
    
    return svm_detector
#train_model    

'''
def cheer_up(times:int):
    for i in range(1 , times+1):
        print("you will become a good progremmer"+str(i)+'!')

sadness=input("Enter 1-10 how sadness you are")    
cheer_up(int(sadness))
'''

def category_varient_map():
    hashParCom={}
    value_qry_element = catVarfileDf['QueryElement']
    for text in value_qry_element:
        words = re.findall(r'(\w+)', text)
        hashmp={};
        lst = []
        for word in words:
            v = [];        
            for index, row in dicfileData.iterrows():
                if (row['Words'].lower() == word.lower()):
                    v.append(row['Variation'])           
            hashmp[word]=v
            lst.append(v);
            #for
        #for            
        pc = list(itertools.product(*lst))
        #print(pc)
        hashParCom[text.strip()]=make_sentenses(pc);
    #for    
    return  hashParCom
#category_varient_map

  
def make_sentenses(lst):
    sentences = [];
    for ar in lst:
        sentence = ""
        for word in ar:
            sentence = sentence+" "+word
        #for
        sentences.append(sentence.strip());
    #for
    return sentences

def create_training_file(csvFile):
    mp = category_varient_map()
    
       
    traindat=[]
    for index, row in catVarfileDf.iterrows():
        rowLength = len(row)
        data =[];
        for i in range(rowLength):
            val=row[i].strip()
            if isBlank(val) == False:
                data.append(val)
            mpVal = mp.get(row[i].strip());
            if mpVal is not None:
                data.extend(mpVal)
        traindat.append(data)
    #for
        
    df=pd.DataFrame(traindat)
    #print(df)
    df.to_csv(csvFile, encoding='utf-8', index=False,  header=True)
    
#create_training_file

def save_model(svm_detector):
    with open(mdlFile, 'wb') as fout:
        cPickle.dump(svm_detector, fout)
#save_model

def load_model():
    detector_reloaded = cPickle.load(open(mdlFile,'rb'))
    return detector_reloaded 
#load_model


def isBlank (myString):
    return not (myString and myString.strip())
#isBlank
 
def lookup_hash():
    
    hsmp = {}
    
    lookupFilePath='../../data/Looup_file.xlsx'
    lookupFile = open(lookupFilePath,errors="backslashreplace")
    lookupData = pd.read_csv(lookupFile, sep=',', quoting=csv.QUOTE_MINIMAL)
    lookupData = lookupData.fillna('')
    
    for index, row in lookupData.iterrows():
        hsmp={row['Obj. name']:row['Long Field Label']}
  
    

#lookup_hash
  
def main():
    
    
    argvs = sys.argv[1:]
    
    
    if argvs[0] == "train" :
    
        #csvTrainFile='../../data/training_data.csv'
        csvTrainFile='training_data.csv'
        create_training_file(csvTrainFile)
        detector = train_model(csvTrainFile)
        save_model(detector)
  
    if argvs[0] == "test"  or argvs[1] == "test" :
        detector = load_model()
        
        #label_test = list of "QUERY ELEMENT" of "input query file"
        
        msg_text = ['prc odr', 'purch Ord']
        
        #print("Input:  " + str(msg_text))
        predictions = detector.predict(msg_text)
        print("Prediction:  " + str(predictions))
        
        prob_pos = detector.predict_proba(msg_text)
        print(prob_pos)
        index = 0
        for text in msg_text:
            print("Input : "+text)
            print("Prediction : "+predictions[index])
            score = prob_pos[index]
            #print(score)
            #print ('Predict confidence scores :', max(score))
            confidence_score = (max(score)*100)
            confidence_score = round(confidence_score,2)
            print("Confidance Score : "+str(confidence_score)) 
            index+=1
        
        #score = accuracy_score(label_test, predictions)
        #print("accuracy:   %0.3f" % score)

if __name__ == "__main__":
    main()        



