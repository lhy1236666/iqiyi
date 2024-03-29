import pandas as pd

# 创建一个字典
mapping = {
    'id': ['1'],
    'name': ['lee']
}
new_data = {
    'id': ['2'],
    
}

# 将字典转换为DataFrame
df = pd.DataFrame(mapping)

# 将DataFrame保存为csv文件
df.to_csv('my_dict_data.csv', index=False)

# 从csv文件中读取数据并转换为DataFrame
df_read = pd.read_csv('my_dict_data.csv')

# 打印读取的DataFrame
print(df_read)
mapping={}
mapping['id']=['2']
print(mapping)
new_df = pd.DataFrame(new_data)

# 读取已有的CSV文件
existing_df = pd.read_csv('my_dict_data.csv')

# 将新数据添加到已有数据的末尾
combined_df = pd.concat([existing_df, new_df], ignore_index=True)

# 将合并后的DataFrame保存为CSV文件
combined_df.to_csv('my_dict_data.csv', index=False)
# 读取保存的CSV文件
df_read = pd.read_csv('./data/my_dict_data.csv')

# 打印读取的DataFrame
print(df_read)



df = pd.read_csv('./data/my_dict_data.csv')

# 根据条件筛选出id为1的行，并提取name列的值
name_value = df[df['id'] == 7]['introdution'].values[0]
first_row_name = df.iloc[0]
name_data = df['id'].values
print(f"The name value of the first row is: {first_row_name}")
print(f"The name value for id=1 is: {name_value}")
print(len(name_data))