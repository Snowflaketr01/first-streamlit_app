import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast favourites')
streamlit.text('🥣Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale Spinach & Rocket Smoothie')
streamlit.text('🐔Hard Boiled free range egg')
streamlit.text('🥑🍞Avacardo toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_selected)
