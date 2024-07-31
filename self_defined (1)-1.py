#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[30]:


def col_types(df):
    """
    The function takes the dataframe as input
    and returns the numeric and non numeric columns seperately
    """
    cat_cols = [col for col in df.columns if df[col].dtypes == "O"]
    num_cols = [col for col in df.columns if df[col].dtypes != "O"]
    return cat_cols,num_cols
    #print(f'There are total {len(cat_cols)} Categorical variables:{(cat_cols)} ')
    #print(f'There are total {len(num_cols)} Numeric variables:{(num_cols)} ')


# In[26]:


cat_cols = col_types(df)[0]
num_cols = col_types(df)[1]


# In[31]:


def cat_sy(df, col_name, plot=False):
    """
    The function takes the dataset as input
    seperates the categorical variables and
    returs the count of different types of each categorical variable
    and the percentage of each type under the categorical varibale
    
    It gives the count plot wich sows the percentage of each categorical variable
    """
    
    print(pd.DataFrame({col_name: df[col_name].value_counts(),
                         "Percentage": 100 * df[col_name].value_counts() / len(df)}))
    
    if plot:
        sns.countplot(x=df[col_name], data=df)
        plt.xticks(rotation=90)
        plt.show(block=True)


# In[32]:


def num_sy(df, num_col, plot=False):
    """
    The function takes the dataset as input
    seperates the numerical variables and
    calculates the basic descriptive stats and quantiles of each numerical variable
    and creates histograms for each numeric variable
    """
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.90, 0.95, 0.99]
    print(df[num_col].describe(quantiles).T)

    if plot:
        df[num_col].hist(bins=50, figsize=(9,5))
        plt.xlabel(num_col)
        plt.title(num_col)
        plt.show()


# In[ ]:




