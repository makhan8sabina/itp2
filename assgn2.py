import csv
import os
import random

data_dir ='data'
os.makedirs(data_dir,
            exist_ok=True)
filepath=os.path.join(data_dir, 'students_scores.csv')
if not os.path.exists(filepath):
    print('Файл не найден')
    exit()

print(f"File found: {filepath}")
print(f"Absolute path: {os.path.abspath(filepath)}")

names =['Assiya', 'Yuliya', 'Aknur', 'Moldir', 'Alua',
        'Farkhad', 'Miras', 'Islam', 'Bekarys', 'Bekmukhammed',
        'Bakdaulet', 'Amir', 'Zhursin', 'Madi', 'Nurali',
        'Assanali', 'Danial', 'Yernur', 'Beknur', 'Damir']
genders=['Female', 'Female','Female','Female','Female',
         'Male', 'Male','Male','Male','Male',
         'Male','Male','Male','Male','Male',
         'Male','Male','Male','Male','Male']
groups=['SE-2501', 'SE-2502','SE-2503','SE-2501','SE-2502','SE-2503',
        'SE-2503','SE-2502','SE-2501','SE-2503','SE-2502',
        'SE-2501','SE-2503','SE-2502','SE-2501','SE-2503',
        'SE-2502','SE-2501','SE-2503','SE-2502','SE-2501']

with open(filepath, 'w', newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['student_id', 'name', 'gender', 'group', 'math_score', 'python_score', 'english_score'])

    for i, name in enumerate(names):
        writer.writerow([
            i+1, name, genders[i], groups[i],
            random.randint(45, 100),
            random.randint(40, 100),
            random.randint(50, 100),
        ])
print(f'Dataset saved to: {os.path.abspath(filepath)}')



print('\n'+'#'*50)
print("TASK 2")
print("#"*50)


with open(filepath, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    print(f"\nFields: {reader.fieldnames}")
    rows=list(reader)

    print('first 5 students')
    for i, row in enumerate(rows[:5]):
        print(f"  Row {i + 1}: {dict(row)}")
    print(f"\nTotal students: {len(rows)}")

import pandas as pd
print("\n" + "-"*50)
print("TASK 3")
print("-"*50)

df=pd.read_csv(filepath)
print('First 5 rows:')
print(df.head())
print(df.dtypes)

print('describe:')
print(df.describe())
score_cols=['math_score', 'python_score', 'english_score' ]
print('mean:')
print(df[score_cols].mean().round(2))
print('median:')
print(df[score_cols].median())
print(df[score_cols].std().round(2))

df['average_score']=df[score_cols].mean(axis=1).round(2)
print(df[['name', 'group', 'average_score']])

high_scorers=df[df['average_score']>=75]
print(f"\n Students with average_score >= 75 ({len(high_scorers)} students.):")
print(high_scorers[['name', 'group', 'average_score']])

group_1=df[df['group']=='SE-2501']
print(f'\n Students of SE-2501({len(group_1)} st)')
print(group_1[['name', 'gender', 'average_score']])

group_means=df.groupby('group')[score_cols].mean().round(2)
print('\n Average_score by gender')
print(group_means)

gender_means=df.groupby('gender')['average_score'].mean().round(2)
print('\n Average_score by gender')
print(gender_means)


print("\n" + "#"*50)
print("TASK 4")
print("#"*50)
import matplotlib.pyplot as plt
import seaborn as sns

group_avg=df.groupby('group')['average_score'].mean()
plt.figure(figsize=(8,5))
plt.bar(group_avg.index, group_avg.values,
        color=['#3498DB', '#E74C3C', '#2ECC71'])
plt.title('Average Score by Study Group')
plt.xlabel('Study Group')
plt.ylabel('Average Score')
plt.ylim(0, 100)

save_path1=os.path.join(data_dir, 'bar_group_avg.png')
plt.savefig(save_path1, dpi=150, bbox_inches='tight')
plt.show()
print(f'saved: {save_path1}')

plt.figure(figsize=(8,5))
plt.hist(df['python_score'], bins=10, color='#9B59B6', edgecolor='white')
plt.title('Distribution of Python Scores')
plt.xlabel('Python Score')
plt.ylabel('Number of Students')

save_path2=os.path.join(data_dir, 'hist_python_scores.png')
plt.savefig(save_path2, dpi=150, bbox_inches='tight')
plt.show()
print(f'saved: {save_path2}')

plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='gender', y='average_score', hue='gender', palette='Set2', legend=False)
plt.title('Score Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score')

save_path3=os.path.join(data_dir, 'box_gender_scores.png')
plt.savefig(save_path3, dpi=150, bbox_inches='tight')
plt.show()
print(f'saved: {save_path3}')

plt.figure(figsize=(8, 6))
corr=df[['math_score', 'python_score', 'english_score', 'average_score']].corr()
sns.heatmap(corr,annot=True, cmap="Blues", fmt='.2f')

plt.title('Correlation Matrix of Student Scores')
save_path4=os.path.join(data_dir, 'heatmap_correlation.png')
plt.savefig(save_path4, dpi=150, bbox_inches='tight')
plt.show()
print(f'saved: {save_path4}')
