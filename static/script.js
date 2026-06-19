async function analyzeSentiment() {

    let text = document.getElementById("inputText").value;

    if (text.trim() === "") {
        alert("Please enter some text");
        return;
    }

    document.getElementById("loading").innerHTML =
        "Analyzing...";

    document.getElementById("result").innerHTML = "";

    try {

        const response = await fetch("/analyze",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    text:text
                })
            }
        );

        const data = await response.json();

        let emoji = "😐";

        if(data.sentiment==="Positive")
            emoji="😊";

        else if(data.sentiment==="Negative")
            emoji="😡";

        document.getElementById("loading").innerHTML = "";

        document.getElementById("result").innerHTML = `
        <div class="result-card">

            <div class="sentiment">
                ${emoji} ${data.sentiment}
            </div>

            <div class="score">
                Polarity Score : ${data.polarity.toFixed(2)}
            </div>

        </div>
        `;

    }

    catch(error){

        document.getElementById("loading").innerHTML = "";

        document.getElementById("result").innerHTML =
        `<p style="color:red;">Server connection failed.</p>`;

    }

}