# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.
import altair as alt
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


#st.header("Load Data")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.


json_file = "data.json"

if "data" not in st.session_state:  
    try:
        with open(json_file, "r") as f:
            st.session_state.data = json.load(f)
    except FileNotFoundError:
        st.session_state.data = {
            "activity_data":{
                "chart_title": "Activity Data",
                "data_points": [
                    {"label": "Walking", "value": 50},
                    {"label": "Reading", "value": 30},
                    {"label": "Coding", "value": 100},
                    {"label": "Exercise","value": 80},
                    {"label": "Cooking","value": 45},
                    {"label": "Gaming","value": 90},
                    {"label": "Meditation","value": 20}
                ]
            },
            "expenses_data":{
                "chart_title": "Weekly Expenses ($)",
                "data_points": [
                    {"label": "Groceries", "value": 60},
                    {"label": "Transport", "value": 25},
                    {"label": "Entertainment", "value": 40},
                    {"label": "Dining", "value": 50},
                    {"label": "Misc", "value": 20}
                ]
        }	    
}
with open(json_file, "w") as f:
    json.dump(st.session_state.data, f)    

# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Ice Cream Flavor Ratings")
st.write("""
This graph allows you to view the ratings(1-10) of different ice cream flavors on a scatter plot   
 """)
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    ice_cream_df = pd.read_csv('data.csv', names=["Flavor","Rating"])
    st.dataframe(ice_cream_df)
    st.subheader("Average Ice Cream Flavor Ratings")
    scatter= alt.Chart(ice_cream_df).mark_circle().encode(
        x="Flavor",
        y="Rating",
    )
    st.altair_chart(scatter)
    
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")


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

for i, item in enumerate(st.session_state.data["activity_data"]["data_points"]):
    new_value = st.slider( #NEW
        label=item["label"],
        min_value=0,
        max_value=300,
        value=item["value"],
        key= f"slider_{i}"
    )
    st.session_state.data["activity_data"]["data_points"][i]["value"] = new_value

df = pd.DataFrame(st.session_state.data["activity_data"]["data_points"])

st.subheader("Activity Levels")
st.bar_chart(data=df.set_index("label")["value"])

# GRAPH 3: DYNAMIC GRAPH
st.subheader("Weekly Expenses")
st.write("""
This graph allows you to interactively adjust the amount of money spent on various daily activites.  
Use the sliders and dropdown below to modify each activity's value (in dollars).  """)
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.

expense_labels=[item["label"] for item in st.session_state.data["expenses_data"]["data_points"]]
selected_expense = st.selectbox("Choose an expense to visualize", expense_labels)#NEW
for i, item in enumerate(st.session_state.data["expenses_data"]["data_points"]):
   if item["label"] == selected_expense:#NEW
       new_value= st.slider(
        f"Adjust value for {item['label']}", 0,200, item["value"], key=f"expense_slider_{i}"
        )
       st.session_state.data["expenses_data"]["data_points"][i]["value"] = new_value
                
   

df_expenses= pd.DataFrame(st.session_state.data["expenses_data"]["data_points"])
st.line_chart(df_expenses.set_index("label")["value"])

