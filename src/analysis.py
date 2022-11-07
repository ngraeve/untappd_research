import pandas as pd

import plotly.express as px


nick = pd.read_csv('C:\\Users\\Pinball\\Documents\\Nick.csv')
jarod = pd.read_csv('C:\\Users\\Pinball\\Documents\\Jarod.csv')

df = pd.merge(nick, jarod, on=['Beer', 'Brewery'])

#nick = nick.groupby('YourRating').size().reset_index(name='counts')
#print(nick)

with pd.option_context("display.max_columns", None):
    fig = px.histogram(jarod, x="YourRating", 
                       marginal="violin", # or violin, rug
                       hover_data=jarod.columns,
                       nbins=10)
    fig.show()



    print(f"Total rows - {df.shape[0]}")
    print(f"Nick > Jarod - {df[df.YourRating_x > df.YourRating_y].shape[0]}")
    print(f"Jarod > Nick - {df[df.YourRating_y > df.YourRating_x].shape[0]}")
    #print(combined['YourRating_x' > 'YourRating_y'].count())
    
    no_sour_df = df[~df['Style_x'].str.contains('Sour')]
    print(f"No Sour total rows - {no_sour_df.shape[0]}")
    print(f"Nick > Jarod (No Sours) - {no_sour_df[no_sour_df.YourRating_x > no_sour_df.YourRating_y].shape[0]}")
    print(f"Jarod > Nick (No Sours) - {no_sour_df[no_sour_df.YourRating_y > no_sour_df.YourRating_x].shape[0]}")
