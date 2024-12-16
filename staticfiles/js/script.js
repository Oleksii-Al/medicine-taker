console.log("Hello");

document.getElementById("toggle-order").addEventListener("click", function() {
    const scheduleContainer = document.querySelector(".schedule-container");
    const days = Array.from(scheduleContainer.getElementsByClassName("day-schedule"))

    days.reverse();
    days.forEach(day => scheduleContainer.appendChild(day));
})