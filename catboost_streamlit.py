from datetime import date
import streamlit as st
import pandas as pd
import numpy as np
import catboost
#from catboost import CatBoostRegressor
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
import datetime


st.write('Дата: ', date.today())

st.title('Возможное заболевание сердца')

st.sidebar.header('Введите параметры')

heart = pd.read_csv('e:/programming/samples/heart.csv')

def user_input_features():    
    age = st.sidebar.slider('Возраст: ', min_value=0, max_value=100, value=1 , step=1, format=None)
    st.sidebar.markdown(f'Возраст: {age} лет')

    sex = st.sidebar.selectbox('Выбирете пол: ', heart['sex'].unique())
    if sex == 1:
        st.sidebar.markdown('Пол: мужской')
    if sex == 0:
        st.sidebar.markdown('Пол: женский')

    cp = st.sidebar.selectbox('Боль в груди: ', heart['cp'].unique())
    if cp == 0:
        st.sidebar.markdown('Боль: отсутствует')
    if cp == 1:
        st.sidebar.markdown('Боль: слабая')
    if cp == 2:
        st.sidebar.markdown('Боль: средняя')
    if cp == 3:
        st.sidebar.markdown('Боль: сильная')

    trestbps = st.sidebar.slider('Давление SYS: ', min_value=50, max_value=250, value=None , step=1, format=None)
    st.sidebar.markdown(f'SYS давление: {trestbps} mmHg')

    chol = st.sidebar.slider('Холестерин: ', min_value=60, max_value=500, value=None , step=1, format=None)
    st.sidebar.markdown(f'Холестерин: {chol} mg/dl')

    fbs = st.sidebar.selectbox('Уровень сахара : ', heart['fbs'].unique())
    if fbs == 1:
        st.sidebar.markdown('Содержание сахара больше 120 mg/dl')
    if fbs == 0:
        st.sidebar.markdown('Содержание сахара меньше 120 mg/dl')

    restecg = st.sidebar.selectbox('Кардиограмма в покое: ', heart['restecg'].unique())
    if restecg == 0:
        st.sidebar.markdown('Кардиограмма хорошая')
    if restecg == 1:
        st.sidebar.markdown('Кардиогамма нормальная')
    if restecg == 2:
        st.sidebar.markdown('Кардиограмма плохая')

    thalach = st.sidebar.slider('Пульс: ', min_value=0, max_value=220, value=None , step=1, format=None)
    st.sidebar.markdown(f'Пульс: {thalach} b/min')

    exang = st.sidebar.selectbox('Стенокардия : ', heart['exang'].unique())
    if exang == 1:
        st.sidebar.markdown('Стенокардия')
    if exang == 0:
        st.sidebar.markdown('Отсутствует')
    
    oldpeak = st.sidebar.slider('Депрессия: ', min_value=0, max_value=10, value=None , step=1, format=None)
    st.sidebar.markdown(f'Уровень депрессии: {oldpeak}')
    
    slope = st.sidebar.selectbox('Наклон сегмента кардиограммы ST: ', heart['slope'].unique())
    if slope == 0:
        st.sidebar.markdown('Наклон маленький')
    if slope == 1:
        st.sidebar.markdown('Наклон средний')
    if slope == 2:
        st.sidebar.markdown('Наклон большой')

    ca = st.sidebar.selectbox('Колличество окр. сосудов: ', heart['ca'].unique())
    if ca == 0:
        st.sidebar.markdown('Отсутствуют')
    if ca == 1:
        st.sidebar.markdown('Мало')
    if ca == 2:
        st.sidebar.markdown('Средне')
    if ca == 3:
        st.sidebar.markdown('Много')
    if ca == 4:
        st.sidebar.markdown('Очень много')

    thal = st.sidebar.selectbox('Заболевание: ', heart['thal'].unique())
    if thal == 0:
        st.sidebar.markdown('Нормальный')
    if thal == 1:
        st.sidebar.markdown('Исправленный')
    if thal == 2:
        st.sidebar.markdown('Обратимый')

    data = {'age': age,
            'sex': sex,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            'fbs': fbs,
            'restecg': restecg,
            'thalach': thalach,
            'exang': exang,
            'slope': slope,
            'oldpeak': oldpeak,
            'ca': ca,
            'thal': thal}

    features = pd.DataFrame(data, index=[0])
    return features
df = user_input_features()


#X = np.array(heart)
X = heart.drop('target', axis=1)
y = np.array(heart.target)
#X = heart.data
#y = heart.target

X_train, X_validation, y_train, y_validation = train_test_split(X, y, train_size=0.7, random_state=17)
X_train.shape, X_validation.shape

cbr = CatBoostClassifier()
cbr.fit(X_train, y_train)
#cbr.fit(X, y)

prediction = cbr.predict(X_validation)

prediction_proba = cbr.predict_proba(df)

st.subheader(f'Прогноз: {prediction_proba}')

#st.balloons()
