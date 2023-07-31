function predictSpecies() {
    const length1 = parseFloat(document.getElementById("length1").value);
    const length2 = parseFloat(document.getElementById("length2").value);
    const length3 = parseFloat(document.getElementById("length3").value);
    const height = parseFloat(document.getElementById("height").value);
    const width = parseFloat(document.getElementById("width").value);

    // Here you can perform any data validation or preprocessing as needed

    // Make a request to the server to get the prediction
    // You can use Fetch API or any other library for this purpose
    // For this example, let's assume we already have the predicted species from the model
    const predictedSpecies = "Bream";

    document.getElementById("prediction").innerText = `Predicted Species: ${predictedSpecies}`;
}
