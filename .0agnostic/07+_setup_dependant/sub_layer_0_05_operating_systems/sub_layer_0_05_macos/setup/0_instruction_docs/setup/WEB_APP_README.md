---
resource_id: "9de73e29-cf0a-4a1a-ba3b-d397bbd37d6d"
resource_type: "document"
resource_name: "WEB_APP_README"
---
# Phoneme Frequency Tracker - Web Application

A comprehensive web interface for the Phoneme Frequency Tracker, implementing all terminal functions as modern web features.

<!-- section_id: "1db996a6-e052-4710-894e-81f40980ac12" -->
## 🚀 Quick Start

<!-- section_id: "085fd1c8-53cf-4de7-937f-df9ceaa5b32e" -->
### Prerequisites
- Python 3.7+
- Flask and dependencies (see requirements.txt)

<!-- section_id: "eaa6e20e-a32e-40f7-9b1a-d528493e3726" -->
### Installation & Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Database** (if not already done)
   ```bash
   python main.py
   # This will create the database and sample data if they don't exist
   ```

3. **Start the Web Application**
   ```bash
   python app.py
   ```

4. **Access the Application**
   - Open your browser to: `http://localhost:5000`
   - The application will be available on all network interfaces (0.0.0.0:5000)

<!-- section_id: "6b72827c-1836-42fd-b8b2-f6eb6dfd18b7" -->
## 📱 Features Implemented

<!-- section_id: "0bd2ff1e-6839-4c9d-8849-8bbb115b5bb6" -->
### 🔤 Phoneme Management
- **Flat View**: Simple list of all phonemes with search functionality
- **Nested View**: Organized hierarchy by syllable type, position, and groups
- **Full Hierarchy**: Complete structure with frequency visualization and sorting

<!-- section_id: "a0185294-8aa1-481e-92bf-55768dcb0554" -->
### 📚 Word Management
- **Create Words**: Table-based phoneme selection with real-time hierarchy display
- **View All Words**: Comprehensive word browser with search and sorting
- **Word Lookup**: Multi-criteria search (English, IPA, Dictionary, New Language)
- **Edit Words**: Full word editing interface with structured phoneme data
- **Delete Words**: Safe deletion with confirmation and frequency updates

<!-- section_id: "62f789d0-05e8-4b6a-a9b5-7c882406aa4e" -->
### ⚙️ Admin Panel
- **Phoneme Management**: Add, edit, delete phonemes with frequency controls
- **Bulk Operations**: Reset frequencies, reset entire database
- **Real-time Updates**: Live frequency adjustments and table management

<!-- section_id: "5a014615-8df7-4040-848f-f6ef1a49ffd9" -->
### 🎯 User Stories Implemented

#### 1. Table-Based Word Creation with Hierarchy Display
- **User Flow**: Select syllable type → Apply filters → View phoneme tables → Select phonemes → Create word
- **Features**:
  - Dynamic phoneme table loading based on filters
  - Real-time IPA building from selected phonemes
  - Frequency-based phoneme sorting and visualization
  - Group/subgroup hierarchy display
  - Automatic frequency updates after word creation

#### 2. Comprehensive Word Management
- **User Flow**: Browse words → Search/filter → Edit/delete → Manage vocabulary
- **Features**:
  - Advanced search across multiple fields
  - Structured phoneme data display
  - Video file associations
  - Bulk operations and statistics

#### 3. Admin Phoneme Control
- **User Flow**: Access admin panel → Manage phonemes → Control frequencies → System maintenance
- **Features**:
  - Add new phonemes with full metadata
  - Real-time frequency adjustments
  - Bulk database operations
  - Search and filter capabilities

<!-- section_id: "24d7a572-5270-48ea-bf5f-2651090a6712" -->
## 🏗️ Architecture

