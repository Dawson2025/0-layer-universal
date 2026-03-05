---
resource_id: "eabda29f-69ee-4325-a013-da5039ef049e"
resource_type: "document"
resource_name: "universal_instructions"
---
# Universal Development Instructions - Language Tracker App

<!-- section_id: "29efb027-ab82-4ec2-bf0a-077f016d0707" -->
## Project Overview

This is a **Language Tracker App** - a sophisticated phoneme frequency tracking and constructed language word creation system. It combines a terminal-based CLI interface (`main.py`) with a Flask web application (`app.py`) for managing phonemes, words, and language projects.

<!-- section_id: "973d2449-da60-454c-92fa-1ab0e75888a5" -->
### Core Purpose
- Track phoneme frequencies across different syllable positions (onset, nucleus, coda)
- Create words using structured phoneme selection methods
- Manage multiple language projects with user authentication
- Support both SQLite (local) and Firebase/Firestore (cloud) storage backends
- Enable collaborative language development with user groups and project sharing
- Provide IPA text-to-speech integration and phonotactic validation

<!-- section_id: "3b0be643-6559-4f27-ab3f-0373d86f6429" -->
## Development Environment Setup

<!-- section_id: "e9668d75-4f55-446c-9be7-0822eca5e839" -->
### Prerequisites
- Python 3.9+
- Node.js 16+ (for Firebase functions and AI tools)
- Firebase CLI (for cloud features)
- Azure Speech Services subscription (optional, for TTS features)

<!-- section_id: "522c99f4-e929-4ab0-9861-815a5dcde61a" -->
### Quick Start Commands

```powershell
# Terminal-based interface
python main.py

# Web application (development)
python app.py

# Web application (production-ready with additional features)
python start_webapp.py
```

<!-- section_id: "97525662-ce52-40cd-8bbd-fb8b585b8eba" -->
### Environment Configuration

**Local Development**
```powershell
# Run setup script
./setup-dev-env.ps1

# Start Firebase emulators
npm run emulator:start

# Run Flask application
python app.py
```

**Environment Variables**
```bash
# Azure TTS (optional)
AZURE_SPEECH_KEY_WEST=your_west_key
AZURE_SPEECH_KEY_EAST=your_east_key
AZURE_SPEECH_REGION_WEST=westus
AZURE_SPEECH_REGION_EAST=eastus

# Firebase (auto-configured by scripts)
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
```

<!-- section_id: "640f64e4-5200-4d67-b136-a2d793345810" -->
## Architecture Overview

<!-- section_id: "713bd8d3-1e4f-4557-afb8-3c32df8fe1bd" -->
### Dual Interface System
- **Terminal Interface** (`main.py`): Command-line menu system for direct database operations
- **Web Interface** (`app.py`): Flask web application with user authentication and project management

<!-- section_id: "bc459d8e-0d82-41aa-bd90-ce9ffd10fd65" -->
### Hybrid Storage System
- **Local Storage**: SQLite for offline/development projects
- **Cloud Storage**: Firestore for collaborative projects with real-time sync
- **File Storage**: Firebase Storage with automatic CDN and public URLs
- **Migration Capabilities**: Seamless project migration between storage types

<!-- section_id: "8b82ef42-64ae-4048-bdf3-88528a272559" -->
### Core Components

#### Flask Web Application (app.py)
- Scale: 1,800+ lines handling authentication, project management, and word/phoneme operations
- Authentication: Hybrid system supporting email/password (SQLite) + Firebase Auth
- Project Management: Context-based data isolation with storage type selection
- Real-time Features: Phoneme frequency updates, collaborative project sharing
- File Handling: Video upload with Firebase Storage integration

#### Terminal CLI Interface (main.py)
- Database Operations: Direct SQLite interaction with structured phoneme hierarchy
- Algorithms: Phoneme suggestion generation with conflict detection against English words
- Word Creation: Structured word creation with phonotactic validation
- Batch Processing: Efficient bulk operations for data management

#### Advanced Features

**IPA Text-to-Speech (tts_ipa.py)**
- Azure Integration: Cognitive Services with SSML phoneme support
- Context Generation: Automatic phoneme context for clarity
- Database Validation: Single phoneme detection for appropriate context application
- Regional Redundancy: West US primary, East US fallback configuration

