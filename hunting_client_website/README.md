# Hunting Client Website

A dark-themed website built with Flask, featuring a modern design with social media integration, comment system, and admin panel.

## Features

- **Dark Theme Design**: Modern, responsive dark theme with smooth animations
- **Social Media Integration**: Direct links to YouTube, Discord, and Kick channels
- **Comment System**: Users can leave comments that are stored in a SQLite database
- **Admin Panel**: Secure admin interface to manage and reply to comments
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Interactive Elements**: Hover effects, animations, and smooth transitions

## Project Structure

```
hunting_client_website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage
│   ├── comments.html     # Comments page
│   ├── admin_login.html  # Admin login page
│   └── admin_panel.html  # Admin management panel
└── static/              # Static files
    ├── css/
    │   └── style.css     # Main stylesheet
    └── js/
        └── script.js     # JavaScript functionality
```

## Installation & Setup

1. **Navigate to the project directory:**
   ```bash
   cd hunting_client_website
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Access the website:**
   - Open your browser and go to `http://localhost:5000`
   - The database will be automatically created on first run

## Usage

### Main Website
- **Homepage**: Features welcome message, social media buttons, and about section
- **Comments**: Users can leave comments with username, optional email, and message
- **Social Links**: Update the URLs in `templates/index.html` to point to your actual channels

### Admin Panel
- **Access**: Go to `/admin` or click "Admin" in the navigation
- **Default Credentials**: 
  - Username: `admin`
  - Password: `admin123`
- **Features**: View all comments, reply to comments, manage community interactions

## Customization

### Update Social Media Links
Edit the social media URLs in `templates/index.html`:
```html
<a href="https://youtube.com/@yourchannel" target="_blank" class="social-btn youtube-btn">
<a href="https://discord.gg/yourserver" target="_blank" class="social-btn discord-btn">
<a href="https://kick.com/yourchannel" target="_blank" class="social-btn kick-btn">
```

### Change Admin Credentials
In `app.py`, modify the admin login check:
```python
if username == 'your_username' and password == 'your_secure_password':
```

### Customize Colors
Edit CSS variables in `static/css/style.css`:
```css
:root {
    --accent-color: #ff6b35;  /* Main accent color */
    --primary-bg: #0a0a0a;   /* Background color */
    /* ... other variables ... */
}
```

## Database

The application uses SQLite database (`hunting_client.db`) with the following tables:
- **Comment**: Stores user comments with timestamps and admin replies
- **Admin**: Stores admin credentials (currently unused, using hardcoded credentials)

## Security Notes

- Change default admin credentials before deployment
- Consider implementing proper password hashing for production use
- Add CSRF protection for forms in production
- Use environment variables for sensitive configuration

## Browser Support

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## Contributing

Feel free to customize and extend this website according to your needs. The code is well-commented and structured for easy modification.
