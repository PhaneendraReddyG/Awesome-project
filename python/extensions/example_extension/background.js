// Background service worker
chrome.runtime.onInstalled.addListener(function(details) {
    console.log('Page Enhancer Extension installed!');
    
    // Set default settings
    chrome.storage.sync.set({
        autoDarkMode: false,
        highlightColor: '#ffeb3b',
        darkModeEnabled: false,
        readingModeEnabled: false,
        linkHighlightingEnabled: false
    });
    
    // Create context menu items
    chrome.contextMenus.create({
        id: "toggleDarkMode",
        title: "Toggle Dark Mode",
        contexts: ["page", "selection"]
    });
    
    chrome.contextMenus.create({
        id: "toggleReadingMode",
        title: "Toggle Reading Mode",
        contexts: ["page"]
    });
    
    chrome.contextMenus.create({
        id: "toggleLinkHighlighting",
        title: "Toggle Link Highlighting",
        contexts: ["page"]
    });
});

// Handle context menu clicks
chrome.contextMenus.onClicked.addListener(function(info, tab) {
    switch(info.menuItemId) {
        case "toggleDarkMode":
            chrome.tabs.sendMessage(tab.id, {action: "toggleDarkMode"});
            break;
        case "toggleReadingMode":
            chrome.tabs.sendMessage(tab.id, {action: "toggleReadingMode"});
            break;
        case "toggleLinkHighlighting":
            chrome.tabs.sendMessage(tab.id, {action: "toggleLinkHighlighting"});
            break;
    }
});

// Handle extension icon click (when no popup is defined)
chrome.action.onClicked.addListener(function(tab) {
    // This will only trigger if popup is not defined in manifest
    console.log('Extension icon clicked on tab:', tab.id);
    
    // You could open a popup programmatically here
    // chrome.action.setPopup({tabId: tab.id, popup: 'popup.html'});
});

// Listen for messages from content scripts
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "saveData") {
        // Save data to storage
        chrome.storage.sync.set({
            [request.key]: request.data
        }, function() {
            sendResponse({success: true});
        });
        return true; // Keep message channel open
    }
    
    if (request.action === "getData") {
        // Retrieve data from storage
        chrome.storage.sync.get([request.key], function(result) {
            sendResponse({data: result[request.key]});
        });
        return true; // Keep message channel open
    }
    
    if (request.action === "logError") {
        console.error('Content script error:', request.error);
        sendResponse({success: true});
    }
});

// Handle tab updates
chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    if (changeInfo.status === 'complete' && tab.url) {
        // Check if we should auto-apply features based on saved settings
        chrome.storage.sync.get(['autoDarkMode', 'darkModeEnabled'], function(result) {
            if (result.autoDarkMode && result.darkModeEnabled) {
                // Wait a bit for the page to fully load
                setTimeout(() => {
                    chrome.tabs.sendMessage(tabId, {action: "toggleDarkMode"});
                }, 1000);
            }
        });
    }
});

// Handle extension updates
chrome.runtime.onUpdateAvailable.addListener(function() {
    console.log('Extension update available');
    // You could notify the user here
});

// Handle storage changes
chrome.storage.onChanged.addListener(function(changes, namespace) {
    console.log('Storage changed:', changes, namespace);
    
    // Sync settings across tabs if needed
    if (namespace === 'sync') {
        Object.keys(changes).forEach(key => {
            const change = changes[key];
            console.log(`Setting "${key}" changed from "${change.oldValue}" to "${change.newValue}"`);
        });
    }
});

// Handle alarms (for periodic tasks)
chrome.alarms.onAlarm.addListener(function(alarm) {
    if (alarm.name === 'checkForUpdates') {
        // Perform periodic tasks
        console.log('Performing periodic check...');
    }
});

// Create periodic alarm (every hour)
chrome.alarms.create('checkForUpdates', {periodInMinutes: 60});

// Handle installation/uninstallation
chrome.runtime.onStartup.addListener(function() {
    console.log('Browser started with Page Enhancer Extension');
});

// Clean up when extension is uninstalled
chrome.runtime.setUninstallURL('https://your-website.com/uninstall-feedback');

// Utility functions
function getCurrentTab() {
    return new Promise((resolve) => {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            resolve(tabs[0]);
        });
    });
}

function sendMessageToCurrentTab(message) {
    return getCurrentTab().then(tab => {
        return new Promise((resolve) => {
            chrome.tabs.sendMessage(tab.id, message, resolve);
        });
    });
}

// Export utility functions for debugging
window.pageEnhancerBackground = {
    getCurrentTab,
    sendMessageToCurrentTab
}; 