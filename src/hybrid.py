from content_based import recommend_movies
from collaborative import collaborative_recommend

def hybrid_recommend(user_id, data):
    content_recs = set(recommend_movies(user_id, data))
    collab_recs = set(collaborative_recommend(user_id, data))

    all_recs = content_recs.union(collab_recs)
    scores = {}

    for movie in all_recs:
        score = 0
        if movie in content_recs:
            score += 2
        if movie in collab_recs:
            score += 1
        scores[movie] = score

    ranked_movies = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_movies
