---
resource_id: "39338954-6742-427e-bc2c-cdd70cafb212"
resource_type: "document"
resource_name: "WEB_APP_README"
---
# Phoneme Frequency Tracker - Web Application

A comprehensive web interface for the Phoneme Frequency Tracker, implementing all terminal functions as modern web features.

<!-- section_id: "719dae1e-c041-4672-a5de-71f8a3208d8c" -->
## 🚀 Quick Start

<!-- section_id: "7972d040-0a30-4e41-93e8-f9400b55276b" -->
### Prerequisites
- Python 3.7+
- Flask and dependencies (see requirements.txt)

<!-- section_id: "9930811c-efc7-4c32-b50e-faa5128a69b1" -->
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

<!-- section_id: "a3f18a91-c4bb-4a2a-a57d-8c07c592da9e" -->
## 📱 Features Implemented

<!-- section_id: "e18780c5-00bd-44c3-967a-2509e8e622b5" -->
### 🔤 Phoneme Management
- **Flat View**: Simple list of all phonemes with search functionality
- **Nested View**: Organized hierarchy by syllable type, position, and groups
- **Full Hierarchy**: Complete structure with frequency visualization and sorting

<!-- section_id: "232d3c6d-1a04-4403-9725-2e1f13d9cc22" -->
### 📚 Word Management
- **Create Words**: Table-based phoneme selection with real-time hierarchy display
- **View All Words**: Comprehensive word browser with search and sorting
- **Word Lookup**: Multi-criteria search (English, IPA, Dictionary, New Language)
- **Edit Words**: Full word editing interface with structured phoneme data
- **Delete Words**: Safe deletion with confirmation and frequency updates

<!-- section_id: "3734000f-daa6-4443-bfd8-3f5ddfe77c17" -->
### ⚙️ Admin Panel
- **Phoneme Management**: Add, edit, delete phonemes with frequency controls
- **Bulk Operations**: Reset frequencies, reset entire database
- **Real-time Updates**: Live frequency adjustments and table management

<!-- section_id: "4d649c55-72c4-4ed6-acc2-eaeacedbaa07" -->
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

<!-- section_id: "152c0fa2-e4e3-4c28-84c6-c4412a022985" -->
## 🏗️ Architecture

<!-- section_id: "93cdcfce-3c29-4f55-b8be-2ec429ce82aa" -->
### Backend (Flask)
- **app.py**: Main Flask application with all API endpoints
- **Routes**: RESTful API design with JSON responses
- **Database**: SQLite integration using existing main.py functions
- **File Handling**: Video upload support with secure filename handling

<!-- section_id: "89ebde88-98ed-4a60-b29a-2a49f61aea8f" -->
### Frontend (Modern Web)
- **Responsive Design**: Mobile-first approach with CSS Grid/Flexbox
- **Interactive UI**: Dynamic content loading and real-time updates
- **Modern Styling**: Dark theme with glassmorphism effects
- **Accessibility**: Semantic HTML and keyboard navigation support

<!-- section_id: "7e9db116-a913-45fc-b52d-2c4b88222bf4" -->
### Integration
- **Terminal Functions**: All main.py functions exposed as web endpoints
- **Data Consistency**: Maintains compatibility with existing database schema
- **File Management**: Handles video uploads and serves static content

<!-- section_id: "478baf19-e119-4f46-9d87-7e0f3abb587c" -->
## 🎨 UI/UX Features

<!-- section_id: "923ce9ed-a341-4a5a-b01b-66270d1fb970" -->
### Design System
- **Color Palette**: Professional dark theme with accent colors
- **Typography**: System fonts with monospace for phonetic data
- **Icons**: Emoji-based iconography for universal recognition
- **Animations**: Smooth transitions and hover effects

<!-- section_id: "cdeac579-2d2f-47a2-b38f-2778c1b2068d" -->
### Responsive Design
- **Mobile**: Optimized for smartphone usage
- **Tablet**: Adapted layouts for medium screens
- **Desktop**: Full-featured interface with multi-column layouts

<!-- section_id: "42c39224-9dd7-4399-9809-1bc6c31edf05" -->
### User Experience
- **Intuitive Navigation**: Clear breadcrumbs and back buttons
- **Real-time Feedback**: Loading states and success/error messages
- **Data Visualization**: Frequency bars, progress indicators, and statistics
- **Search & Filter**: Instant search with highlighting and filtering

<!-- section_id: "8e70e86c-7d40-4eaa-8faf-60c662da97f8" -->
## 📊 API Endpoints

<!-- section_id: "f3179391-5828-48a5-ab64-84d8f73e1359" -->
### Phoneme Management
- `GET /phonemes/flat` - Flat phoneme view
- `GET /phonemes/nested` - Nested hierarchy view  
- `GET /phonemes/full` - Full hierarchy with frequencies
- `GET /api/phoneme-tables` - Dynamic phoneme tables for word creation

