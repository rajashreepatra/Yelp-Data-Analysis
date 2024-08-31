# Yelp-User Engagement-Analysis using SQL AND Python

**Project Overview**
This project analyzes user engagement data from Yelp to understand its impact on the success of restaurants across various metropolitan areas in the USA and Canada. The primary objective is to investigate the relationship between user engagement (reviews, tips, and check-ins) and business success metrics (review count and ratings). The project includes a detailed exploration of the data, analysis of key metrics, and actionable recommendations.

**Problem Statement**
The project aims to explore the relationship between user engagement on Yelp and the success of restaurants, as measured by review count and average star rating. The goal is to determine how different types of user interactions contribute to a restaurant's overall performance.

**Research Objectives**
1. Quantify the correlation between user engagement (reviews, tips, check-ins) and business success metrics (review count, average star rating).
2. Analyze the impact of review sentiment on these success metrics.

**Hypotheses**
1. Higher levels of user engagement correlate with higher review counts and ratings for restaurants.
2. Positive sentiment expressed in reviews and tips contributes to higher overall ratings and review counts for restaurants.

**Data Overview**
* Dataset: The dataset consists of information about businesses across 8 metropolitan areas in the USA and Canada, stored in five JSON files: business, review, user, tip, and check-in.
* Scope: The analysis focuses on 150k businesses, with a subset of 35k open restaurants.

**Analysis & Findings**
1. Correlation Between Engagement and Success:
    * Higher ratings do not necessarily lead to higher review counts, and vice versa.
    * Success is not solely determined by ratings or review counts; user engagement reflects activity but not overall satisfaction or performance.
      
2. User Engagement Insights:
    * Engagement tends to increase with ratings from 1 to 4 stars but drops at 5 stars, possibly indicating a saturation point or selectivity.
    * Correlation between reviews, tips, and check-ins suggests that increased activity in one area drives higher engagement across other areas.
      
3. Geographical Insights:
     * Philadelphia has the highest success score, combining high ratings with active user engagement.
   
4. Sentiment Analysis:
     * Positive sentiments (useful, funny, cool) are strongly correlated with success, indicating higher user satisfaction and engagement.
       
5. Peak Business Hours:
     * User engagement peaks from 4 PM to 1 AM, suggesting higher demand for dining out during these times, influenced by work schedules and social activities.
  
**Recommendations:**

1. **Operational Adjustments:**
    * Businesses should optimize staffing and resources during peak hours to ensure quality service and efficient operations.
2. **Strategic Marketing:**
    * Less successful businesses should focus on improving service quality and actively engaging with customer feedback to enhance user engagement over time.
3. **Expansion Opportunities:**
    *  Cities with high success scores, such as Philadelphia, offer opportunities for restaurant chains to expand or invest further.
