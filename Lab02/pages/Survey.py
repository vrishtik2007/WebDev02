# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).
import altair as alt
# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Ice Cream Flavor Ratings")
st.write("Please rate the ice cream flavors(1-10)")
if st.button("Clear all submissions"):
    open("data.csv", "w").close()  
    st.session_state.submitted_data = []

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    flavor_input = st.text_input("Flavor:")
    rating_input = st.text_input("Rating(1-10):")

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        try:
            rating_num=int(rating_input)
        except ValueError:
            rating_num=None
        # --- YOUR LOGIC GOES HERE ---
        # TO DO:
        # 1. Create a new row of data from 'category_input' and 'value_input'.
        # 2. Append this new row to the 'data.csv' file.
        #    - You can use pandas or Python's built-in 'csv' module.
        #    - Make sure to open the file in 'append' mode ('a').
        #    - Don't forget to add a newline character '\n' at the end.
        if rating_num is not None:
            if 1 <= rating_num <= 10:  
                new_row = [flavor_input, rating_num]
                with open("data.csv", "a") as file:
                    file.write(f"{new_row[0]},{new_row[1]}\n")
                st.success("Your data has been submitted!")
                st.write(f"You entered: **Flavor:** {flavor_input}, **Rating:** {rating_input}")
            else:
                st.error("Rating must be between 1 and 10.")


# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
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
