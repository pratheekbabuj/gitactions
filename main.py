import pandas as pd

class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.xlsx'):
            self.data = pd.read_excel(self.file_path)
        else:
            raise ValueError("Unsupported file format. Only CSV and XLSX are supported.")

    def summarize_numeric_variables(self):
        if self.data is None:
            print("Data has not been loaded. Please call the load_data() method first.")
            return
        
        numeric_columns = self.data.select_dtypes(include=['number'])
        summary = numeric_columns.describe()
        print("Summary of Numeric Variables:")
        print(summary)

# Example usage
data_analyzer = DataAnalyzer('titanic.csv')
data_analyzer.load_data()
data_analyzer.summarize_numeric_variables()
