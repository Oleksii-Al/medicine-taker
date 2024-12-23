document.addEventListener("DOMContentLoaded", function() {
    let week_order = document.getElementById("toggle-order");

    if (week_order) {
        week_order.innerText = "Monday-Sunday";
        
        week_order.addEventListener("click", function() {
            const scheduleContainer = document.querySelector(".schedule-container");
            const days = Array.from(scheduleContainer.getElementsByClassName("day-schedule"));

            // Переворачиваем порядок дней
            days.reverse();
            days.forEach(day => scheduleContainer.appendChild(day));

            // Меняем текст кнопки в зависимости от текущего состояния
            if (week_order.innerText === "Monday-Sunday") {
                week_order.innerText = "Sunday-Monday";
            } else {
                week_order.innerText = "Monday-Sunday";
            }
        });
    } else {
        console.log("Element with id 'toggle-order' not found.");
    }
});