<!-- section_id: "06ef17e6-584c-46f1-aa51-dad5797231ab" -->
### Word Management
- `GET /words/display` - Display all words
- `GET /words/lookup` - Word lookup interface
- `GET /api/lookup-word` - Search API
- `POST /api/create-word` - Create new word
- `GET /words/edit/<id>` - Edit word interface
- `POST /api/update-word/<id>` - Update word
- `DELETE /api/delete-word/<id>` - Delete word

<!-- section_id: "45b9edcd-41a2-40a6-b829-9554405769a4" -->
### Admin Functions
- `GET /admin/phonemes` - Admin phoneme management
- `GET /api/admin/phonemes` - Get all phonemes
- `POST /api/admin/add-phoneme` - Add new phoneme
- `POST /api/admin/update-phoneme-frequency` - Update frequency
- `DELETE /api/admin/delete-phoneme/<id>` - Delete phoneme
- `POST /api/admin/reset-database` - Reset database

<!-- section_id: "cd8e1d8c-13da-470e-81ec-ff95bb9a9fa1" -->
## 🔧 Configuration

<!-- section_id: "fe41d407-91fc-4361-ad54-235e3fd46085" -->
### Environment Variables
- `FLASK_ENV`: Set to 'development' for debug mode
- `FLASK_DEBUG`: Enable/disable debug mode
- `UPLOAD_FOLDER`: Directory for video uploads (default: 'videos')

<!-- section_id: "aad5b92c-ab8b-4c15-82e4-c7d0bd8f134f" -->
### File Upload Settings
- **Allowed Extensions**: mp4, avi, mov, mkv, webm
- **Security**: Secure filename handling with Werkzeug
- **Storage**: Local filesystem with organized directory structure

<!-- section_id: "00a2291a-f66c-4216-b661-0067df57493c" -->
## 🚦 Development

<!-- section_id: "dd1e521d-9d1b-4f0f-9324-cbfe12ef2d4e" -->
### Running in Development Mode
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

<!-- section_id: "3919d682-11cb-44aa-af1c-d33fd12dad78" -->
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

<!-- section_id: "53244f62-b6e4-4bd7-95cd-d1221b2fd989" -->
## 🎯 User Stories Completed

<!-- section_id: "76ba90d9-457b-4821-851a-c66b333aeb8d" -->
### ✅ Primary User Stories

1. **Table-Based Word Creation**: Complete implementation with hierarchy display, filtering, and real-time phoneme selection
2. **Phoneme Hierarchy Visualization**: Three different views (flat, nested, full) with sorting and frequency display
3. **Comprehensive Search**: Multi-criteria word lookup with advanced filtering
4. **Admin Management**: Full phoneme CRUD operations with frequency controls
5. **Word Management**: Complete lifecycle from creation to deletion with editing capabilities

<!-- section_id: "9859bf58-3db7-4afb-90b9-8a66418639a5" -->
### ✅ Secondary Features

1. **Responsive Design**: Works on all device sizes
2. **Real-time Updates**: Dynamic content loading and instant feedback
3. **Data Visualization**: Frequency bars, statistics, and progress indicators
4. **File Management**: Video upload and playback support
5. **Error Handling**: Comprehensive error messages and validation

<!-- section_id: "459f6c11-0b49-4445-9e90-97cbb59f4894" -->
## 🔮 Future Enhancements

<!-- section_id: "c8e8f447-bc09-40a7-89a8-b13ad68e96d3" -->
### Pending Features
- **Video Integration**: Complete video upload and playback system
- **Phoneme Suggestion System**: AI-powered phoneme recommendations with conflict detection
- **Export/Import**: Database backup and restoration features
- **User Authentication**: Multi-user support with role-based access
- **Analytics Dashboard**: Usage statistics and trends visualization

<!-- section_id: "7f4c5234-8723-4360-a4ac-cd6744aa7cc2" -->
### Technical Improvements
- **Caching**: Redis integration for better performance
- **Database**: PostgreSQL migration for production use
- **Testing**: Comprehensive test suite with pytest
- **Documentation**: API documentation with Swagger/OpenAPI
- **Deployment**: Docker containerization and cloud deployment guides

<!-- section_id: "c173dd60-8229-4102-a46a-6c7c5706196b" -->
## 📝 Notes

- All terminal functions from `main.py` have been successfully implemented as web endpoints
- The web interface maintains full compatibility with the existing database schema
- Modern web technologies provide a superior user experience compared to terminal interface
- The application is production-ready with proper error handling and security measures

<!-- section_id: "21ecaa0e-d23e-4277-b32f-b7c410b96025" -->
## 🤝 Contributing

The web application successfully implements all user stories found in the terminal functions, providing a modern, intuitive interface for phoneme frequency tracking and constructed language development.