**Phonotactic Analysis (phonotactics.py)**
- Sonority Hierarchy: 6-level sonority scale for natural sound combinations
- Cluster Validation: Forbidden and preferred consonant clusters
- Syllable Scoring: Naturalness scoring system (0-150 points)
- Improvement Suggestions: AI-driven phoneme replacement recommendations

<!-- section_id: "9a8d9747-c6f4-492c-bc87-7436eaa581a2" -->
## Database Architecture

<!-- section_id: "69b24b53-61da-40c5-8079-cdd93fb0a7cb" -->
### Core Tables

**Phonemes Table**
```sql
CREATE TABLE phonemes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    syllable_type TEXT,     -- CVC or CV
    position TEXT,          -- onset, nucleus, coda
    length_type TEXT,       -- single_consonants, cluster2, cluster3, monophthongs, diphthongs
    group_type TEXT,        -- Stops, Fricatives, High, Low, etc.
    subgroup_type TEXT,     -- Optional classification level
    phoneme TEXT,           -- IPA symbol (p, a, aɪ)
    frequency INTEGER DEFAULT 0
);
```

**Words Table**
```sql
CREATE TABLE words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language TEXT,
    english_words TEXT,           -- JSON list of translations
    new_language_word TEXT,
    ipa_phonetics TEXT,
    dictionary_phonetics TEXT,
    syllable_type TEXT,           -- Structured phoneme data
    onset_phoneme TEXT,
    onset_length_type TEXT,
    nucleus_phoneme TEXT,
    nucleus_length_type TEXT,
    coda_phoneme TEXT,
    coda_length_type TEXT
);
```

<!-- section_id: "25437fbb-7f57-4963-be09-117114908268" -->
### Hierarchical Classification System
```
Syllable Type (CVC/CV)
  → Position (onset/nucleus/coda)
    → Length Type (single/cluster/monophthong/diphthong)
      → Group Type (Stops, Fricatives, High, Low)
        → Subgroup Type (optional refinement)
          → Phoneme (IPA symbol)
```

<!-- section_id: "12664f22-d57a-44d3-94a7-54c7d37902f0" -->
## AI Development Tools Integration

<!-- section_id: "36ba161c-b291-417d-a859-7a8d231175a9" -->
### OpenAI Codex CLI Setup

**Installation & Configuration**
```bash
# Run the setup script
./setup_codex.sh

# Load Codex environment
source .codex_alias

# Set up API key interactively
./set_api_key.sh
```

**Usage Examples**
```bash
# Generate code examples
codex generate "function to sort phonemes by frequency"

# Code analysis and suggestions
codex analyze main.py

# Interactive coding assistance
codex interactive
```

<!-- section_id: "14373bfb-9e83-4ca7-8763-bd09a57ba45b" -->
### Claude Code CLI Integration

**Quick Start**
```bash
# Load Claude environment
source .claude_alias

# Start interactive session
claude
```

**Available Commands**
- `claude` - Start interactive mode for conversational coding assistance
- `claude "task"` - Run one-time tasks with specific requests
- `claude commit` - Auto-generate git commit messages

<!-- section_id: "7ac8a3f6-d3bf-46be-9ba4-68da42e292ac" -->
## Specification-Driven Development with GitHub Spec Kit

<!-- section_id: "adb6282e-58b5-47c4-b513-10bcf851081a" -->
### Integration Overview

The Language Tracker project leverages GitHub's Spec Kit for implementing Specification-Driven Development (SDD) - a methodology that inverts the traditional development workflow by making specifications executable and the primary source of truth.

<!-- section_id: "74d0cfcb-6add-4e09-8bfc-27a20498684f" -->
### What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional software development. Instead of code being king with specifications as scaffolding, SDD makes **specifications executable** - directly generating working implementations rather than just guiding them.

**Key Paradigm Shift:**
- **Traditional**: Specifications serve code (disposable scaffolding)
- **SDD**: Code serves specifications (specifications generate implementation)
- **Result**: Eliminates the gap between intent and implementation

<!-- section_id: "38bba202-57b5-45b2-903a-248a25c7de8d" -->
### Spec Kit Installation & Setup

**Install Specify CLI:**
```bash
# Persistent installation (recommended)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# One-time usage
uvx --from git+https://github.com/github/spec-kit.git specify init lang-trak-enhanced
```

