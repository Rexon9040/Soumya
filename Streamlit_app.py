import streamlit

streamlit.title('My parent Lunch plan')

streamlit.header ('Lunch menu')
streamlit.text('Dal & Rice')
streamlit.text('Paneer & Roti')
streamlit.text('Boiled Egg & chapati with muttan curry')

streamlit.header ('mom breakfast')
streamlit.text('🥣 Soup & Salad')
streamlit.text('🥑 avocado & Orange')

import Pandas 
my_fruit_list = pandas.read_csv("C:\Users\004KNT744\Documents\Panda.csv")
streamlit.dataframe(my_fruit_list)
