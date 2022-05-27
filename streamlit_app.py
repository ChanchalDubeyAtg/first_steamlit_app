import pandas
import requests
import snowflake.connector
from urllib.error import URLError
#import streamlit
streamlit.title("My Mom\'s New Healthy Diner")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)

#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
 fruit_choice=streamlit.text_input('What fruit would you like information about?','kiwi')
 if not fruit_choice:
  streamlit.error("What fruit would you like information about?")
 else:
  fruityvice_response = requests.get ("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
  streamlit.dataframe(fruityvice_normalized)
except URLError as e:
 streamlit.error()
streamlit.write('The user entered',fruit_choice)

#import requests 


pip install --upgrade pip --user
pip install -r https://raw.githubusercontent.com/snowflakedb/snowflake-connector-python/v2.7.6/tested_requirements/requirements_36.reqs
streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
my_cur.execute("insert into fruit_load_list values(from streamlit)")


