from django.shortcuts import render




# Create your views here.
def Orbit(request):
    if request.method == "POST":
        data = request.POST
        NEO_flag = data.get('textNEO_flag')
        One_km_NEO_flag = data.get('textOne_km_NEO_flag')
        PHA_flag = data.get('textPHA_flag')
        H = data.get('textH')
        G = data.get('textG')
        Num_obs = data.get('textNum_obs')
        rms = data.get('textrms')
        U = data.get('textU')
        Epoch = data.get('textEpoch')
        Peri = data.get('textPeri')
        Node = data.get('textNode')
        M = data.get('textM')
        i = data.get('texti')
        e = data.get('texte')
        a = data.get('texta')
        n = data.get('textn')
        Num_opps = data.get('textNum_opps')
        Tp = data.get('textTp')
        Orbital_period = data.get('textOrbital_period')
        Perihelion_dist = data.get('textPerihelion_dist')
        Aphelion_dist = data.get('textAphelion_dist')
        Semilatus_rectum = data.get('textSemilatus_rectum')
        Synodic_period = data.get('textSynodic_period')
        if('buttonsubmit' in request.POST):
            import pandas as pd
            path="C:\\Users\\Acer\\Downloads\\2023_projects\\8_orbittype\\train_dataset.csv"
            data=pd.read_csv(path)
            print(data)
            print(data.info())
            data.describe()
            data.head()
            data.shape
            
            inputs = data.drop(['Orbit_type'],axis=1)
            output = data['Orbit_type']
            print(inputs)
            print(output)
           
            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,test_size=0.8,random_state=20)
            x_train.shape

            from sklearn.preprocessing import StandardScaler
            sc=StandardScaler()
            x_train=sc.fit_transform(x_train)
            x_test=sc.transform(x_test)
             
            from sklearn.ensemble import RandomForestClassifier
            model=RandomForestClassifier(n_estimators=200,random_state=20)
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            print(y_pred)
            print(y_test)

            from sklearn.metrics import confusion_matrix
            cm=confusion_matrix(y_test,y_pred)
            print(cm)

            from sklearn.metrics import accuracy_score
            acc=accuracy_score(y_test,y_pred)*100
            print("accuracy"+str(),acc)

            result=model.predict([[NEO_flag,One_km_NEO_flag,PHA_flag,H,G,Num_obs,rms,U,Epoch,M,Peri,Node,i,e,n,a,Num_opps,Tp,Orbital_period,Perihelion_dist,Aphelion_dist,Semilatus_rectum,Synodic_period]])
            print(result)
            
            
            return render(request, 'Orbit.html', context={'result': result})
    return render(request, 'Orbit.html')

             

def Home(request):
     return render(request,'Home.html')