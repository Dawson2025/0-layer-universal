// resource_id: "52b6e1b7-7125-4bc8-a2bf-9f7b5155a145"
// resource_type: "document"
// resource_name: "vite.config"
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
})
