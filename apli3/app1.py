import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


print('case studies: movies anda data analysis')
print('-----------------------------------------')
print('MOVIES')
movies=pd.read_csv('movies.csv')
print(movies.head(2))
print(movies.columns)
print(movies.index)
print(movies.shape)
print('-----------------------------------------')
print('TAGS')
tags=pd.read_csv('tags.csv')
print(tags.head(2))
print(tags.columns)
print(tags.index)
print(tags.shape)
print('-----------------------------------------')
print('RATING')
ratings=pd.read_csv('ratings.csv')
print(ratings.head(2))
print(ratings.columns)
print(ratings.index)
print(ratings.shape)
print('ok')
print('-----------------------------------------')
print('-----------------------------------------')
print('ELIMIMAR TIMESTAMP')
print('-----------------------------------------')
del ratings['timestamp']
print('-----------------------------------------')
del tags['timestamp']
print(tags.head(2))
print(ratings.head(2))
# print('-----------------------------------------')
# print('-----------------------------------------')


# print(tags.iloc[[0,11,2000]])
# print('------------------CABEZA-----------------------')
# print(ratings.head())
# print('-----------------COLA------------------------')
# print(ratings.tail())
# print('-----------------------------------------')
# statistics=ratings['rating'].describe()
# print(statistics)
# print('promedio')
# print(ratings['rating'].mean())
# print('minimo')
# print(ratings['rating'].min())
# print('maximo')
# print(ratings['rating'].max())
# print('media')
# print(ratings['rating'].median())
# print('moda')
# print(ratings['rating'].mode())


# filter=ratings['rating']>5
# print(filter.any())
# print('-----------------------------------------')
# print('-----------------------------------------')

# print('movies')
# print(movies.shape)

# print(movies.isnull().any())

# print('-----------------------------------------')
# print('-----------------------------------------')
# print('rating')
# print(ratings.shape)

# print(ratings.isnull().any())

# print('-----------------------------------------')
# print('-----------------------------------------')
# print('tags')
# print(tags.shape)

# print(tags.isnull().any())

# tags=tags.dropna()

# import matplotlib.pyplot as plt

# ratings.hist(figsize=(10, 8), edgecolor='black',color='purple',column='rating')
# plt.suptitle('Histogramas de columnas numéricas')
# plt.show()

# print(ratings.head(10))
# print(ratings.shape)


print('-----------------------------------------')
print('-----------------------------------------')

print(tags.head(3))
tagstwovariableS=tags[['movieId','tag']]
print(tagstwovariableS.head(5))

print(ratings.shape)



# Sample ratings
samplestaken = ratings[1000:1020]
print(samplestaken.shape)
print(samplestaken.head(2))

# Tags
print(tags.head(2))
print(tags.shape)

tags_counts = tags['tag'].value_counts()
print(tags_counts.shape)
print(tags_counts.iloc[:10])  # ← CORREGIDO

# Gráfico de tags
tags_counts.iloc[:10].plot(kind='bar', figsize=[15, 10], color='skyblue', edgecolor='black')
plt.title("Top 10 Tags más frecuentes")
plt.xlabel("Tag")
plt.ylabel("Frecuencia")
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()  # ← muestra la gráfica en pantalla


# Ratings
ratings_counts = ratings['rating'].value_counts()
print(ratings_counts.shape)
print(ratings_counts.iloc[:10])  # ← CORREGIDO

# Gráfico de ratings
ratings_counts.iloc[:10].plot(kind='bar', figsize=[15, 10], color='lightgreen', edgecolor='black')
plt.title("Top 10 Ratings más frecuentes")
plt.xlabel("Rating")
plt.ylabel("Frecuencia")
plt.xticks(rotation=0)
plt.tight_layout()
#plt.show()  # ← muestra la gráfica en pantalla

print('-----------------------------------------')
print('-----------------------------------------')
print(movies.head(3))
print('-----------------------------------------')
print(movies.shape)
print('-----------------------------------------')
# print(movies.columns)
Animation=movies['genres'].str.contains('Animation', case=False, na=False)
Animation_df=movies[Animation]
print(Animation_df)
print('-----------------------------------------')
print(Animation_df.shape)

counts=ratings[['movieId', 'rating']].groupby('movieId').mean()
print(ratings.shape)
print(counts)  



# Calcular promedio de rating por movieId
average_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()

# Unir con los títulos de películas
movie_ratings = pd.merge(average_ratings, movies[['movieId', 'title']], on='movieId')

# Ordenar de mayor a menor promedio
movie_ratings_sorted = movie_ratings.sort_values(by='rating', ascending=False)

# Mostrar los 10 con mejor promedio
print(movie_ratings_sorted.head(10))
