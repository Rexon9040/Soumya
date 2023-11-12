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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
Fruits_seleceted = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['avocado','apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(my_fruit_list)
