---
resource_id: "f71945cc-6b47-4066-891e-aa924afa767d"
resource_type: "document"
resource_name: "ARCHITECTURE"
---
# Architecture Overview

<!-- section_id: "92a20ae7-ee31-4a0c-9ac4-a494c2019bb4" -->
## Tech Stack

<!-- section_id: "53688e4e-2abd-42da-8d3a-275a05c8dbe0" -->
### Core Technologies
- **React**: v19.1.1 - UI library for building component-based interfaces
- **Vite**: v7.1.7 - Build tool and development server with Hot Module Replacement (HMR)
- **JavaScript (ES Modules)**: Modern JavaScript with ES module syntax

<!-- section_id: "b9b8a4e2-3b4f-41af-bba1-692dc15a0d93" -->
### Development Tools
- **ESLint**: v9.36.0 - Code linting and quality enforcement
- **@vitejs/plugin-react**: v5.0.4 - Vite plugin for React support with Fast Refresh

<!-- section_id: "f42ee395-9788-4f4d-b5c9-4ce147cb337d" -->
## Application Architecture

<!-- section_id: "11131178-aae4-42ab-bfd2-aa3dc46aa513" -->
### Project Structure

```
website/
├── public/              # Static assets served directly
│   └── vite.svg        # Vite logo
├── src/                # Application source code
│   ├── main.jsx        # React application entry point
│   ├── App.jsx         # Main application component (authentication form)
│   ├── App.css         # Component-specific styles (BYU-Idaho branding)
│   ├── index.css       # Global styles and resets
│   └── assets/         # Images and static resources
│       └── react.svg   # React logo
├── backend/            # Placeholder directory (empty logic.js)
├── frontend/           # Placeholder directory (empty README.md)
├── index.html          # HTML entry point
├── vite.config.js      # Vite configuration
├── eslint.config.js    # ESLint configuration
└── package.json        # Project dependencies and scripts
```

<!-- section_id: "21e6841a-f93e-46ac-a994-de0d74f9ebc6" -->
### Entry Point Flow

1. **index.html** (line 11) - Loads the application
   - Contains a `<div id="root">` mount point
   - Loads `/src/main.jsx` as ES module

2. **src/main.jsx** (lines 6-10) - React initialization
   - Imports React and ReactDOM
   - Creates root render point
   - Renders `<App />` component in StrictMode

3. **src/App.jsx** - Main application component
   - Authentication form (login/signup toggle)
   - Form state management with React hooks

<!-- section_id: "48b9ec90-e0c0-4ed8-b189-e073cd9fde14" -->
## Build System

<!-- section_id: "b2afb3a3-f7da-45c6-8654-3a4dff629b3d" -->
### Vite Configuration

**File**: `vite.config.js`

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})
```

- Minimal configuration with React plugin
- Default settings for:
  - Development server: `http://localhost:5173`
  - Build output: `dist/` directory
  - Hot Module Replacement (HMR)

<!-- section_id: "4fa7564a-95ad-476d-aa46-429870c74008" -->
### Build Process

1. **Development**: `npm run dev`
   - Starts Vite dev server on port 5173
   - Enables HMR for instant updates
   - Source maps for debugging

2. **Production**: `npm run build`
   - Bundles and minifies code
   - Optimizes assets
   - Outputs to `dist/` directory
   - Tree-shaking for smaller bundle size

3. **Preview**: `npm run preview`
   - Serves production build locally
   - Tests production bundle before deployment

<!-- section_id: "810c174e-d117-4849-a353-5c3eed035ae4" -->
## Application State

<!-- section_id: "e0e10e0a-1c8e-4af2-9ed7-40c184916d88" -->
### State Management

Currently uses **local component state** only:

```javascript
// App.jsx lines 5-10
const [isLogin, setIsLogin] = useState(true)
const [formData, setFormData] = useState({
  email: '',
  password: '',
  confirmPassword: ''
})
```

**No external state management libraries** (Redux, Zustand, etc.)

<!-- section_id: "4a70a93b-ffee-4824-ae06-fc7f43a8cde8" -->
## Styling Architecture

<!-- section_id: "3d3559f1-15b0-4f09-985d-d2bfa0f08b4f" -->
### CSS Organization

1. **index.css** - Global styles
   - CSS variables for dark/light themes
   - Base typography and reset styles
   - Default button and link styles
   - Media query for light mode preference

2. **App.css** - Component styles
   - BYU-Idaho brand colors (CSS variables)
   - Authentication card styling
   - Form input and button styles
   - Responsive design (mobile breakpoint at 480px)

<!-- section_id: "f537d1f2-e312-4060-8502-4c37bcf116ae" -->
### BYU-Idaho Brand Colors

```css
--brand-blue: #006EB6
--dark-blue: #214491
--medium-blue: #4F9ACF
--light-blue: #A0D4ED
--gray: #949598
--black: #000000
--white: #FFFFFF
```

<!-- section_id: "c7f8dff6-3111-4e58-aa60-fe7a0b2658c3" -->
## Current Limitations

<!-- section_id: "c4939deb-8d37-4061-b89b-6c1795738418" -->
### No Backend Integration
- `backend/logic.js` is empty
- No API endpoints or server
- Form submissions log to console only (App.jsx:22, 28)

<!-- section_id: "80024f2f-37da-4e69-a734-1464c003a436" -->
### No Routing
- Single page application
- No React Router or navigation system
- No multi-page support

<!-- section_id: "b645b622-3298-403e-bfea-4703d53c0921" -->
### No Data Persistence
- No database integration
- No localStorage usage
- Form data not saved

<!-- section_id: "bd1b7a57-9ebf-4273-9314-7797a08f9cc6" -->
### No Authentication
- Authentication UI only (visual interface)
- No actual login/signup functionality
- No session management
- No token handling

<!-- section_id: "51b39acf-ae23-40a8-9009-fabc29b2ae71" -->
## Future Architecture Considerations

<!-- section_id: "16591558-943e-42bf-9f04-c791237b4815" -->
### Planned Additions

1. **Backend**: Express.js or similar Node server
2. **Database**: MongoDB, PostgreSQL, or Firebase
3. **Routing**: React Router for multi-page navigation
4. **State Management**: Context API or Redux for global state
5. **Authentication**: JWT tokens or OAuth integration
6. **API Layer**: Axios or fetch-based API service

<!-- section_id: "e23c126a-ca0f-4798-8b09-39b5edc8a9a8" -->
### Scalability Notes

The current architecture is suitable for:
- Small single-page applications
- Prototypes and proof-of-concepts
- Static landing pages

For production applications, consider:
- Adding a proper backend API
- Implementing authentication and authorization
- Using a state management solution
- Setting up proper error handling
- Adding loading states and user feedback
- Implementing form validation beyond basic HTML5