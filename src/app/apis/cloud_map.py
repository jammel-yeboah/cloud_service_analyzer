import pandas as pd

df= pd.read_excel("apis/cmap_sheet.xlsx", "Sheet1")
print(df)

class Options:
    def get_categories(): #returns a list of cloud categories to be listed on select menu on forms page
        items= df['Service category'].unique()
        results= [(item, item) for item in items] ##flask wtf requires tuples of data and id
        return results

    def get_service_type():
        pass



