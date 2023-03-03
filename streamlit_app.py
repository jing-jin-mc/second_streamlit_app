import streamlit
import snowflake.connector
import pandas as pd

streamlit.title('Amazing Athleisure Catalog')

### connect to snowflake ###
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it in a car 
my_cur.execute("SELECT color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

# put the data into a dataframe and visulize it 
df = pd.DataFrame(my_catalog)
streamlit.write('Number of  colors to choose: ' , len(df) )

# get a color list and put it into a select box
color_list = df[0].values.tolist()
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

# build the image caption
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';")
df2 = my_cur.fetchone()

streamlit.image( df2[0],width=400, caption= product_caption )
streamlit.write('Price: ', df2[1]) 
streamlit.write('Sizes Available: ',df2[2]) 
streamlit.write(df2[3])

