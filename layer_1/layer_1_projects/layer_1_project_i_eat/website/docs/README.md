---
resource_id: "6dafde61-ee84-4f8d-a311-94709845f41d"
resource_type: "readme_document"
resource_name: "README"
---
# Website Documentation

Complete documentation for the React + Vite web application.

<!-- section_id: "fc836205-d4f3-4c71-af6b-b57d108df98e" -->
## Quick Links

- **[Architecture Overview](./ARCHITECTURE.md)** - System design, tech stack, and project structure
- **[Component Documentation](./COMPONENTS.md)** - Detailed component breakdown and API reference
- **[Development Guide](./DEVELOPMENT.md)** - Setup, workflow, and best practices
- **[Code Reference](./CODE_REFERENCE.md)** - File-by-file code walkthrough

<!-- section_id: "99699869-66f8-45bc-ae1a-121156b33a56" -->
## Documentation Overview

<!-- section_id: "9aed8039-d98d-4010-8719-582cd3e6cf21" -->
### ARCHITECTURE.md

Learn about the application's technical foundation:

- **Tech Stack**: React 19.1.1, Vite 7.1.7, ESLint
- **Project Structure**: Directory organization and file purposes
- **Build System**: Vite configuration and build process
- **State Management**: Current approach (local state only)
- **Styling**: CSS organization and BYU-Idaho branding
- **Limitations**: No backend, routing, or data persistence
- **Future Considerations**: Planned additions and scalability

**Key Sections:**
- Entry Point Flow: How the app initializes
- Build Process: Development, production, and preview modes
- Current Limitations: What's not implemented yet
- Future Architecture: Scalability recommendations

<!-- section_id: "d45c0476-c724-46db-8192-8858a8736cca" -->
### COMPONENTS.md

Deep dive into React components:

- **App Component**: Main authentication form component
  - State variables (`isLogin`, `formData`)
  - Event handlers (`handleInputChange`, `handleSubmit`)
  - Conditional rendering logic
  - Form validation
  - UI structure and styling

- **Main Entry (main.jsx)**: React initialization
  - StrictMode configuration
  - Root render setup

**Key Sections:**
- State Variables: What each state controls
- Event Handlers: Function-by-function breakdown
- Conditional Rendering: Dynamic UI logic
- Accessibility Features: WCAG compliance
- Best Practices: Current practices and potential improvements

<!-- section_id: "246bee31-c6b2-4eb9-9bec-d4b9d51c2dab" -->
### DEVELOPMENT.md

Practical guide for developers:

- **Prerequisites**: Node.js, npm, Git requirements
- **Setup**: Initial installation and configuration
- **Workflow**: Development server, HMR, file watching
- **Code Quality**: Linting and formatting
- **Building**: Production builds and optimization
- **Project Structure**: File organization
- **Working with Components**: Creating new components
- **Styling**: CSS conventions and variables
- **State Management**: useState patterns
- **Debugging**: Browser DevTools and common issues
- **Git Workflow**: Version control best practices
- **Testing**: How to add tests (not currently configured)
- **Deployment**: Vercel, Netlify, and static hosting

**Key Sections:**
- Development Server: Starting and using HMR
- Production Build: Creating optimized builds
- Debugging: Common issues and solutions
- Git Workflow: Current branch and modified files

<!-- section_id: "d5c5b99d-e52b-45f7-93aa-0cc3a9410d96" -->
### CODE_REFERENCE.md

Line-by-line code documentation:

- **index.html**: HTML entry point and script loading
- **vite.config.js**: Build configuration
- **package.json**: Dependencies and scripts
- **main.jsx**: React initialization code
- **App.jsx**: Complete component implementation
- **App.css**: BYU-Idaho brand styling
- **index.css**: Global styles and resets
- **Backend & Frontend**: Placeholder directories

**Key Sections:**
- Each File: Purpose, key lines, and explanations
- Code Patterns: Common patterns used throughout
- Dependencies: What each dependency does

<!-- section_id: "068ed353-9a2e-4f27-a6f2-7ebd690fdd7b" -->
## Quick Start

<!-- section_id: "96ae494f-fc37-4f6a-a9a5-c7d0a8ee0957" -->
### For New Developers

1. Read **ARCHITECTURE.md** to understand the system
2. Follow **DEVELOPMENT.md** setup instructions
3. Reference **COMPONENTS.md** when working with UI
4. Use **CODE_REFERENCE.md** for specific implementation details

<!-- section_id: "e68b4964-4f91-4355-9d79-90d49eb8c070" -->
### For Code Review

