# Alan 
# Python week5

import graphlab
song_data = graphlab.SFrame('C:\\Users\\yl\\Downloads\\song_data.csv')
song_data[song_data['artist']=='Kanye West'].unique()
song_data[song_data['artist']=='Foo Fighters'].unique()
song_data[song_data['artist']=='Taylor Swift'].unique()
song_data[song_data['artist']=='Lady GaGa'].unique()

song_count = song_data.groupby(key_columns='artist', operations={'total_count': graphlab.aggregate.SUM('listen_count')})
song_count.sort('total_count',ascending=True)


train_data,test_data = song_data.random_split(.8,seed=0)

popularity_model = graphlab.popularity_recommender.create(train_data,
                                                         user_id='user_id',
                                                         item_id='song')

personalized_model = graphlab.item_similarity_recommender.create(train_data,
                                                                user_id='user_id',
                                                                item_id='song')