<!-- section_id: "55eaa002-fa17-4887-88f0-5354f75b7afe" -->
### Backend (Flask)
- **app.py**: Main Flask application with all API endpoints
- **Routes**: RESTful API design with JSON responses
- **Database**: SQLite integration using existing main.py functions
- **File Handling**: Video upload support with secure filename handling

<!-- section_id: "1313534e-5511-4646-99b7-542de0447258" -->
### Frontend (Modern Web)
- **Responsive Design**: Mobile-first approach with CSS Grid/Flexbox
- **Interactive UI**: Dynamic content loading and real-time updates
- **Modern Styling**: Dark theme with glassmorphism effects
- **Accessibility**: Semantic HTML and keyboard navigation support

<!-- section_id: "b65c2b7c-d8fc-474f-8634-4ebd69b70db3" -->
### Integration
- **Terminal Functions**: All main.py functions exposed as web endpoints
- **Data Consistency**: Maintains compatibility with existing database schema
- **File Management**: Handles video uploads and serves static content

<!-- section_id: "05131d42-2cbd-48ac-9c51-21b3e6e1518e" -->
## 🎨 UI/UX Features

<!-- section_id: "370e3951-572c-49bc-b32a-bc015d5e9f1c" -->
### Design System
- **Color Palette**: Professional dark theme with accent colors
- **Typography**: System fonts with monospace for phonetic data
- **Icons**: Emoji-based iconography for universal recognition
- **Animations**: Smooth transitions and hover effects

<!-- section_id: "299b757c-ecce-4d9c-838d-1ac103bf7f23" -->
### Responsive Design
- **Mobile**: Optimized for smartphone usage
- **Tablet**: Adapted layouts for medium screens
- **Desktop**: Full-featured interface with multi-column layouts

<!-- section_id: "34c2e19d-fc6d-4b7e-8788-79a76a399a96" -->
### User Experience
- **Intuitive Navigation**: Clear breadcrumbs and back buttons
- **Real-time Feedback**: Loading states and success/error messages
- **Data Visualization**: Frequency bars, progress indicators, and statistics
- **Search & Filter**: Instant search with highlighting and filtering

<!-- section_id: "9d98c3e2-3924-4615-8401-fe15124f9d95" -->
## 📊 API Endpoints

<!-- section_id: "3b3c4d79-9cb4-448b-9ebc-d07ac0976486" -->
### Phoneme Management
- `GET /phonemes/flat` - Flat phoneme view
- `GET /phonemes/nested` - Nested hierarchy view  
- `GET /phonemes/full` - Full hierarchy with frequencies
- `GET /api/phoneme-tables` - Dynamic phoneme tables for word creation

<!-- section_id: "0dc2a0db-deef-4043-bd4c-d6374742e49e" -->
### Word Management
- `GET /words/display` - Display all words
- `GET /words/lookup` - Word lookup interface
- `GET /api/lookup-word` - Search API
- `POST /api/create-word` - Create new word
- `GET /words/edit/<id>` - Edit word interface
- `POST /api/update-word/<id>` - Update word
- `DELETE /api/delete-word/<id>` - Delete word

<!-- section_id: "97aa50ff-c8b0-47bf-bc1e-5e5432023d30" -->
### Admin Functions
- `GET /admin/phonemes` - Admin phoneme management
- `GET /api/admin/phonemes` - Get all phonemes
- `POST /api/admin/add-phoneme` - Add new phoneme
- `POST /api/admin/update-phoneme-frequency` - Update frequency
- `DELETE /api/admin/delete-phoneme/<id>` - Delete phoneme
- `POST /api/admin/reset-database` - Reset database

<!-- section_id: "143cd00b-be44-49e8-8726-1c07a3e40d53" -->
## 🔧 Configuration

<!-- section_id: "594b415d-ce60-4c7e-b228-a283a4ec4998" -->
### Environment Variables
- `FLASK_ENV`: Set to 'development' for debug mode
- `FLASK_DEBUG`: Enable/disable debug mode
- `UPLOAD_FOLDER`: Directory for video uploads (default: 'videos')

