import streamlit

streamlit.title('My parent Lunch plan')

streamlit.header ('Lunch menu')
streamlit.text('Dal & Rice')
streamlit.text('Paneer & Roti')
streamlit.text('Boiled Egg & chapati with muttan curry')

streamlit.header ('mom breakfast')
streamlit.text('🥣 Soup & Salad')
streamlit.text('🥑 avocado & Orange')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)


