// static/main.js
document.addEventListener("DOMContentLoaded", function(){
    const form = document.getElementById("scrapeForm");
    form.addEventListener("submit", function(){
      // Show loader when form is submitted
      document.getElementById("loader").style.display = "block";
   });
});