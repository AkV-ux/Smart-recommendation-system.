def collaborative_recommend(user_id, data):
    user_movie_matrix = data.pivot_table(
        index="user_id",
        columns="movie",
        values="rating"
    ).fillna(0)

    similarity = user_movie_matrix.dot(user_movie_matrix.T)

    similar_users = similarity[user_id].sort_values(ascending=False).drop(user_id)

    if similar_users.empty:
        return []

    top_user = similar_users.idxmax()

    top_user_movies = set(
        data[data["user_id"] == top_user]["movie"]
    )

    user_movies = set(
        data[data["user_id"] == user_id]["movie"]
    )

    return top_user_movies - user_movies
