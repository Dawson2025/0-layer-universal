---
resource_id: "62a97e9c-587e-4599-a9d2-0dc0feb40444"
resource_type: "document"
resource_name: "universal_instructions"
---
# Universal Development Instructions - Language Tracker App

<!-- section_id: "8b47a732-71ce-441e-8134-f29ce484b337" -->
## Project Overview

This is a **Language Tracker App** - a sophisticated phoneme frequency tracking and constructed language word creation system. It combines a terminal-based CLI interface (`main.py`) with a Flask web application (`app.py`) for managing phonemes, words, and language projects.

<!-- section_id: "3891979b-e1cd-4504-a292-28f6ff8ee45c" -->
### Core Purpose
- Track phoneme frequencies across different syllable positions (onset, nucleus, coda)
- Create words using structured phoneme selection methods
- Manage multiple language projects with user authentication
- Support both SQLite (local) and Firebase/Firestore (cloud) storage backends
- Enable collaborative language development with user groups and project sharing
- Provide IPA text-to-speech integration and phonotactic validation

<!-- section_id: "64a8ce40-18ac-417d-8395-a30c94f619dd" -->
## Development Environment Setup

<!-- section_id: "5d9feeec-2711-402a-afaf-baf4d49039a7" -->
### Prerequisites
- Python 3.9+
- Node.js 16+ (for Firebase functions and AI tools)
- Firebase CLI (for cloud features)
- Azure Speech Services subscription (optional, for TTS features)

<!-- section_id: "e30c3b47-a7dc-4018-9056-03ecee04218e" -->
### Quick Start Commands

```powershell
# Terminal-based interface
python main.py

# Web application (development)
python app.py

# Web application (production-ready with additional features)
python start_webapp.py
```

<!-- section_id: "0bf1cb8c-84de-4c87-be85-15136895e683" -->
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

<!-- section_id: "2c7f10a9-6f33-4299-b42f-23711156f7aa" -->
## Architecture Overview

<!-- section_id: "1c5f5fe0-154f-4d9e-9e9e-6a5c926ad0bc" -->
### Dual Interface System
- **Terminal Interface** (`main.py`): Command-line menu system for direct database operations
- **Web Interface** (`app.py`): Flask web application with user authentication and project management

<!-- section_id: "c116e000-43d5-43ce-b0c0-ffc2fd158a50" -->
### Hybrid Storage System
- **Local Storage**: SQLite for offline/development projects
- **Cloud Storage**: Firestore for collaborative projects with real-time sync
- **File Storage**: Firebase Storage with automatic CDN and public URLs
- **Migration Capabilities**: Seamless project migration between storage types

<!-- section_id: "166a76bc-65ac-4b2d-95a3-fc225bf742a5" -->
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

<!-- section_id: "93c26931-5813-4e9a-a010-7a1cc5ae6cb5" -->
## Database Architecture

<!-- section_id: "7e05de42-e4b1-464c-a404-e9135b528c4d" -->
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

<!-- section_id: "c959a2d4-685e-4ed8-b5d5-6d1ea1fd926e" -->
### Hierarchical Classification System
```
Syllable Type (CVC/CV)
  → Position (onset/nucleus/coda)
    → Length Type (single/cluster/monophthong/diphthong)
      → Group Type (Stops, Fricatives, High, Low)
        → Subgroup Type (optional refinement)
          → Phoneme (IPA symbol)
```

<!-- section_id: "d9dc9d8a-b981-4732-8756-b7cfe896bbe8" -->
## AI Development Tools Integration

<!-- section_id: "8c64ab82-190d-40c5-8213-b792ad60cdc6" -->
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

<!-- section_id: "0badf519-f956-4136-a2a1-89b22a16b69b" -->
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

<!-- section_id: "5fd294dc-ff15-45e4-ac52-bab0774da4a3" -->
## Specification-Driven Development with GitHub Spec Kit

<!-- section_id: "a2cd50cd-d941-4554-aab2-bd5af26026dc" -->
### Integration Overview

