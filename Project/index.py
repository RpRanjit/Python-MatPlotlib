import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("netflix_titles.csv")
# print(data)

# clean data
data = data.dropna(subset= ['type', 'release_year', 'rating', 'country', 'duration'])

# type_counts = data['type'].value_counts()
# plt.figure(figsize=(6,4))
# print(type_counts.index)
# print(type_counts.values)
# # How many Movies and TV shows? bar chart
# plt.bar(type_counts.index, type_counts.values, color = ['skyblue', 'orange'])
# plt.title("Number of Movies VS TV Shows on Netflix")
# plt.xlabel("Type")
# plt.ylabel("Count")
# plt.tight_layout()
# plt.savefig('Movies_vs_TV_Shows_bar.png')
# plt.show()

# What is the presentage of each content rating(PG, R, TV-MA)? Pie chart
# rating_counts = data['rating'].value_counts()
# plt.figure(figsize = (8,6))
# plt.pie(rating_counts, labels= rating_counts.index, autopct= "%1.1f%%", startangle=90)
# plt.title("Percentage of Content ratings")
# plt.tight_layout()
# plt.savefig('Content_Rating_pie.png')
# plt.show()


# How has the number of release changed over the years? line plot
# print(data.columns)
# release_years = data['release_year'].value_counts()
# plt.figure(figsize=(8,6))
# plt.plot(release_years.index, release_years.values, color = "orange")
# plt.xlabel(" Relears Years")
# plt.ylabel(" No of Movies or TV shows")
# plt.title("Release Change per Years")
# plt.tight_layout()
# plt.savefig('Releace_Changes_per_years_line.png')
# plt.show()

# What is the distribution of movie durations? Histogram
# movie_data = data[data["type"] == "Movie"].copy()
# movie_data['duration_int'] = movie_data['duration'].str.replace(' min','').astype(int)

# plt.figure(figsize=(8,6))
# plt.hist(movie_data['duration_int'], bins= 30, color="purple", edgecolor = "black")
# plt.title("Distribution of Movie Duration")
# plt.xlabel("Duration (Movies)")
# plt.ylabel("No of Movies")
# plt.tight_layout()
# plt.savefig('Movie_Duration_histogram.png')
# plt.show()


# Relationship between release year and number of shows? Scatter Plot

# release_count = data["release_year"].value_counts().sort_index()
# plt.figure(figsize=(10,6))
# plt.scatter(release_count.index, release_count.values, color = "red")
# plt.xlabel("Relears Years")
# plt.ylabel(" Number of shows")
# plt.title("Release Years Vs Number of Shows")
# plt.tight_layout()
# plt.savefig('Release_years_scatter.png')
# plt.show()

# Top 10 Countries with the highest number of shows? Bar chart horizontal
# county_counts = data['country'].value_counts().head(10)
# plt.figure(figsize=(8,6))
# plt.barh(county_counts.index, county_counts.values, color='teal')
# plt.xlabel("Number of Shows")
# plt.ylabel("Country")
# plt.title("Top 10 Countries by Number of Shows")
# plt.tight_layout()
# plt.savefig('Top10_country_barh.png')
# plt.show()


# Compare Multiple plots together(er Movies vs Tv shows by year) Save Final Charts Saving figures
print(data['type'])
content_by_year = data.groupby(['release_year', 'type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize=(12,5))

# first subplot.movies
ax[0].plot(content_by_year.index,content_by_year['Movie'], color='blue')
ax[0].set_title("Movies Releases Per Year")
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')
# Second subplot.TV shows
ax[0].plot(content_by_year.index,content_by_year['TV Show'], color='orange')
ax[0].set_title("TV shows Releases Per Year")
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of TV shows')

fig.suptitle("Comparision of movies and TV shows relese per years")
plt.tight_layout()
plt.savefig("movies_tv_shows_comparision.png")
plt.show()