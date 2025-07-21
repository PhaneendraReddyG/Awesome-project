# Page Enhancer Browser Extension

A powerful browser extension that enhances your web browsing experience with features like dark mode, reading mode, and link highlighting.

## Features

- 🌙 **Dark Mode**: Toggle dark theme on any website
- 📖 **Reading Mode**: Distraction-free reading experience
- 🔗 **Link Highlighting**: Make links more visible
- ⚙️ **Customizable Settings**: Adjust colors and preferences
- ⌨️ **Keyboard Shortcuts**: Quick access to features
- 📊 **Page Statistics**: View page information

## Installation

### Chrome/Edge/Brave

1. Download or clone this repository
2. Open Chrome and go to `chrome://extensions/`
3. Enable "Developer mode" (toggle in top right)
4. Click "Load unpacked"
5. Select the `example_extension` folder
6. The extension should now appear in your extensions list

### Firefox

1. Download or clone this repository
2. Open Firefox and go to `about:debugging`
3. Click "This Firefox"
4. Click "Load Temporary Add-on"
5. Select the `manifest.json` file from the `example_extension` folder

## Usage

### Popup Interface

1. Click the extension icon in your browser toolbar
2. Use the buttons to toggle features:
   - **Toggle Dark Mode**: Switch between light and dark themes
   - **Reading Mode**: Hide distractions and improve readability
   - **Highlight Links**: Make all links more visible

### Keyboard Shortcuts

- `Ctrl + Shift + D`: Toggle dark mode
- `Ctrl + Shift + R`: Toggle reading mode

### Context Menu

Right-click on any webpage to access:
- Toggle Dark Mode
- Toggle Reading Mode
- Toggle Link Highlighting

### Settings

In the popup, you can configure:
- **Auto Dark Mode**: Automatically enable dark mode at night
- **Highlight Color**: Choose your preferred link highlighting color

## File Structure

```
example_extension/
├── manifest.json          # Extension configuration
├── popup.html            # Popup interface
├── popup.js              # Popup functionality
├── content.js            # Page modification scripts
├── content.css           # Injected styles
├── background.js         # Background service worker
├── styles/
│   └── popup.css         # Popup styling
└── README.md             # This file
```

## Features Explained

### Dark Mode
- Changes background to dark colors
- Adjusts text colors for readability
- Applies filters to images and videos
- Works on any website

### Reading Mode
- Centers content with optimal width
- Uses serif fonts for better readability
- Hides navigation, ads, and other distractions
- Increases font size and line spacing

### Link Highlighting
- Makes all links more visible
- Customizable highlight color
- Adds padding and bold text
- Easy to spot clickable elements

## Development

### Prerequisites
- Basic knowledge of HTML, CSS, and JavaScript
- Understanding of browser extension APIs

### Making Changes

1. **Modify Features**: Edit `content.js` to change page modifications
2. **Update UI**: Modify `popup.html` and `popup.css` for interface changes
3. **Add Permissions**: Update `manifest.json` if you need new permissions
4. **Test**: Reload the extension in `chrome://extensions/`

### Adding New Features

1. Add the feature logic to `content.js`
2. Create UI elements in `popup.html`
3. Add event handlers in `popup.js`
4. Update `manifest.json` if needed
5. Test thoroughly

## Troubleshooting

### Extension Not Loading
- Check `manifest.json` syntax
- Verify all file paths are correct
- Look for errors in the browser console

### Features Not Working
- Ensure the extension has necessary permissions
- Check if content scripts are running
- Verify message passing between components

### Performance Issues
- Minimize DOM manipulations
- Use efficient selectors
- Avoid excessive storage operations

## Browser Compatibility

- ✅ Chrome 88+
- ✅ Edge 88+
- ✅ Brave (Chromium-based)
- ✅ Firefox 109+
- ⚠️ Safari (requires different approach)

## Permissions Used

- `activeTab`: Access to current tab
- `storage`: Save user preferences
- `scripting`: Inject scripts into pages
- `contextMenus`: Add right-click menu items

## Security Considerations

- Only requests necessary permissions
- Validates all user input
- Uses secure storage for settings
- No external data collection

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

If you encounter issues:
1. Check the browser console for errors
2. Verify the extension is properly loaded
3. Try disabling other extensions
4. Report issues with detailed information

## Future Enhancements

- [ ] Custom CSS injection
- [ ] Text-to-speech functionality
- [ ] Screenshot capture
- [ ] Bookmark integration
- [ ] Export/import settings
- [ ] Multiple themes
- [ ] Performance optimizations

---

**Note**: This is an example extension for educational purposes. For production use, consider additional security measures and thorough testing. 