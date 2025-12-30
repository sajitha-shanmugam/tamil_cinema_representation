import kagglehub
import pandas as pd

# 1) Download dataset
path = kagglehub.dataset_download("rohithmahadevan/tamil-movies-dataset")
csv_path = f"{path}/Tamil_Movies_Dataset.csv"

print("CSV path:", csv_path)

# 2) Load
df = pd.read_csv(csv_path)
print(df.head())
print(df.columns)
print(df.shape)

# 3) Rename columns to simpler names
df = df.rename(columns={
    'MovieName': 'title',
    'Genre': 'genre',
    'Rating': 'imdb_rating',
    'Year': 'year',
    'PeopleVote': 'num_votes'
})

# 4) Basic cleaning
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df = df.dropna(subset=['title', 'year'])

df.to_csv('tamil_movies_clean.csv', index=False)
print("Saved tamil_movies_clean.csv")
