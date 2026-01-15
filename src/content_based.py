def recommend_movies(user_id, data):
    user_data = data[data["user_id"] == user_id]

    if user_data.empty:
        return []

    genre_preferences = user_data.groupby("genre")["rating"].mean()
    favorite_genre = genre_preferences.idxmax()

    watched_movies = set(user_data["movie"])

    recommendations = data[
        (data["genre"] == favorite_genre) &
        (~data["movie"].isin(watched_movies))
    ]["movie"].unique()

    return recommendations
