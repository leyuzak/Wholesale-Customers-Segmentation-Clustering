# 🛒 Wholesale Customers Segmentation using Clustering

This project focuses on **customer segmentation** using unsupervised machine learning techniques.  
By analyzing annual spending patterns across multiple product categories, meaningful customer groups are identified to support data-driven business decisions.

---

## 🎯 Project Objective

The objective of this project is to segment wholesale customers into distinct groups based on their purchasing behavior.  
Clustering helps uncover hidden customer segments without using labeled target variables and enables better understanding of customer profiles for marketing, inventory management, and strategic planning.

---

## 📊 Dataset Description

The dataset contains annual spending data of wholesale customers across the following product categories:

- Fresh  
- Milk  
- Grocery  
- Frozen  
- Detergents_Paper  
- Delicassen  

Additionally, two categorical features are provided:
- **Channel** (customer type)
- **Region** (geographical region)

The dataset consists of **440 observations and 8 features**.  
Since no target variable is available, the problem is treated as an **unsupervised learning task**.

---

## 🔍 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the data distribution and relationships between features.  
Histograms and boxplots revealed that spending variables are **highly skewed** and contain significant **outliers**.

Correlation analysis showed strong relationships between certain categories, especially:
- Grocery and Detergents_Paper  
- Milk and Grocery  

Scatter plots and PCA projections indicated natural groupings among customers, motivating the application of clustering algorithms.

---

## 🧹 Data Preprocessing

Before clustering, the following preprocessing steps were applied:

- Only numerical spending features were used for clustering.
- Categorical variables such as Channel and Region were excluded to avoid bias.
- All features were scaled using **StandardScaler** to handle differences in magnitude and ensure fair distance calculations.

---

## 🤖 Model Training

The **K-Means clustering algorithm** was selected for customer segmentation due to its simplicity, efficiency, and interpretability.

The optimal number of clusters was determined using the **Elbow Method**, which indicated that **three clusters** provide the best balance between model complexity and within-cluster variance.

To visualize cluster separation, **Principal Component Analysis (PCA)** was used to project the data into two dimensions.

---

## 🏆 Results and Interpretation

The clustering results revealed three distinct customer segments:

- **Balanced / Low-to-Medium Spenders:** Customers with moderate spending across all product categories.
- **Fresh-Focused Customers:** Customers with very high spending on fresh products, often associated with restaurants or hospitality businesses.
- **Grocery & Dairy Heavy Customers:** Customers with high spending on grocery, milk, and detergents, resembling retail-oriented purchasing behavior.

PCA visualization confirmed that these clusters are well separated, indicating successful customer segmentation.

---

## 🚀 Deployment

The trained clustering model and preprocessing pipeline were deployed as an interactive **Streamlit application** using **Docker** on Hugging Face Spaces.  
Users can input annual spending values and instantly receive a predicted customer segment.

### 🔗 Live Demo (Hugging Face)
👉 https://huggingface.co/spaces/leyuzak/Wholesale-Customers-Segmentation-using-Clustering

---

## 📘 Kaggle Notebook

The complete analysis, including EDA, clustering, and visualizations, is available on Kaggle:

👉 https://www.kaggle.com/code/leyuzakoksoken/wholesale-customers-segmentation-using-clustering

---

## 🛠️ Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Streamlit  
- Docker  
- Hugging Face Spaces  

---

## ✅ Conclusion

This project demonstrates how unsupervised learning techniques can be effectively applied to real-world business data to extract meaningful insights.  
Customer segmentation using clustering provides a powerful foundation for personalized strategies and data-driven decision-making.

