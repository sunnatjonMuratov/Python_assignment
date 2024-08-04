document.getElementById("reservation-form").addEventListener("submit", function(event) {
        let name = document.getElementById("name").value;
        let date = document.getElementById("date").value;
        let time = document.getElementById("time").value;
        let guests = document.getElementById("guests").value;

        if (name === "" || date === "" || time === "" || guests === "") {
            alert("Please fill out all fields before submitting.");
            event.preventDefault();
        }
    });


function updateTime() {
        const now = new Date();
        const formattedTime = now.toLocaleTimeString();
        const formattedDate = now.toLocaleDateString();

        document.getElementById("current-time").innerHTML = formattedDate + " " + formattedTime;
    }

    setInterval(updateTime, 1000);  // Update every second