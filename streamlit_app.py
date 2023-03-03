import streamlit
import snowflake.connector
import pandas as pd

streamlit.title('Zena\'s Amazing Athleisure Catalog')

### connect to snowflake ###
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it in a car 
my_cur.execute("SELECT color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

# put the data into a dataframe and visulize it 
df = pd.DataFrame(my_catalog)
streamlit.write(df)



my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

