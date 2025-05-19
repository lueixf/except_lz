import pandas as pd

class df_except:

    def __init__(self, name, name2, name3): 
        self.name = name
        self.name2 = name2
        self.name3 = name3

    def data (self):
        try:
            pd.read_csv(self.name3)
        except FileNotFoundError as e:
            print(f"возникла следующая ошибка:{e}")

    def open(self): 
        
        try:
            pd.read_csv(self.name2)
        except  pd.errors.EmptyDataError:
            print(f"Возникла сдующая ошибка: Датафрейм {self.name2} пуст.")

    def false(self):

        df1 = pd.read_csv('var11.csv')
        df2 = pd.read_csv('var1.csv')
        res1 = list(df1.columns)
        res2 = list(df2.columns)

        if res1 == res2:
            print("Чтение датафрейма завершено успешно.") 
        else:
            print("Структура датафрейма НЕ соответствует ожидаемой.")

            try:
                res1 == res2
            except:
                print(f"-Названия столбцов НЕ совпадают.")
                print(f"Ожидаемые:{res1}")
                print(f"Фактический:{res2}")
            
            common_col = df1.columns.intersection(df2.columns)

            for col in common_col:
                dtype1 = df1[col].dtype
                dtype2 = df2[col].dtype
                print(f"- В столбце {col} тип дфнных не соответствует ожидаемому.")
                print(f"Ожидается: {dtype1}, Фактически: {dtype2}")

            print("Чтение датафрейма завершено успешно.") 

    def main():

        file_path = "var1.csv"
        file_path2 = "var3.csv"
        file_path3 = "var11.csv"
        processor = df_except(file_path, file_path2, file_path3)
        processor.data()
        processor.open()
        processor.false()

    if __name__ == "__main__":
        main()   


