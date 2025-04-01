
const API_KEY = "AIzaSyANgpauG1EEfnvHKbUzV4HcVFLUqrTGQzU"; // Replace with your actual API key

const requestBody = {
    contents: [{
        parts: [{ text: "Explain how AI works" }]
    }]
};
console.log("JAVA")

fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${API_KEY}`, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(requestBody)
})
.then(response => response.json())
.then(data => {
    console.log("Response:", data);
})
.catch(error => {
    console.error("Error:", error);
});
