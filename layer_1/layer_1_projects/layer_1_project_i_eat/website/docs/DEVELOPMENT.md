---
resource_id: "ac9eb9f4-2b7c-4d6a-9738-cbe76c8c98d5"
resource_type: "document"
resource_name: "DEVELOPMENT"
---
# Development Guide

<!-- section_id: "145a0834-05fa-419d-ae5c-798da7dfaf53" -->
## Prerequisites

- **Node.js**: v16.0.0 or higher
- **npm**: v7.0.0 or higher (comes with Node.js)
- **Git**: For version control

<!-- section_id: "84c5cd51-15e2-477f-9784-34784a18356f" -->
## Initial Setup

<!-- section_id: "59ab69f8-87f1-4614-b117-976b5c41452d" -->
### 1. Clone the Repository

```bash
git clone <repository-url>
cd I-eat-repo/website
```

<!-- section_id: "7add3abc-20b4-4979-a83b-f2e0a1901020" -->
### 2. Install Dependencies

```bash
npm install
```

This installs all dependencies from `package.json`:

**Production Dependencies:**
- `react@^19.1.1`
- `react-dom@^19.1.1`

**Development Dependencies:**
- `vite@^7.1.7`
- `@vitejs/plugin-react@^5.0.4`
- `eslint@^9.36.0` and related plugins
- TypeScript type definitions

<!-- section_id: "edcb58fa-5fd4-49c7-9596-ce40c0405150" -->
## Development Workflow

<!-- section_id: "eb4b3224-0459-4c11-8cab-43014687b948" -->
### Starting the Development Server

```bash
npm run dev
```

**What happens:**
1. Vite dev server starts on `http://localhost:5173`
2. Opens automatically in your default browser
3. Watches for file changes
4. Provides Hot Module Replacement (HMR)

**Output:**
```
  VITE v7.1.7  ready in XXX ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

<!-- section_id: "baf98097-bfc7-4f1d-9670-87686bd40f8d" -->
### Hot Module Replacement (HMR)

When you save changes to files:

- **JavaScript/JSX**: Component state is preserved, only changed code updates
- **CSS**: Styles update instantly without page reload
- **React Components**: Fast Refresh maintains component state

<!-- section_id: "e88b3021-7951-4ce3-9125-8afe9ae3809d" -->
### File Watching

Vite watches these files:
- `src/**/*.jsx`
- `src/**/*.css`
- `index.html`
- `vite.config.js`

Changes trigger automatic rebuilds.

<!-- section_id: "c81a3ca8-c0d8-48bf-8a82-c21941be4c3b" -->
## Code Quality

<!-- section_id: "0edb6dbe-5c8e-441b-b852-bc7d3b780924" -->
### Running the Linter

```bash
npm run lint
```

**What it does:**
- Checks all `.js` and `.jsx` files
- Enforces ESLint rules from `eslint.config.js`
- Reports warnings and errors

**Common ESLint Rules:**
- React Hooks rules (hooks must follow rules of hooks)
- React Refresh rules (components must be properly exported)
- JavaScript best practices

<!-- section_id: "36ff10c2-51b6-488f-b0c2-fdde2b071340" -->
### Fixing Lint Errors

Most errors can be auto-fixed:

```bash
npm run lint -- --fix
```

<!-- section_id: "3229e4a0-e252-465a-b792-cc5ca2245307" -->
## Building for Production

<!-- section_id: "7a514443-fce3-4a1f-8590-0bed72be4756" -->
### Create Production Build

```bash
npm run build
```

**Build Process:**
1. Bundles all JavaScript/JSX files
2. Minifies code
3. Optimizes assets
4. Generates source maps
5. Outputs to `dist/` directory

**Output Structure:**
```
dist/
├── index.html          # HTML entry point
├── assets/
│   ├── index-[hash].js   # Bundled JavaScript
│   └── index-[hash].css  # Bundled CSS
└── vite.svg            # Static assets
```

**Build Optimizations:**
- Tree-shaking (removes unused code)
- Code splitting (separates vendor and app code)
- Asset optimization (images, fonts)
- CSS minification
- JavaScript minification

<!-- section_id: "3a20768d-e3bc-4386-9d22-96f959f06384" -->
### Preview Production Build

```bash
npm run preview
```

**What happens:**
1. Serves the `dist/` folder
2. Runs on `http://localhost:4173` (default)
3. Simulates production environment

**Use this to:**
- Test production build locally
- Verify optimizations work correctly
- Check for production-only issues

<!-- section_id: "8bd0e9b3-409b-47bb-b498-060971f269f6" -->
## Project Structure

<!-- section_id: "271b90fa-a3ac-475b-befa-593a47330449" -->
### Source Code Organization

