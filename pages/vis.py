import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Visionary')

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
uploaded = st.file_uploader(label='Загрузите свой датасет в формате csv для исследования', type='csv')
if uploaded is not None:
    data = pd.read_csv(uploaded)
else:
    data = pd.read_csv(path)

st.header(body='Изначальный датафрейм')
st.dataframe(data=data)

st.header(body='Проверяем датафрейм на наличие пропусков и очищаем если надо...')
missed = data.isna().sum()
missed = missed[missed > 0]
if len(missed) == 0:
    st.write('В изначальном датафрейме нет пропусков, правки не понадобились c:')
else:
    for col in data.columns:
        if data[col].dtype == 'object': #Категориальные признаки
            data[col] = data[col].fillna(data[col].mode()[0])
        else:
            data[col] = data[col].fillna(data[col].mean())
    st.write('Заменили пропуски в файле с:')
    st.download_button(label='Скачать готовый CSV файл', data=data.to_csv(), file_name='data.csv')


st.header(body='Что будем делать с данными?')

graphics=('area', 'bar', 'line', 'scatter')
cols = data.columns.tolist()
cols.append('Проверить частоту')

col1, col2, col3 = st.columns(3)

graphic = col1.selectbox(label='Выбери тип графика', options=graphics, index=3)
x = col2.selectbox(label='Что будем показывать по оси Х?', options=cols[:-1], index=0)
y = col3.selectbox(label='Что будем показывать по оси У?', options=cols, index=1)


if y == 'Проверить частоту':
    # Если X числовой — строим гистограмму частот (как в seaborn.histplot)
    if pd.api.types.is_numeric_dtype(data[x]):
        fig, ax = plt.subplots()
        ax.hist(data[x].dropna(), bins=20)
        ax.set_xlabel(x)
        ax.set_ylabel('Частота')
        st.pyplot(fig)
    else:
        # Если X категориальный — считаем value_counts и рисуем столбчатую диаграмму частот
        freq = data[x].value_counts(dropna=False).reset_index()
        freq.columns = [x, 'count']
        st.bar_chart(freq, x=x, y='count')
else:
    if graphic == 'area':
        st.area_chart(data=data, x=x, y=y)
    elif graphic == 'bar':
        st.bar_chart(data=data, x=x, y=y)
    elif graphic == 'line':
        st.line_chart(data=data, x=x, y=y)
    elif graphic == 'scatter':
        st.scatter_chart(data=data, x=x, y=y)



