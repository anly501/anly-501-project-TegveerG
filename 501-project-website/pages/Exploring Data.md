# Exploring Data
---

[![](../images/EDA.jpeg)](https://pub.towardsai.net/overview-of-exploratory-data-analysis-with-haberman-dataset-6b7e2cf73a58)

## Data To Be Explored
---

1. [REKT Database](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Exploring_Data/EDA_REKT_Record_Data.ipynb)

[![](../images/REKT_database.jpeg)](https://defiyield.app/rekt-database)

2. [Twitter API](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/Twitter_API_cleaning.ipynb)

3. News API (https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/Twitter_API_cleaning.ipynb)


## REKT Database Univariate Analysis: Numerical Variables
---

The REKT Database is our record data, which contains a mix of both numeric and categorical variables. Univariate analysis has been conducted on both numeric and categorical variables. The univariate analysis for numeric variables includes showcasing the moments, including median, skewness, and range, of the funds returned and funds lost variables. We also show that by log-transforming both the funds variables, we obtain an approximate Normal Distribution (bell-curve shape) for each variable.

Moreover, outlier detection through boxplots is showcased for the funds variables (not log- transformed).

[![](../images/Funds_Lost_USD_Moments.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

[![](../images/Funds_Returned_USD_Moments.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

**Applying Log Normal Transformation to both Funds Variables, we get an ideal fit for our data with no skewness or kurtosis present:**

[![](../images/Log_Funds_Lost_Moments.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

[![](../images/Log_Funds_Returned_Moments.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

## REKT Database Univariate Analysis: Categorical Variables
---

The univariate analysis for categorical variables, including extracted datetime features and scam type, showcases the distribution of when attacks took place, particularly in which months and day of the week. The scam type variable 14 unique categories or types of attacks that have been recorded in the REKT Database. For exploration, we highlight which scams are most prevalent in the data

[![](../images/Attack_Day_of_Week_Moments.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

[![](../images/Attack_Months_Moments.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

[![](../images/Scam_Types_Barplot.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

## REKT Database Univariate Analysis: Outlier Detection
---

[![](../images/Outlier_Funds_Returned_USD.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

[![](../images/Outlier_Drop_Returned_Lost_USD.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

[![](../images/Outliers_Funds_Lost_USD.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

[![](../images/Outliers_Drop_Funds_Lost_USD.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

## REKT Database Bivariate Analysis : Numerical-Numerical
---

In this section, we dive into the correlations of each numeric variable with each other using a correlation matrix. We can see that funds returned and funds lost are moderately correlated around 0.5 as their pearson correlation coefficient. This signifies that funds were not always returned for each attack! In fact, upon cleaning the dataset further by eliminating those projects that were disbanded or deactivated, more than 90% of the dataset contains no funds returned values. Therefore, when funds were returned, they must be returned in accordance with the magnitude of the loss.

[![](../images/Bivariate_Funds_Date_Corr.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)


## Twitter Sentiment Analysis from Vader
---

In this section, we build wordclouds for positive and negative sentiment words from our twitter corpus. 

[![](../images/Top_Positive_Words_Vader.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

[![](../images/Top_Positive_Words.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

[![](../images/Top_Negative_Words.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)

[![](../images/Barplot_Neg_Words.jpeg)](https://github.com/anly501/anly-501-project-TegveerG/blob/main/codes/Data_Cleaning/REKT_Database_Cleaning.ipynb)


