import pandas as pd
arr = ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4']

cars = {'Brand': arr,
        'Price': [32000,35000,37000,45000]
        }

df = pd.DataFrame(cars, columns = ['Brand', 'Price'])

print (df)

df.to_excel (r'C:\Users\nguye\Desktop\export_dataframe.xlsx', index = True, header=True)
