import pandas as pd
from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

app = Flask(__name__)

# Load the dataset
data = pd.read_csv("fish_market.csv")

# Split features and target variable
X = data.drop("Species", axis=1)
y = data["Species"]

# Encode the target variable (fish species)
le = LabelEncoder()
y = le.fit_transform(y)

# Initialize the Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the entire dataset
clf.fit(X, y)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.get_json()
        
        # Convert input data to DataFrame
        input_df = pd.DataFrame(data, index=[0])
        
        # Make predictions using the trained model
        predictions = clf.predict(input_df)
        
        # Convert the predictions back to class labels
        predicted_species = le.inverse_transform(predictions)
        
        # Return the predictions as JSON response
        return jsonify({"predicted_species": predicted_species[0]})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
