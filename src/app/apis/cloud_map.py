
import pandas as pd
from pprint import pprint

df= pd.read_excel("cmap_sheet.xlsx", "Sheet1")

class Options:
    def get_categories(): #returns a list of cloud categories to be listed on select menu on forms page
        items= df['Service category'].unique()
        results= [(item, item) for item in items] ##flask wtf requires tuples of data and id
        return results

    def get_service_type():
        pass


def q(category, type):
    res= (df.query('Service_category== @category and Service_type== @type')).to_dict('list')
    print(res)
    print(res['aws_offering'][0])

q('Compute', 'FaaS')



