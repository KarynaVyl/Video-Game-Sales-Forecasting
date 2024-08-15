import streamlit as st
import pandas as pd

# Додаємо можливість завантаження файлу
uploaded_file = st.file_uploader("Виберіть файл CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Перегляд перших 10 рядків даних:")
    st.write(df.head(10))  # Виводимо перші 10 рядків даних

    # Візуалізація прогнозованих і фактичних продажів
    st.title('Візуалізація прогнозованих та фактичних продажів відеоігор')
    
    # Графік порівняння прогнозованих і фактичних продажів
    st.subheader('Прогнозовані vs Фактичні продажі (Топ-10 ігор)')
    
    fig = df[['Game_Title', 'Predicted_Sales', 'Actual_Sales']].set_index('Game_Title').plot(kind='bar', figsize=(10, 8)).get_figure()
    st.pyplot(fig)

    # Таблиця з топ-10 іграми
    st.subheader('Таблиця Топ-10 ігор за прогнозованими продажами')
    st.write(df[['Game_Title', 'Predicted_Sales', 'Actual_Sales']])
    
else:
    st.write("Завантажте файл CSV для перегляду даних.")