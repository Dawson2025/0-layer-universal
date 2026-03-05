// resource_id: "b9157b3d-3458-4954-ab6b-d73ae5cb826c"
// resource_type: "document"
// resource_name: "background"
// background.js
chrome.action.onClicked.addListener(() => {
  chrome.runtime.openOptionsPage(); // This opens settings.html automatically
});