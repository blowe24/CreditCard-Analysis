import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# assign csv to an object
cc_statement = pd.read_csv("/Users/bradenlowe/Desktop/CreditCard Analysis/activity (2).csv")
cc_multipliers = pd.read_csv("/Users/bradenlowe/Desktop/CreditCard Analysis/CreditCard Multipliers - Sheet1.csv")

# create new df with only spent and category from cc statement
statement_consice = cc_statement[['Amount', 'Category']]
multiplier_consise = cc_multipliers[['Card', 'Restraunts', 'Grocieries', 'Flights', 'Hotel', 'Elsewhere', 'Streaming']]

# itterate through statment to find total spent in each category    
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
    
# Points dictionary for each card
points = {
    'Gold': 0,
    'Sapphire Preffered': 0,
    'Venture X': 0,
    'Sapphire Reserve': 0,
    'Platinum': 0,
    'Venture': 0
    }

## Define the multipliers fro each card
multipliers = {}
for index, row in multiplier_consise.iterrows():
    card = row['Card']
    multipliers[card] = {
        'Restraunts': row['Restraunts'],
        'Grocieries': row['Grocieries'],
        'Flights': row['Flights'],
        'Hotel': row['Hotel'],
        'Elsewhere': row['Elsewhere'],
        'Streaming': row['Streaming']
    }

# function to calculate points
def calculatePoints(card, amount, multipliers):
    if card in multipliers:
        multiplier = multipliers[card]
        points = amount * multiplier['Restraunts']
        points += amount * multiplier['Grocieries']
        points += amount * multiplier['Flights']
        points += amount * multiplier['Hotel']
        points += amount * multiplier['Elsewhere']
        points += amount * multiplier['Streaming']
        return points
    else:
        return 0  # return 0 if card is not found in multipliers

# iterate through each card and add to total points
for index, row in multiplier_consise.iterrows():
    card = row['Card']
    total_points = 0
    total_points += calculatePoints(card, spend['restraunt'], multipliers)
    total_points += calculatePoints(card, spend['grocieries'], multipliers)
    total_points += calculatePoints(card, spend['flights'], multipliers)
    total_points += calculatePoints(card, spend['hotel'], multipliers)
    total_points += calculatePoints(card, spend['streaming'], multipliers)
    total_points += calculatePoints(card, spend['all_other'], multipliers)
    points[card] = total_points

# Visualizations # seaborn theme
sns.set_theme(style="white", palette=None)
sns.color_palette("Blues", as_cmap=True)

# Bar grapth showing total points   

points_df = pd.DataFrame.from_dict(points, orient='index')
points = dict(sorted(points.items(), key=lambda item: item[1], reverse=True))

cmap = plt.cm.get_cmap('viridis')

plt.bar(range(len(points)), list(points.values()), align='center')
plt.xticks(range(len(points)), list(points.keys()))

plt.xlabel('Cards')  
plt.ylabel('Total Points')
plt.title('Total Potential Points by Card')

plt.show()
