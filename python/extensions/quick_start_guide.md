# Quick Start Guide: Building Browser Extensions

## 🚀 5-Minute Setup

### 1. Create Basic Structure
```
my-extension/
├── manifest.json
├── popup.html
├── popup.js
├── content.js
└── background.js
```

### 2. Essential Files

**manifest.json** (Extension Configuration):
```json
{
  "manifest_version": 3,
  "name": "My Extension",
  "version": "1.0",
  "description": "A simple extension",
  "permissions": ["activeTab"],
  "action": {
    "default_popup": "popup.html"
  },
  "content_scripts": [{
    "matches": ["<all_urls>"],
    "js": ["content.js"]
  }],
  "background": {
    "service_worker": "background.js"
  }
}
```

**popup.html** (User Interface):
```html
<!DOCTYPE html>
<html>
<head><title>My Extension</title></head>
<body>
  <h2>My Extension</h2>
  <button id="actionBtn">Click Me!</button>
  <script src="popup.js"></script>
</body>
</html>
```

**popup.js** (Popup Logic):
```javascript
document.getElementById('actionBtn').addEventListener('click', function() {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, {action: "performAction"});
  });
});
```

**content.js** (Page Modifications):
```javascript
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "performAction") {
    document.body.style.backgroundColor = "lightblue";
  }
});
```

**background.js** (Background Tasks):
```javascript
chrome.runtime.onInstalled.addListener(function() {
  console.log('Extension installed!');
});
```

### 3. Test Your Extension

**Chrome/Edge:**
1. Go to `chrome://extensions/`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select your extension folder

**Firefox:**
1. Go to `about:debugging`
2. Click "This Firefox"
3. Click "Load Temporary Add-on"
4. Select `manifest.json`

## 🎯 Common Use Cases

### Page Modifier
```javascript
// content.js
function modifyPage() {
  // Change all links to open in new tab
  document.querySelectorAll('a').forEach(link => {
    link.target = '_blank';
  });
}
```

### Data Collector
```javascript
// content.js
function collectData() {
  const data = {
    title: document.title,
    url: window.location.href,
    links: document.querySelectorAll('a').length
  };
  chrome.runtime.sendMessage({action: "saveData", data: data});
}
```

### Ad Blocker
```javascript
// content.js
function blockAds() {
  const adSelectors = ['[class*="ad"]', '[id*="ad"]'];
  adSelectors.forEach(selector => {
    document.querySelectorAll(selector).forEach(el => {
      el.style.display = 'none';
    });
  });
}
```

## 🔧 Key Concepts

### Permissions
- `"activeTab"` - Access current tab
- `"storage"` - Save data locally
- `"tabs"` - Access all tabs
- `"bookmarks"` - Access bookmarks
- `"notifications"` - Show notifications

### Message Passing
```javascript
// Send message from popup to content script
chrome.tabs.sendMessage(tabId, {action: "doSomething"});

// Listen in content script
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "doSomething") {
    // Do something
    sendResponse({success: true});
  }
});
```

### Storage
```javascript
// Save data
chrome.storage.sync.set({key: "value"});

// Load data
chrome.storage.sync.get(['key'], function(result) {
  console.log(result.key);
});
```

## 📝 Best Practices

1. **Security**: Validate all user input
2. **Performance**: Minimize DOM operations
3. **UX**: Provide clear feedback
4. **Privacy**: Request minimal permissions
5. **Testing**: Test on multiple websites

## 🚨 Common Issues

**Extension not loading:**
- Check `manifest.json` syntax
- Verify file paths
- Look for console errors

**Content script not running:**
- Check `matches` pattern in manifest
- Verify permissions
- Test on different websites

**Permissions denied:**
- Request appropriate permissions
- Check browser settings
- Verify extension is enabled

## 📚 Next Steps

1. **Add icons** to your extension
2. **Create an options page** for settings
3. **Add keyboard shortcuts** for quick access
4. **Implement context menus** for right-click actions
5. **Publish to Chrome Web Store** or Firefox Add-ons

## 🛠️ Development Tools

- **Chrome DevTools**: Debug your extension
- **Extension Reloader**: Auto-reload during development
- **WebExtensions API**: Official documentation
- **Extension Workshop**: Firefox development guide

## 💡 Pro Tips

- Start simple and add features gradually
- Use the browser's built-in debugging tools
- Test on different types of websites
- Keep your code modular and well-documented
- Follow the WebExtensions standard for cross-browser compatibility

---

**Ready to build?** Start with the example extension in the `example_extension/` folder and modify it to suit your needs! 