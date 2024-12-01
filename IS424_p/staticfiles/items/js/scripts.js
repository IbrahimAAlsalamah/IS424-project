// scripts.js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    if (form) {
        form.onsubmit = function () {
            const inputs = form.querySelectorAll("input[required]");
            for (let input of inputs) {
                if (!input.value) {
                    alert(`${input.name} is required`);
                    return false;
                }
            }
        };
    }
});
