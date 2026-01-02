import pandas as pd 
import json


# df = pd.read_excel('ods_files/Annual_exam_marks.ods', engine='odf')
# print(df)

# Skip row 1 (title), use row 2 as header
df = pd.read_excel(
    'ods_files/Annual_exam_marks.ods',
    engine='odf',
    header=1  # Use row 2 as header (0-indexed: row 1)
)

# print("Column names (from row 2):")
print(df.columns.tolist())
# print(f"\nNumber of data rows (starting from row 3): {len(df)}")

# Convert to dictionaries
rows_dict = df.to_dict('records')

# print(rows_dict)


# print("\n" + "="*50)
# print("EACH DATA ROW AS DICTIONARY:")
# print("="*50)

# for i, row in enumerate(rows_dict, start=3):  # Data starts at row 3
#     print(f"\n📋 Excel Row {i}:")
#     print(row)
    
rows_dict_json = json.dumps(rows_dict, indent=2)
# print(rows_dict_json)

with open('result_array.json' , 'w') as f:
    f.write(rows_dict_json)