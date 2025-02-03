import asyncio

from metagpt.actions import WriteAnalysisCode
from metagpt.roles.di.data_interpreter import DataInterpreter
from metagpt.utils.recovery_util import save_history
from shared_queue import log_execution


# async def main(requirement: str):
#     role = DataInterpreter(use_reflection=True, tools=["<all>"])
#     # role = DataInterpreter(use_reflection=True)
#     await role.run(requirement)
#     save_history(role=role)

async def main_generator(requirement: str):
    await log_execution("#### 🔥Starting main function\n")
    role = DataInterpreter(use_reflection=True, tools=["<all>"])
    await role.run(requirement)
    role.set_actions([WriteAnalysisCode])
    role._set_state(0)
    await role.run(requirement_2)
    save_history(role=role)
    await log_execution("#### Finished main function😊\n")

async def main_generator_with_interpreter(interpreter: DataInterpreter, requirement: str):
    await log_execution("#### 🔥Starting main function\n")
    role = interpreter  # 假设 'interpreter' 类似于 'role'
    role.set_actions([WriteAnalysisCode])
    role._set_state(0)
    await role.run(requirement)
    save_history(role=role)
    await log_execution("#### Finished main function😊\n")


if __name__ == "__main__":
    # data_path = "your/path/to/titanic"
    # train_path = f"{data_path}/split_train.csv"
    # eval_path = f"{data_path}/split_eval.csv"
    # requirement = f"This is a titanic passenger survival dataset, your goal is to predict passenger survival outcome. The target column is Survived. Perform data analysis, data preprocessing, feature engineering, and modeling to predict the target. Report accuracy on the eval data. Train data path: '{train_path}', eval data path: '{eval_path}'."
    # requirement = "Plot a heatmap of the global warming trends for each of the European Union countries using the dataset at https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv . Save the graph at the current working dictionary named 'heatmap'. Put countries on the y-axis and years on the x-axis."
    requirement = """
    You are a quantitative trading data cleaning assistant. Your task is to identify the main futures contract based on the following requirements:
    
    Input:
    - Daily frequency futures contract data, path is /Users/tuozhou/Desktop/RA/SZRI/ChatInterpreter/data/BTC_1day.csv
    
    Steps:
    1. Identify the column representing trading volume
    2. Determine the main contract (RIC identifier) based on the trading volume of the most recent day
    3. Store the results in a DataFrame named 'df_main_ric_daily'
    
    Expected Output:
    - DataFrame containing the identified main contracts, and export the csv file
    
    Notes:
    - Main contract is defined as the contract with the highest trading volume for each day
    - RIC (Reuters Instrument Code) is used as the contract identifier
    - Drop nan value, and the started some lines include the nan value, please read the middle lines   to identify the input csv file's structure.
    - Determine the main contract (RIC identifier) based on the trading volume  with sum operation by RIC and time window previous to the target day, defualt time window length is 1 day 
"""

    # requirement_2 = (
    #     "please use the previous result add 2")
    # requirement = "This is a house price dataset, your goal is to predict the sale price of a property based on its features. The target column is SalePrice. Perform data analysis, data preprocessing, feature engineering, and modeling to predict the target. Report RMSE between the logarithm of the predicted value and the logarithm of the observed sales price on the eval data. Train data path: '/Users/tuozhou/Desktop/RA/SZRI/ML_Assistant/data/05_house-prices-advanced-regression-techniques/split_train.csv', eval data path: '/Users/tuozhou/Desktop/RA/SZRI/ML_Assistant/data/05_house-prices-advanced-regression-techniques/split_eval.csv'."
    asyncio.run(main_generator(requirement))
