# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA
df = pd.read_csv("netflix_titles.csv")

# CLEAM DATA

df = df.dropna(subset=['type', 'release_year',
               'rating', 'country', 'duration'])

# Movies vs tvShows
type_count = df['type'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(type_count.index, type_count.values, color=["skyblue", "orange"])
plt.title("Number of Movies V/S Tv Shoes on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_vs_tvshows.png")
plt.show()

# RATING PERCENTAGE
rating_counts = df["rating"].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(rating_counts, labels=rating_counts.index,
        autopct="%1.1f%%", startangle=90, pctdistance=0.85, labeldistance=1.1)
plt.title("Percentage of Ratings")
plt.tight_layout()
plt.savefig("content_rating_pie.png")
plt.show()

# MOVIES DURATION
movie_df = df[df["type"] == "Movie"].copy()
movie_df["duration_int"] = movie_df['duration'].str.replace(
    ' min', '').astype(int)
plt.hist(movie_df["duration_int"], bins=30, color='purple', edgecolor='black')
plt.title("Distribution of Movies Duration")
plt.xlabel("Distribution (minutes)")
plt.ylabel("Number of movies")
plt.tight_layout()
plt.savefig("movie_duration_histogram.png")
plt.show()

# RELEASE YEAR VS NO OF SHOWS
release_counts = df["release_year"].value_counts().sort_index()
plt.scatter(release_counts.index, release_counts.values,
            color="red", marker="o")
plt.title("Release Year vs Number of Shows")
plt.xlabel("Release Year")
plt.ylabel("Number of movies")
plt.tight_layout()
plt.grid()
plt.savefig("release_year_scatter.png")
plt.show()

# Counting top 10 countries
country_counts = df["country"].value_counts().head(10)
plt.figure(figsize=(8, 6))
plt.barh(country_counts.index, country_counts.values, color="teal")
plt.title("Top 10 Countries by Number of Shows")
plt.xlabel("Number of Shows")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("Top_10_Countries.png")
plt.show()


# Movies and tv Show per year
content_by_year = df.groupby(
    ['release_year', 'type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# first Subplot:Movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color="blue")
ax[0].set_title("Movies Released Per Year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")

# first Subplot:Tv Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color="orange")
ax[1].set_title("TV Shows Released Per Year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Number of Movies")

fig.suptitle("Comperison of Movies and TV Shows Released Over Year")
plt.tight_layout()
plt.savefig("Movies_TV_Shows_Comperision.png")
plt.show()
