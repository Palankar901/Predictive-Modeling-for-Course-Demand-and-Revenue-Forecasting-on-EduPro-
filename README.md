# Predictive-Modeling-for-Course-Demand-and-Revenue-Forecasting-on-EduPro
Hello everyone,

This project focused on using EduPro’s historical platform data to predict course demand and forecast revenue. The goal was to move course-planning decisions away from intuition and toward evidence-based insights.

We analyzed data from 3,000 users, 60 courses, 60 teachers, and 10,000 transactions recorded during 2025. The data included course category, type, level, price, duration, ratings, teacher attributes, and transaction amounts.

The exploratory analysis showed total recorded revenue of approximately $911,000. Artificial Intelligence, Business, and Project Management emerged as the highest-revenue course categories. We also found that nearly two-thirds of the course catalog was free, which is important when interpreting demand and revenue together.

For predictive modeling, we created features such as price bands, duration buckets, rating tiers, and course-level historical performance measures. We tested Linear Regression, Ridge, Lasso, Random Forest, and Gradient Boosting models.

The revenue models performed strongly. The Lasso Regression model achieved the best result, with an R-squared value close to 0.99 and an average error of roughly $2,135 per course. However, enrollment-demand prediction was less reliable, with the best R-squared around 0.12. This indicates that enrollment volumes are influenced by additional factors that are not captured in the current dataset, such as marketing campaigns, learner preferences, seasonality, and course visibility.

A key lesson from the project is that predictive models should support—not replace—business decisions. EduPro should use the dashboard to compare categories, test pricing scenarios, and prioritize course launches, while continuing to validate results through controlled experiments.

For future improvement, EduPro should collect explicit course-to-teacher mapping, refund information, marketing exposure data, and more time-series history. These additions would make demand forecasts more accurate and enable stronger pricing and launch decisions.

Overall, this project demonstrates how EduPro can use data science to plan its content roadmap, optimize revenue, and allocate resources more effectively.

Thank you.
