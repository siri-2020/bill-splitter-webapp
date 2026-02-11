# Bill Splitter Web App

A modern web application for splitting restaurant bills fairly among multiple people. Converted from a Pygame desktop application to a Flask web app optimized for deployment on Render.com.

## Features

- 🍽️ Add multiple dishes with prices
- 👥 Add multiple people
- ✅ Assign dishes to people (supports shared dishes)
- 💰 Automatic fair bill calculation
- 📥 Download bill summary as text file
- 📱 Responsive design for mobile and desktop
- 🎨 Beautiful, modern UI

## How It Works

1. **Add Dishes**: Enter each dish name and price from your bill
2. **Add People**: Enter the names of everyone sharing the bill
3. **Assign Orders**: Select which dishes each person ordered (can share dishes)
4. **Get Results**: See how much each person owes and download the summary

## Deployment on Render.com

### Method 1: Using GitHub (Recommended)

1. Push this code to a GitHub repository
2. Go to [Render.com](https://render.com) and sign up/log in
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: bill-splitter (or your preferred name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click "Create Web Service"
7. Wait for deployment to complete
8. Access your app at the provided URL!

### Method 2: Manual Deploy

1. Install Render CLI: `npm install -g render`
2. Login: `render login`
3. From this directory, run: `render deploy`

## Local Development

To run locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open http://localhost:5000 in your browser.

## Environment Variables

- `PORT`: The port to run on (automatically set by Render)

## File Structure

```
bill-splitter-web/
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Main HTML template with CSS/JS
├── requirements.txt      # Python dependencies
├── render.yaml          # Render.com configuration
└── README.md            # This file
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Deployment**: Render.com
- **Server**: Gunicorn

## Differences from Original Pygame Version

The web version maintains all core functionality while adapting to a web environment:

- ✅ All bill splitting logic preserved
- ✅ Multi-step workflow maintained
- ✅ File download functionality (replaces local file save)
- ❌ QR code image removed (can be added back via upload or URL)
- ✅ Improved responsive design
- ✅ Modern, accessible UI

## Contributing

Feel free to fork this project and customize it for your needs!

## License

Open source - feel free to use and modify as needed.
