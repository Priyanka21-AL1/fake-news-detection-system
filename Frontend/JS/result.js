const newsText = localStorage.getItem("newsText");
const prediction = localStorage.getItem("prediction");
const confidence = localStorage.getItem("confidence");

document.getElementById("newsText").innerText =
    newsText || "No News Found";

if (prediction === "REAL") {

    document.getElementById("prediction").innerHTML =
        "🟢 REAL";

} else if (prediction === "FAKE") {

    document.getElementById("prediction").innerHTML =
        "🔴 FAKE";

} else {

    document.getElementById("prediction").innerHTML =
        "No Prediction";
}

document.getElementById("confidence").innerHTML =
    confidence
        ? confidence + "%"
        : "No Confidence Data";

function goBack() {
    window.location.href = "index.html";
}