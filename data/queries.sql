'First we need to select whole-food that are plant based

  2 - Spices and Herbs
  9 - Fruits and Fruit Juices
 11 - Vegetables and Vegetable Products
 12 - Nut and Seed Products
 16 - Legumes and Legume Products
 20 - Cereal Grains and Pasta

In the `food` table we have 390,292 entries.
In the `wfpb_food` table we will have 8,380 entries.

Less noise and faster queries.
'

create table wfpb_food as select * from food where food_category_id in (2, 9, 11, 12, 16, 20);

'Then remove irrelevant food items by name
delete from wfpb_food where description like '%KEYWORD%'

The following keywords were found relevant:
- butter
- Pasta
- FLOUR
- ENRICHED
- Hummus
- HUMMUS
- SILK
'

'Next we need to filter `food_nutrient` association table from foods that are
not wfpb.

In the `food_nutrient` table we have 6,173,460 entries.
In the `wfpb_food_nutrient` table we will have 175,221 entries.
'

create table wfpb_food_nutrient as select * from food_nutrient where fdc_id in (select fdc_id from wfpb_food);

'Finally make your query'
select f.description name, fc.description category, j.name, j.amount, j.unit_name from wfpb_food f, (select fn.fdc_id, n.name, fn.amount, n.unit_name from wfpb_food_nutrient fn,
 nutrient n on fn.nutrient_id = n.id where n.id=1103) j on f.fdc_id=j.fdc_id, food_category fc on f.food_category_id=fc.id where category='Grains' order by amount + 0 desc limit 40;
