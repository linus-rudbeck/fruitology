import ast
import pandas as pd


class DataProcessor:
    def __init__(self, filename="data.csv"):
        self.filename = filename
        self.df = None
    
    def load_data(self):
        self.df = pd.read_csv(self.filename)
    
    def process_nutritions(self):
        self.df["nutritions"] = self.df["nutritions"].apply(ast.literal_eval)
        
        nutritions_list = self.df["nutritions"].tolist()
        nutritions_df = pd.DataFrame(nutritions_list)

        self.df = pd.concat([self.df, nutritions_df], axis=1)

        self.df.drop(columns=["nutritions"], inplace=True)
    
    def calculate_mean_nutrition(self):
        columns = ["calories", "fat"]
        return self.df[columns].mean()
    
    def process_data(self):
        self.load_data()
        self.process_nutritions()
        return self.calculate_mean_nutrition()