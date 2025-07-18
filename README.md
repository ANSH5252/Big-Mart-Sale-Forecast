# 🛒 Big Mart Sales Forecast
A machine learning project that predicts sales for different products across Big Mart outlets using regression models. Built with Python, Pandas, Scikit-learn, and deployed via Streamlit for a user-friendly interface.

## 🚀 Features
- 📈 Predicts item-level sales for various Big Mart outlets

- 🧠 Trained using ensemble models (Voting Regressor with Random Forest, XGBoost, and Lasso)

- 📊 Clean and interactive Streamlit UI

- ⚙️ Handles categorical and missing data efficiently

- 📦 Supports model serialization with joblib

## 🧰 Tech Stack
- Language: Python 🐍

- Libraries Used:

  - `pandas`, `numpy` – Data preprocessing and manipulation

  - `scikit-learn`, `xgboost` – Model building

  - `joblib` – Model serialization

  - `streamlit` – Web application framework

- Techniques Used:

  - Feature Encoding (Label Encoding, One-Hot Encoding)

  - Missing Value Imputation

  - Outlier Detection and Removal

  - Ensemble Learning (Voting Regressor with multiple base models)

## 🧾 Project Structure
```
BIG-MART-SALE-FORECAST/
│
├── app.py                     # Streamlit application entry point
├── voting_model.pkl           # Trained Voting Regressor model
├── Encoder.pkl                # Encoder to Encode Textual Data
├── b_m_s_f.ipynb              # Jupyter Notebook
├── train.csv                  # Original training dataset
├── test.csv                   # Original test dataset
├── requirements.txt           # Project dependencies
├── License                    # MIT LICENSE
└── README.md                  # Project documentation
```
🖥️ How to Run
1. Clone the Repository
```
git clone https://github.com/ANSH5252/Big-Mart-Sale-Forecast.git
cd Big-Mart-Sale-Forecast
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Launch Streamlit App
```
streamlit run app.py
```
## 🔍 How It Works

- Data Preprocessing:
  - Missing values are imputed using median/mode

  - Categorical features are encoded (Label Encoding / One-Hot Encoding)

  - Outliers are detected via visualization (boxplots) and removed

  - Final cleaned dataset is used to train models

- Model Training:
  - Voting Regressor combines:

    - Random Forest Regressor 🌲

    - XGBoost Regressor ⚡

    - Lasso Regression 🔗

  - Model is trained on processed training data and saved as .pkl file

- Prediction:
  - Users input features in Streamlit UI

  - Model outputs estimated item sales for given inputs

## 🧪 Example Usage

- Open the Streamlit app in your browser

- Fill in:

  - Item type, Outlet type, Item MRP, etc.

- Click "Predict Sales"

- See the forecasted sales value instantly

## 📸 Screenshots


## 🤝 Contributing

- Contributions and feedback are welcome!

- Steps to contribute:

  - Fork this repository

  - Create a new feature branch

  - Commit your changes

  - Submit a pull request 🚀

## ⭐ If You Liked This Project
- Please consider giving it a 🌟 Star on GitHub! It helps a lot.

## 📄 License
- This project is licensed under the MIT License.

## 👨‍💻 Author
**Anshuman Dash**   

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/ANSH5252) 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/anshuman-dash-739793351/)