import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000  # 행 수

states = ['QLD', 'NSW', 'VIC', 'WA', 'SA', 'NT']
vehicle_types = ['Heavy Duty Truck', 'Medium Duty Truck', 'Light Commercial', 'Construction Equipment', 'Bus']
industries = ['Mining', 'Construction', 'Logistics', 'Agriculture', 'Government']

df = pd.DataFrame({
    'sale_id': range(1, n+1),
    'date': pd.date_range('2022-01-01', '2024-12-31', periods=n).strftime('%Y-%m-%d'),
    'vehicle_type': np.random.choice(vehicle_types, n),
    'state': np.random.choice(states, n),
    'industry': np.random.choice(industries, n),
    'unit_price': np.random.randint(90000, 500000, n), 
    'units_sold': np.random.choice([1, 2, 3, 5], n),
})

df['revenue'] = df['unit_price'] * df['units_sold']  



# 결측값 인위적으로 추가 (실제 데이터 시뮬레이션)
df.loc[np.random.choice(df.index, 30), 'industry'] = np.nan
df.loc[np.random.choice(df.index, 20), 'unit_price'] = np.nan


df.to_csv('data/sales_data.csv', index=False)
print(df.head())

