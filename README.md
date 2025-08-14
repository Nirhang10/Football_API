# Football_API
# ⚽ Football Dashboard

A modern, responsive web application for displaying football club information, match fixtures, and league standings with stunning visual design and smooth animations.

## 🌟 Features

### 🏟️ Club Dashboard
- **Club Profile**: Display club name, logo, stadium, and location with country flags
- **Squad Management**: Interactive player roster with positions and nationalities
- **Coaching Staff**: Coach information with contracts and nationalities
- **Statistics**: Real-time squad statistics and team metrics

### ⚽ Match System
- **Live Match Display**: Head-to-head match visualization with team logos
- **Competition Branding**: Support for various competitions (Premier League, Champions League, etc.)
- **Interactive VS Layout**: Animated match cards with rotating elements
- **Match Status**: Real-time match status and result tracking

### 🏆 Premier League Integration
- **League Overview**: Season information and current matchday
- **Fixtures & Results**: Complete match listing with dates and outcomes
- **Team Links**: Direct navigation to individual club pages
- **Statistics Dashboard**: League-wide statistics and metrics

## 🎨 Design Features

### ✨ Modern UI/UX
- **Glass-morphism Design**: Backdrop blur effects and transparency
- **Gradient Backgrounds**: Sport-themed color schemes
- **Smooth Animations**: Hover effects, transitions, and micro-interactions
- **Responsive Layout**: Mobile-first design that works on all devices

### 🎪 Interactive Elements
- **Pulsing Animations**: Logo and badge effects
- **Hover Transformations**: 3D card effects and scaling
- **Loading States**: Professional loading animations
- **Color-coded Results**: Visual indicators for match outcomes

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Templating**: Django Templates (Jinja2 syntax)
- **Styling**: Modern CSS with Flexbox/Grid
- **Animations**: Pure CSS animations and transitions
- **Icons**: Emoji-based iconography
- **Responsive**: CSS Media Queries

## 📁 Project Structure

```
football-dashboard/
├── templates/
│   ├── football.html              # Club dashboard template
│   ├── match.html                 # Individual match display
│   ├── PL_match.html             # Premier League fixtures
│   └── improved_index_template.html # Weather dashboard reference
├── static/
│   ├── css/
│   │   ├── club-dashboard.css
│   │   ├── match-display.css
│   │   └── premier-league.css
│   ├── js/
│   │   ├── animations.js
│   │   └── interactions.js
│   └── images/
│       ├── logos/
│       └── flags/
├── docs/
│   ├── screenshots/
│   └── design-specs.md
├── README.md
├── requirements.txt
└── LICENSE
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 3.2+
- Modern web browser with CSS Grid support

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/football-dashboard.git
   cd football-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server**
   ```bash
   python manage.py runserver
   ```

4. **Open your browser**
   ```
   http://localhost:8000
   ```

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: 320px - 767px

## 🎯 Template Context Variables

### Club Dashboard (`football.html`)
```python
context = {
    'club': {
        'club_name': 'Manchester United',
        'club_logo': '/static/logos/man-utd.png',
        'club_venue': 'Old Trafford',
        'place_name': 'Manchester, England',
        'place_flag': '/static/flags/england.png'
    },
    'squad': [
        {
            'name': 'Player Name',
            'position': 'Forward',
            'nationality': 'England'
        }
    ],
    'coach': {
        'lastname': 'Manager Name',
        'nation': 'Country',
        'contract': '2025'
    }
}
```

### Match Display (`match.html`)
```python
context = {
    'match': {
        'competition': 'Premier League',
        'logo': '/static/logos/premier-league.png',
        'first_team_home': 'Arsenal',
        'first_team_home_logo': '/static/logos/arsenal.png',
        'first_away_team': 'Chelsea',
        'first_away_team_logo': '/static/logos/chelsea.png'
    }
}
```

### Premier League (`PL_match.html`)
```python
context = {
    'leauge_info': {
        'league_name': 'Premier League',
        'league_logo': '/static/logos/premier-league.png',
        'season': '2024-25',
        'matchday': '15'
    },
    'matches': [
        {
            'home_team': 'Arsenal',
            'home_logo': '/static/logos/arsenal.png',
            'home_team_id': 1,
            'away_team': 'Chelsea',
            'away_logo': '/static/logos/chelsea.png',
            'away_team_id': 2,
            'match_date': '2024-03-15',
            'match_winner': 'Arsenal'
        }
    ]
}
```

## 🎨 Design System

### Color Palette
- **Primary**: `#667eea` → `#764ba2` (Gradient)
- **Success**: `#00b894` → `#00cec9` (Home wins)
- **Warning**: `#e17055` → `#d63031` (Away wins)
- **Info**: `#74b9ff` → `#0984e3` (TBD matches)
- **Premier League**: `#37003c` → `#00ff87`

### Typography
- **Font Family**: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- **Headings**: 800-900 font weight
- **Body**: 500-600 font weight
- **Labels**: 600-700 font weight, uppercase

### Animations
- **Duration**: 0.3s - 0.8s
- **Easing**: `ease-out`, `ease-in-out`
- **Transform**: `translateY()`, `scale()`, `rotate()`

## 📸 Screenshots

### Club Dashboard
![Club Dashboard](docs/screenshots/club-dashboard.png)

### Match Display
![Match Display](docs/screenshots/match-display.png)

### Premier League
![Premier League](docs/screenshots/premier-league.png)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow responsive design principles
- Maintain consistent animation timing
- Use semantic HTML structure
- Optimize images and assets
- Test across different browsers

## 📝 Changelog

### v1.0.0 (2024-08-13)
- ✨ Initial release with club dashboard
- ⚽ Match display system
- 🏆 Premier League integration
- 📱 Full responsive design
- 🎨 Modern glass-morphism UI

## 🐛 Known Issues

- Logo images may not load if paths are incorrect
- Some animations may be reduced on devices with `prefers-reduced-motion`
- Internet Explorer not supported (modern browsers only)

## 🔮 Future Roadmap

- [ ] **Live Score Updates**: Real-time match score integration
- [ ] **Player Statistics**: Detailed player performance metrics
- [ ] **League Table**: Interactive league standings
- [ ] **Match Highlights**: Video integration
- [ ] **Fantasy Integration**: Fantasy football features
- [ ] **Mobile App**: Progressive Web App (PWA)
- [ ] **Multi-language**: Internationalization support
- [ ] **Dark Mode**: Theme switching capability

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Design Inspiration**: Modern sports broadcasting interfaces
- **Color Schemes**: Official Premier League branding
- **Icons**: Emoji-based iconography for cross-platform compatibility
- **Animation Libraries**: Pure CSS animations for performance

## 📞 Support

- **Email**: nirhanglimbu558@gmail.com
- **Issues**: [GitHub Issues](https://github.com/Nirhang10/football-dashboard/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Nirhang10/football-dashboard/discussions)

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

**Made with ❤️ for football fans around the world** 🌍⚽
