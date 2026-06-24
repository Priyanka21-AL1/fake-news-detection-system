async function checkNews() {

    // Get text from textarea
    const text = document.getElementById("newsText").value;

    // Validation
    if (!text.trim()) {
        alert("Please enter news text.");
        return;
    }

    try {

        // Call Spring Boot API
        const response = await fetch(
            "http://localhost:8081/api/news/check",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    text: text
                })
            }
        );

        // Convert response to JSON
        const data = await response.json();

console.log("API Response:", data);

localStorage.setItem("prediction", data.prediction);
localStorage.setItem("confidence", data.confidence);
        /*
        Example Response

        {
            "prediction": "REAL",
            "confidence": 96.2
        }
        */

        // Store result in browser
        localStorage.setItem(
            "prediction",
            data.prediction
        );

        localStorage.setItem(
            "confidence",
            data.confidence
        );

        localStorage.setItem(
            "newsText",
            text
        );

        // Redirect to result page
        window.location.href = "result.html";

    } catch (error) {

        console.error(error);

        alert(
            "Unable to connect to server."
        );
    }
}