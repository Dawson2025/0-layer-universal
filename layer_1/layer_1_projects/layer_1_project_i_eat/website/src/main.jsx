// resource_id: "d34a8f27-fafb-4b4e-bb37-c64a126cc55a"
// resource_type: "document"
// resource_name: "main"
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