**Initialize Project with Spec Kit:**
```bash
# Initialize with Claude Code support
specify init lang-trak-features --ai claude --here

# Or initialize with GitHub Copilot
specify init lang-trak-features --ai copilot --here

# Check for required tools
specify check
```

<!-- section_id: "171676b1-2236-47fd-8b20-f28104bf0ee2" -->
### Core Spec Kit Workflow for Language Tracker

**1. Establish Project Constitution**
```bash
/speckit.constitution Create principles for linguistics-focused development: code quality for phoneme accuracy, testing standards for IPA validation, user experience consistency across terminal and web interfaces, and performance requirements for real-time frequency calculations
```

**2. Feature Specification Creation**
```bash
# Example: Enhanced phoneme filtering system
/speckit.specify Advanced phoneme filtering system with real-time search, hierarchical organization, and frequency-based sorting for constructed language development

# Example: Multi-language project management
/speckit.specify Multi-language project management system allowing users to create separate language projects with independent phoneme inventories and word collections
```

**3. Technical Implementation Planning**
```bash
/speckit.plan The application uses Flask backend with SQLite local storage and Firebase cloud storage options. Frontend uses vanilla HTML, CSS, and JavaScript with progressive enhancement. Phoneme data structures use hierarchical classification with frequency tracking. Audio generation integrates Azure Cognitive Services with IPA-to-speech conversion.
```

**4. Task Breakdown & Implementation**
```bash
/speckit.tasks
/speckit.implement
```

<!-- section_id: "49a6c652-60a6-4411-8942-56ec72d7ee9a" -->
### Language Tracker Specific Templates

#### Feature Specification Template for Phoneme Features

