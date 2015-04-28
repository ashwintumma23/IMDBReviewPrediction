# Script to fetch the reviews of top 5 movies , and 50 reviews for each movie

rm -rf *.html

# Movie 1 - The Shawshank Redemption
wget http://www.imdb.com/title/tt0111161/reviews?start=0 -O review_1_0.html
wget http://www.imdb.com/title/tt0111161/reviews?start=10 -O review_1_10.html
wget http://www.imdb.com/title/tt0111161/reviews?start=20 -O review_1_20.html
wget http://www.imdb.com/title/tt0111161/reviews?start=30 -O review_1_30.html
wget http://www.imdb.com/title/tt0111161/reviews?start=40 -O review_1_40.html

# Movie 2- The Godfather 
wget http://www.imdb.com/title/tt0068646/reviews?start=0 -O review_2_0.html
wget http://www.imdb.com/title/tt0068646/reviews?start=10 -O review_2_10.html
wget http://www.imdb.com/title/tt0068646/reviews?start=20 -O review_2_20.html
wget http://www.imdb.com/title/tt0068646/reviews?start=30 -O review_2_30.html
wget http://www.imdb.com/title/tt0068646/reviews?start=40 -O review_2_40.html

# Movie 3- The Godfather Part 2 
wget http://www.imdb.com/title/tt0071562/reviews?start=0 -O review_3_0.html
wget http://www.imdb.com/title/tt0071562/reviews?start=10 -O review_3_10.html
wget http://www.imdb.com/title/tt0071562/reviews?start=20 -O review_3_20.html
wget http://www.imdb.com/title/tt0071562/reviews?start=30 -O review_3_30.html
wget http://www.imdb.com/title/tt0071562/reviews?start=40 -O review_3_40.html

# Movie 4 - The Dark Knight 
wget http://www.imdb.com/title/tt0468569/reviews?start=0 -O review_4_0.html
wget http://www.imdb.com/title/tt0468569/reviews?start=10 -O review_4_10.html
wget http://www.imdb.com/title/tt0468569/reviews?start=20 -O review_4_20.html
wget http://www.imdb.com/title/tt0468569/reviews?start=30 -O review_4_30.html
wget http://www.imdb.com/title/tt0468569/reviews?start=40 -O review_4_40.html

# Movie 5 - Pulp Fiction 
wget http://www.imdb.com/title/tt0110912/reviews?start=0 -O review_5_0.html
wget http://www.imdb.com/title/tt0110912/reviews?start=10 -O review_5_10.html
wget http://www.imdb.com/title/tt0110912/reviews?start=20 -O review_5_20.html
wget http://www.imdb.com/title/tt0110912/reviews?start=30 -O review_5_30.html
wget http://www.imdb.com/title/tt0110912/reviews?start=40 -O review_5_40.html
