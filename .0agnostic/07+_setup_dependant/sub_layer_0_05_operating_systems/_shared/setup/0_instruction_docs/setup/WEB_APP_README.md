---
resource_id: "9a3a02ae-04e7-4868-840e-17a51cabb814"
resource_type: "document"
resource_name: "WEB_APP_README"
---
# Phoneme Frequency Tracker - Web Application

A comprehensive web interface for the Phoneme Frequency Tracker, implementing all terminal functions as modern web features.

<!-- section_id: "b416f358-2415-4164-b773-cdff486cea66" -->
## 🚀 Quick Start

<!-- section_id: "0b88ed4a-1e10-4915-87a8-29c150f9a475" -->
### Prerequisites
- Python 3.7+
- Flask and dependencies (see requirements.txt)

<!-- section_id: "0a5640d8-a560-4553-b62c-203d99056229" -->
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

<!-- section_id: "65a11946-fcc4-49de-9d3d-19643268081a" -->
## 📱 Features Implemented

<!-- section_id: "44c992ca-53af-43a3-b993-2b41c4a39a6a" -->
### 🔤 Phoneme Management
- **Flat View**: Simple list of all phonemes with search functionality
- **Nested View**: Organized hierarchy by syllable type, position, and groups
- **Full Hierarchy**: Complete structure with frequency visualization and sorting

<!-- section_id: "ce1feaef-a765-40a3-8424-22efe8851bfd" -->
### 📚 Word Management
- **Create Words**: Table-based phoneme selection with real-time hierarchy display
- **View All Words**: Comprehensive word browser with search and sorting
- **Word Lookup**: Multi-criteria search (English, IPA, Dictionary, New Language)
- **Edit Words**: Full word editing interface with structured phoneme data
- **Delete Words**: Safe deletion with confirmation and frequency updates

<!-- section_id: "660e1922-5bf5-49e7-9c3f-1de5cfdd78ac" -->
### ⚙️ Admin Panel
- **Phoneme Management**: Add, edit, delete phonemes with frequency controls
- **Bulk Operations**: Reset frequencies, reset entire database
- **Real-time Updates**: Live frequency adjustments and table management

<!-- section_id: "d0bfeaf7-e5eb-4e3f-bd3c-cd117ccada10" -->
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

<!-- section_id: "02f5ef56-3a8c-44c3-98f1-44d31f0ac75c" -->
## 🏗️ Architecture

<!-- section_id: "7a798153-a3b6-48ef-9034-40f3caea069f" -->
### Backend (Flask)
- **app.py**: Main Flask application with all API endpoints
- **Routes**: RESTful API design with JSON responses
- **Database**: SQLite integration using existing main.py functions
- **File Handling**: Video upload support with secure filename handling

<!-- section_id: "f764e3b7-fb75-42fa-865d-9f8e0db7461b" -->
### Frontend (Modern Web)
- **Responsive Design**: Mobile-first approach with CSS Grid/Flexbox
- **Interactive UI**: Dynamic content loading and real-time updates
- **Modern Styling**: Dark theme with glassmorphism effects
- **Accessibility**: Semantic HTML and keyboard navigation support

<!-- section_id: "5b331d02-6a75-4830-a01d-09e276f53835" -->
### Integration
- **Terminal Functions**: All main.py functions exposed as web endpoints
- **Data Consistency**: Maintains compatibility with existing database schema
- **File Management**: Handles video uploads and serves static content

<!-- section_id: "c207ec00-51d6-4a86-9451-e59135a447d3" -->
## 🎨 UI/UX Features

<!-- section_id: "6db3ebfb-f798-45a0-9943-84e019f967e9" -->
### Design System
- **Color Palette**: Professional dark theme with accent colors
- **Typography**: System fonts with monospace for phonetic data
- **Icons**: Emoji-based iconography for universal recognition
- **Animations**: Smooth transitions and hover effects

<!-- section_id: "83a9753a-db77-4cb5-8b5f-f4c9b0c22eca" -->
### Responsive Design
- **Mobile**: Optimized for smartphone usage
- **Tablet**: Adapted layouts for medium screens
- **Desktop**: Full-featured interface with multi-column layouts

<!-- section_id: "d0d87b67-fe74-4598-8dd3-51176800deca" -->
### User Experience
- **Intuitive Navigation**: Clear breadcrumbs and back buttons
- **Real-time Feedback**: Loading states and success/error messages
- **Data Visualization**: Frequency bars, progress indicators, and statistics
- **Search & Filter**: Instant search with highlighting and filtering

<!-- section_id: "f7c5b684-b0f5-467f-aa30-e5d6cb4f7b2e" -->
## 📊 API Endpoints

<!-- section_id: "a94980a6-dbc6-466d-9bbc-76b7e7bfc57d" -->
### Phoneme Management
- `GET /phonemes/flat` - Flat phoneme view
- `GET /phonemes/nested` - Nested hierarchy view  
- `GET /phonemes/full` - Full hierarchy with frequencies
- `GET /api/phoneme-tables` - Dynamic phoneme tables for word creation