The Language Tracker project leverages GitHub's Spec Kit for implementing Specification-Driven Development (SDD) - a methodology that inverts the traditional development workflow by making specifications executable and the primary source of truth.

<!-- section_id: "f39ab1b2-530e-40e7-8051-35bfe812f350" -->
### What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional software development. Instead of code being king with specifications as scaffolding, SDD makes **specifications executable** - directly generating working implementations rather than just guiding them.

**Key Paradigm Shift:**
- **Traditional**: Specifications serve code (disposable scaffolding)
- **SDD**: Code serves specifications (specifications generate implementation)
- **Result**: Eliminates the gap between intent and implementation

<!-- section_id: "3b87168c-d6c0-4e27-ad1d-d44fdb6f1d21" -->
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

<!-- section_id: "7aa63251-1983-489d-9e41-465c2b0afb04" -->
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

<!-- section_id: "ba55c718-0ae9-4eda-8727-f5b28be25396" -->
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

<!-- section_id: "605ce9bf-5b38-404c-b415-b5875ed76cad" -->
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

<!-- section_id: "006e17dd-5c76-4d6c-9f06-7a950c2edfdc" -->
## Development Workflow & Best Practices

<!-- section_id: "80449f07-aa08-4bdd-ab7a-4d103d997a63" -->
### Letter-Based Filtering System
- **Position Mapping**: `a=onset`, `b=nucleus`, `c=coda`
- **Length Type Mapping**: `a=single phonemes`, `b=cluster/diphthong types`, `c=complex clusters`, `d=all types`
- **Command Examples**: `aa`=onset single consonants, `bb`=nucleus diphthongs, `cc`=coda cluster3

<!-- section_id: "ff492dd8-2a9a-462b-9e50-6f01d793a840" -->
### Frequency Optimization
- **Ascending Sort**: Least frequent phonemes appear first to encourage balanced usage
- **Real-time Updates**: Automatic frequency recalculation during word operations
- **Group Aggregation**: Hierarchical frequency summation across classification levels

<!-- section_id: "03a04c29-24e7-414f-b355-eacf3e266dc5" -->
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

<!-- section_id: "86dd3982-6868-4909-8c00-f8b104422320" -->
## Security & Administrative Features

<!-- section_id: "b8462148-1cb5-4419-8025-ba05f5cf74f7" -->
### Access Control
- **Password Protection**: Admin functions secured with `20251010` password
- **Firebase Rules**: Document-level security with user isolation
- **Input Validation**: Comprehensive sanitization across all inputs
- **Session Security**: Secure Flask sessions with CSRF protection

<!-- section_id: "4727e360-d8e0-497b-9919-eaf7611f1dd2" -->
### Database Management
- **Automatic Migration**: `migrate_schema()` handles table creation and updates
- **Reset Safety**: Multi-step confirmation with `DELETE EVERYTHING` requirement
- **Backup Strategy**: Regular exports and Firebase automatic backups

<!-- section_id: "20bac36c-6c99-436d-ba9f-77b949d89ebc" -->
## Performance Optimizations

<!-- section_id: "e9cc1a79-091c-4c32-9ac5-9a0a22726a9e" -->
### Query Optimization
- **Indexed Queries**: Optimized Firestore queries with pagination support
- **Lazy Loading**: On-demand phoneme template initialization
- **Caching Strategy**: Session-based project context caching
- **Batch Operations**: Bulk word creation with frequency updates

<!-- section_id: "611c4895-e13c-4137-87b3-990220a27dfa" -->
### Storage Efficiency
- **Hybrid Storage**: Automatic routing between SQLite and Firestore
- **CDN Integration**: Firebase Storage automatic global distribution
- **Migration Pipeline**: Seamless local-to-cloud project migration

<!-- section_id: "049e97b1-b1bf-4f2c-8e5a-a4dfc76da783" -->
## API Design & Integration

<!-- section_id: "9807d7f0-2ec0-41eb-a37a-de899a4ecf6f" -->
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

