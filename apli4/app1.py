

print('LOAD THE DATASET')
import pandas as pd
df = pd.read_csv('students_dirty_dataset_100.csv')
print(df.head(10))
print(df.tail(3))
print(df.shape)



print('EXPLORE THE DATASET')
print(df.info()) 
print('---------------------------')
print(df.describe(include='all'))  # include='all' to get stats for all columns




print('---------------------------')
print('CHECK FOR NULL VALUES')
print(df.isnull().sum()) # Check for null values in each column
print('---------------------------')
print('CHECK FOR DUPLICATES')
print(df.duplicated().sum())  # Check for duplicate rows
print('---------------------------')
print('CHECK FOR UNIQUE VALUES')
print(df['department'].value_counts())  # Count unique values in 'department' column




print('---------------------------')
print('HALDER MISSING VALUES')
df['age'].fillna(df['age'].median(),inplace=True)  # Fill missing values in 'department' with 'Unknown'
print('EMPTY VALUES')
print('---------------------------')
df['english_score'].fillna(df['english_score'].mean(), inplace=True)  # Fill missing values in 'english_score' with mean
print('---------------------------')
df['admission_year'].fillna(df['admission_year'].mode()[0], inplace=True)  # Fill missing values in 'admission_year' with mode
print('---------------------------')
df['math_score'].fillna(df['math_score'].mean(), inplace=True)  # Fill missing values in 'math_score' with mean
print('---------------------------')
df['gender'].fillna('Unknown', inplace=True)  # Fill missing values in
print(df.isnull().sum())  # Check for null values in each column after filling




print('---------------------------')
print('NORMA CATEGORICAL VALUES')
df['department'] = df['department'].str.strip().str.lower()  # Normalize 'department' values
print(df['department'].head(10)) # Check unique values in 'department' after normalization


print('---------------------------')
print('REMOVE DUPLICATES')
df.drop_duplicates(inplace=True)  # Remove duplicate rows
df.reset_index(drop=True, inplace=True)  # Reset index after removing duplicates
print(df.shape)  # Check shape after removing duplicates


print('---------------------------')
print('CREATE NEW FEATURES')
df['average_score'] = df[['english_score','math_score']].mean(axis=1)  # Create a new feature 'average_score'
print(df['average_score'].head(10))  # Check the new feature


print('---------------------------')
print('DISPLAY TOP PERFORMING STUDENTS')
topStudents = df.sort_values(by='average_score', ascending=False).head(10)  # Get top 5 students by average score
print(topStudents[['student_id', 'name', 'average_score']])  # Display only relevant columns


print('---------------------------')
print('SAVE THE CLEANED DATASET')
df.to_csv('students_cleaned_dataset.csv', index=False)  # Save the cleaned dataset to a new CSV file

