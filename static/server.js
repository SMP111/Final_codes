const express = require('express');
const fs = require('fs');
const axios = require('axios');  // Import axios
const app = express();

// Serve static files if you have any (e.g., CSS or client-side JS)
app.use(express.static('static'));

// Route for the main page
app.get('/', (req, res) => {
    fs.readFile('index.html', 'utf8', (err, data) => {
        if (err) {
            res.status(500).send('Internal Server Error');
            return;
        }
        res.send(data);
    });
});

// Chatbot endpoint (modify as needed)
app.post('/chat', express.json(), (req, res) => {
    const userMessage = req.body.message;
    
    // Send the user message to Flask server
    axios.post('http://localhost:5000/chat', { message: userMessage })
        .then((response) => {
            // Return the Flask server's response
            res.json({ response: response.data.response });
        })
        .catch((error) => {
            console.error("Error contacting Flask server:", error);
            res.status(500).send('Error contacting Flask server');
        });
});

app.listen(5000, () => {
    console.log('Server running on http://localhost:5000/');
});
