
# Smart Hybrid Recommendation System
I first built and compared both content-based and collaborative filtering recommendation systems, analyzing their strengths, limitations, and recommendation behavior.
Then upgraded it into a content-based system that recommends items based on a user’s genre preferences, while collaborative filtering leverages similarity between users. The hybrid system merges both approaches and prioritizes items recommended by both models, improving recommendation confidence and diversity. 

A modular movie recommendation system that combines **content-based filtering** and **collaborative filtering** into a **hybrid recommendation engine**.  
The system generates personalized and ranked movie recommendations for users based on their preferences and similarities with other users.

## Project Overview

Recommendation systems are widely used in platforms like Netflix, Amazon, and Spotify.  
This project demonstrates how different recommendation strategies work individually and how combining them improves recommendation quality.

The system includes:
- Content-Based Filtering
- Collaborative Filtering
- Hybrid Recommendation with Weighted Scoring

## Project Structure
smart-recommendation-system/
│
├── data/
│ └── movies.csv
│
├── src/
│ ├── content_based.py
│ ├── collaborative.py
│ ├── hybrid.py
│ └── main.py
│
├── README.md
└── requirements.txt

## Recommendation Approaches;

### 1️⃣ Content-Based Filtering
Recommends movies based on a user’s past preferences.

**Logic:**
- Identify the user’s favorite genre using average ratings
- Recommend unseen movies from that genre

**Pros:**
- Personalized
- Explainable
- Works even with a single user

**Cons:**
- Limited when a user has already watched most content in a genre

### 2️⃣ Collaborative Filtering
Recommends movies based on user similarity.

**Logic:**
- Build a user–movie rating matrix
- Compute similarity between users
- Recommend movies liked by similar users

**Pros:**
- Introduces new interests
- Solves content exhaustion problem

**Cons:**
- Needs sufficient user data
- Cold-start problem for new users

### 3️⃣ Hybrid Recommendation System
Combines both approaches to produce ranked recommendations.

**Scoring Strategy:**
- Content-based recommendation → +2
- Collaborative recommendation → +1
- Recommended by both → +3 (higher confidence)

This improves both **accuracy** and **diversity**.





