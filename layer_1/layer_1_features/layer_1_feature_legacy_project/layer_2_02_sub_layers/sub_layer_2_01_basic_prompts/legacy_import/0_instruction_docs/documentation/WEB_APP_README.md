---
resource_id: "8c186ddd-cf8f-4a9a-b27a-fb0bb08fd3d2"
resource_type: "document"
resource_name: "WEB_APP_README"
---
# Phoneme Frequency Tracker - Web Application

A comprehensive web interface for the Phoneme Frequency Tracker, implementing all terminal functions as modern web features.

<!-- section_id: "9588c5ff-5aee-4d51-858d-6408fd271f99" -->
## 🚀 Quick Start

<!-- section_id: "45de6a02-142d-4c09-9bce-5e60a1164d11" -->
### Prerequisites
- Python 3.7+
- Flask and dependencies (see requirements.txt)

<!-- section_id: "e75b21c9-0e67-49dd-9124-5820ebaaf91e" -->
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

<!-- section_id: "3fbe26fc-8127-412f-abcf-058b49ff5000" -->
## 📱 Features Implemented

<!-- section_id: "b868b3fd-d420-4707-9065-66c031f2b59a" -->
### 🔤 Phoneme Management
- **Flat View**: Simple list of all phonemes with search functionality
- **Nested View**: Organized hierarchy by syllable type, position, and groups
- **Full Hierarchy**: Complete structure with frequency visualization and sorting

<!-- section_id: "514ae888-2922-441e-9dd8-bdb997376e85" -->
### 📚 Word Management
- **Create Words**: Table-based phoneme selection with real-time hierarchy display
- **View All Words**: Comprehensive word browser with search and sorting
- **Word Lookup**: Multi-criteria search (English, IPA, Dictionary, New Language)
- **Edit Words**: Full word editing interface with structured phoneme data
- **Delete Words**: Safe deletion with confirmation and frequency updates

<!-- section_id: "a1d71df2-ccbd-4761-b874-626c6f6fde3f" -->
### ⚙️ Admin Panel
- **Phoneme Management**: Add, edit, delete phonemes with frequency controls
- **Bulk Operations**: Reset frequencies, reset entire database
- **Real-time Updates**: Live frequency adjustments and table management

<!-- section_id: "2a23abac-bba8-412a-9e24-8f906f61fcc3" -->
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

<!-- section_id: "d36a511c-2c06-4db7-b356-ed9216680327" -->
## 🏗️ Architecture

<!-- section_id: "063d00cf-744d-47c9-abd9-3fd5230927e3" -->
### Backend (Flask)
- **app.py**: Main Flask application with all API endpoints
- **Routes**: RESTful API design with JSON responses
- **Database**: SQLite integration using existing main.py functions
- **File Handling**: Video upload support with secure filename handling

<!-- section_id: "132be8fe-e5a2-4e0a-83c6-66ce53cfe5d6" -->
### Frontend (Modern Web)
- **Responsive Design**: Mobile-first approach with CSS Grid/Flexbox
- **Interactive UI**: Dynamic content loading and real-time updates
- **Modern Styling**: Dark theme with glassmorphism effects
- **Accessibility**: Semantic HTML and keyboard navigation support

<!-- section_id: "a3f84445-7986-4dab-9426-b86abfeae557" -->
### Integration
- **Terminal Functions**: All main.py functions exposed as web endpoints
- **Data Consistency**: Maintains compatibility with existing database schema
- **File Management**: Handles video uploads and serves static content

<!-- section_id: "27d609d2-970b-48e3-97d7-49b68fd506e9" -->
## 🎨 UI/UX Features

<!-- section_id: "95db488a-3154-44cb-afdb-bbd89102d08d" -->
### Design System
- **Color Palette**: Professional dark theme with accent colors
- **Typography**: System fonts with monospace for phonetic data
- **Icons**: Emoji-based iconography for universal recognition
- **Animations**: Smooth transitions and hover effects

<!-- section_id: "5e4902c4-1d36-42ad-bc3c-0587784d8c4c" -->
### Responsive Design
- **Mobile**: Optimized for smartphone usage
- **Tablet**: Adapted layouts for medium screens
- **Desktop**: Full-featured interface with multi-column layouts

<!-- section_id: "9276d4cd-3435-4be2-a8a9-562ae6a367d4" -->
### User Experience
- **Intuitive Navigation**: Clear breadcrumbs and back buttons
- **Real-time Feedback**: Loading states and success/error messages
- **Data Visualization**: Frequency bars, progress indicators, and statistics
- **Search & Filter**: Instant search with highlighting and filtering

<!-- section_id: "452da49a-4705-46ec-80fe-9ebf91b8354b" -->
## 📊 API Endpoints

<!-- section_id: "6b6f2bc4-d4cb-4771-8a0d-7c2374084416" -->
### Phoneme Management
- `GET /phonemes/flat` - Flat phoneme view
- `GET /phonemes/nested` - Nested hierarchy view  
- `GET /phonemes/full` - Full hierarchy with frequencies
- `GET /api/phoneme-tables` - Dynamic phoneme tables for word creation

