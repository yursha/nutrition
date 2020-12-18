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
         fn.amount nutrient_amount_per_100g,
         (fn.amount * 100 / energy.amount) nutrient_amount_per_100kcal,
         (fn.amount / fat.amount) nutrient_amount_per_1gfat
    FROM food_nutrient fn
      JOIN nutrient n ON fn.nutrient_id = n.id
      JOIN food f ON f.fdc_id = fn.fdc_id
      JOIN food_category fc ON f.food_category_id = fc.id
      JOIN (SELECT fdc_id, amount FROM food_nutrient WHERE nutrient_id = 1008) energy
           ON fn.fdc_id = energy.fdc_id
      JOIN (SELECT fdc_id, amount FROM food_nutrient WHERE nutrient_id = 1004) fat
           ON fn.fdc_id = fat.fdc_id
    WHERE f.food_category_id in (1, 2, 9, 11, 12, 15, 16, 20)
    ORDER BY (nutrient_amount_per_100g + 0) DESC
""")
nutrients = c.fetchall()

c.execute("SELECT * FROM nutrition_dri WHERE fdc_nutrient_id <> '' AND amount <> 'ND'")
dri = c.fetchall()

data = json.dumps({'nutrients': nutrients, 'dri': dri})

con.close()

with open('data.json', 'w') as output:
  output.write(data)
