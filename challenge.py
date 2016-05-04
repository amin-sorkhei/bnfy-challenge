__author__ = 'sorkhei'

import pandas as pd
from pandas.tseries.offsets import DateOffset

def task2():
    '''
    :return: a csv file called merged.csv where each row is a movie ID, genre and corresponding tags as a long string
    separated by '-'
    '''
    tags = pd.read_csv('tags.csv', names=['id', 'tag'], skiprows=1)
    movies = pd.read_csv('sub_filter_2_600each.csv', names=['id','genres'], usecols=[0,2], skiprows=1)

    # to avoid any warning and errors and make sure everything is fine and smooth
    tags['tag'] = tags['tag'].astype(str)
    merged_table = pd.merge(movies, tags)

    # print merged_table
    result = merged_table.groupby(['id', 'genres'])['tag'].apply(lambda x: '-'.join(x))
    result_csv = open('merged.csv', 'w')
    result.to_csv(result_csv, header='movie_title, genre, tags')
    print 'please take a look at the result.csv'




def task3():
    '''
    :return: Print the balance mean for the last three months
    '''

    '''
    PLEASE note that
    1-The most recent transaction date is considered as the time basis
    2-Mean is taken over all the bank accounts
    '''

    transactions = pd.read_csv('account.csv', names=['date', 'balance'], usecols=[3, 4], skiprows=1)
    transactions['balance'] = transactions['balance'].astype(int)
    transactions['date'] = pd.to_datetime(transactions['date'])

    base_time = pd.to_datetime(transactions['date'].max()) - DateOffset(months=3)
    print transactions[transactions['date'] > base_time]['balance'].mean()


def task3_b():
    '''
    :return: Print the balance for the last three months
    '''

    '''
    PLEASE note that
    1-The most recent transaction date is considered as the time basis
    2-Mean is taken over all unique bank accounts
    '''
    transactions = pd.read_csv('account.csv', names=['account_no', 'date', 'balance'], usecols=[2, 3, 4], skiprows=1)
    transactions['balance'] = transactions['balance'].astype(int)
    transactions['date'] = pd.to_datetime(transactions['date'])

    unique_accounts = transactions.groupby('account_no')
    base_time = pd.to_datetime(transactions['date'].max()) - DateOffset(months=3)
    print unique_accounts.apply(lambda x: x[x['date'] > base_time]['balance'].mean())


def task3_c():
    '''
    :return: Print the balance for the last three months
    '''

    '''
    PLEASE note that
    1-The most recent transaction date for each bank account is considered as the time basis
    2-Mean is taken over all unique bank accounts
    '''
    transactions = pd.read_csv('account.csv', names=['account_no', 'date', 'balance'], usecols=[2, 3, 4], skiprows=1)
    transactions['balance'] = transactions['balance'].astype(int)
    transactions['date'] = pd.to_datetime(transactions['date'])

    unique_accounts = transactions.groupby('account_no')
    base_time = pd.to_datetime(transactions['date'].max()) - DateOffset(months=3)
    print unique_accounts.apply(lambda x: x[x['date'] > pd.to_datetime(x['date'].max()) - DateOffset(months=3)]\
        ['balance'].mean())

