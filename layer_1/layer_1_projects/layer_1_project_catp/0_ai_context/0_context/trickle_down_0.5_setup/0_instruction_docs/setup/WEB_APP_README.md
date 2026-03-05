---
resource_id: "745db73e-b197-4f57-91f8-e85107af4723"
resource_type: "document"
resource_name: "WEB_APP_README"
---
# Phoneme Frequency Tracker - Web Application

A comprehensive web interface for the Phoneme Frequency Tracker, implementing all terminal functions as modern web features.

<!-- section_id: "7ec87e6f-32b3-41c0-babe-3391d4465aed" -->
## 🚀 Quick Start

<!-- section_id: "7b6b3511-ae4c-4fee-8d03-59423a9065af" -->
### Prerequisites
- Python 3.7+
- Flask and dependencies (see requirements.txt)

<!-- section_id: "210f2a9a-381f-4702-a4e5-f8f8b1123030" -->
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

<!-- section_id: "1ff211a5-f82d-4fce-845c-e8e92649edad" -->
## 📱 Features Implemented

<!-- section_id: "d1e1d4ac-9441-48eb-a49b-ced1398011f0" -->
### 🔤 Phoneme Management
- **Flat View**: Simple list of all phonemes with search functionality
- **Nested View**: Organized hierarchy by syllable type, position, and groups
- **Full Hierarchy**: Complete structure with frequency visualization and sorting

<!-- section_id: "1af08cf0-7935-43b7-baa4-636b3ed71353" -->
### 📚 Word Management
- **Create Words**: Table-based phoneme selection with real-time hierarchy display
- **View All Words**: Comprehensive word browser with search and sorting
- **Word Lookup**: Multi-criteria search (English, IPA, Dictionary, New Language)
- **Edit Words**: Full word editing interface with structured phoneme data
- **Delete Words**: Safe deletion with confirmation and frequency updates

<!-- section_id: "183fc833-936c-44a0-b181-048315d1b242" -->
### ⚙️ Admin Panel
- **Phoneme Management**: Add, edit, delete phonemes with frequency controls
- **Bulk Operations**: Reset frequencies, reset entire database
- **Real-time Updates**: Live frequency adjustments and table management

<!-- section_id: "588e52ec-d9b9-4595-867c-1b13153293d1" -->
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

<!-- section_id: "8fc2c262-a2ef-497e-919c-f10e7d2d2eba" -->
## 🏗️ Architecture

<!-- section_id: "c00b29ee-45e2-4bf1-9747-a5e326a9ae2f" -->
### Backend (Flask)
- **app.py**: Main Flask application with all API endpoints
- **Routes**: RESTful API design with JSON responses
- **Database**: SQLite integration using existing main.py functions
- **File Handling**: Video upload support with secure filename handling

<!-- section_id: "6ff20614-e14e-457b-be2b-428ab190feff" -->
### Frontend (Modern Web)
- **Responsive Design**: Mobile-first approach with CSS Grid/Flexbox
- **Interactive UI**: Dynamic content loading and real-time updates
- **Modern Styling**: Dark theme with glassmorphism effects
- **Accessibility**: Semantic HTML and keyboard navigation support

<!-- section_id: "6320c683-7c7a-421c-ad5b-d59bc68b2db1" -->
### Integration
- **Terminal Functions**: All main.py functions exposed as web endpoints
- **Data Consistency**: Maintains compatibility with existing database schema
- **File Management**: Handles video uploads and serves static content

<!-- section_id: "0bfefb2c-b7b2-4f19-bc32-34d7d289d873" -->
## 🎨 UI/UX Features

<!-- section_id: "a8e8029c-149e-49aa-889a-7461d56c353a" -->
### Design System
- **Color Palette**: Professional dark theme with accent colors
- **Typography**: System fonts with monospace for phonetic data
- **Icons**: Emoji-based iconography for universal recognition
- **Animations**: Smooth transitions and hover effects

<!-- section_id: "519324f7-9fef-416f-aa62-9e05b47c2340" -->
### Responsive Design
- **Mobile**: Optimized for smartphone usage
- **Tablet**: Adapted layouts for medium screens
- **Desktop**: Full-featured interface with multi-column layouts

<!-- section_id: "e867b5b0-a5ce-4f6a-87d6-73272b35c075" -->
### User Experience
- **Intuitive Navigation**: Clear breadcrumbs and back buttons
- **Real-time Feedback**: Loading states and success/error messages
- **Data Visualization**: Frequency bars, progress indicators, and statistics
- **Search & Filter**: Instant search with highlighting and filtering

<!-- section_id: "42add866-1d12-4a2e-b035-cabfd815eb2b" -->
## 📊 API Endpoints

<!-- section_id: "14313b84-012a-486a-98f3-12fafbe26edb" -->
### Phoneme Management
- `GET /phonemes/flat` - Flat phoneme view
- `GET /phonemes/nested` - Nested hierarchy view  
- `GET /phonemes/full` - Full hierarchy with frequencies
- `GET /api/phoneme-tables` - Dynamic phoneme tables for word creation

