# My Movie Journey: Ratings, Genres & More

Welcome to **My Movie Journey: Ratings, Genres & More**, a Tableau dashboard where I explore and analyze my personal movie ratings from the past 10 months. This project showcases my data visualization skills while offering insights into my movie-watching habits, preferences, and how they compare with IMDb ratings.

## 🎞️ **Live Dashboard**
[View the interactive Tableau dashboard here](https://public.tableau.com/views/MyMovieJourneyRatingsGenresMore/MyMovieJourneyRatingsGenresMore?:language=fr-FR&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

##🌟 **Dashboard Preview**
(Here’s an overview of the interactive dashboard in action)
![image](https://github.com/user-attachments/assets/8d20c2ba-49c4-433c-8bb4-c19e6bb020b9)

## 📂 **Dataset**
The data comes from my [IMDb ratings list](https://m.imdb.com/user/ur175189411/ratings/?sort=date_added%2Casc), reflecting all the movies I've rated over the past 10 months.

## 🐍 **Data Preparation with Python**
Before creating the dashboard, I used a simple Python script with **pandas** to prepare the data. The main task was to **separate movies with multiple genres** into distinct rows for better analysis in Tableau. 

The script processes the original dataset, splits the genres, and saves the modified version as `imdb_movies_multi_genre.csv`.

You can find the Python script (`prepare_data.py`) in this repository.

## 📊 **Key Features of the Dashboard**

1. **Distribution of Movies by Genre (%)**  
   - See the percentage breakdown of movies I've watched by genre.
   - *Interactive Filter:* Click on any genre to filter the entire dashboard.

2. **My Top 10 Highest-Rated Movies**  
   - Displays the movies I've rated the highest, with ratings ranging from 9 to 10.

3. **Movies I Wish I Didn't Watch**  
   - A playful section highlighting the lowest-rated films, reflecting my personal disappointments.

4. **My Ratings - IMDb's Ratings**  
   - Compares my ratings to IMDb's, showcasing where my opinions differ the most.

5. **My Top 5 Directors by Average Rating**  
   - Highlights the directors whose movies I've rated the highest on average.

6. **Movies I've Watched by Release Year**  
   - A heatmap showing how many movies I've watched from different release years.
   - *Fun Fact:* I’ve watched the most movies from 2003—my birth year!

7. **Average Ratings by Genre (Genres with 4+ Movies)**  
   - Displays the average ratings I've given to genres where I've rated at least four movies.

## 🎨 **Design & Interactivity**
- *Clean Layout:* Optimized for clarity and readability.
- *Interactive Filters:* Easily filter the dashboard by clicking on genres.
- *IMDb Theme Touch:* Includes the IMDb logo to reflect the data source.

## 🌟 **Insights**
- My preferences lean heavily toward certain genres like Drama and Thriller.
- Some highly acclaimed movies didn't resonate with me (*sorry, The Godfather!*).
- Directors like Peter Jackson and Denis Villeneuve consistently impressed me.

## 💡 **Why This Project?**
This project combines my passion for movies with data visualization. It's not just about the movies but also a reflection of how data can tell personal stories.

---

**Feedback is welcome!**
If you enjoyed exploring this dashboard, feel free to star the repo or leave a comment. 🌟

