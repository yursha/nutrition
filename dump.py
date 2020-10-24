import sqlite3
import json

con = sqlite3.connect('db')
c = con.cursor()

print('Querying database')
c.execute("""
  SELECT
         f.description food_name,
         fc.id food_category_id,
         n.id nutrient_id,
         n.name nutrient_name,
         n.unit_name nutrient_unit,
         fn.amount nutrient_amount_per_100g
    FROM food_nutrient fn
      JOIN nutrient n ON fn.nutrient_id = n.id
      JOIN food f ON f.fdc_id = fn.fdc_id
      JOIN food_category fc ON f.food_category_id = fc.id
    WHERE f.food_category_id in (1, 2, 9, 11, 12, 15, 16, 20)
    ORDER BY (nutrient_amount_per_100g + 0) DESC
""")
data = json.dumps(c.fetchall())

con.close()

with open('data.json', 'w') as output:
  output.write(data)
