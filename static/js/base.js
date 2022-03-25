/* jshint esversion: 8 */

// Messaging functionality - display and remove messages
// Credits: adapted from CI blog lesson
setTimeout(function () {
    let messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        let alert = new bootstrap.Alert(message);
        alert.close();
    });
}, 2500);

// Stop comment resubmission on page refresh - see bug #12
// Credits: taken from webtrickshome.com per credits section
if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
  }
// Keep scroll position on page refresh - for UX purposes so user
// can see "comment pending approval" notification without scrolling  
// Credits: taken from stack overflow, see bug#13 & accreditation
document.addEventListener("DOMContentLoaded", function(event) { 
    var scrollpos = localStorage.getItem('scrollpos');
    if (scrollpos) window.scrollTo(0, scrollpos);
});
window.onbeforeunload = function(e) {
    localStorage.setItem('scrollpos', window.scrollY);
};