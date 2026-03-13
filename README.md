
# Nepal Weather Prediction Project

This project focuses on analyzing weather data from major cities in Nepal and building machine learning models to predict temperature. The project is divided into two main parts: Exploratory Data Analysis (EDA) and Machine Learning Modeling.

## Project Structure

- `eda.ipynb`: Jupyter notebook for exploratory data analysis, data cleaning, and visualization.
- `ML_Prediction-Model.ipynb`: Jupyter notebook for building, training, and evaluating machine learning models.
- `nepal_weather_data.csv`: The original raw weather dataset.
- `cleaned_nepal_weather_data.csv`: The cleaned dataset generated from `eda.ipynb`.
- `model_comparison.csv`: A CSV file comparing the performance of the different machine learning models.
- `requirements.txt`: A list of Python libraries required to run the project.
- `README.md`: This file, providing an overview of the project.

## 1. Exploratory Data Analysis (EDA)

The `eda.ipynb` notebook performs a thorough analysis of the weather data. The key steps include:

- **Data Loading and Cleaning:** The raw data is loaded, and only the more reliable data from the "Open-Meteo_API" source is used. Data types are corrected, and new time-based features like month and day of the week are created.
- **Data Exploration:** The structure of the data, including data types, missing values, and descriptive statistics, is examined.
- **Visualization:** Various plots are generated to understand the data better:
    - Temperature trends over time for all cities.
    - Temperature distribution per city.
    - Rainfall analysis, including total rainfall per city and average monthly rainfall.
    - Wind speed analysis.
    - Correlation heatmap to show relationships between different weather features.

The cleaned data is saved to `cleaned_nepal_weather_data.csv`.

## 2. Machine Learning Modeling

The `ML_Prediction-Model.ipynb` notebook focuses on building and comparing predictive models.

- **Data Preparation:** The cleaned dataset is loaded. The features (`temp_max_c`, `precipitation_mm`, `wind_speed_max`) and the target variable (`temperature`) are defined. The data is then split into training and testing sets.
- **Model Building and Comparison:** Three different regression models are built and evaluated:
    1.  **Linear Regression:** A baseline model to establish initial performance.
    2.  **Random Forest Regressor:** An ensemble model known for its accuracy and robustness.
    3.  **Gradient Boosting Regressor:** An advanced ensemble model that often provides high performance.
- **Evaluation:** The models are evaluated using standard regression metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.
- **Visualization:** The predictions of each model are plotted against the actual values to visually assess their performance.
- **Results:** The performance metrics for all models are saved to `model_comparison.csv`.

## How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Jupyter notebooks:**
    - Start with `eda.ipynb` to perform the data analysis and generate the cleaned data file.
    - Then, run `ML_Prediction-Model.ipynb` to build and evaluate the machine learning models.

    ```bash
    jupyter notebook
    ```
