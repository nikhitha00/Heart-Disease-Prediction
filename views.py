# Heart-Disease-Prediction

def heart(request):
    if(request.method=="POST"):
        data=request.POST
        BMI=data.get('textBMI')
        Smoking=data.get('textSmoking')
        AlcoholDrinking=data.get('textAlcoholDrinking')
        stroke=data.get('textStroke')
        physicalhealth =data.get('textPhysicalHealth')
        Mentalhealth=data.get('textMentalHealth')
        Diffwalking=data.get('textDiffWalking')
        Sex=data.get('textSex')
        Agecategory=data.get('textAgeCategory')
        Race=data.get('textRace')
        Diabetic=data.get('textDiabetic')
        PhysicalActivity=data.get('textPhysicalActivity')
        GenHealth=data.get('textGenHealth')
        Sleeptime=data.get('textSleepTime')
        Asthma=data.get('textAsthma')
        KidneyDisease=data.get('textKidneyDisease')
        SkinCancer=data.get('textSkinCancer')
        if('buttonpredict' in request.POST):
            import pandas as pd
            path="C:\\Users\\nikhi\\OneDrive\\Desktop\\Data\\Data\\heart_disease.csv"
            data=pd.read_csv(path)
            import sklearn
            from sklearn.preprocessing import LabelEncoder
            le_Smoking=LabelEncoder()
            le_HeartDisease=LabelEncoder()
            le_AlcoholDrinking=LabelEncoder()
            le_Stroke=LabelEncoder()
            le_DiffWalking=LabelEncoder()
            le_Sex=LabelEncoder()
            le_AgeCategory=LabelEncoder()
            le_Race=LabelEncoder()
            le_Diabetic=LabelEncoder()
            le_PhysicalActivity=LabelEncoder()
            le_GenHealth=LabelEncoder()
            le_KidneyDisease=LabelEncoder()
            le_SkinCancer=LabelEncoder()
            data['Smoking_n']=le_Smoking.fit_transform(data['Smoking'])
            data['HeartDisease_n']=le_HeartDisease.fit_transform(data['HeartDisease'])
            data['AlcoholDrinking_n']=le_AlcoholDrinking.fit_transform(data['AlcoholDrinking'])
            data['Stroke_n']=le_Stroke.fit_transform(data['Stroke'])
            data['DiffWalking_n']=le_DiffWalking.fit_transform(data['DiffWalking'])
            data['Sex_n']=le_Sex.fit_transform(data['Sex'])
            data['AgeCategory_n']=le_AgeCategory.fit_transform(data['AgeCategory'])
            data['Race_n']=le_Race.fit_transform(data['Race'])
            data['Diabetic_n']=le_Diabetic.fit_transform(data['Diabetic'])
            data['PhysicalActivity_n']=le_PhysicalActivity.fit_transform(data['PhysicalActivity'])
            data['GenHealth_n']=le_GenHealth.fit_transform(data['GenHealth'])
            data['KidneyDisease_n']=le_KidneyDisease.fit_transform(data['KidneyDisease'])
            data['SkinCancer_n']=le_SkinCancer.fit_transform(data['SkinCancer'])
            inputs=data.drop(['HeartDisease','HeartDisease_n','Smoking','AlcoholDrinking','Stroke','DiffWalking','Sex','AgeCategory','Race','GenHealth','Diabetic','KidneyDisease','SkinCancer','PhysicalActivity','Asthma'],axis=1)
            output=data.drop(['BMI','Smoking','HeartDisease','AlcoholDrinking','Stroke','PhysicalHealth','MentalHealth','DiffWalking','Sex','AgeCategory','Stroke_n','DiffWalking_n','Sex_n','AgeCategory_n','Race_n','Diabetic_n','PhysicalActivity_n','GenHealth_n','KidneyDisease_n','SkinCancer_n','Race','Diabetic','PhysicalActivity','GenHealth','SleepTime','Asthma','KidneyDisease','SkinCancer','Smoking_n','AlcoholDrinking_n'],axis=1)
            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
            import sklearn
            from sklearn.linear_model import LogisticRegression
            model=LogisticRegression()
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            result=model.predict([[25.66,15,15,8,0,0,1,1,1,11,5,0,1,2,0,0]])
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            return render(request,'heart.html',context={'result':"heart="+str(result[0])})
    return render(request,'heart.html')