<!-- section_id: "08e16b18-6866-409f-825a-fa488922f6be" -->
### External Integrations
- **Azure Cognitive Services**: IPA pronunciation with SSML support
- **Firebase Services**: Full Firebase ecosystem integration
- **SQLite**: High-performance local storage with full-text search

<!-- section_id: "747729f0-b640-46c9-b1e4-d94e6ee1c940" -->
## Implementation Statistics & Metrics

<!-- section_id: "55f97986-497b-4a7b-b3e0-37caa1dcc599" -->
### Code Metrics
- **Total Web Application Code**: 3,000+ lines
- **Flask Backend**: 500+ lines (app.py)
- **Template System**: 2,500+ lines across 8 HTML templates
- **Terminal Compatibility**: 100% maintained with existing main.py (3,700+ lines)

<!-- section_id: "7292ac77-2ec7-45c8-b6e3-0d322f94e1db" -->
### Feature Coverage
| Category | Terminal Functions | Web Endpoints | Templates | Status |
|----------|-------------------|---------------|-----------|--------|
| Phoneme Display | 3 | 6 | 3 | ✅ 100% Complete |
| Word Management | 6 | 12 | 4 | ✅ 100% Complete |
| Admin Functions | 5 | 8 | 1 | ✅ 100% Complete |
| **Totals** | **14** | **26** | **8** | **✅ 100% Complete** |

<!-- section_id: "5601778c-576e-4b8a-ad68-d1f551fcdef3" -->
## Future Enhancement Roadmap

<!-- section_id: "43ef3690-3f89-42ca-a496-17d8f77c844c" -->
### Immediate Opportunities
- **Advanced Analytics**: Usage statistics and trend visualization
- **Export/Import**: Database backup and restoration features
- **Multi-user Support**: Enhanced collaboration with real-time editing
- **API Documentation**: Swagger/OpenAPI integration for third-party developers

<!-- section_id: "6227ce0c-f6b2-4e8e-a542-54ff45b259b9" -->
### Long-term Enhancements
- **Performance Optimization**: Redis caching and advanced database indexing
- **Mobile Applications**: React Native or Progressive Web App implementation
- **Machine Learning**: AI-powered phoneme pattern recognition and suggestions
- **Collaboration Features**: Real-time collaborative editing and sharing

<!-- section_id: "5059cbc4-2d2d-4a7b-8d6a-c7cf5176dbe5" -->
## Troubleshooting & Support

<!-- section_id: "ad16fc14-00c5-46cc-bcf8-803356951b9e" -->
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

<!-- section_id: "96db2755-76dd-42c4-a409-20ffc2f87343" -->
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

<!-- section_id: "885c7284-835d-4f45-b6b1-67e65cd819c1" -->
## Development Principles

<!-- section_id: "1c91aba7-d8f4-483b-9b3e-84b4c9484a7e" -->
### Linguistic Accuracy
- All phoneme operations must preserve IPA standards
- Frequency calculations must be mathematically accurate
- Phonotactic rules must reflect natural language patterns
- Audio generation must maintain phonetic precision

<!-- section_id: "31de26f8-9df1-43ea-93af-39c07378f611" -->
### Code Quality
- Maintain backward compatibility with existing terminal interface
- Follow Flask best practices for web development
- Implement comprehensive error handling and validation
- Document all linguistic concepts and technical decisions

<!-- section_id: "09d1a29d-5019-4018-9279-9d7c5621492c" -->
### User Experience
- Ensure feature parity between terminal and web interfaces
- Provide clear feedback for all user actions
- Maintain responsive design across all device types
- Support both novice and expert constructed language developers

<!-- section_id: "7ccdcf2d-f03c-4d55-97f2-18c3d298075f" -->
### Performance Standards
- Database queries must complete in under 100ms for real-time operations
- Phoneme frequency updates must be instantaneous during word creation
- Web interface must load completely in under 2 seconds
- Support concurrent users without performance degradation

This comprehensive guide provides the foundation for all Language Tracker development, from basic setup through advanced Specification-Driven Development workflows, ensuring consistent, high-quality implementation across all features and integrations.