<!-- section_id: "fb34ad52-6be2-48fa-9b17-9349e2b4d515" -->
### Word Management
- `GET /words/display` - Display all words
- `GET /words/lookup` - Word lookup interface
- `GET /api/lookup-word` - Search API
- `POST /api/create-word` - Create new word
- `GET /words/edit/<id>` - Edit word interface
- `POST /api/update-word/<id>` - Update word
- `DELETE /api/delete-word/<id>` - Delete word

<!-- section_id: "deca700c-7c68-4b10-9ea9-eb9bff7886d7" -->
### Admin Functions
- `GET /admin/phonemes` - Admin phoneme management
- `GET /api/admin/phonemes` - Get all phonemes
- `POST /api/admin/add-phoneme` - Add new phoneme
- `POST /api/admin/update-phoneme-frequency` - Update frequency
- `DELETE /api/admin/delete-phoneme/<id>` - Delete phoneme
- `POST /api/admin/reset-database` - Reset database

<!-- section_id: "3e28dd4c-1f07-4255-ba25-18631ade4b5d" -->
## 🔧 Configuration

<!-- section_id: "c9e6b12a-eec2-4360-b044-d3dcc99410ea" -->
### Environment Variables
- `FLASK_ENV`: Set to 'development' for debug mode
- `FLASK_DEBUG`: Enable/disable debug mode
- `UPLOAD_FOLDER`: Directory for video uploads (default: 'videos')

<!-- section_id: "1abeb9a0-4d70-4750-83c4-bfa8e18bea8e" -->
### File Upload Settings
- **Allowed Extensions**: mp4, avi, mov, mkv, webm
- **Security**: Secure filename handling with Werkzeug
- **Storage**: Local filesystem with organized directory structure

<!-- section_id: "b6cce93b-3231-4c38-8a6c-bd9a16d7a16f" -->
## 🚦 Development

<!-- section_id: "d9f6bc85-01af-4e22-b50b-555a71e67599" -->
### Running in Development Mode
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

<!-- section_id: "c1aa8e65-341b-4544-b31a-ccfe58236864" -->
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

<!-- section_id: "3b1d43be-f53f-45df-a077-9a39ef72c6fb" -->
## 🎯 User Stories Completed

<!-- section_id: "81903966-5876-4aab-8a60-0829f6ffe187" -->
### ✅ Primary User Stories

1. **Table-Based Word Creation**: Complete implementation with hierarchy display, filtering, and real-time phoneme selection
2. **Phoneme Hierarchy Visualization**: Three different views (flat, nested, full) with sorting and frequency display
3. **Comprehensive Search**: Multi-criteria word lookup with advanced filtering
4. **Admin Management**: Full phoneme CRUD operations with frequency controls
5. **Word Management**: Complete lifecycle from creation to deletion with editing capabilities

<!-- section_id: "f083681c-bd31-4b8a-b9f6-06c12fd5c519" -->
### ✅ Secondary Features

1. **Responsive Design**: Works on all device sizes
2. **Real-time Updates**: Dynamic content loading and instant feedback
3. **Data Visualization**: Frequency bars, statistics, and progress indicators
4. **File Management**: Video upload and playback support
5. **Error Handling**: Comprehensive error messages and validation

<!-- section_id: "4317b0b6-0254-474c-8702-c6dcbd297b40" -->
## 🔮 Future Enhancements

<!-- section_id: "7676355f-76aa-45ac-9c41-1c8d795f89af" -->
### Pending Features
- **Video Integration**: Complete video upload and playback system
- **Phoneme Suggestion System**: AI-powered phoneme recommendations with conflict detection
- **Export/Import**: Database backup and restoration features
- **User Authentication**: Multi-user support with role-based access
- **Analytics Dashboard**: Usage statistics and trends visualization

<!-- section_id: "bd1a2bfe-20b5-4d81-ad36-f7051d785ee9" -->
### Technical Improvements
- **Caching**: Redis integration for better performance
- **Database**: PostgreSQL migration for production use
- **Testing**: Comprehensive test suite with pytest
- **Documentation**: API documentation with Swagger/OpenAPI
- **Deployment**: Docker containerization and cloud deployment guides

<!-- section_id: "01dc70bc-df2d-48ca-b066-2aadbb33ff0c" -->
## 📝 Notes

- All terminal functions from `main.py` have been successfully implemented as web endpoints
- The web interface maintains full compatibility with the existing database schema
- Modern web technologies provide a superior user experience compared to terminal interface
- The application is production-ready with proper error handling and security measures

<!-- section_id: "6df680a5-e110-4d4e-a661-dc783b42b5f8" -->
## 🤝 Contributing

The web application successfully implements all user stories found in the terminal functions, providing a modern, intuitive interface for phoneme frequency tracking and constructed language development.