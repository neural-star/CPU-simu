import os
import json
import pandas as pd

def read_settings(path: str, bit: int = 4, register=True):
    df = pd.read_excel(path)
    name = df.columns[0]
    columns = [name, "2/2Byte", "3/2Byte", "4/2Byte", "説明・備考"]
    commands = {}

    for i in range(len(df)):
        opecode = df.iloc[i, 1:bit+1].fillna("").astype(str).str.cat()
        commands[opecode] = df.loc[i, columns].fillna("").tolist()

    if register:
        settingspath = fr"databases\{name}.json"
    else:
        settingspath = r"databases\temp.json"
    os.makedirs(os.path.dirname(settingspath), exist_ok=True)
    with open(settingspath, "w", encoding="utf-8") as f:
        json.dump(commands, f, indent=4, ensure_ascii=False)