1. Check **ARCHITECTURE.md** for design decisions
2. Review **COMPONENTS.md** for component contracts
3. Verify against **DEVELOPMENT.md** best practices
4. Cross-reference **CODE_REFERENCE.md** for implementation

<!-- section_id: "ae024d14-0949-4457-a005-4c6df37b1b2a" -->
### For Debugging

1. Check **DEVELOPMENT.md** "Debugging" section
2. Review **COMPONENTS.md** for component behavior
3. Reference **CODE_REFERENCE.md** for specific code locations
4. Consult **ARCHITECTURE.md** for system limitations

<!-- section_id: "1958e98f-6a68-4762-81f0-834d487c1de5" -->
## Project Status

<!-- section_id: "2d077c37-dcf5-4305-bcb5-df62b0bd608e" -->
### What's Working

- React 19 application with functional components
- Authentication UI (login/signup toggle)
- Form state management
- BYU-Idaho brand styling
- Hot Module Replacement (HMR)
- Production build optimization

<!-- section_id: "761e21d6-dc78-4b97-9051-e362ac850d24" -->
### What's Not Implemented

- Backend API or server
- Actual authentication logic
- Data persistence (database, localStorage)
- Routing or multi-page navigation
- Form validation beyond HTML5
- Error handling and user feedback
- Loading states
- Testing infrastructure

<!-- section_id: "865f76a7-2e15-40fe-bc04-e2b8c0b079be" -->
### Current Branch

```
Branch: feature/new-branch
Main: main
```

<!-- section_id: "fd13ac68-4a3a-4cba-b4e3-373d8e410c33" -->
### Modified Files

```
M  website/src/App.css
M  website/src/App.jsx
?? .claude/
?? .mcp.json
?? 0_context/
?? CLAUDE.md
```

<!-- section_id: "2472b2f0-0417-46a2-a511-427886e3a234" -->
## File Locations

<!-- section_id: "84c8e4e9-50ec-4539-8b52-06fabf3bb11e" -->
### Source Code

```
website/src/
├── main.jsx        # React entry (10 lines)
├── App.jsx         # Main component (103 lines)
├── App.css         # Component styles (141 lines)
└── index.css       # Global styles (69 lines)
```

<!-- section_id: "a64a3d78-cb40-42ea-a029-b9dff90c21b3" -->
### Configuration

```
website/
├── vite.config.js      # Vite config (7 lines)
├── package.json        # Dependencies (27 lines)
├── eslint.config.js    # ESLint rules
└── index.html          # HTML template (14 lines)
```

<!-- section_id: "842472f0-1c16-4b06-b565-53629181ef3f" -->
### Documentation (This Folder)

```
website/docs/
├── README.md           # This file
├── ARCHITECTURE.md     # System design
├── COMPONENTS.md       # Component docs
├── DEVELOPMENT.md      # Dev guide
└── CODE_REFERENCE.md   # Code walkthrough
```

<!-- section_id: "223c55e6-1dbd-4dfa-b0fd-627ebf84499c" -->
## Technologies Used

<!-- section_id: "c3f5cdc0-34f6-42ad-bbf7-fc4b75ccc9f0" -->
### Core
- **React**: v19.1.1 - UI library
- **Vite**: v7.1.7 - Build tool
- **JavaScript**: ES Modules

<!-- section_id: "93731d84-8393-4ab9-9746-f56b91f53c84" -->
### Development
- **ESLint**: v9.36.0 - Code linting
- **@vitejs/plugin-react**: v5.0.4 - React Fast Refresh

<!-- section_id: "eb327c77-f725-455f-bd00-82890c9bf25d" -->
### Future Plans
- **React Router**: For navigation
- **Express/Fastify**: Backend API
- **MongoDB/PostgreSQL**: Database
- **Vitest**: Testing framework
- **TypeScript**: Type safety

<!-- section_id: "bd54c9c2-e1d5-468d-beb3-c4f4e19d6575" -->
## Common Tasks

<!-- section_id: "7381f93e-324b-40bf-97bf-a3515237e029" -->
### Start Development Server
```bash
cd website
npm run dev
# Opens http://localhost:5173
```

<!-- section_id: "9c70ddb5-afe4-47f6-866f-861b9f47fcae" -->
### Build for Production
```bash
npm run build
# Outputs to website/dist/
```

<!-- section_id: "a438bef6-2983-4650-8b16-47d0d790fbe6" -->
### Run Linter
```bash
npm run lint
```

