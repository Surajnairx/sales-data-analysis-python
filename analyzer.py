import pandas as pd
import json 
import os

from helper import calculate_total, format_currency

df = pd.read_csv('data/sales.csv')
print('CSV DATA :')
print(df)
print('\n')

totals = []

for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

# Add totals to our data
df['total'] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")

print(df)

os.makedirs('output', exist_ok=True)

df.to_json('output/sales_data.json', orient='records', indent=2)

df.to_csv('output/sales_with_totals.csv', index=False)


print("\nFiles saved:")
print("- output/sales_data.json")

print("- output/sales_with_totals.csv")