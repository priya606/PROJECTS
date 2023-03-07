# -*- coding: utf-8 -*-
"""classification evaluation metrics(KNN )ML-5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wy_PQDftffAjQpFiI6hsdqFD-hChWhCk
"""

mport numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/Social_Network_Ads.csv')

df.head(10)

df.info()

"""for binary classiication we can use logistic regression


"""

df1=pd.get_dummies(df['Gender'])

df1.head()

df2=pd.concat([df,df1],axis=1)

df2.head()

df2.drop('Gender',axis=1,inplace=True)

df2.head()

x=df2[['User ID','Age','EstimatedSalary','Female','Male']]
y=df2[['Purchased']]

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=5)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(xtrain,ytrain)

y_pred=lr.predict(xtest)
y_pred

df=pd.DataFrame()
df['actual values']=ytest.values.ravel()
df['predicted values']=y_pred

df.head(10)

y_pred_test=lr.predict(xtest)
y_pred_train=lr.predict(xtrain)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytrain,y_pred_train))
print(accuracy_score(ytest,y_pred_test))

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(ytest,y_pred_test)
cm

import itertools
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=30)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    #print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

classes=['purchased','Not purchased']
plt.figure(figsize=(6,6),dpi=70)
plot_confusion_matrix(cm,classes)

from sklearn.metrics import precision_score
print('precision score is:',precision_score(ytest,y_pred_test))

from sklearn.metrics import recall_score
print('recall score is:',recall_score(ytest,y_pred_test))

from sklearn.metrics import f1_score
print('f1_score is:',f1_score(ytest,y_pred_test))

"""####jaccard score gives us ratio of intersection upon union"""

from sklearn.metrics import jaccard_score
print('jaccard_score is:',jaccard_score(ytest,y_pred_test))

"""log_loss(lower the better)
log_score(higher the better it is form of ratio)
"""

from sklearn.metrics import log_loss
print(log_loss(ytest,y_pred_test))

"""##Naive Bayes Classifier """

from sklearn.naive_bayes import GaussianNB
rb_classifier=GaussianNB()
rb_classifier.fit(xtrain,ytrain)

y_pred=rb_classifier.predict(xtest)
print('accuracy_score is:',accuracy_score(ytest,y_pred))

#binary classification(logistic,naive bayes)
#multi class(knn,decision trees,ensemble models)