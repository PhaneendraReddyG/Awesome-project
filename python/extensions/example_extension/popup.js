// Popup functionality
document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const darkModeBtn = document.getElementById('darkModeBtn');
    const readingModeBtn = document.getElementById('readingModeBtn');
    const highlightLinksBtn = document.getElementById('highlightLinksBtn');
    const autoDarkModeCheckbox = document.getElementById('autoDarkMode');
    const highlightColorInput = document.getElementById('highlightColor');
    const statusDiv = document.getElementById('status');
    
    // Page info elements
    const pageTitle = document.getElementById('pageTitle');
    const pageUrl = document.getElementById('pageUrl');
    const linkCount = document.getElementById('linkCount');
    
    // Initialize popup
    initializePopup();
    
    // Event listeners
    darkModeBtn.addEventListener('click', toggleDarkMode);
    readingModeBtn.addEventListener('click', toggleReadingMode);
    highlightLinksBtn.addEventListener('click', toggleLinkHighlighting);
    autoDarkModeCheckbox.addEventListener('change', saveSettings);
    highlightColorInput.addEventListener('change', saveSettings);
    
    function initializePopup() {
        updateStatus('Loading...', 'loading');
        
        // Get current tab info
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            const currentTab = tabs[0];
            
            // Update page info
            pageTitle.textContent = currentTab.title || 'No title';
            pageUrl.textContent = currentTab.url || 'No URL';
            
            // Get page statistics
            chrome.tabs.sendMessage(currentTab.id, {action: "getPageInfo"}, function(response) {
                if (response && response.linkCount !== undefined) {
                    linkCount.textContent = response.linkCount;
                } else {
                    linkCount.textContent = 'N/A';
                }
            });
            
            // Load saved settings
            loadSettings();
            
            updateStatus('Ready', 'success');
        });
    }
    
    function toggleDarkMode() {
        updateStatus('Toggling dark mode...', 'loading');
        
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {action: "toggleDarkMode"}, function(response) {
                if (response && response.success) {
                    updateStatus('Dark mode toggled!', 'success');
                    setTimeout(() => updateStatus('Ready', 'success'), 2000);
                } else {
                    updateStatus('Failed to toggle dark mode', 'error');
                    setTimeout(() => updateStatus('Ready', 'success'), 2000);
                }
            });
        });
    }
    
    function toggleReadingMode() {
        updateStatus('Toggling reading mode...', 'loading');
        
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {action: "toggleReadingMode"}, function(response) {
                if (response && response.success) {
                    updateStatus('Reading mode toggled!', 'success');
                    setTimeout(() => updateStatus('Ready', 'success'), 2000);
                } else {
                    updateStatus('Failed to toggle reading mode', 'error');
                    setTimeout(() => updateStatus('Ready', 'success'), 2000);
                }
            });
        });
    }
    
    function toggleLinkHighlighting() {
        updateStatus('Toggling link highlighting...', 'loading');
        
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {
                action: "toggleLinkHighlighting",
                color: highlightColorInput.value
            }, function(response) {
                if (response && response.success) {
                    updateStatus('Link highlighting toggled!', 'success');
                    setTimeout(() => updateStatus('Ready', 'success'), 2000);
                } else {
                    updateStatus('Failed to toggle link highlighting', 'error');
                    setTimeout(() => updateStatus('Ready', 'success'), 2000);
                }
            });
        });
    }
    
    function loadSettings() {
        chrome.storage.sync.get(['autoDarkMode', 'highlightColor'], function(result) {
            if (result.autoDarkMode !== undefined) {
                autoDarkModeCheckbox.checked = result.autoDarkMode;
            }
            if (result.highlightColor) {
                highlightColorInput.value = result.highlightColor;
            }
        });
    }
    
    function saveSettings() {
        const settings = {
            autoDarkMode: autoDarkModeCheckbox.checked,
            highlightColor: highlightColorInput.value
        };
        
        chrome.storage.sync.set(settings, function() {
            updateStatus('Settings saved!', 'success');
            setTimeout(() => updateStatus('Ready', 'success'), 1500);
        });
    }
    
    function updateStatus(message, type) {
        statusDiv.textContent = message;
        statusDiv.className = `status ${type}`;
    }
    
    // Handle errors gracefully
    chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
        if (request.action === "error") {
            updateStatus(request.message || 'An error occurred', 'error');
            setTimeout(() => updateStatus('Ready', 'success'), 3000);
        }
    });
}); 