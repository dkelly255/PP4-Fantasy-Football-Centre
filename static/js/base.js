/* jshint esversion: 8 */

setTimeout(function () {
    let messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        let alert = new bootstrap.Alert(message);
        alert.close();
    });
}, 2500);
