function colorizeAscii(asciiArt) {
    const colors = ["red", "green", "blue", "purple", "orange", "yellow", "cyan"];
    const lines = asciiArt.split("\n");
    return lines.map(line => {
        const color = colors[Math.floor(Math.random() * colors.length)];
        return `<span style="color: ${color}; font-family: monospace;">${line}</span>`;
    }).join("<br>");
}

document.addEventListener("DOMContentLoaded", function() {
    const inputField = document.getElementById("input");
    const outputDiv = document.getElementById("output");

    async function sendToBackend(text) {
        try {
            console.log(`📡 Sending request to Flask with text: ${text}`);

            const response = await fetch("http://127.0.0.1:5000/ascii", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ text: text }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log("🎨 Received ASCII Art from Flask:", data.ascii_art);

            return colorizeAscii(data.ascii_art);
        } catch (error) {
            console.error("🚨 Error fetching ASCII art:", error);
            return "Error generating ASCII art.";
        }
    }

    inputField.addEventListener("keypress", async function(event) {
        if (event.key === "Enter") {
            let command = inputField.value.trim();
            if (command) {
                let userCommand = document.createElement("p");
                userCommand.innerHTML = `> ${command}`;
                outputDiv.appendChild(userCommand);

                let asciiResponse = await sendToBackend(command);
                let responseElem = document.createElement("p");
                responseElem.innerHTML = asciiResponse;
                outputDiv.appendChild(responseElem);
            }
            inputField.value = "";
        }
    });
});
