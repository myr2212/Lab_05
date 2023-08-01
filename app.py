
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# In[6]:


app = Flask(__name__)


# In[17]:


# Load the dataset
data = pd.read_csv("https://raw.githubusercontent.com/myr2212/Lab_05/main/Fish.csv")
data.head()


# In[11]:


# Split features and target variable
X = data.drop("Species", axis=1)
y = data["Species"]


# In[12]:


# Encode the target variable (fish species)
le = LabelEncoder()
y = le.fit_transform(y)


# In[13]:


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[14]:


# Initialize the Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)


# In[15]:


# Train the model on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)


# In[16]:


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_report_str = classification_report(y_test, y_pred, target_names=le.classes_)

print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report_str)


# In[18]:


# Train the model on the entire dataset
clf.fit(X, y)


# In[19]:


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
# Serve the frontend webpage
@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
