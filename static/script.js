// PocketSmart AI - Frontend JavaScript

document.addEventListener("DOMContentLoaded", function () {

    console.log("PocketSmart AI loaded successfully!");

    // Handle planner forms
    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function (event) {

            event.preventDefault();

            const button = form.querySelector("button");

            if (button) {
                button.innerText = "Generating...";
                button.disabled = true;
            }

            // Small delay for demo UI
            setTimeout(function () {

                if (button) {
                    button.innerText = "Generate Recommendation";
                    button.disabled = false;
                }

                alert(
                    "Your request has been received! AI recommendations will appear here."
                );

            }, 1000);

        });

    });

});