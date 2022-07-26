
import pandas as pd
import numpy as np
import os

class filter_options:
    def __init__(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        self.df= pd.read_excel(f'{basedir}/cmap_sheet.xlsx', 'Sheet1')

    def get_categories(self): #returns a list of cloud categories to be listed on select menu on forms page
        items= self.df['Service_category'].unique()
        results= [(item, item) for item in items] ##flask wtf requires tuples of data and id
        results.insert(0, ("Choose...", "Choose..."))
        return results

    def get_service_type(self, category=None):
        if category is None: items= self.df['Service_type'].unique()
        else: items= self.df.loc[self.df['Service_category'] == category, 'Service_type'].unique()
        results= [(item, item) for item in items] ##flask wtf requires tuples of data and id
        results.insert(0, ("Choose...", "Choose..."))
        return results

    def get_products(self, category, type):
        res= (self.df.query('Service_category== @category and Service_type== @type')).to_dict('list')
        products= {'gcp': res['gcp_offering'][0].split(',')[0],
                    'aws': res['aws_offering'][0].split(',')[0],
                    'azure': res['azure_offering'][0].split(',')[0]}
        return products