```
src/
├── main.jsx        # Application entry point
├── App.jsx         # Main component
├── App.css         # Component styles
├── index.css       # Global styles
└── assets/         # Static assets (images, fonts, etc.)
```

<!-- section_id: "15d84e3a-ff8c-4a00-b03a-d70c2dbb1b10" -->
### Configuration Files

```
website/
├── vite.config.js      # Vite build configuration
├── eslint.config.js    # ESLint rules
├── package.json        # Dependencies and scripts
└── index.html          # HTML template
```

<!-- section_id: "cfdde423-4d42-4e73-aafc-576d708176da" -->
## Working with Components

<!-- section_id: "41d06bc9-ef27-41a5-b7ae-b997fde377e4" -->
### Creating a New Component

1. Create file in `src/components/` (create directory if needed):

```bash
mkdir -p src/components
touch src/components/MyComponent.jsx
```

2. Write the component:

```javascript
import { useState } from 'react'
import './MyComponent.css'

function MyComponent() {
  return (
    <div>
      <h2>My Component</h2>
    </div>
  )
}

export default MyComponent
```

3. Import in `App.jsx`:

```javascript
import MyComponent from './components/MyComponent'
```

<!-- section_id: "51e4f694-1b0e-4524-98b7-70b346c45fd8" -->
### Component Best Practices

1. **One component per file**
2. **Use functional components** with hooks
3. **Export as default** for single component files
4. **Name files** same as component (PascalCase)
5. **Keep components small** (under 200 lines)

<!-- section_id: "fceead32-565a-402a-9cbe-9f90e21d5a26" -->
## Styling

<!-- section_id: "1432198a-ee9d-4cf4-a850-10a78da57a41" -->
### CSS Organization

1. **Global Styles**: `index.css`
   - CSS resets
   - Global variables
   - Typography
   - Universal styles

2. **Component Styles**: `App.css`, etc.
   - Component-specific styles
   - Import in component file
   - Use CSS classes, not inline styles

<!-- section_id: "53d2660e-e648-4843-aee5-506a0001cc08" -->
### CSS Naming Convention

Use descriptive class names:

```css
/* Good */
.auth-card { }
.submit-btn { }
.form-group { }

/* Avoid */
.card { }
.btn { }
.group { }
```

<!-- section_id: "6433b2b0-25bf-478e-a2fe-0fb5e4fb06eb" -->
### CSS Variables

Define in `:root` for reusability:

```css
:root {
  --brand-blue: #006EB6;
  --spacing-md: 1rem;
}

.button {
  background: var(--brand-blue);
  padding: var(--spacing-md);
}
```

<!-- section_id: "54219ca8-807d-4f14-a206-2e4ff57aaa3c" -->
## State Management

<!-- section_id: "05abc4ad-fdff-45c6-8d5b-99a222ff127c" -->
### Using useState

```javascript
import { useState } from 'react'

function MyComponent() {
  const [count, setCount] = useState(0)

  const increment = () => {
    setCount(count + 1)
  }

  return <button onClick={increment}>Count: {count}</button>
}
```

<!-- section_id: "f07378ae-1db1-4879-85d6-e3bcd7e8af9d" -->
### Form State Pattern

```javascript
const [formData, setFormData] = useState({
  field1: '',
  field2: ''
})

const handleChange = (e) => {
  setFormData({
    ...formData,
    [e.target.name]: e.target.value
  })
}
```

<!-- section_id: "6153af15-adfa-496e-8c89-67ec2c3b9ce5" -->
## Debugging

<!-- section_id: "b9f8de3a-ac7f-4b6a-b79a-476a91e53617" -->
### Browser DevTools

1. **React DevTools**:
   - Install React DevTools extension
   - Inspect component tree
   - View props and state
   - Profile performance

2. **Console Logs**:
   - Check console for errors
   - Use `console.log()` for debugging
   - View network requests

<!-- section_id: "dc08f884-076c-409e-a3c8-5b8b12526bfb" -->
### Vite DevTools

Open dev server and press:
- `r` - Restart server
- `u` - Show server URL
- `o` - Open in browser
- `c` - Clear console
- `q` - Quit server

<!-- section_id: "60180454-56c6-4c6e-a646-dfb42e0b993d" -->
### Common Issues

#### Port Already in Use

**Error**: `Port 5173 is already in use`

**Solution**:
```bash
# Kill process on port 5173
lsof -ti:5173 | xargs kill -9

# Or use different port
npm run dev -- --port 3000
```

#### Module Not Found

**Error**: `Cannot find module 'xyz'`

