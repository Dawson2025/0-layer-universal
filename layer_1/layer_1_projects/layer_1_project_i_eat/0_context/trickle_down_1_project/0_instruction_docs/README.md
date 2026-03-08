---
resource_id: "843814d6-e170-4951-8c35-aacac4357979"
resource_type: "readme_document"
resource_name: "README"
---
# I-Eat University Food Delivery Platform Documentation

Welcome to the documentation for the I-Eat University Food Delivery Platform.

<!-- section_id: "90b27e03-cb5a-481b-bce9-608cee7fe1dc" -->
## Table of Contents

<!-- section_id: "32033dde-05ce-405e-b8be-30fd781d629d" -->
### Core Project Documentation
- **[Environments and Integrations](./ENVIRONMENTS_AND_INTEGRATIONS.md)** - Complete guide to dev, testing, staging, and production environments
- [Quickstart](./QUICK_START.md)
- [Project Constitution](./trickle-down-1-project/constitution.md)
- [Project Instructions](./trickle-down-1-project/project_instructions.md)

<!-- section_id: "acd82874-fe19-4866-800f-39ed100f3d55" -->
### Testing
- [Testing Guide (Root)](../../../README_TESTING.md) - Quick start guide
- [Realistic Navigation Testing](./REALISTIC_NAVIGATION_TASKS.md)
- [Realistic vs Direct Navigation](./REALISTIC_vs_DIRECT_NAVIGATION.md)
- [Navigation Testing Guide](./NAVIGATION_TESTING_GUIDE.md)

<!-- section_id: "c53bd2d8-5c32-4a6e-b4eb-b70c0cf2b5ad" -->
### Trickle-Down Documentation Structure
- [Level 0: Universal Instructions](./0_context/1_trickle_down/trickle-down-0-universal_instructions/)
- [Level 0.5: Environment Setup](./0_context/0.5_setup/meta-intelligent-orchestration/README.md)
  - [Supabase Orchestration Instance](./0_context/0.5_setup/meta-intelligent-orchestration/instances/supabase/README.md)
- [Level 0.75: Universal Tools](./0_context/0.75_universal_tools/README.md)
  - [Meta-Intelligent Orchestration Framework](./0_context/0.75_universal_tools/meta-intelligent-orchestration/README.md)
  - [Browser Automation Framework](./0_context/0.75_universal_tools/browser-automation/README.md)
  - [Visual Orchestration Framework](./0_context/0.75_universal_tools/visual-orchestration/README.md)
  - [Project Analysis Framework](./0_context/0.75_universal_tools/project-analysis/README.md)
- [Level 1: Project Constitution](./0_context/1_trickle_down/trickle-down-1-project/constitution.md)
- [Level 1.5: Project Tools](./0_context/1_trickle_down/trickle-down-1.5-project-tools/README.md)
  - [Meta-Intelligent Orchestration System](./0_context/1_trickle_down/trickle-down-1.5-project-tools/meta-intelligent-orchestration/README.md)
  - [Authentication Management System](./0_context/1_trickle_down/trickle-down-1.5-project-tools/authentication-management/README.md)
  - [Supabase Instance Tools](./0_context/1_trickle_down/trickle-down-1.5-project-tools/supabase-instance/README.md)
  - [Development Workflow Tools](./0_context/1_trickle_down/trickle-down-1.5-project-tools/development-workflow/README.md)
- [Level 2: Features](./0_context/1_trickle_down/trickle-down-2-features/)
- [Level 3: Components](./0_context/1_trickle_down/trickle-down-3-components/)

<!-- section_id: "4e948005-9557-4a70-a35f-e0c4e1cc3e51" -->
## About
I-Eat is a university-focused food delivery platform that connects students with food delivery services on campus. The platform features:

- **Student Users**: Order food, earn points from teachers, track deliveries
- **Delivery Drivers**: Accept orders, navigate campus locations, complete deliveries  
- **Points System**: Teachers award points to students for academic performance
- **Campus Integration**: Specialized for university dorms, classrooms, and campus locations

<!-- section_id: "dd0138e2-0451-40cc-89b1-4efe941889a6" -->
### Technology Stack
- **Frontend**: React 19.1.1 + Vite 7.1.7
- **Backend**: Supabase (Authentication, Database, Real-time)
- **Mobile**: React Native (planned)
- **Deployment**: Vercel/Netlify (web), App Store/Google Play (mobile)

<!-- section_id: "b1a354a1-d209-4daf-82ca-1c206adeb11d" -->
### Previewing the Web App
Launch the development server:

```bash
cd website
npm install
npm run dev
```

Then open your browser to http://localhost:5173 (Vite default port).

<!-- section_id: "1e76eba4-3d89-40bd-b178-daec38b40f11" -->
## Key Features

<!-- section_id: "ae0ead8a-ef2a-4a15-8551-5849920e9c6d" -->
### For Students
- Browse campus food vendors and menus
- Place food orders with campus-specific delivery locations
- Earn and redeem points from teachers
- Track order status in real-time
- Rate and review food and delivery experience

<!-- section_id: "110df3bb-6cfb-4061-a02b-788361b58b58" -->
### For Delivery Drivers
- Register and verify driver status
- Accept available delivery orders
- Navigate to campus locations (dorms, classrooms, etc.)
- Update delivery status and communicate with students
- Track earnings and delivery history

<!-- section_id: "cd81bcfb-7f50-4c1e-a78d-4e4bcaa28488" -->
### For Teachers/Administrators
- Award points to students for academic performance
- Monitor platform usage and student engagement
- Manage campus location database
- View analytics and reporting

<!-- section_id: "dc8e4640-7d11-44c5-9ff6-a15da67161af" -->
## Related Summaries
- Authentication implementation: ../AUTHENTICATION_IMPLEMENTATION.md
- Points system management: ../POINTS_SYSTEM_SUMMARY.md
- Delivery tracking flow: ../DELIVERY_TRACKING_SUMMARY.md
- Mobile app development: ../MOBILE_APP_SUMMARY.md
- Campus integration summary: ../CAMPUS_INTEGRATION_SUMMARY.md