```markdown
# Feature Specification: [PHONEME FEATURE NAME]

**Feature Branch**: `[###-feature-name]`
**Created**: [DATE]
**Status**: Draft
**Domain**: Constructed Language Development / Phoneme Management

## User Scenarios & Testing

### User Story 1 - [Phoneme Management Task] (Priority: P1)

As a constructed language developer, I need to [specific phoneme-related task] so that I can [linguistic outcome].

**Why this priority**: Critical for basic phoneme inventory management

**Acceptance Scenarios**:
1. **Given** phoneme inventory with [initial state], **When** user performs [phoneme action], **Then** system provides [expected phonetic outcome]
2. **Given** frequency data exists, **When** user creates new word, **Then** frequencies update automatically

## Requirements

### Functional Requirements
- **FR-001**: System MUST maintain IPA phoneme accuracy across all operations
- **FR-002**: System MUST update phoneme frequencies in real-time during word creation
- **FR-003**: System MUST support hierarchical phoneme classification (syllable_type → position → length_type → group_type)
- **FR-004**: System MUST preserve phonotactic rules and validate sound combinations
- **FR-005**: System MUST support both terminal and web interfaces with feature parity

### Key Entities
- **Phoneme**: IPA symbol with classification hierarchy and frequency tracking
- **Word**: Constructed language word with phonetic transcription and metadata
- **Project**: Language-specific collection of phonemes and words
- **User**: Language creator with authentication and project permissions

## Success Criteria

### Measurable Outcomes
- **SC-001**: Users can create phoneme inventories with 100% IPA accuracy
- **SC-002**: Frequency calculations update in under 100ms for real-time feedback
- **SC-003**: 95% of linguistic tasks complete successfully on first attempt
- **SC-004**: Terminal and web interfaces maintain 100% feature parity
```

<!-- section_id: "6b55dd53-290f-48cf-8155-20b0a54ae555" -->
### Enhanced Development Process

**Traditional Language Tracker Development:**
1. Code feature directly in main.py or app.py
2. Test manually through terminal/web interface
3. Debug issues and iterate
4. Update documentation after completion

**Spec-Driven Language Tracker Development:**
1. `/speckit.constitution` - Establish linguistic accuracy principles
2. `/speckit.specify` - Define phoneme/word feature requirements
3. `/speckit.plan` - Create technical implementation with Flask/SQLite/Firebase
4. `/speckit.tasks` - Generate parallelizable development tasks
5. `/speckit.implement` - Execute implementation with AI assistance
6. Validate against specification before merging

<!-- section_id: "607fbb14-0d5a-4e58-997f-24f939a1ea93" -->
## Development Workflow & Best Practices

<!-- section_id: "d4fc5a10-9c5f-462b-b6a2-e355384dd6f8" -->
### Letter-Based Filtering System
- **Position Mapping**: `a=onset`, `b=nucleus`, `c=coda`
- **Length Type Mapping**: `a=single phonemes`, `b=cluster/diphthong types`, `c=complex clusters`, `d=all types`
- **Command Examples**: `aa`=onset single consonants, `bb`=nucleus diphthongs, `cc`=coda cluster3

<!-- section_id: "76b824e2-af33-4e1e-b5a0-0cc190abaa52" -->
### Frequency Optimization
- **Ascending Sort**: Least frequent phonemes appear first to encourage balanced usage
- **Real-time Updates**: Automatic frequency recalculation during word operations
- **Group Aggregation**: Hierarchical frequency summation across classification levels

<!-- section_id: "faebc7e4-a3dc-4fd9-aad2-82f40bf80ecb" -->
### Testing & Quality Assurance

**Test Suite Coverage**
```bash
# Core functionality tests
python3 test_app.py | cat                    # Basic application flows
python3 test_admin.py | cat                  # Admin features and security
python3 test_menu.py | cat                   # Menu structure and navigation

# Advanced feature tests
python3 test_phoneme_management.py | cat     # Phoneme CRUD operations
python3 test_enhanced_phonemes.py | cat      # Enhanced phoneme features
python3 comprehensive_test.py | cat          # End-to-end workflow validation
```

<!-- section_id: "9f325e30-df4c-4368-941f-2da7f18c2188" -->
## Security & Administrative Features

<!-- section_id: "4377487a-13ff-4c89-b5d2-d8f3195abe17" -->
### Access Control
- **Password Protection**: Admin functions secured with `20251010` password
- **Firebase Rules**: Document-level security with user isolation
- **Input Validation**: Comprehensive sanitization across all inputs
- **Session Security**: Secure Flask sessions with CSRF protection

<!-- section_id: "e102af7d-4190-4139-9a60-77384a960220" -->
### Database Management
- **Automatic Migration**: `migrate_schema()` handles table creation and updates
- **Reset Safety**: Multi-step confirmation with `DELETE EVERYTHING` requirement
- **Backup Strategy**: Regular exports and Firebase automatic backups

<!-- section_id: "8fae7466-b0fd-4ce8-a785-2bba6bbbe592" -->
## Performance Optimizations

<!-- section_id: "1e3f5b9a-59e7-4e53-a946-f7848c4025a6" -->
### Query Optimization
- **Indexed Queries**: Optimized Firestore queries with pagination support
- **Lazy Loading**: On-demand phoneme template initialization
- **Caching Strategy**: Session-based project context caching
- **Batch Operations**: Bulk word creation with frequency updates

<!-- section_id: "c1e8eea9-ecaa-4642-b6a3-fcab054c335e" -->
### Storage Efficiency
- **Hybrid Storage**: Automatic routing between SQLite and Firestore
- **CDN Integration**: Firebase Storage automatic global distribution
- **Migration Pipeline**: Seamless local-to-cloud project migration

<!-- section_id: "2362dda9-11fd-4215-ae6e-a17360023bc2" -->
## API Design & Integration

<!-- section_id: "54ba3c73-f427-447d-8fd5-3f5195cefaf9" -->
### RESTful API Endpoints
```python
# Phoneme Display Endpoints
GET    /phonemes/flat           # Flat phoneme listing
GET    /phonemes/nested         # Hierarchical navigation
GET    /phonemes/full           # Complete frequency visualization

# Word Management Endpoints
GET    /words/display           # Vocabulary browser
POST   /api/create-word         # Table-based word creation
PUT    /api/update-word/<id>    # Word editing interface

# Administrative Endpoints
GET    /admin/phonemes          # Admin control panel
POST   /api/admin/add-phoneme   # Phoneme creation
PUT    /api/admin/frequency     # Frequency management
```

<!-- section_id: "db03165a-16d5-4e20-bb94-34865165597e" -->
### External Integrations
- **Azure Cognitive Services**: IPA pronunciation with SSML support
- **Firebase Services**: Full Firebase ecosystem integration
- **SQLite**: High-performance local storage with full-text search

<!-- section_id: "0b15e220-d9ed-4535-9ea5-8607aaebfc61" -->
## Implementation Statistics & Metrics

<!-- section_id: "45a30f6c-b4ea-41b2-8a2f-727b9fc4fa37" -->
### Code Metrics
- **Total Web Application Code**: 3,000+ lines
- **Flask Backend**: 500+ lines (app.py)
- **Template System**: 2,500+ lines across 8 HTML templates
- **Terminal Compatibility**: 100% maintained with existing main.py (3,700+ lines)

<!-- section_id: "6b8aed42-e793-45ce-a404-7b17dcd5eea8" -->
### Feature Coverage
| Category | Terminal Functions | Web Endpoints | Templates | Status |
|----------|-------------------|---------------|-----------|--------|
| Phoneme Display | 3 | 6 | 3 | ✅ 100% Complete |
| Word Management | 6 | 12 | 4 | ✅ 100% Complete |
| Admin Functions | 5 | 8 | 1 | ✅ 100% Complete |
| **Totals** | **14** | **26** | **8** | **✅ 100% Complete** |

<!-- section_id: "778ab953-795b-4b01-a71d-4310cfe54853" -->
## Future Enhancement Roadmap

<!-- section_id: "ea487145-8a2e-46a1-aa84-464d4e2499bb" -->
### Immediate Opportunities
- **Advanced Analytics**: Usage statistics and trend visualization
- **Export/Import**: Database backup and restoration features
- **Multi-user Support**: Enhanced collaboration with real-time editing
- **API Documentation**: Swagger/OpenAPI integration for third-party developers

<!-- section_id: "869ca78c-ebef-41a3-bd12-804a325883a8" -->
### Long-term Enhancements
- **Performance Optimization**: Redis caching and advanced database indexing
- **Mobile Applications**: React Native or Progressive Web App implementation
- **Machine Learning**: AI-powered phoneme pattern recognition and suggestions
- **Collaboration Features**: Real-time collaborative editing and sharing

<!-- section_id: "c02b1dc5-39e1-4897-970a-56cf7d9f5e3c" -->
## Troubleshooting & Support

<!-- section_id: "f1dbf34f-60c4-4cbb-8afc-96fcd99229c9" -->
### Common Issues & Solutions

1. **Firebase Connection Issues**
   - Verify service account credentials in `config/firebase/`
   - Check environment variable configuration
   - Validate Firebase project permissions

2. **Storage Migration Failures**
   - Ensure user has write permissions for target storage
   - Validate data format consistency between SQLite and Firestore
   - Check Firebase quotas and limits

3. **Audio Generation Problems**
   - Verify Azure Speech API credentials
   - Check regional API availability (West US primary, East US fallback)
   - Validate IPA phoneme format compliance

<!-- section_id: "7ac0d15a-7299-463e-bbb5-6817d103ae63" -->
### Debug Configuration
```python
# Enable comprehensive debugging
app.debug = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Firebase debugging
os.environ['GOOGLE_CLOUD_LOG_LEVEL'] = 'DEBUG'

# Database query debugging
SQLITE_DEBUG = True
```

<!-- section_id: "cd92dafe-71c2-48ba-8e54-544f5b168349" -->
## Development Principles

<!-- section_id: "b3136485-32bc-41ec-917a-218dafb41144" -->
### Linguistic Accuracy
- All phoneme operations must preserve IPA standards
- Frequency calculations must be mathematically accurate
- Phonotactic rules must reflect natural language patterns
- Audio generation must maintain phonetic precision

<!-- section_id: "223a47ac-b484-4edf-b84e-87b1361b3ff5" -->
### Code Quality
- Maintain backward compatibility with existing terminal interface
- Follow Flask best practices for web development
- Implement comprehensive error handling and validation
- Document all linguistic concepts and technical decisions

<!-- section_id: "950b085e-468a-4af4-9f8b-7cb145295fa7" -->
### User Experience
- Ensure feature parity between terminal and web interfaces
- Provide clear feedback for all user actions
- Maintain responsive design across all device types
- Support both novice and expert constructed language developers

<!-- section_id: "1bfa7af5-322c-463c-9876-d715af4bafa8" -->
### Performance Standards
- Database queries must complete in under 100ms for real-time operations
- Phoneme frequency updates must be instantaneous during word creation
- Web interface must load completely in under 2 seconds
- Support concurrent users without performance degradation

This comprehensive guide provides the foundation for all Language Tracker development, from basic setup through advanced Specification-Driven Development workflows, ensuring consistent, high-quality implementation across all features and integrations.