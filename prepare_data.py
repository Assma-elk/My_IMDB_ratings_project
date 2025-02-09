import pandas as pd

# 1Load the dataset
df = pd.read_csv('imdb_movies.csv')

# Function to split genres into a list
def get_genres(Genres):
    if pd.isna(Genres):
        return []
    return [g.strip() for g in Genres.split(',')]

# Apply the function to create a list of genres for each movie
df['Genres_List'] = df['Genres'].apply(get_genres)

# Explode the genres (one row per genre per movie)
df_exploded = df.explode('Genres_List')

# Rename for clarity
df_exploded = df_exploded.rename(columns={'Genres_List': 'Single_Genres'})

# Save the multi-genre data
df_exploded.to_csv('imdb_movies_multi_genre.csv', index=False)

# Confirmation message
print("Multi-genre data created successfully! Check 'imdb_movies_multi_genre.csv'.")
