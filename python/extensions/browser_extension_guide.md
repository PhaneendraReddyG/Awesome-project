# Browser Extension Development Guide

## What is a Browser Extension?

A browser extension is a software program that extends the functionality of a web browser. Extensions can:
- Modify web pages
- Add new features to the browser
- Integrate with web services
- Enhance user experience

## Supported Browsers

1. **Chrome/Chromium-based browsers** (Chrome, Edge, Brave, Opera)
2. **Firefox**
3. **Safari** (requires different approach)

## Basic Structure

Every browser extension needs these core files:

```
my-extension/
├── manifest.json          # Extension configuration
├── popup.html            # Extension popup interface
├── popup.js              # Popup functionality
├── content.js            # Script that runs on web pages
├── background.js         # Background service worker
├── icons/                # Extension icons
│   ├── icon16.png
│   ├── icon48.png
│   └── icon128.png
└── styles/
    └── popup.css         # Styling for popup
```

## Step-by-Step Guide

### 1. Create the Manifest File

The `manifest.json` is the heart of your extension:

```json
{
  "manifest_version": 3,
  "name": "My First Extension",
  "version": "1.0",
  "description": "A simple browser extension",
  
  "permissions": [
    "activeTab",
    "storage"
  ],
  
  "action": {
    "default_popup": "popup.html",
    "default_title": "Click me!"
  },
  
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
  
  "background": {
    "service_worker": "background.js"
  },
  
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

### 2. Create the Popup Interface

```html
<!-- popup.html -->
<!DOCTYPE html>
<html>
<head>
  <title>My Extension</title>
  <link rel="stylesheet" href="styles/popup.css">
</head>
<body>
  <div class="container">
    <h2>My Extension</h2>
    <button id="actionButton">Click Me!</button>
    <div id="result"></div>
  </div>
  <script src="popup.js"></script>
</body>
</html>
```

### 3. Add Popup Functionality

```javascript
// popup.js
document.addEventListener('DOMContentLoaded', function() {
  const actionButton = document.getElementById('actionButton');
  const resultDiv = document.getElementById('result');
  
  actionButton.addEventListener('click', function() {
    // Send message to content script
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.sendMessage(tabs[0].id, {action: "performAction"}, function(response) {
        resultDiv.textContent = response.message;
      });
    });
  });
});
```

### 4. Create Content Script

```javascript
// content.js
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "performAction") {
    // Modify the current webpage
    document.body.style.backgroundColor = "lightblue";
    sendResponse({message: "Action completed!"});
  }
});
```

### 5. Add Background Script

```javascript
// background.js
chrome.runtime.onInstalled.addListener(function() {
  console.log('Extension installed!');
});

// Handle extension icon click
chrome.action.onClicked.addListener(function(tab) {
  console.log('Extension icon clicked!');
});
```

## Common Use Cases

### 1. Page Modifier Extension
```javascript
// content.js - Modify page content
function modifyPage() {
  // Change all links to open in new tab
  const links = document.querySelectorAll('a');
  links.forEach(link => {
    link.target = '_blank';
  });
}

modifyPage();
```

### 2. Data Collector Extension
```javascript
// content.js - Collect data from page
function collectData() {
  const data = {
    title: document.title,
    url: window.location.href,
    timestamp: new Date().toISOString()
  };
  
  chrome.runtime.sendMessage({
    action: "saveData",
    data: data
  });
}

collectData();
```

### 3. Ad Blocker Extension
```javascript
// content.js - Block ads
function blockAds() {
  const adSelectors = [
    '[class*="ad"]',
    '[id*="ad"]',
    '[class*="advertisement"]'
  ];
  
  adSelectors.forEach(selector => {
    const elements = document.querySelectorAll(selector);
    elements.forEach(element => {
      element.style.display = 'none';
    });
  });
}

blockAds();
```

## Permissions Explained

Common permissions you might need:

- `"activeTab"` - Access to current tab
- `"storage"` - Store data locally
- `"tabs"` - Access to all tabs
- `"bookmarks"` - Access to bookmarks
- `"history"` - Access to browsing history
- `"notifications"` - Show notifications
- `"webRequest"` - Intercept network requests

## Testing Your Extension

### Chrome/Edge:
1. Open `chrome://extensions/`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select your extension folder

### Firefox:
1. Open `about:debugging`
2. Click "This Firefox"
3. Click "Load Temporary Add-on"
4. Select your `manifest.json`

## Publishing Your Extension

### Chrome Web Store:
1. Create a developer account ($5 one-time fee)
2. Package your extension
3. Submit for review

### Firefox Add-ons:
1. Create a Mozilla account
2. Submit for review
3. Free to publish

## Best Practices

1. **Security**: Always validate user input
2. **Performance**: Minimize content script execution
3. **User Experience**: Provide clear feedback
4. **Privacy**: Only request necessary permissions
5. **Testing**: Test on multiple websites
6. **Documentation**: Write clear README files

## Common Issues and Solutions

### Issue: Extension not loading
**Solution**: Check manifest.json syntax and file paths

### Issue: Content script not running
**Solution**: Verify matches pattern in manifest

### Issue: Permissions denied
**Solution**: Request appropriate permissions in manifest

## Advanced Features

### 1. Options Page
```json
{
  "options_page": "options.html"
}
```

### 2. Context Menus
```javascript
chrome.contextMenus.create({
  id: "sampleContextMenu",
  title: "Sample Context Menu Item",
  contexts: ["all"]
});
```

### 3. Keyboard Shortcuts
```json
{
  "commands": {
    "_execute_action": {
      "suggested_key": {
        "default": "Ctrl+Shift+Y"
      }
    }
  }
}
```

## Resources

- [Chrome Extension Documentation](https://developer.chrome.com/docs/extensions/)
- [Firefox Extension Documentation](https://extensionworkshop.com/)
- [WebExtensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions)

## Example Projects to Build

1. **Dark Mode Toggle** - Switch websites to dark theme
2. **Password Generator** - Generate secure passwords
3. **Link Shortener** - Shorten URLs quickly
4. **Note Taker** - Save notes while browsing
5. **Language Translator** - Translate text on web pages
6. **Screenshot Tool** - Capture webpage screenshots
7. **Bookmark Manager** - Enhanced bookmarking
8. **Reading Time Calculator** - Estimate reading time

Start with a simple project and gradually add more complex features! 