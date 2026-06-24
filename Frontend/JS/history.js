async function loadHistory() {

    try {

        const response = await fetch(
            "http://localhost:8081/api/news/history"
        );

        const data = await response.json();

        const container =
            document.getElementById(
                "historyContainer"
            );

        container.innerHTML = "";

        if (data.length === 0) {

            container.innerHTML =
                "<h3>No Prediction History Found</h3>";

            return;
        }

        data.reverse().forEach(item => {

            const predictionClass =
                item.prediction === "REAL"
                ? "real"
                : "fake";

            container.innerHTML += `
                <div class="history-card">

                    <h3>News Text</h3>
                    <p>${item.inputText}</p>

                    <h3>Prediction</h3>
                    <p class="${predictionClass}">
                        ${item.prediction}
                    </p>

                    <h3>Confidence</h3>
                    <p>${item.confidence}%</p>

                </div>
            `;
        });

    } catch(error) {

        console.error(error);

        alert(
            "Unable to load history."
        );
    }
}

function goHome() {
    window.location.href = "index.html";
}

loadHistory();