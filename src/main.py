import pandas as pd

from content_based import recommend_movies
from collaborative import collaborative_recommend
from hybrid import hybrid_recommend

# Load data
data = pd.read_csv("data/movies.csv")

user_ids = data["user_id"].unique()

# -------------------------
# CONTENT-BASED
# -------------------------
print("\n=== CONTENT-BASED RECOMMENDATIONS ===")
for uid in user_ids:
    recs = recommend_movies(uid, data)
    print(f"\nUser {uid}:")
    if len(recs) > 0:
        print(list(recs))
    else:
        print("No recommendations available.")

# -------------------------
# COLLABORATIVE FILTERING
# -------------------------
print("\n=== COLLABORATIVE FILTERING RECOMMENDATIONS ===")
for uid in user_ids:
    recs = collaborative_recommend(uid, data)
    print(f"\nUser {uid}:")
    if len(recs) > 0:
        print(list(recs))
    else:
        print("No recommendations available.")

# -------------------------
# HYBRID SYSTEM
# -------------------------
print("\n=== HYBRID RECOMMENDATIONS ===")
for uid in user_ids:
    hybrid = hybrid_recommend(uid, data)
    print(f"\nUser {uid}:")
    if len(hybrid) > 0:
        for movie, score in hybrid:
            print(f"- {movie} (score: {score})")
    else:
        print("No recommendations available.")
