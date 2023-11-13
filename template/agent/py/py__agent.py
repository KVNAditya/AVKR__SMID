from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
import datetime
import openpyxl

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import VotingClassifier

# Create your views here.
from template.agent.py.models import ClientRegister_Model,Social_Media,detection_ratio,detection_accuracy

def root():
    import os
    try:
        init_isr = os.getcwd().split("\\")
    except:
        init_isr = os.getcwd().split("/")
    isr = ""
    itr_isr_index = 0
    itr_isr = 0

    for itr_molecule in init_isr:
        itr_isr_index = itr_isr_index + 1
        if(itr_molecule == 'Program'):
            break
        for index in range(0,itr_isr_index+1):
            if(index == 0):
                isr = init_isr[index]
            else:
                isr = isr + "/" + init_isr[index]
    return isr

def login(request):


    if request.method == "POST" or 'submit_login' in request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            enter = ClientRegister_Model.objects.get(username=username,password=password)
            request.session["userid"] = enter.id

            return redirect('ViewYourProfile')
        except Exception as e:
            print(e)

    return render(request,'login.html')

def Register1(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        ClientRegister_Model.objects.create(username=username, email=email, password=password, phoneno=phoneno,
                                            country=country, state=state, city=city)

        return render(request, 'Register1.html')
    else:
        return render(request,'Register1.html')

def ViewYourProfile(request):
    userid = request.session['userid']
    obj = ClientRegister_Model.objects.get(id= userid)
    return render(request,'ViewYourProfile.html',{'objects':obj})

def Traverse_DataSets(request):
    if request.method == "POST":
        kword = request.POST.get('keyword')
        if request.method == "POST":
            news = request.POST.get('keyword')

        df_fake = pd.read_csv(root() + "/init__main/db/train_label__false.csv")
        df_true = pd.read_csv(root() + "/init__main/db/train_label__true.csv")
        df_fake.head()
        df_true.head(5)
        df_fake["class"] = 0
        df_true["class"] = 1
        df_fake.shape, df_true.shape
        # Removing last 10 rows for manual testing
        df_fake_manual_testing = df_fake.tail(10)
        for i in range(23480, 23470, -1):
            df_fake.drop([i], axis=0, inplace=True)

        df_true_manual_testing = df_true.tail(10)
        for i in range(21416, 21406, -1):
            df_true.drop([i], axis=0, inplace=True)
            df_fake.shape, df_true.shape
            df_fake_manual_testing["class"] = 0
            df_true_manual_testing["class"] = 1
            df_fake_manual_testing.head(10)
            df_true_manual_testing.head(10)
            df_manual_testing = pd.concat([df_fake_manual_testing, df_true_manual_testing], axis=0)
            df_manual_testing.to_csv(root() + "/init__main/db/test.csv")
            df_merge = pd.concat([df_fake, df_true], axis=0)
            df_merge.head(10)
            df_merge.columns
            df = df_merge.drop(["title", "subject", "date"], axis=1)
            df.isnull().sum()
            df = df.sample(frac=1)
            df.head()
            df.reset_index(inplace=True)
            df.drop(["index"], axis=1, inplace=True)
            df.columns
            df.head()

            def wordopt(text):
                text = text.lower()
                text = re.sub('\[.*?\]', '', text)
                text = re.sub("\\W", " ", text)
                text = re.sub('https?://\S+|www\.\S+', '', text)
                text = re.sub('<.*?>+', '', text)
                text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
                text = re.sub('\n', '', text)
                text = re.sub('\w*\d\w*', '', text)
                return text

        cv = CountVectorizer()
        df["text"] = df["text"].apply(wordopt)
        x = df["text"]
        y = df["class"]

        x = cv.fit_transform(x)

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

        from sklearn.linear_model import LogisticRegression
        print("Testing and Predicting Results----")
        LR = LogisticRegression()
        LR.fit(x_train, y_train)

        News = [news]
        vector1 = cv.transform(News).toarray()
        predict_text = LR.predict(vector1)
        if predict_text == 1:
            val = 'True'
        else:
            val = 'Fake'
        print(val)

        Social_Media.objects.create(News_Data=news,Prediction=val)

        return render(request, 'Traverse_DataSets.html',{'objs': val})
    return render(request, 'Traverse_DataSets.html')