**Solution**:
```bash
# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

#### HMR Not Working

**Solution**:
1. Check browser console for errors
2. Restart dev server
3. Clear browser cache
4. Check file permissions

<!-- section_id: "e3efe5db-dba2-4176-ba8b-687f71d8f588" -->
## Git Workflow

<!-- section_id: "2a51eb04-b0df-49b3-a2c2-df2ff3217956" -->
### Current Branch

```bash
git status
# On branch: feature/new-branch
```

<!-- section_id: "c1d94b79-a074-4ce1-9d2a-547b0938631c" -->
### Common Commands

```bash
# Check status
git status

# Stage changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to remote
git push origin feature/new-branch

# Pull latest changes
git pull origin main
```

<!-- section_id: "02f5b992-61fd-4040-9c56-1c9e1083ccf5" -->
### Modified Files (Current)

```
M website/src/App.css
M website/src/App.jsx
?? .claude/
?? .mcp.json
?? 0_context/
?? CLAUDE.md
```

<!-- section_id: "91c3c3fa-c9c3-4c51-bdfe-2d1344ce535c" -->
## Environment Variables

Currently no environment variables are used. To add them:

1. Create `.env` file in `website/` directory:

```bash
VITE_API_URL=http://localhost:3000
VITE_APP_NAME=My App
```

2. Access in code:

```javascript
const apiUrl = import.meta.env.VITE_API_URL
```

**Important:**
- Prefix with `VITE_` to expose to client
- Never commit `.env` to git
- Add `.env` to `.gitignore`

<!-- section_id: "3f7ae717-d36b-487d-96a3-af5385ae1034" -->
## Performance Optimization

<!-- section_id: "34a8c7af-62a1-4312-8db1-c9af57a2d9b6" -->
### Current Optimizations

1. **Vite**: Fast HMR and optimized builds
2. **React 19**: Latest performance improvements
3. **Code Splitting**: Automatic vendor chunk separation

<!-- section_id: "21b497ec-c57f-4f4c-8f97-fa9d20af0f82" -->
### Future Optimizations

1. **Lazy Loading**: Dynamic imports for routes
2. **Image Optimization**: WebP format, lazy loading
3. **Code Splitting**: Route-based splitting
4. **Memoization**: React.memo, useMemo, useCallback

<!-- section_id: "4a709e20-0db9-42e3-a573-235905d92958" -->
## Testing

Currently no tests are configured. To add testing:

<!-- section_id: "7b524c9e-9269-43f8-985c-7d0ad585bc30" -->
### Install Vitest (Recommended for Vite)

```bash
npm install -D vitest @testing-library/react @testing-library/jest-dom
```

<!-- section_id: "0024f4b3-c9bd-4e29-b32c-8e2b0b99ba23" -->
### Configure in `vite.config.js`

```javascript
export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './src/test/setup.js',
  },
})
```

<!-- section_id: "7f6c3e77-a676-426f-afaa-8ae034508c05" -->
### Add Test Script to `package.json`

```json
{
  "scripts": {
    "test": "vitest",
    "test:ui": "vitest --ui"
  }
}
```

<!-- section_id: "6cb7c5f4-e4da-479d-91d2-eee7ae5d24c7" -->
## Deployment

<!-- section_id: "d58e8d99-3833-4668-b3d3-043e78af7d9f" -->
### Build for Deployment

```bash
npm run build
```

<!-- section_id: "3a8da8a5-90ce-4bdc-91b5-66094d8f00db" -->
### Deploy to Vercel (Recommended)

```bash
npm install -g vercel
vercel
```

<!-- section_id: "f026bc2a-16ec-4115-ae8f-7a6063f4a55e" -->
### Deploy to Netlify

```bash
npm install -g netlify-cli
netlify deploy --prod
```

<!-- section_id: "715300f0-c2fe-401c-a9ce-6e39a708c8ef" -->
### Static Server Deployment

After building, serve the `dist/` folder with any static server:

```bash
# Using Python
cd dist
python -m http.server 8000

# Using Node.js
npx serve dist
```

<!-- section_id: "9f91b132-c7ce-4c78-9d07-e3a89f504bd2" -->
## Troubleshooting

<!-- section_id: "1eb92d14-c34f-4a9d-b59b-a2ed8b649dfa" -->
### Clear Vite Cache

```bash
rm -rf node_modules/.vite
npm run dev
```

<!-- section_id: "a203f489-3fcc-4016-8b7f-90f299917b3b" -->
### Reinstall Dependencies

```bash
rm -rf node_modules package-lock.json
npm install
```

<!-- section_id: "17f7b3db-d77f-416e-bd0d-4629e4467cf1" -->
### Check Node Version

```bash
node --version  # Should be v16+
npm --version   # Should be v7+
```

<!-- section_id: "8c5073c8-fe2f-4bff-8324-f836a11d1de8" -->
## Additional Resources

- **Vite Documentation**: https://vite.dev
- **React Documentation**: https://react.dev
- **ESLint Rules**: https://eslint.org/docs/rules/
- **React DevTools**: Browser extension for React debugging