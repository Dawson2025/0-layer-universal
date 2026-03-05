// resource_id: "97d97a12-df30-4521-b1c1-9c71963403e7"
// resource_type: "document"
// resource_name: "popup"
// popup.js
document.getElementById("open-settings").addEventListener("click", () => {
  chrome.runtime.openOptionsPage(); // Opens settings.html in a new tab
});