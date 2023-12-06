console.log ("hello")
const body = document.querySelector("body");
const icon = document.querySelector("#icon");
function changeMode() {
    body.classList.toggle("dark-mode");
    const isDarkMode = body.classList.contains("dark-mode")
    localStorage.setItem("dark-mode" , isDarkMode)
}

icon.addEventListener("click", changeMode);
const saveMode = localStorage.getItem("dark-mode")

if (saveMode !== null && saveMode === "true"){
    body.classList.add("dark-mode")
}
