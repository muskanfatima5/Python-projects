import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "Asia/Dubai",
    "Asia/Tokyo",
    "America/New_York",
    "America/Los_Angeles",
    "Europe/London",
    "Australia/Sydney",
    "Europe/Berlin",
    "Asia/Kolkata"
    ]

st.title("Time Zone Converter App")

selected_time_zone = st.multiselect("Select Time Zones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.subheader("Select Timezones")

for tz in selected_time_zone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    # %I indicate am or pm and %p changes the format to 12 hours from 24 hours

    st.write(f"**{tz}**: {current_time}")



st.subheader("Convert Time between Timezones")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):

    dt = datetime.combine(datetime.today(), current_time,  tzinfo=ZoneInfo(from_tz))

    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    st.success(f"Converted Time in {to_tz}: {converted_time}")
