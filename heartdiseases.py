import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
class Predictor:

    def has_disease(self, row):
        self.train(self)
        return True if self.predict(self, row) == 1 else False

    @staticmethod
    def train(self):
        df = pd.read_csv('dataset.csv')
        dataset = df
        self.standardScaler = StandardScaler()
        columns_to_scale = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak',
                            'slope', 'ca', 'thal']
        dataset[columns_to_scale] = self.standardScaler.fit_transform(dataset[columns_to_scale])
        y = dataset['target']
        X = dataset.drop(['target'], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
        self.knn_classifier = KNeighborsClassifier(n_neighbors=8)
        self.knn_classifier.fit(X, y)
        score = self.knn_classifier.score(X_test, y_test)
        print('--Training Dataset Complete--')
        print('Score: ' + str(score))

    @staticmethod
    def predict(self, row):
        user_df = np.array(row).reshape(1, 13)
        user_df = self.standardScaler.transform(user_df)
        predicted = self.knn_classifier.predict(user_df)
        print("Predicted: " + str(predicted[0]))
        return predicted[0]


#row = [[37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2]]
# row = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# col = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
# for i in range(0, 13):
#     row[0][i] = input(f"Enter {col[i]} : ")  # OverWriting the List


la=str()
def onClick():
    row=[[age.get(),gender.get(),cp.get(),tbps.get(),chol.get(),fbs.get(),restecg.get(),thalach.get(),exang.get(),oldpeak.get(),slope.get(),ca.get(),thal.get()]]
    print(row)
    predictor = Predictor()
    o = predictor.has_disease(row)
    root2 = tk.Tk()
    root2.title("Prediction Window")
    if (o == True):
        print("Person Have Heart Disease")
        la="Person has a high chance of having a Heart Disease"
        tk.Label(root2, text=la, font=("times new roman", 20), fg="white", bg="maroon", height=2).grid(row=15, column=1)
    else:
        print("Person has a low chance of having a Heart Disease")
        la="Person has a low chance of having a Heart Disease"
        tk.Label(root2, text=la, font=("times new roman", 20), fg="white", bg="green", height=2).grid(row=15, column=1)

    return True
root = tk.Tk()
root.geometry("2000x600")
root.title("Heart Disease Predictor")
root.configure(bg='white')

# Force high-contrast widget colors (macOS dark mode can invert defaults).
root.option_add("*Label.Background", "white")
root.option_add("*Label.Foreground", "black")
root.option_add("*Radiobutton.Background", "white")
root.option_add("*Radiobutton.Foreground", "black")
root.option_add("*Entry.Background", "white")
root.option_add("*Entry.Foreground", "black")
root.option_add("*Entry.InsertBackground", "black")
root.option_add("*Button.Background", "white")
root.option_add("*Button.Foreground", "black")

# Load via Pillow because the file has JPEG data with a .png extension.
bg_image = Image.open("s1.jpeg")
bg_image = bg_image.resize((840, 520), Image.Resampling.LANCZOS)
bg = ImageTk.PhotoImage(bg_image)
  
# Show image using label
label5 = Label( root, image = bg)
# label5.resize((100,100),Image.ANTIALIAS)
label5.place(x = 560, y = 100)
# label. 
tk.Label(root,text="""Fill your Details""",font=("times new roman", 12),bg = "white").grid(row=0)

tk.Label(root,text='Age',padx=20, font=("times new roman", 12),bg = "white").grid(row=1,column=0)
age = tk.IntVar()
tk.Entry(root,textvariable=age).grid(row=1,column=1)

tk.Label(root,text="""Sex""",padx=20, font=("times new roman", 12),bg = "white").grid(row=2,column=0)
gender = tk.IntVar()
tk.Radiobutton(root,text="Male",padx=20,variable=gender,value=1,bg = "white").grid(row=2,column=1)
tk.Radiobutton(root,text="Female ",padx=20,variable=gender,value=0,bg = "white").grid(row=2,column=2)

tk.Label(root,text='Chest pain type (0-3)', font=("times new roman", 12),bg = "white").grid(row=3,column=0)
cp = tk.IntVar()
tk.Entry(root,textvariable=cp).grid(row=3,column=1)

tk.Label(root,text='Resting blood pressure', font=("times new roman", 12),bg = "white").grid(row=4,column=0)
tbps = tk.IntVar()
tk.Entry(root,textvariable=tbps).grid(row=4,column=1)

tk.Label(root,text='Cholestoral (mg/dl)', font=("times new roman", 12),bg = "white").grid(row=5,column=0)
chol = tk.IntVar()
tk.Entry(root,textvariable=chol).grid(row=5,column=1)

tk.Label(root,text="""Blood sugar > 120(mg/dl)""",padx=20, font=("times new roman", 12),bg = "white").grid(row=6,column=0)
fbs=tk.IntVar()
tk.Radiobutton(root,text="True",padx=20,variable=fbs,value=1,bg = "white").grid(row=6,column=1)
tk.Radiobutton(root,text="False",padx=20,variable=fbs,value=0,bg = "white").grid(row=6,column=2)

tk.Label(root,text="""Resting Electrocardiographic""",padx=20, font=("times new roman", 12),bg = "white").grid(row=7,column=0)
restecg=tk.IntVar()
tk.Radiobutton(root,text="0",padx=20,variable=restecg,value=0,bg = "white").grid(row=7,column=1)
tk.Radiobutton(root,text="1",padx=20,variable=restecg,value=1,bg = "white").grid(row=7,column=2)
tk.Radiobutton(root,text="2",padx=20,variable=restecg,value=2,bg = "white").grid(row=7,column=3)

tk.Label(root,text='Max Heart rate', font=("times new roman", 12),bg = "white").grid(row=8,column=0)
thalach = tk.IntVar()
tk.Entry(root,textvariable=thalach).grid(row=8,column=1)

tk.Label(root,text="""Pain during exercise""",padx=20, font=("times new roman", 12),bg = "white").grid(row=9,column=0)
exang=tk.IntVar()
tk.Radiobutton(root,text="Yes",padx=20,variable=exang,value=1,bg = "white").grid(row=9,column=1)
tk.Radiobutton(root,text="No",padx=20,variable=exang,value=0,bg = "white").grid(row=9,column=2)

tk.Label(root,text='ECG entry rate', font=("times new roman", 12),bg = "white").grid(row=10,column=0)
oldpeak = tk.DoubleVar()
tk.Entry(root,textvariable=oldpeak).grid(row=10,column=1)

tk.Label(root,text="""ECG peak""",padx=20, font=("times new roman", 12),bg = "white").grid(row=11,column=0)
slope=tk.IntVar()
tk.Radiobutton(root,text="upsloping",padx=20,variable=slope,value=0,bg = "white").grid(row=11,column=1)
tk.Radiobutton(root,text="flat",padx=20,variable=slope,value=1,bg = "white").grid(row=11,column=2)
tk.Radiobutton(root,text="downsloping",padx=20,variable=slope,value=2,bg = "white").grid(row=11,column=3)

tk.Label(root,text="""vessels colored by flourosop""",padx=20, font=("times new roman", 12),bg = "white").grid(row=12,column=0)
ca=tk.IntVar()
tk.Radiobutton(root,text="0",padx=20,variable=ca,value=0,bg = "white").grid(row=12,column=1)
tk.Radiobutton(root,text="1",padx=20,variable=ca,value=1,bg = "white").grid(row=12,column=2)
tk.Radiobutton(root,text="2",padx=20,variable=ca,value=2,bg = "white").grid(row=12,column=3)
tk.Radiobutton(root,text="3",padx=20,variable=ca,value=3,bg = "white").grid(row=12,column=4)

tk.Label(root,text="""Thalassemia""",padx=20, font=("times new roman", 12),bg = "white").grid(row=13,column=0)
thal=tk.IntVar()
tk.Radiobutton(root,text="0",padx=20,variable=thal,value=0,bg = "white").grid(row=13,column=1)
tk.Radiobutton(root,text="1",padx=20,variable=thal,value=1,bg = "white").grid(row=13,column=2)
tk.Radiobutton(root,text="2",padx=20,variable=thal,value=2,bg = "white").grid(row=13,column=3)
tk.Radiobutton(root,text="3",padx=20,variable=thal,value=3,bg = "white").grid(row=13,column=4)

tk.Label(root,text="""Heart Disease Prediction""",font=("Agency FB", 40),bg = "white").grid(row=0,column=6)

tk.Button(root, text='Predict', command=onClick,bg = "white").grid(row=14, column=2, sticky=tk.W, pady=4)

# tk.Label(root,text="""Heart Disease Prediction""",font=("times new roman", 30),bg = "white").grid(row=30)

root.mainloop()
