// Wait for the entire DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {
  
  // Fetch data from the HelloSalut API with the language set to French
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')

    // Convert the response to JSON format
    .then(response => response.json())

    // Once the data is available, update the HTML element with the translation
    .then(data => {
      // Set the text content of the element with id="hello" to the translated word
      document.getElementById('hello').textContent = data.hello;
    })

    // If there's an error during the fetch or JSON parsing, log it to the console
    .catch(error => console.error('Error fetching translation:', error));
});
