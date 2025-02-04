from enum import Enum

from pydantic import BaseModel

from metagpt.prompts.task_type import (
    FEATURE_ENGINEERING_PROMPT,
    IMAGE2WEBPAGE_PROMPT,
    MODEL_EVALUATE_PROMPT,
    MODEL_TRAIN_PROMPT, FUTURES_CONTRACT_PROMPT, CALCULATE_MAIN_CONTRACT_PROMPT,
)


class TaskTypeDef(BaseModel):
    name: str
    desc: str = ""
    guidance: str = ""


class TaskType(Enum):
    """By identifying specific types of tasks, we can inject human priors (guidance) to help task solving"""

    # EDA = TaskTypeDef(
    #     name="eda",
    #     desc="For performing exploratory data analysis",
    #     guidance=EDA_PROMPT,
    # )
    FUTURES_CONTRACT_PREPROCESS = TaskTypeDef(
        name="futures contract preprocess",
        desc="Read and clean the data from the CSV file, identifying the volume and RIC columns; Drop nan value, and the started some lines include the nan value, please read the middle lines to identify the input csv file's structure",
        guidance=FUTURES_CONTRACT_PROMPT,
    )
    CALCULATE_MAIN_CONTRACT = TaskTypeDef(
        name="calculate main contract",
        desc="Calculate the main contract by summing trading volumes and identify the main RIC for each day; Determine the main contract (RIC identifier) based on the trading volume with sum operation by RIC and time window previous to the target day, defualt time window length is 1 day",
        guidance=CALCULATE_MAIN_CONTRACT_PROMPT,
    )


    # FEATURE_ENGINEERING = TaskTypeDef(
    #     name="fea new columnsture engineering",
    #     desc="Only for creating for input data.",
    #     guidance=FEATURE_ENGINEERING_PROMPT,
    # )
    # MODEL_TRAIN = TaskTypeDef(
    #     name="model train",
    #     desc="Only for training model.",
    #     guidance=MODEL_TRAIN_PROMPT,
    # )
    # MODEL_EVALUATE = TaskTypeDef(
    #     name="model evaluate",
    #     desc="Only for evaluating model.",
    #     guidance=MODEL_EVALUATE_PROMPT,
    # )
    # IMAGE2WEBPAGE = TaskTypeDef(
    #     name="image2webpage",
    #     desc="For converting image into webpage code.",
    #     guidance=IMAGE2WEBPAGE_PROMPT,
    # )
    OTHER = TaskTypeDef(name="other", desc="Any tasks not in the defined categories")

    # Legacy TaskType to support tool recommendation using type match. You don't need to define task types if you have no human priors to inject.
    # TEXT2IMAGE = TaskTypeDef(
    #     name="text2image",
    #     desc="Related to text2image, image2image using stable diffusion model.",
    # )
    # WEBSCRAPING = TaskTypeDef(
    #     name="web scraping",
    #     desc="For scraping data from web pages.",
    # )
    # EMAIL_LOGIN = TaskTypeDef(
    #     name="email login",
    #     desc="For logging to an email.",
    # )

    @property
    def type_name(self):
        return self.value.name

    @classmethod
    def get_type(cls, type_name):
        for member in cls:
            if member.type_name == type_name:
                return member.value
        return None
