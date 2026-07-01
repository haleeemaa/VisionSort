const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");

imageInput.onchange = function () {
    preview.src = URL.createObjectURL(imageInput.files[0]);
};

async function predict() {
    console.log("Predict button clicked");

    let file = imageInput.files[0];

    if (!file) {
        alert("Choose an image first");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    try {
        let response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            body: formData
        });

        console.log("Response received");

        let data = await response.json();
        console.log(data);

        document.getElementById("result").innerHTML = `
            <h2>${data.prediction}</h2>
            <p><b>Confidence:</b> ${data.confidence}%</p>
            <p><b>Suggestion:</b> ${data.suggestion}</p>
        `;

        console.log("Result added to page");

    } catch (err) {
        console.error(err);
        alert("Error: " + err);
    }
}
let chartInstance = null;

async function toggleDashboard() {

    const dashboard = document.getElementById("dashboard");

    // If dashboard is currently visible, just hide it and stop here
    if (dashboard.style.display === "block") {
        dashboard.style.display = "none";
        return;
    }

    // Otherwise, show it and load the data
    dashboard.style.display = "block";

    try {
        let response = await fetch("http://127.0.0.1:8000/history");
        let data = await response.json();
        let records = data.history;

        // Count how many predictions fall into each category
        let counts = {
            plastic: 0,
            paper: 0,
            metal: 0,
            glass: 0,
            cardboard: 0,
            trash: 0
        };

        records.forEach(function (record) {
            if (counts.hasOwnProperty(record.prediction)) {
                counts[record.prediction]++;
            }
        });

        document.getElementById("totalImages").innerText =
            "Total Images: " + records.length;

        // If a chart already exists, destroy it before drawing a new one
        if (chartInstance) {
            chartInstance.destroy();
        }

        let ctx = document.getElementById("pieChart").getContext("2d");

        chartInstance = new Chart(ctx, {
            type: "pie",
            data: {
                labels: Object.keys(counts),
                datasets: [{
                    data: Object.values(counts),
                    backgroundColor: [
                        "#4CAF50",
                        "#FFC107",
                        "#2196F3",
                        "#9C27B0",
                        "#795548",
                        "#F44336"
                    ]
                }]
            }
        });

    } catch (err) {
        console.error(err);
        alert("Could not load dashboard: " + err);
    }
}