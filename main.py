import pandas as pd
import matplotlib.pyplot as plt

# assign csv to an object
cc_statement = pd.read_csv("/Users/bradenlowe/Desktop/CreditCard Analysis/activity (2).csv")
cc_multipliers = pd.read_csv("/Users/bradenlowe/Desktop/CreditCard Analysis/CreditCard Multipliers - Sheet1.csv")

# create new df with only spent and category from cc statement
statement_consice = cc_statement[['Amount', 'Category']]
multiplier_consise = cc_multipliers[['Card', 'Restraunts', 'Grocieries', 'Flights', 'Hotel', 'Elsewhere', 'Streaming']]

# itterate through statment to find total spent in each category
#def spendPerCategory():
    
spend = {    
            "restraunt": 0,
            "grocieries": 0, 
            "flights": 0,
            "hotel": 0,
            "streaming": 0,
            "all_other": 0
        }
for index, row in statement_consice.iterrows():
    category = str(row['Category'])
    amount = row['Amount']
        
    if "Restaurant" in category:
        spend['restraunt'] += amount
    elif "Groceries" in category:
        spend['grocieries'] += amount
    elif "Airline" in category:
        spend['flights'] += amount
    elif "Travel Agencies" in category:
        spend['hotel'] += amount
    elif "streaming" in category:
        spend['streaming'] += amount
    else:
        spend['all_other'] += amount
    
#    plt.bar(range(len(spend)), list(spend.values()), align='center')
#    plt.xticks(range(len(spend)), list(spend.keys()))

#    plt.xlabel('Keys')  
#    plt.ylabel('Spent')
#    plt.title('Total Spent in Each Category')

#    plt.show()    
#    return spend

# spendPerCategory()

## def multipliers():
#def points():
points = {
    'Gold': 0,
    'Sapphire Preffered': 0,
    'Venture X': 0,
    'Sapphire Reserve': 0,
    'Platinum': 0,
    'Capital One': 0
    }
    
for index, card in multiplier_consise.iterrows():
    
    
    print(card)

