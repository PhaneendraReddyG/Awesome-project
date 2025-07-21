// Content script - runs on web pages
(function() {
    'use strict';
    
    // State management
    let isDarkMode = false;
    let isReadingMode = false;
    let isLinkHighlighting = false;
    let originalStyles = {};
    
    // Initialize content script
    initializeContentScript();
    
    // Listen for messages from popup
    chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
        switch(request.action) {
            case 'toggleDarkMode':
                toggleDarkMode();
                sendResponse({success: true});
                break;
                
            case 'toggleReadingMode':
                toggleReadingMode();
                sendResponse({success: true});
                break;
                
            case 'toggleLinkHighlighting':
                toggleLinkHighlighting(request.color);
                sendResponse({success: true});
                break;
                
            case 'getPageInfo':
                sendResponse({
                    linkCount: document.querySelectorAll('a').length,
                    title: document.title,
                    url: window.location.href
                });
                break;
                
            default:
                sendResponse({success: false, error: 'Unknown action'});
        }
        return true; // Keep message channel open for async response
    });
    
    function initializeContentScript() {
        // Check for saved settings and apply them
        chrome.storage.sync.get(['autoDarkMode', 'highlightColor'], function(result) {
            if (result.autoDarkMode) {
                // Auto-apply dark mode based on time or user preference
                const hour = new Date().getHours();
                if (hour >= 18 || hour <= 6) {
                    toggleDarkMode();
                }
            }
        });
        
        // Add keyboard shortcuts
        document.addEventListener('keydown', function(e) {
            // Ctrl+Shift+D for dark mode
            if (e.ctrlKey && e.shiftKey && e.key === 'D') {
                e.preventDefault();
                toggleDarkMode();
            }
            
            // Ctrl+Shift+R for reading mode
            if (e.ctrlKey && e.shiftKey && e.key === 'R') {
                e.preventDefault();
                toggleReadingMode();
            }
        });
    }
    
    function toggleDarkMode() {
        isDarkMode = !isDarkMode;
        
        if (isDarkMode) {
            applyDarkMode();
        } else {
            removeDarkMode();
        }
        
        // Save state
        chrome.storage.sync.set({darkModeEnabled: isDarkMode});
    }
    
    function applyDarkMode() {
        const darkModeCSS = `
            html, body {
                background-color: #1a1a1a !important;
                color: #e0e0e0 !important;
            }
            
            * {
                background-color: #1a1a1a !important;
                color: #e0e0e0 !important;
                border-color: #333 !important;
            }
            
            a {
                color: #4a9eff !important;
            }
            
            a:hover {
                color: #66b3ff !important;
            }
            
            input, textarea, select {
                background-color: #2a2a2a !important;
                color: #e0e0e0 !important;
                border: 1px solid #444 !important;
            }
            
            button {
                background-color: #333 !important;
                color: #e0e0e0 !important;
                border: 1px solid #555 !important;
            }
            
            button:hover {
                background-color: #444 !important;
            }
            
            img, video {
                filter: brightness(0.8) contrast(1.2) !important;
            }
        `;
        
        // Create and inject dark mode stylesheet
        const style = document.createElement('style');
        style.id = 'page-enhancer-dark-mode';
        style.textContent = darkModeCSS;
        document.head.appendChild(style);
        
        // Add dark mode indicator
        addNotification('Dark mode enabled', 'dark-mode');
    }
    
    function removeDarkMode() {
        const darkModeStyle = document.getElementById('page-enhancer-dark-mode');
        if (darkModeStyle) {
            darkModeStyle.remove();
        }
        
        addNotification('Dark mode disabled', 'dark-mode');
    }
    
    function toggleReadingMode() {
        isReadingMode = !isReadingMode;
        
        if (isReadingMode) {
            applyReadingMode();
        } else {
            removeReadingMode();
        }
        
        chrome.storage.sync.set({readingModeEnabled: isReadingMode});
    }
    
    function applyReadingMode() {
        // Hide non-essential elements
        const elementsToHide = [
            'nav', 'header', 'footer', 'aside', 
            '.sidebar', '.navigation', '.menu',
            '.advertisement', '.ads', '.social-share',
            '.comments', '.related-posts'
        ];
        
        elementsToHide.forEach(selector => {
            const elements = document.querySelectorAll(selector);
            elements.forEach(element => {
                if (!element.dataset.readingModeHidden) {
                    element.dataset.readingModeHidden = 'true';
                    element.style.display = 'none';
                }
            });
        });
        
        // Apply reading-friendly styles
        const readingModeCSS = `
            body {
                max-width: 800px !important;
                margin: 0 auto !important;
                padding: 20px !important;
                font-family: 'Georgia', 'Times New Roman', serif !important;
                font-size: 18px !important;
                line-height: 1.6 !important;
                color: #333 !important;
                background-color: #fafafa !important;
            }
            
            h1, h2, h3, h4, h5, h6 {
                font-family: 'Georgia', 'Times New Roman', serif !important;
                color: #222 !important;
            }
            
            p {
                margin-bottom: 1.2em !important;
            }
            
            img {
                max-width: 100% !important;
                height: auto !important;
                margin: 20px 0 !important;
            }
        `;
        
        const style = document.createElement('style');
        style.id = 'page-enhancer-reading-mode';
        style.textContent = readingModeCSS;
        document.head.appendChild(style);
        
        addNotification('Reading mode enabled', 'reading-mode');
    }
    
    function removeReadingMode() {
        // Remove reading mode styles
        const readingModeStyle = document.getElementById('page-enhancer-reading-mode');
        if (readingModeStyle) {
            readingModeStyle.remove();
        }
        
        // Restore hidden elements
        const hiddenElements = document.querySelectorAll('[data-reading-mode-hidden="true"]');
        hiddenElements.forEach(element => {
            element.style.display = '';
            delete element.dataset.readingModeHidden;
        });
        
        addNotification('Reading mode disabled', 'reading-mode');
    }
    
    function toggleLinkHighlighting(color = '#ffeb3b') {
        isLinkHighlighting = !isLinkHighlighting;
        
        if (isLinkHighlighting) {
            applyLinkHighlighting(color);
        } else {
            removeLinkHighlighting();
        }
        
        chrome.storage.sync.set({linkHighlightingEnabled: isLinkHighlighting});
    }
    
    function applyLinkHighlighting(color) {
        const links = document.querySelectorAll('a');
        
        links.forEach(link => {
            if (!link.dataset.enhanced) {
                link.dataset.enhanced = 'true';
                link.style.backgroundColor = color;
                link.style.padding = '2px 4px';
                link.style.borderRadius = '3px';
                link.style.textDecoration = 'none';
                link.style.fontWeight = 'bold';
            }
        });
        
        addNotification('Link highlighting enabled', 'link-highlight');
    }
    
    function removeLinkHighlighting() {
        const enhancedLinks = document.querySelectorAll('a[data-enhanced="true"]');
        
        enhancedLinks.forEach(link => {
            link.style.backgroundColor = '';
            link.style.padding = '';
            link.style.borderRadius = '';
            link.style.textDecoration = '';
            link.style.fontWeight = '';
            delete link.dataset.enhanced;
        });
        
        addNotification('Link highlighting disabled', 'link-highlight');
    }
    
    function addNotification(message, type) {
        // Remove existing notification
        const existingNotification = document.getElementById('page-enhancer-notification');
        if (existingNotification) {
            existingNotification.remove();
        }
        
        // Create notification
        const notification = document.createElement('div');
        notification.id = 'page-enhancer-notification';
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #333;
            color: white;
            padding: 12px 20px;
            border-radius: 6px;
            font-family: Arial, sans-serif;
            font-size: 14px;
            z-index: 10000;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            animation: slideIn 0.3s ease-out;
        `;
        
        // Add animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideIn {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
        `;
        document.head.appendChild(style);
        
        document.body.appendChild(notification);
        
        // Auto-remove after 3 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 3000);
    }
    
    // Utility function to get page statistics
    function getPageStatistics() {
        return {
            links: document.querySelectorAll('a').length,
            images: document.querySelectorAll('img').length,
            paragraphs: document.querySelectorAll('p').length,
            headings: document.querySelectorAll('h1, h2, h3, h4, h5, h6').length
        };
    }
    
    // Expose functions to window for debugging
    window.pageEnhancer = {
        toggleDarkMode,
        toggleReadingMode,
        toggleLinkHighlighting,
        getPageStatistics
    };
    
})(); 