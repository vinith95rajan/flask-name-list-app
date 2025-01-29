document.addEventListener("DOMContentLoaded", function () {
    fetch("/api/names")
        .then(response => response.json())
        .then(data => {
            let dropdown = document.getElementById("name-list");
            dropdown.innerHTML = ""; // Clear existing options
            data.names.forEach(name => {
                let option = document.createElement("option");
                option.textContent = name;
                dropdown.appendChild(option);
            });
        })
        .catch(error => console.error("Error fetching names:", error));
});