<!-- section_id: "fc9f44c2-13d7-48c1-b06b-05fbb6654b50" -->
### Preview Production Build
```bash
npm run preview
# Opens http://localhost:4173
```

<!-- section_id: "662466c6-8049-4bcb-8ad5-4e7ff2e2cde2" -->
## Key Concepts

<!-- section_id: "5dfe20be-edfc-4805-adcd-7280c799fa0e" -->
### Hot Module Replacement (HMR)

Vite's HMR updates code instantly without full page reload:
- Save a file → See changes immediately
- Component state preserved
- Faster development cycle

<!-- section_id: "a74f89d4-c0c7-4a17-b718-0c7df27ba609" -->
### Component State

React `useState` manages local component data:
```javascript
const [value, setValue] = useState(initialValue)
```

<!-- section_id: "9392f1e0-be49-484c-b6d8-bcda6fd8569d" -->
### Controlled Components

Form inputs tied to React state:
```javascript
<input value={state} onChange={handleChange} />
```

<!-- section_id: "5e4f3b78-8836-4c95-b78c-33cdcdf500d2" -->
### CSS Variables

Reusable design tokens:
```css
:root { --brand-blue: #006EB6; }
.button { background: var(--brand-blue); }
```

<!-- section_id: "df6949f1-9b40-4898-bcf3-3397a5eefe74" -->
## BYU-Idaho Branding

<!-- section_id: "5887038e-5b18-4b5b-9e8f-fe2618792177" -->
### Brand Colors

```css
--brand-blue: #006EB6      /* Primary brand color */
--dark-blue: #214491       /* Darker variant */
--medium-blue: #4F9ACF     /* Medium variant */
--light-blue: #A0D4ED      /* Light variant */
--gray: #949598            /* Text/UI gray */
```

<!-- section_id: "42b29fce-9c6d-4575-853d-4e8188d3ac0d" -->
### Usage

- **Primary Buttons**: `--brand-blue`
- **Headings**: `--dark-blue`
- **Backgrounds**: Gradient from `--light-blue` to `--brand-blue`
- **Secondary Text**: `--gray`

<!-- section_id: "f2ff97b0-a91b-42e1-aeef-d6404521a08a" -->
## Getting Help

<!-- section_id: "a2ac42c2-4638-453d-8acb-d16fb0a992a3" -->
### Documentation Questions

If documentation is unclear:
1. Check the specific doc file for details
2. Review related sections in other docs
3. Search for keywords across all docs
4. Check code examples in CODE_REFERENCE.md

<!-- section_id: "4ae8ea29-a921-4ae2-8404-c0c3bba93ea4" -->
### Code Questions

For implementation questions:
1. Start with COMPONENTS.md for component behavior
2. Check CODE_REFERENCE.md for specific lines
3. Review DEVELOPMENT.md for patterns
4. Consult ARCHITECTURE.md for design decisions

<!-- section_id: "b16bfbce-d529-4cb7-9d66-16723c24563e" -->
### Setup Issues

For environment problems:
1. Check DEVELOPMENT.md prerequisites
2. Review "Common Issues" section
3. Try "Troubleshooting" steps
4. Verify Node.js and npm versions

<!-- section_id: "01c6efaf-00f3-4949-afe3-a3e1b26d5cd2" -->
## Contributing

When adding features:

1. **Update Components**: Modify or create in `src/`
2. **Update Styles**: Add to component CSS or `index.css`
3. **Update Docs**: Keep documentation in sync
   - Add new components to COMPONENTS.md
   - Update ARCHITECTURE.md for design changes
   - Add new patterns to DEVELOPMENT.md
   - Update CODE_REFERENCE.md with new files

<!-- section_id: "c464830f-75a7-494b-87f6-34f38c224cb9" -->
## Maintenance

<!-- section_id: "a57f41fc-54ca-476c-882a-ff2819e42873" -->
### Keeping Docs Updated

When code changes:
- Update line numbers in CODE_REFERENCE.md
- Add new components to COMPONENTS.md
- Document new patterns in DEVELOPMENT.md
- Update architecture diagrams if structure changes

<!-- section_id: "b9269361-6cba-460f-8067-57c958b74ddd" -->
### Documentation Standards

- Use markdown for all docs
- Include code examples
- Reference specific file locations
- Keep line numbers current
- Update quick reference sections

<!-- section_id: "9da74daa-aa2b-4d76-b4e4-69522a92bbee" -->
## License

See repository root for license information.

<!-- section_id: "0e00c279-eac6-4359-867e-75573b5b57fe" -->
## Contact

For project-specific questions, refer to the main repository README.
