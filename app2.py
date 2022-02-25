# from crypt import methods
# from curses import meta
from unittest.mock import patch
from flask import Flask, request, render_template
import json
import os
import pickle
import csv

from matplotlib.font_manager import json_dump
import ekstraksi
import warnings
warnings.filterwarnings(action='ignore')

app = Flask(__name__)

def visualize():
    pass

@app.route("/", methods=["GET"])
def home():
    keyL = ["jenis", "jumlah"]
    filecount = {key: [] for key in keyL}
    countOK=0
    countNG=0
    data=[]                                                                                         
    datacsv=[]
    jsn = open('data.json')
    filedict = json.load(jsn)

    # print(filedict['file'])
    a=filedict['file']
    b=filedict['prediksi']

  
    for i in b:
        if i=='OK':
            countOK+=1
        else:
            countNG+=1
            
    tmpcsv=['OK',countOK]
    datacsv.append(tmpcsv)
    tmpcsv=['NG',countNG]
    datacsv.append(tmpcsv)
    
    filecount['jenis'].append('OK')
    filecount['jenis'].append('NG')
        
    filecount['jumlah'].append(countOK)
    filecount['jumlah'].append(countNG)
    # with open('datacsv.json', 'w', encoding='UTF8', newline='') as c:
    #     # writer = csv.writer(c)
    #     c.write(json.dumps(filecount))
    # c.close()
    #     # write the header
    #     # writer.writerow(headercsv)

    #     # write multiple rows
    #     # writer.writerows(datacsv)
    
    # data.append(countNG)
    # data.append(countOK)
    data.append(countNG)
    data.append(countOK)
    legend = 'Testing result'
    labels = ["NG", "OK"]
    values = data
    return render_template('dash.html',val=zip(a,b),values=values,labels=labels,legend=legend)

@app.route("/testing", methods=["GET"])
def testing():
    return render_template('testing.html')

@app.route("/predict",methods=['POST'])
def predict():
    keyList = ["file", "prediksi"]
    filetxt = {key: [] for key in keyList}
    
    # soundfile = request.files['soundfile']
    # soundpath = "./sounds/"+soundfile.filename
    # soundfile.save(soundpath)
    
    for soundfile in request.files.getlist('soundfile'):
        soundfile.save("./sounds/"+soundfile.filename)
        print(soundfile)

    # file_sound = soundpath
    #preprocess
    pca_path = './models/pca_2component.pkl'
    scaler_path = './models/scaler_n2.pkl'
    svm_model_path = './models/svm_n2.pkl'

    model_load = pickle.load(open(svm_model_path,'rb'))
    scaler_load = pickle.load(open(scaler_path,'rb'))
    pca_load = pickle.load(open(pca_path,'rb'))
    folderpath = 'sounds/'
    print(folderpath)
    cek = 'Successful! Please Click Dashboard for Detail Information!'
    list_prediction = []
    list_prediction.append(cek)
    for f in os.listdir(folderpath):

        file_wav =ekstraksi.preprocess(os.path.join(folderpath,f))
        r = file_wav.reshape(1,-1)
        pred = model_load.predict(pca_load.transform(scaler_load.transform(r)))
        if pred == 1:
            val = 'OK'
        else:
            val = 'NG'
        temp = f'{f} is {val}'
        
        # list_prediction.append(temp)
        filetxt['file'].append(f)
        filetxt['prediksi'].append(val)
        
        print(temp)
        os.remove(folderpath+f)
        print(filetxt)
    with open('data.json','w') as f:
        f.write(json.dumps(filetxt))
    f.close()
    
    
    return render_template('testing.html',prediction=list_prediction)

@app.route('/predict_folder',methods=['POST'])
def predict_folder():
    path = request.files['folder']

    return render_template('testing.html',prediction=path)
if __name__ == "__main__":
    app.run(debug=True)