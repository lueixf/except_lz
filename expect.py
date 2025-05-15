import pandas as pd
class df_except:
    def __init__(self):
        try:
            df = pd.read_csv('var1.csv')
        except FileNotFoundError :
            print('Файл отсутствует')
        except pd.errors.EmptyDataError:
            print('файл пустой')
        except pd.errors.ParserError:
            print('Файл не соответствует ожидаемой структуре ')

    def check(self):
        pass