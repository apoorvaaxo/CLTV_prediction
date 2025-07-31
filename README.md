# Customer Lifetime Value (CLTV) Prediction and Optimization for an E-commerce Business

### **Live Application**

This project's core output is an interactive web application that demonstrates the predictive model and its business insights.

[![CLTV App Screenshot]("C:/Users/DELL/OneDrive/Desktop/CLTV_Predictor.png")](https://your-app-url-here.streamlit.app)

* **Live App Link:** [Click here to view the live application!](https://your-app-url-here.streamlit.app)

---

### **Project Overview**

This project demonstrates an end-to-end data science pipeline for predicting Customer Lifetime Value (CLTV) and translating those predictions into actionable business strategies. The primary goal was to leverage historical e-commerce transaction data to forecast the future value of individual customers, enabling the business to optimize marketing spend, personalize customer experiences, and improve retention.

The project uses a hybrid approach, combining a robust probabilistic model (BG/NBD and Gamma-Gamma) with data-driven segmentation to deliver tangible, quantifiable business recommendations.

### **Business Problem & Motivation**

An e-commerce company wants to move from a reactive marketing approach to a proactive, value-driven strategy. Without a clear understanding of which customers are most valuable, marketing efforts can be inefficient, leading to high acquisition costs and poor retention. This project addresses the core challenge of identifying high-potential customers and at-risk customers to maximize long-term profitability.

### **Key Deliverables**

1.  **Cleaned & Pre-processed Data:** A refined dataset of e-commerce transactions ready for analysis.
2.  **Feature-Engineered Customer Data:** A comprehensive customer-level DataFrame with RFM (Recency, Frequency, Monetary) and other key behavioral metrics.
3.  **Probabilistic CLTV Model:** A predictive model that forecasts future customer purchases and total spend.
4.  **Customer Segmentation:** Actionable customer segments based on predicted CLTV.
5.  **Strategic Recommendations:** Specific, data-driven marketing and retention strategies for each customer segment, including a framework for A/B testing.

### **Methodology**

1.  **Data Ingestion & Cleaning (`01_EDA_and_Cleaning.ipynb`):** Loaded raw transactional data and performed extensive EDA to handle missing `CustomerID`, negative quantities, and ensure data integrity.
2.  **Feature Engineering (`02_Feature_Engineering.ipynb`):** Transformed raw data into customer-level features. Key features included:
    * **RFM:** Recency (days since last purchase), Frequency (number of purchases), and Monetary (total spend).
    * **Tenure:** Customer age from first purchase.
    * **Advanced Features:** Average Order Value (AOV), Average Purchase Gap, and Product Diversity.
3.  **CLTV Prediction Modeling (`03_CLTV_Probabilistic_Models.ipynb`):** Utilized the `lifetimes` library to build a probabilistic model.
    * **BG/NBD Model:** Predicted future purchase frequency.
    * **Gamma-Gamma Model:** Predicted the average monetary value per transaction.
    * These models were combined to forecast a 12-month CLTV for each customer.
4.  **Segmentation & Strategy (`04_Customer_Segmentation_and_Strategy.ipynb`):** Segmented customers into High-Value, Medium-Value, and Low-Value tiers based on their predicted CLTV. Analyzed the RFM characteristics of each segment to propose tailored, actionable business strategies.

### **Key Findings & Business Recommendations**

* **High-Value Segment (The "VIPs"):** This segment constitutes approximately **20%** of our customer base but is predicted to generate a disproportionately high amount of future revenue, with an average predicted CLTV of over **₹11.2 crore**. They have an average `Frequency` of **12.03** and a `Recency` of just **20.90** days.
    * **Recommendation:** Implement a tiered loyalty program and provide exclusive access to products to retain these critical customers.

* **Medium-Value Segment (The "Growth Tier"):** This segment shows solid potential for growth. They have an average `Frequency` of **2.78** and an average `AOV` of **₹28,137**.
    * **Recommendation:** Focus on upselling and cross-selling campaigns to increase their average order value and purchase frequency.

* **Low-Value / At-Risk Segment:** This segment has a high `Recency` of **226.58** days, indicating a high probability of churn.
    * **Recommendation:** Use cost-effective "win-back" campaigns, such as a time-sensitive discount, to re-engage them.


### **Technologies Used**

* **Programming Language:** Python
* **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `lifetimes`, `lightgbm`
* **Environment:** Conda, Jupyter Notebook
* **Version Control:** Git & GitHub

### **How to View the Analysis**

The full analysis and code are available in the following Jupyter notebooks:
* `01_EDA_and_Cleaning.ipynb`: Initial data exploration and preprocessing.
* `02_Feature_Engineering.ipynb`: Creation of RFM and advanced customer features.
* `03_CLTV_Probabilistic_Models.ipynb`: Building the BG/NBD and Gamma-Gamma models.
* `04_Customer_Segmentation_and_Strategy.ipynb`: Customer segmentation and strategic recommendations.

