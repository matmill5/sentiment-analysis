var fileUploadLabel = document.getElementById("fileUploadLabel");
var fileBrowser = document.getElementById("inputGroupFile04");

fileBrowser.addEventListener("input", function(){
    fileUploadLabel.textContent = "File Selected";
});