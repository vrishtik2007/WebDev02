# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.

st.info("TODO: Add your data loading logic here.")

json_file = "data.json"

# --- Initialize session state if not already present ---
if "data" not in st.session_state:  # ✅ Check first
    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            st.session_state.data = json.load(f)
    

# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Graph 1: Static") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.
st.warning("Placeholder for your first graph.")


# GRAPH 2: DYNAMIC GRAPH
st.subheader("Daily Activity Graph") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.
if "activity_data" not in st.session_state:
    st.session_state.activity_data_data = "activity_data.json"

st.write("""
This graph allows you to interactively adjust the amount of time spent on various daily activities.  
Use the sliders below to modify each activity's value (in minutes).  """)

for i, item in enumerate(st.session_state.data["data_points"]):
    new_value = st.slider( #NEW
        label=item["label"],
        min_value=0,
        max_value=300,
        value=item["value"],
        key= f"slider_{i}"
    )
    st.session_state.data["data_points"][i]["value"] = new_value

df = pd.DataFrame(st.session_state.data["data_points"])

# --- Bar chart ---
st.subheader("Activity Levels")
st.bar_chart(data=df.set_index("label")["value"])

# GRAPH 3: DYNAMIC GRAPH
st.subheader("Graph 3: Dynamic") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.
st.warning("Placeholder for your third graph.")
