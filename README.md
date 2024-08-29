# Market Research Analysis - Restaurants in Taipei



## North Star Metric and Dimensions
- **Price Distribution:** Calculate average spending per person for understanding customer behavior and restaurant positioning.
- **Restaurant Desity:** Calculate the number of restaurants per district. This can indicate market saturation or opportunity.
- **Geographic Dimension:** Districts in Taipei
- **Restaurant Categories:** Types of cuisine and restaurants
   

## Summary of Insights

### Geographic Dimension
 
![image-2](https://github.com/user-attachments/assets/85631ff2-38c5-4531-846a-d1f7283dcce9)
<p> </p>

**Price Distribution:**
> 
> - The standard deviation of 114.37 TWD for prices indicates a substantial spread in average prices across districts. → There are significant differences in average meal costs depending on which district you're in.
>     - The highest average prices are in 中山區 (588 TWD) and 大安區 (583 TWD), both over 1.7 standard deviations above the mean.
>     - The lowest average prices are in 文山區 (235 TWD), 1.35 standard deviations below the mean.
> - Approximately 68% of districts have average prices within 114.37 TWD of the overall mean (389 ± 114.37 TWD).

<p> </p>

 **Category Variety:**
> 
> - The extremely small standard deviation for category variety (less than 1) indicates very little variation in the number of categories across districts. → Most districts have similar category variety, clustering around 76 categories.
> - This suggests that regardless of location or price level, most districts offer a similar variety of cuisine types.
> - 大同區 has the highest variety with 79 categories, while 南港區 has the lowest with 71.

<p> </p>

 **Price vs. Variety Relationship:**
> 
> - The districts with the highest prices (中山區 and 大安區) also have above-average category variety.
> - There are no districts that clearly fit the criteria of "high prices but low variety" that we were initially looking for.

  <p> </p>

 **Restaurant Density:**
 
> There is a significant concentration of restaurants in a few key districts, with a long tail of districts having fewer establishments.
> 
> 
> The top three districts account for 46% of all restaurants in the dataset.
> 
> - 大安區 (Da'an District): 2,274 restaurants (20% of total)
> - 中山區 (Zhongshan District): 1,835 restaurants (16% of total)
> - 信義區 (Xinyi District): 1,113 restaurants (10% of total)

> Local Economies:  The distribution likely reflects the economic and demographic characteristics of each district. 大安區, 中山區,  信義區 are likely to be the major commercial or tourist centers, while lower-density areas may be more residential or industrial.
> 

> Consumer Behavior: The concentration of restaurants might indicate where people prefer to dine out, which could be influenced by factors such as workplace locations, entertainment venues, or transportation hubs.
>

<p> </p>

### Restaurant Categories

 **Price Disparity**
> 
> - The most significant price disparities are seen in Italian cuisine and cafes, with ranges of over 1000 TWD and 600 TWD respectively.
> - Chinese and Japanese cuisine show more moderate price ranges, suggesting these categories might have more standardized pricing across the city.

<p> </p>
  
**Combinations of Restaurant Types**
> High-end Focus: 精緻高級 (high-end/refined) and 約會餐廳 (date restaurant) appear frequently in the top combinations, indicating a strong market for upscale dining experiences.
> 

> Diverse Offerings: Popular restaurants often combine different types of cuisine or dining styles (e.g., Chinese cuisine with bar services, or hotpot with high-end dining).
> 

> All-day Dining: Many top combinations include both 午餐 (lunch) and 晚餐 (dinner), suggesting a preference for restaurants that operate throughout the day.
> 

> Japanese Influence: Japanese cuisine, including 居酒屋 (izakaya), features prominently in the popular combinations. (e.g., 居酒屋 (izakaya) with hotpot)
>


## Recommendations & Next Steps
<p> </p>
**Temporal Analysis**
Analyze restaurant performance across different times of day, days of the week, and seasons.
Required Data: Hourly/daily sales data, customer footfall, seasonal promotions.
<p> </p>

**Competition Intensity Mapping**
Create a heat map of competition intensity for different cuisine types across districts.
Required Data: Detailed categorization of restaurants, customer ratings, market share estimates.
<p> </p>

**Economic Indicator Correlation**
Analyze how broader economic indicators correlate with restaurant performance across districts.
Required Data: District-level economic data (average income, employment rates), correlation with restaurant metrics.
