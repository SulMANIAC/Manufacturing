window.onload = function() {
    var acknowledgeButton = document.querySelector('header button:first-child');
    var logoutButton = document.querySelector('header button:last-child');

    acknowledgeButton.addEventListener('click', function() {
        alert('All Current Alarms Have Been Acknowledged');
    });

    logoutButton.addEventListener('click', function() {
        alert('You have logged out.');
    });
};
