def split_csv_string(csv_string):
  items = csv_string.split(',')
  return items
csv_data = "apple,banana,pear,orange"
items_list = split_csv_string(csv_data)
print(items_list)