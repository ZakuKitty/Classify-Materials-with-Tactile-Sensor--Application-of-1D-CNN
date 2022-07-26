import numpy as np
import joblib
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd

#load data
testdata = np.load('D:\Jupyter\CNN\Test\Data_NPY\cloth.test.npy')

def model_train():
    #load files
    datasets,labels = np.load('D:\Jupyter\CNN\Test\Data_NPY\datasets.npy'),np.load('D:\Jupyter\CNN\Test\Data_NPY\labels.npy')
    # Test train split
    X_train,X_test,y_train,y_test = train_test_split(datasets,labels, test_size=0.2, random_state=0)
    y_train,y_test = y_train.flatten(),y_test.flatten()

    #Model building and training
    clf = SVC(C=0.00368,kernel='rbf',probability=True,decision_function_shape="ovo")
    print("[INFO] Successfully initialize a new model !")
    print("[INFO] Training the model....")
    clt=clf.fit(X_train,y_train)
    print("[INFO] The Model Has Been Trained.")
    joblib.dump(clt,"svm_1.pkl")
    print('[INFO] The model has been saved.')
    acc = clt.score(X_test,y_test)
    print("[INFO] The accuracy of the model is",acc)

# Test selected data
def model_predict(testdata):
    model = joblib.load("D:\Jupyter\CNN\Test\Saved_Models\svm_1.pkl")
    res = model.predict(testdata)
    for x in res:
            if x == 1:
                print('table')
            if x == 2:
                print('cloth')
            if x == 3:
                print('Aluminum')
    prop = model.predict_proba(testdata)
    print(prop)
    return prop

# Execute model and save output
if __name__ == "__main__":
    model_train()
    prediction = model_predict(testdata)
    a = open("D:\Jupyter\CNN\Test\Output\SVM_Output.csv", "a")
    pd.DataFrame(prediction).to_csv("D:\Jupyter\CNN\Test\Output\SVM_Output.csv")