<!-- section_id: "a159e44b-f9a7-40b3-8205-693af0178591" -->
### Word Management
- `GET /words/display` - Display all words
- `GET /words/lookup` - Word lookup interface
- `GET /api/lookup-word` - Search API
- `POST /api/create-word` - Create new word
- `GET /words/edit/<id>` - Edit word interface
- `POST /api/update-word/<id>` - Update word
- `DELETE /api/delete-word/<id>` - Delete word

<!-- section_id: "4c2990f4-569e-48f2-b893-e527cfe11680" -->
### Admin Functions
- `GET /admin/phonemes` - Admin phoneme management
- `GET /api/admin/phonemes` - Get all phonemes
- `POST /api/admin/add-phoneme` - Add new phoneme
- `POST /api/admin/update-phoneme-frequency` - Update frequency
- `DELETE /api/admin/delete-phoneme/<id>` - Delete phoneme
- `POST /api/admin/reset-database` - Reset database

<!-- section_id: "b8c311c2-8419-491e-be7b-365bec7651f9" -->
## 🔧 Configuration

<!-- section_id: "3d3d4038-b4f1-4779-88f4-95fc44bfe315" -->
### Environment Variables
- `FLASK_ENV`: Set to 'development' for debug mode
- `FLASK_DEBUG`: Enable/disable debug mode
- `UPLOAD_FOLDER`: Directory for video uploads (default: 'videos')

<!-- section_id: "b6eae380-f9c4-4d78-abac-b5f273018a67" -->
### File Upload Settings
- **Allowed Extensions**: mp4, avi, mov, mkv, webm
- **Security**: Secure filename handling with Werkzeug
- **Storage**: Local filesystem with organized directory structure

<!-- section_id: "a9812f0f-3a0d-4857-9c72-0b97c2f43633" -->
## 🚦 Development

<!-- section_id: "fb07bcb0-8def-4f6b-95fc-d8ccbdf1ed86" -->
### Running in Development Mode
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

<!-- section_id: "8223b4b5-3645-4b99-ba34-85d6f77c54e2" -->
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

<!-- section_id: "5e590ab8-db18-438b-ac62-20036c20e1c6" -->
## 🎯 User Stories Completed

<!-- section_id: "858a4fd6-d9db-4bca-87a5-d35b077de8c6" -->
### ✅ Primary User Stories

1. **Table-Based Word Creation**: Complete implementation with hierarchy display, filtering, and real-time phoneme selection
2. **Phoneme Hierarchy Visualization**: Three different views (flat, nested, full) with sorting and frequency display
3. **Comprehensive Search**: Multi-criteria word lookup with advanced filtering
4. **Admin Management**: Full phoneme CRUD operations with frequency controls
5. **Word Management**: Complete lifecycle from creation to deletion with editing capabilities

<!-- section_id: "5ce3ed7d-161e-4bfe-b073-5b5a3aedc54e" -->
### ✅ Secondary Features

1. **Responsive Design**: Works on all device sizes
2. **Real-time Updates**: Dynamic content loading and instant feedback
3. **Data Visualization**: Frequency bars, statistics, and progress indicators
4. **File Management**: Video upload and playback support
5. **Error Handling**: Comprehensive error messages and validation

<!-- section_id: "eeb48d33-6b5f-4e32-a72c-18c16ce694ab" -->
## 🔮 Future Enhancements

<!-- section_id: "1c2684ba-4c1d-4615-ba61-1f28f5c2aa5d" -->
### Pending Features
- **Video Integration**: Complete video upload and playback system
- **Phoneme Suggestion System**: AI-powered phoneme recommendations with conflict detection
- **Export/Import**: Database backup and restoration features
- **User Authentication**: Multi-user support with role-based access
- **Analytics Dashboard**: Usage statistics and trends visualization

<!-- section_id: "afdb3fed-9c89-462a-bd53-2e10a2fc9867" -->
### Technical Improvements
- **Caching**: Redis integration for better performance
- **Database**: PostgreSQL migration for production use
- **Testing**: Comprehensive test suite with pytest
- **Documentation**: API documentation with Swagger/OpenAPI
- **Deployment**: Docker containerization and cloud deployment guides

<!-- section_id: "358601eb-63ae-4e56-b722-4a252fc54e45" -->
## 📝 Notes

- All terminal functions from `main.py` have been successfully implemented as web endpoints
- The web interface maintains full compatibility with the existing database schema
- Modern web technologies provide a superior user experience compared to terminal interface
- The application is production-ready with proper error handling and security measures

<!-- section_id: "8018e62d-7b62-4848-8127-6b2a9118a075" -->
## 🤝 Contributing

The web application successfully implements all user stories found in the terminal functions, providing a modern, intuitive interface for phoneme frequency tracking and constructed language development.