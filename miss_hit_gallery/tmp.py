import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from os import path as pth


this_path = pth.dirname(pth.abspath(__file__))
data_folder = pth.join(this_path, "..", "tmp")

directory = ""

headers = ["path", "file", "file_length", "function", 'cnest', 'cyc', 'function_length', 'globals', 'npath', 'parameters', 'persistent']

dict_to_import = {key: [] for key in headers}


with open(pth.join(data_folder, "cpp_spm.json"), 'r') as ff:
    data = json.load(ff)

for file in data["metrics"].keys():

    if pth.dirname(file) != directory:
        directory = pth.dirname(file)
        tmp = directory
    else:
        tmp = ""
    
    print(f"{tmp}")

    file_name = pth.basename(file)
    file_length = data["metrics"][file]["file_metrics"]["file_length"]["measure"]

    print(f"\t{file_name}\n\tfile length: {file_length}")



    keys = ['cnest', 'cyc', 'function_length', 'globals', 'npath', 'parameters', 'persistent']

    for function in data["metrics"][file]["function_metrics"].keys():

        print(f"\t{function}")

        dict_to_import["path"].append(directory)
        dict_to_import["file"].append(file_name)
        dict_to_import["file_length"].append(file_length)
        dict_to_import["function"].append(function)

        for key in keys:

            value=data["metrics"][file]["function_metrics"][function][key]["measure"]

            print(f"\t\t{key}: {value}")

            dict_to_import[key].append(value)


df = pd.DataFrame(dict_to_import)

print(df.head())


sns.histplot(data=df, x="cyc", shrink=3)

plt.show()
