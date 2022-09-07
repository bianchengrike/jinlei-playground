from sklearn.datasets import load_breast_cancer

breast_cancer=load_breast_cancer()
x=breast_cancer.data
y=breast_cancer.target

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=33,test_size=0.3)

from sklearn.preprocessing import StandardScaler

breast_cancer_ss=StandardScaler()

x_train=breast_cancer_ss.fit_transform(x_train)
x_test=breast_cancer_ss.transform(x_test)

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()
lr.fit(x_train,y_train)
lr_y_predict=lr.predict(x_test)

from sklearn.metrics import classification_report

print ('Accuracy:',lr.score(x_test,y_test))
print(classification_report(y_test,lr_y_predict,target_names=['benign','malignant']))
