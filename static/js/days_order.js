let week_order = document.getElementById("toggle-order");
week_order.innerText = "Monday-Sunday";
week_order.addEventListener("click", function() {
    const scheduleContainer = document.querySelector(".schedule-container");
    const days = Array.from(scheduleContainer.getElementsByClassName("day-schedule"))

    days.reverse();
    days.forEach(day => scheduleContainer.appendChild(day));
    if (week_order.innerText == "Monday-Sunday") {
        week_order.innerText = "Sunday-Monday";
    }    else {
        week_order.innerText = "Monday-Sunday";
    }

});