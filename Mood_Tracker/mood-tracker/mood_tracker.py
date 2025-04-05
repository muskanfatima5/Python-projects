import streamlit as st # For web interface
import pandas as pd # For data manipulation
import datetime # For date and time handling
import csv # For reading and writing CSV file
import os # For file operations

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE)

def save_mood_data(date, mood):
    with open(MOOD_FILE, "a") as file:

        writer = csv.writer(file)
        writer.writerow([date, mood])


st.title("Mood Tracker")
today = datetime.date.today()

st.subheader("How are you feeling Today?")
mood = st.selectbox("Select your mood:", ["Happy", "Sad", "Neutral", "Angry", "Excited", "Bored", "Stressed"])

if st.button("Save Mood"):
    save_mood_data(today, mood)
    st.success(f"Mood '{mood}' saved for {today} sucessfuly!")


data = load_mood_data()
if not data.empty:

    st.subheader("Mood Trends Over Time")

    data["Date"] = pd.to_datetime(data["Date"])
    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)




