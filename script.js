function processUserInput() {
    const userInput = document.getElementById('user-input').value;
    const assistantOutput = document.getElementById('assistant-output');
  
    // Simulate a basic response from the assistant
    const response = generateAssistantResponse(userInput);
  
    // Display the response
    assistantOutput.innerHTML = `<strong>You:</strong> ${userInput}<br><strong>Assistant:</strong> ${response}`;
  
    // Clear the input field
    document.getElementById('user-input').value = '';
  }
  
  function generateAssistantResponse(userInput) {
    // This is a simple example, and you would replace this with more sophisticated logic
    const responses = {
      'hello': 'Hello! How can I assist you today?',
      'how are you': 'I am just a computer program, but thank you for asking!',
      'bye': 'Goodbye! Have a great day!',
      // Add more responses based on user input
    };
  
    const lowercaseInput = userInput.toLowerCase();
  
    // Check if there is a predefined response for the user input
    if (responses[lowercaseInput]) {
      return responses[lowercaseInput];
    } else {
      return 'I am not sure how to respond to that.';
    }
  }
  