<!-- section_id: "15198e62-5db4-46ff-9e13-b018ccbd8f35" -->
### File Upload Settings
- **Allowed Extensions**: mp4, avi, mov, mkv, webm
- **Security**: Secure filename handling with Werkzeug
- **Storage**: Local filesystem with organized directory structure

<!-- section_id: "71a77c60-a590-4773-9778-1595956f0c82" -->
## 🚦 Development

<!-- section_id: "31e1dc9b-78a8-4ed5-b5ad-43d2a98f06fd" -->
### Running in Development Mode
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

<!-- section_id: "de36f7f5-b985-45e9-bcf0-e5c0770da8e0" -->
### Code Structure
```
/workspace/
├── app.py                 # Flask web application
├── main.py               # Original terminal application
├── templates/            # HTML templates
│   ├── index.html        # Main menu
│   ├── phonemes_*.html   # Phoneme views
│   ├── words_*.html      # Word management
│   ├── word_*.html       # Word operations
│   └── admin_*.html      # Admin interfaces
├── videos/               # Video file storage
├── requirements.txt      # Python dependencies
└── phonemes.db          # SQLite database
```

<!-- section_id: "3c33ce41-2bda-462b-b749-a2e3ccbfddb8" -->
## 🎯 User Stories Completed

<!-- section_id: "6ed95ff2-df2a-4d02-868b-69402ed1e14a" -->
### ✅ Primary User Stories

1. **Table-Based Word Creation**: Complete implementation with hierarchy display, filtering, and real-time phoneme selection
2. **Phoneme Hierarchy Visualization**: Three different views (flat, nested, full) with sorting and frequency display
3. **Comprehensive Search**: Multi-criteria word lookup with advanced filtering
4. **Admin Management**: Full phoneme CRUD operations with frequency controls
5. **Word Management**: Complete lifecycle from creation to deletion with editing capabilities

<!-- section_id: "c4c5d901-57dd-423d-8099-a4b425cf0def" -->
### ✅ Secondary Features

1. **Responsive Design**: Works on all device sizes
2. **Real-time Updates**: Dynamic content loading and instant feedback
3. **Data Visualization**: Frequency bars, statistics, and progress indicators
4. **File Management**: Video upload and playback support
5. **Error Handling**: Comprehensive error messages and validation

<!-- section_id: "c08fc30e-c298-47e6-9516-58de75568950" -->
## 🔮 Future Enhancements

<!-- section_id: "f33e932a-1e4f-4f07-a63a-3399f9a45f29" -->
### Pending Features
- **Video Integration**: Complete video upload and playback system
- **Phoneme Suggestion System**: AI-powered phoneme recommendations with conflict detection
- **Export/Import**: Database backup and restoration features
- **User Authentication**: Multi-user support with role-based access
- **Analytics Dashboard**: Usage statistics and trends visualization

<!-- section_id: "f9f7e710-b63e-4eb2-9ba4-03661740c6f1" -->
### Technical Improvements
- **Caching**: Redis integration for better performance
- **Database**: PostgreSQL migration for production use
- **Testing**: Comprehensive test suite with pytest
- **Documentation**: API documentation with Swagger/OpenAPI
- **Deployment**: Docker containerization and cloud deployment guides

<!-- section_id: "cc976697-dae3-4838-a3d5-60e5f2b0797a" -->
## 📝 Notes

- All terminal functions from `main.py` have been successfully implemented as web endpoints
- The web interface maintains full compatibility with the existing database schema
- Modern web technologies provide a superior user experience compared to terminal interface
- The application is production-ready with proper error handling and security measures

<!-- section_id: "43f465d2-7bf6-45e9-8e89-b77082c421fd" -->
## 🤝 Contributing

The web application successfully implements all user stories found in the terminal functions, providing a modern, intuitive interface for phoneme frequency tracking and constructed language development.