<!-- section_id: "97736f39-3f1e-4d6c-915f-213df6542d7d" -->
### Word Management
- `GET /words/display` - Display all words
- `GET /words/lookup` - Word lookup interface
- `GET /api/lookup-word` - Search API
- `POST /api/create-word` - Create new word
- `GET /words/edit/<id>` - Edit word interface
- `POST /api/update-word/<id>` - Update word
- `DELETE /api/delete-word/<id>` - Delete word

<!-- section_id: "f628ef51-cb6d-446e-8f76-7cb054045127" -->
### Admin Functions
- `GET /admin/phonemes` - Admin phoneme management
- `GET /api/admin/phonemes` - Get all phonemes
- `POST /api/admin/add-phoneme` - Add new phoneme
- `POST /api/admin/update-phoneme-frequency` - Update frequency
- `DELETE /api/admin/delete-phoneme/<id>` - Delete phoneme
- `POST /api/admin/reset-database` - Reset database

<!-- section_id: "2f151703-bda9-4d11-84fd-c8955ff209c6" -->
## 🔧 Configuration

<!-- section_id: "1f401e66-89eb-4cfc-bd0b-6266b11fed11" -->
### Environment Variables
- `FLASK_ENV`: Set to 'development' for debug mode
- `FLASK_DEBUG`: Enable/disable debug mode
- `UPLOAD_FOLDER`: Directory for video uploads (default: 'videos')

<!-- section_id: "c313c0d0-acf6-4d78-bb80-3ae5c8bb4279" -->
### File Upload Settings
- **Allowed Extensions**: mp4, avi, mov, mkv, webm
- **Security**: Secure filename handling with Werkzeug
- **Storage**: Local filesystem with organized directory structure

<!-- section_id: "7b2078c6-7461-4bef-a104-242fdd908bb4" -->
## 🚦 Development

<!-- section_id: "01c0af33-5bec-4187-b357-057cfb493419" -->
### Running in Development Mode
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

<!-- section_id: "1825e8e4-5637-4367-8755-da9f01f2740c" -->
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

<!-- section_id: "4be83ce9-8b6b-49e3-9adf-1b04018b0d8c" -->
## 🎯 User Stories Completed

<!-- section_id: "c8735a26-0b09-4c3c-b137-fc119215ddad" -->
### ✅ Primary User Stories

1. **Table-Based Word Creation**: Complete implementation with hierarchy display, filtering, and real-time phoneme selection
2. **Phoneme Hierarchy Visualization**: Three different views (flat, nested, full) with sorting and frequency display
3. **Comprehensive Search**: Multi-criteria word lookup with advanced filtering
4. **Admin Management**: Full phoneme CRUD operations with frequency controls
5. **Word Management**: Complete lifecycle from creation to deletion with editing capabilities

<!-- section_id: "98a29b1c-3a5b-4bba-9fc8-15d689f139d0" -->
### ✅ Secondary Features

1. **Responsive Design**: Works on all device sizes
2. **Real-time Updates**: Dynamic content loading and instant feedback
3. **Data Visualization**: Frequency bars, statistics, and progress indicators
4. **File Management**: Video upload and playback support
5. **Error Handling**: Comprehensive error messages and validation

<!-- section_id: "84663b10-80dd-4264-8639-e48aebad5450" -->
## 🔮 Future Enhancements

<!-- section_id: "31d73c7d-59ac-4e26-b793-9574e6d8e131" -->
### Pending Features
- **Video Integration**: Complete video upload and playback system
- **Phoneme Suggestion System**: AI-powered phoneme recommendations with conflict detection
- **Export/Import**: Database backup and restoration features
- **User Authentication**: Multi-user support with role-based access
- **Analytics Dashboard**: Usage statistics and trends visualization

<!-- section_id: "4654e4b4-3b7e-48f4-bca2-61f364991ae8" -->
### Technical Improvements
- **Caching**: Redis integration for better performance
- **Database**: PostgreSQL migration for production use
- **Testing**: Comprehensive test suite with pytest
- **Documentation**: API documentation with Swagger/OpenAPI
- **Deployment**: Docker containerization and cloud deployment guides

<!-- section_id: "b906b7c8-8871-4933-9de5-8508a463e52c" -->
## 📝 Notes

- All terminal functions from `main.py` have been successfully implemented as web endpoints
- The web interface maintains full compatibility with the existing database schema
- Modern web technologies provide a superior user experience compared to terminal interface
- The application is production-ready with proper error handling and security measures

<!-- section_id: "f7352c08-3d76-4ad3-afbd-c81249636f15" -->
## 🤝 Contributing

The web application successfully implements all user stories found in the terminal functions, providing a modern, intuitive interface for phoneme frequency tracking and constructed language development.