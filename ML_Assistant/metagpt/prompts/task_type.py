# Prompt for taking on "eda" tasks
EDA_PROMPT = """
The current task is about exploratory data analysis, please note the following:
- Distinguish column types with `select_dtypes` for tailored analysis and visualization, such as correlation.
- Remember to `import numpy as np` before using Numpy functions.
"""

# Prompt for taking on "data_preprocess" tasks
FUTURES_CONTRACT_PROMPT = """
The current task is about data preprocessing, please note the following:
- Read the CSV file from a specified file path (e.g., /path/to/your/file.csv).
- Print the first several rows of the CSV file to inspect its structure. This will help determine the correct column names for trading dates, trading volume, and contract identifiers (RIC).
- Identify some essential columns, for example:
    •	Trade Date: The column representing the trading date (e.g., “Trade Date”). Convert this column to datetime format.
	•	Volume: The column representing the trading volume (e.g., “Volume” or “TradingVolume”). Ensure this column is numeric (convert to integer if necessary, handling any formatting issues such as commas).
	•	RIC: The column representing the contract identifier. Ensure this column is treated as a string.
- Remove all rows containing any NaN values to ensure clean data.
"""

CALCULATE_MAIN_CONTRACT_PROMPT = """
- Calculate the main contract by summing trading volumes and identify the main RIC for each day
- Determine the main contract (RIC identifier) based on the trading volume with sum operation by RIC and specific date, the specific date is determined by an offset and target date, the default offset is -1 (which means 1 day prior to target date)
- Group the data by “Trade Date” and “RIC”, summing up the trading volume for each group; Notice as_index if groupby is applied
"""

# Prompt for taking on "feature_engineering" tasks
FEATURE_ENGINEERING_PROMPT = """
The current task is about feature engineering. when performing it, please adhere to the following principles:
- Generate as diverse features as possible to improve the model's performance step-by-step. 
- Use available feature engineering tools if they are potential impactful.
- Avoid creating redundant or excessively numerous features in one step.
- Exclude ID columns from feature generation and remove them.
- Each feature engineering operation performed on the train set must also applies to the test separately at the same time.
- Avoid using the label column to create features, except for cat encoding.
- Use the data from previous task result if exist, do not mock or reload data yourself.
- Always copy the DataFrame before processing it and use the copy to process.
"""

# Prompt for taking on "model_train" tasks
MODEL_TRAIN_PROMPT = """
The current task is about training a model, please ensure high performance:
- Keep in mind that your user prioritizes results and is highly focused on model performance. So, when needed, feel free to use models of any complexity to improve effectiveness, such as XGBoost, CatBoost, etc.
- If non-numeric columns exist, perform label encode together with all steps.
- Use the data from previous task result directly, do not mock or reload data yourself.
- Set suitable hyperparameters for the model, make metrics as high as possible.
"""

# Prompt for taking on "model_evaluate" tasks
MODEL_EVALUATE_PROMPT = """
The current task is about evaluating a model, please note the following:
- Ensure that the evaluated data is same processed as the training data. If not, remember use object in 'Done Tasks' to transform the data.
- Use trained model from previous task result directly, do not mock or reload model yourself.
"""

# Prompt for taking on "image2webpage" tasks
IMAGE2WEBPAGE_PROMPT = """
The current task is about converting image into webpage code. please note the following:
- Single-Step Code Generation: Execute the entire code generation process in a single step, encompassing HTML, CSS, and JavaScript. Avoid fragmenting the code generation into multiple separate steps to maintain consistency and simplify the development workflow.
- Save webpages: Be sure to use the save method provided.
"""
