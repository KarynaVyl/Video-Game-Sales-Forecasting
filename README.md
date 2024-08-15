# Прогнозування Продажів Відеоігор / Video game sales

## Розгорнутий додаток

Ви можете переглянути розгорнутий додаток за наступним посиланням:

[Мій Streamlit додаток](https://Video-Game-Sales-Forecasting.streamlit.app)

## Опис проекту

Цей проект має на меті прогнозування продажів відеоігор у Японії на основі даних про продажі в Північній Америці та Європі, а також інших атрибутів, таких як назва гри, платформа, жанр і видавець. Аналіз зосереджено на побудові моделі для прогнозування і візуалізації результатів. 

## Файли проекту

- vgsales.csv: Дані про продажі відеоігор.
- streamlit_app.py: Основний код Streamlit додатку для візуалізації результатів прогнозування.
- requirements.txt: Перелік необхідних бібліотек Python.
- predicted_sales.csv: Дані про актуальні і прогнозні продажі відеоігр.
- Video games sales report.txt: Звіт за результатами аналізу даних
- video_games_sales.py: Код з машинним навчанням для отримання прогнозів

## Опис функціоналу

1. Завантаження даних: Завантаження даних з файлу vgsales.csv.
   
2. Очищення та обробка даних: Видалення дублікатів, заповнення пропущених значень і кодування категоріальних змінних.

3. Навчання моделі: Використання XGBoost для навчання моделі прогнозування продажів відеоігор.

4. Візуалізація результатів:
   - Кореляційна матриця між продажами в різних регіонах.
   - Топ-10 ігор за прогнозованими продажами, включаючи їх фактичні та прогнозовані продажі.

## Прогнозовані vs фактичні продажі

![Predicted vs Actual Sales](images/predicted%20vs%20actual%20sales.png)

## Топ 10 ігор за прогнозованими продажами

![Top 10 Games Predicted Sales](images/top%2010%20games%20predicted%20sales.png)

----

## Встановлення та налаштування

Щоб запустити цей проект на вашій машині, виконайте наступні кроки:

1. **Клонування репозиторію:**

   ```bash
   git clone https://github.com/KarynaVyl/Video-Game-Sales-Forecasting.git
   cd Video-Game-Sales-Forecasting
   ```
   
2. **Створення і активація віртуального середовища:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Для Windows: .venv\Scripts\activate
   ```

3. **Встановлення необхідних бібліотек:**
Встановіть усі залежності, перелічені у файлі requirements.txt, виконавши:
    ```bash
    pip install -r requirements.txt
    ```
4. **Запуск коду:**

Запустіть Streamlit додаток для перегляду візуалізацій:

    streamlit run streamlit_app.py
