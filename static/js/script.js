// Highlight the current day of the week
$(document).ready(function () {
    $('.opening-hours li').eq(new Date().getDay()).addClass('today');
});