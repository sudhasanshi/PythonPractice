import pandas as pd

filename="sample.xlsx"
output="sample.json"

def excel_to_json(name, json_file):
    df =  pd.read_excel(name, sheet_name="Sheet1")
    df_stripped = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df_stripped.to_json(json_file, orient='records', indent=4)
    print("json file created successfully")

   
excel_to_json(filename, output)
