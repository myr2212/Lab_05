function predictFishSpecies() {
  // Get the input values
  var length1 = parseFloat(document.getElementById("length1").value);
  var length2 = parseFloat(document.getElementById("length2").value);
  var length3 = parseFloat(document.getElementById("length3").value);
  var height = parseFloat(document.getElementById("height").value);
  var width = parseFloat(document.getElementById("width").value);
  
  // Create the input data object
  var inputData = {
    "Length1": length1,
    "Length2": length2,
    "Length3": length3,
    "Height": height,
    "Width": width
  };

  // Send a POST request to the Flask backend
  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(inputData)
  })
  .then(response => response.json())
  .then(data => {
    // Display the predicted species
    var outputContainer = document.getElementById("output-container");
    var predictedSpecies = document.getElementById("predicted-species");
    predictedSpecies.textContent = "Predicted Species: " + data.predicted_species;
    outputContainer.style.display = "block";
  })
  .catch(error => {
    console.error("Error:", error);
  });
}
