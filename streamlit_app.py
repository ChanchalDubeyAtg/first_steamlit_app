import pandas
import requests
import snowflake.connector
from urllib.error import URLError
import streamlit
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
#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
 fruityvice_response = requests.get ("https://fruityvice.com/api/fruit/" + fruit_choice)
 fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized

#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
 fruit_choice=streamlit.text_input('What fruit would you like information about?','kiwi')
 if not fruit_choice:
  streamlit.error("What fruit would you like information about?")
 else:
  back_from_function = get_fruityvice_data(fruit_choice)
  streamlit.dataframe(back_from_function)
except URLError as e:
 streamlit.error()
streamlit.write('The user entered',fruit_choice)

streamlit.header("The fruit load list contains:")
#snowflake-realated functions
def get_fruit_load_list():
 with my_cnx.cursor() as my_cur:
  my_cur.execute("SELECT * FROM fruit_load_list")
  return my_cur.fetchall()
 
#add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])\
 my_data_rows = get_fruit_load_list()
 streamlit.dataframe(my_data_rows)



#import requests 


#pip install --upgrade pip --user
#pip install -r https://raw.githubusercontent.com/snowflakedb/snowflake-connector-python/v2.7.6/tested_requirements/requirements_36.reqs
#streamlit.stop()



