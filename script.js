
document.addEventListener("DOMContentLoaded", function() {
    const inputField = document.getElementById("input");
    const outputDiv = document.getElementById("output");

    // Function to process commands
    function processCommand(command) {
        let response = "";

        switch (command.toLowerCase()) {
            case "simo":
                response = "That's me!!!!!";
                break;
            case "hello":
                response = "Reality distorts. You feel the static hum.";
                break;
            case "exit":
                response = "Logging off... but the ghosts remain.";
                break;
            case "bye":
                response = "Logging off... see you around around your corner.";
                break;
            default:
                response = `> ${command} is unknown. Try another whisper.`;
        }

        return response;
    }

    // Handle user input
    inputField.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            let command = inputField.value.trim();
            if (command) {
                let userCommand = document.createElement("p");
                userCommand.innerHTML = `> ${command}`;
                outputDiv.appendChild(userCommand);

                let response = document.createElement("p");
                response.innerHTML = processCommand(command);
                outputDiv.appendChild(response);
            }
            inputField.value = "";
        }
    });
});
