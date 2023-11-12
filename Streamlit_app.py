import streamlit

streamlit.title('My parent Lunch plan')

streamlit.header ('Lunch menu')
streamlit.text('Dal & Rice')
streamlit.text('Paneer & Roti')
streamlit.text('Boiled Egg & chapati with muttan curry')

streamlit.header ('mom breakfast')
streamlit.text('🥣 Soup & Salad')
streamlit.text('🥑 avocado & Orange')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.

streamlit.dataframe(my_fruit_list)
