# Calories Burned Prediction - Kaggle Playground Series S5E5

This project is a solution for the [Kaggle Playground Series S5E5 competition](https://www.kaggle.com/competitions/playground-series-s5e5).

---

## Project Structure

- `app/` — Streamlit app files for interactive calorie prediction
- `models/` — Saved machine learning models and preprocessing artifacts
- `notebooks/` — Jupyter notebooks for EDA, modeling, and analysis
- `requirements.txt` — Python dependencies
- `submission (8).csv` — Sample submission file

---

## Dataset

The dataset is **not included** here due to size constraints.  
Please download the data directly from the [Kaggle competition page](https://www.kaggle.com/competitions/playground-series-s5e5/data).

### Sample data preview:

**Train data (first 5 rows):**

| id | Sex    | Age | Height | Weight | Duration | Heart_Rate | Body_Temp | Calories |
|----|--------|-----|--------|--------|----------|------------|-----------|----------|
| 0  | male   | 36  | 189.0  | 82.0   | 26.0     | 101.0      | 41.0      | 150.0    |
| 1  | female | 64  | 163.0  | 60.0   | 8.0      | 85.0       | 39.7      | 34.0     |
| 2  | female | 51  | 161.0  | 64.0   | 7.0      | 84.0       | 39.8      | 29.0     |
| 3  | male   | 20  | 192.0  | 90.0   | 25.0     | 105.0      | 40.7      | 140.0    |
| 4  | female | 38  | 166.0  | 61.0   | 25.0     | 102.0      | 40.6      | 146.0    |

**Test data (first 5 rows):**

| id     | Sex    | Age | Height | Weight | Duration | Heart_Rate | Body_Temp |
|--------|--------|-----|--------|--------|----------|------------|-----------|
| 750000 | male   | 45  | 177.0  | 81.0   | 7.0      | 87.0       | 39.8      |
| 750001 | male   | 26  | 200.0  | 97.0   | 20.0     | 101.0      | 40.5      |
| 750002 | female | 29  | 188.0  | 85.0   | 16.0     | 102.0      | 40.4      |
| 750003 | female | 39  | 172.0  | 73.0   | 20.0     | 107.0      | 40.6      |
| 750004 | female | 30  | 173.0  | 67.0   | 16.0     | 94.0       | 40.5      |

---

## Approach

### Models Tried

- **LightGBM**  
  - RMSE: 3.6037  
  - MAE: 2.1762  
  - R²: 0.9966  
  - RMSLE: 0.0620

- **CatBoost**  
  - RMSE: 3.5561  
  - MAE: 2.1225  
  - R²: 0.9967  
  - RMSLE: 0.0614

### Model Choice

The final model chosen was **CatBoostRegressor** because it gave better performance metrics compared to LightGBM and handles categorical features natively, which simplifies preprocessing. Additionally, CatBoost is known for robustness on tabular data and good speed on this dataset size.

---

## How to Run

1. Clone the repo.
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the data files from [Kaggle competition](https://www.kaggle.com/competitions/playground-series-s5e5/data) and place them in the root folder or update paths accordingly in the notebooks or scripts.

4. Run the training notebook or script to train the model and save artifacts.

5. Run the Streamlit app to interactively predict calories burned:

    ```bash
    streamlit run app/app.py
    ```

---

## Files Description

- **`train_save_model.ipynb`** — Notebook to preprocess data, train CatBoost model, and save the model, scaler, and feature list.
- **`app/app.py`** — Streamlit app for interactive calorie prediction.
- **`requirements.txt`** — Required Python libraries:

    ```
    pandas
    numpy
    catboost
    scikit-learn
    joblib
    streamlit
    ```

- **`notebooks/eda.ipynb`** — Exploratory Data Analysis with visuals and metric comparison.

---

## Videos

Click on images below to see videos of the output app, and power bi dashboard!!

---

[![Watch Video 1](https://img.youtube.com/vi/pU8obDOXmoU/maxresdefault.jpg)](https://youtu.be/pU8obDOXmoU)

[![Watch Video 2](https://img.youtube.com/vi/tUagI4G9kLU/maxresdefault.jpg)](https://youtu.be/tUagI4G9kLU)


---

## Contact

For questions or feedback, feel free to reach out.

---

*Good luck and happy modeling!*
