import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load dataset
df = pd.read_csv('data/car_data.csv')

# Clean column names
df.columns = df.columns.str.strip()

# Feature Engineering
df['Current_Year'] = 2026
df['Years_Old'] = df['Current_Year'] - df['Year']

# Drop unnecessary columns
df.drop(['Car_Name', 'Year'], axis=1, inplace=True)

# Convert categorical variables
df = pd.get_dummies(df, drop_first=True)

# Split data
X = df.drop('Selling_Price', axis=1)
y = df['Selling_Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('model/car_price_model.pkl', 'wb'))

print("✅ Model trained successfully!")
print(X.columns)