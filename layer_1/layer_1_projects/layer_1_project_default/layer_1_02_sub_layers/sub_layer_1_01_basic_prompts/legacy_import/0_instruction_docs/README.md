---
resource_id: "f8291653-a3f5-4045-af46-5449da9d4aec"
resource_type: "readme_document"
resource_name: "README"
---
# I-Eat University Food Delivery Platform Documentation

Welcome to the documentation for the I-Eat University Food Delivery Platform.

<!-- section_id: "512677ef-d059-4bd6-8ca6-edf4fbdf17b0" -->
## Table of Contents

<!-- section_id: "bb5637b4-e87a-4313-8ea1-51f153dd78f1" -->
### Core Project Documentation
- **[Environments and Integrations](./ENVIRONMENTS_AND_INTEGRATIONS.md)** - Complete guide to dev, testing, staging, and production environments
- [Quickstart](./QUICK_START.md)
- [Project Constitution](./trickle-down-1-project/constitution.md)
- [Project Instructions](./trickle-down-1-project/project_instructions.md)

<!-- section_id: "b12414cc-541b-4076-8206-b881c9cd4a5b" -->
### Testing
- [Testing Guide (Root)](../../../README_TESTING.md) - Quick start guide
- [Realistic Navigation Testing](./REALISTIC_NAVIGATION_TASKS.md)
- [Realistic vs Direct Navigation](./REALISTIC_vs_DIRECT_NAVIGATION.md)
- [Navigation Testing Guide](./NAVIGATION_TESTING_GUIDE.md)

<!-- section_id: "804c776e-7921-4a72-a28c-5bd9d4215735" -->
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

<!-- section_id: "b3ed408c-6aa5-4a39-9d72-1d68b0fa2925" -->
## About
I-Eat is a university-focused food delivery platform that connects students with food delivery services on campus. The platform features:

- **Student Users**: Order food, earn points from teachers, track deliveries
- **Delivery Drivers**: Accept orders, navigate campus locations, complete deliveries  
- **Points System**: Teachers award points to students for academic performance
- **Campus Integration**: Specialized for university dorms, classrooms, and campus locations

<!-- section_id: "22b2cbad-8a92-4916-9416-3a55f73e7d11" -->
### Technology Stack
- **Frontend**: React 19.1.1 + Vite 7.1.7
- **Backend**: Supabase (Authentication, Database, Real-time)
- **Mobile**: React Native (planned)
- **Deployment**: Vercel/Netlify (web), App Store/Google Play (mobile)

<!-- section_id: "ebbf6e24-ca74-4380-8c4e-1744f98cdb92" -->
### Previewing the Web App
Launch the development server:

```bash
cd website
npm install
npm run dev
```

Then open your browser to http://localhost:5173 (Vite default port).

<!-- section_id: "1f779af6-1730-476f-8718-ac0bad6312e1" -->
## Key Features

<!-- section_id: "ad627ffb-327c-4f9b-939c-6b0e3c7057c6" -->
### For Students
- Browse campus food vendors and menus
- Place food orders with campus-specific delivery locations
- Earn and redeem points from teachers
- Track order status in real-time
- Rate and review food and delivery experience

<!-- section_id: "13910f23-c5ed-440c-b4c6-1dac2c23ca68" -->
### For Delivery Drivers
- Register and verify driver status
- Accept available delivery orders
- Navigate to campus locations (dorms, classrooms, etc.)
- Update delivery status and communicate with students
- Track earnings and delivery history

<!-- section_id: "7ad23ff1-61ec-46ec-a271-a94fe1852cec" -->
### For Teachers/Administrators
- Award points to students for academic performance
- Monitor platform usage and student engagement
- Manage campus location database
- View analytics and reporting

<!-- section_id: "b6489015-014a-4f64-93d8-9ee0367498ca" -->
## Related Summaries
- Authentication implementation: ../AUTHENTICATION_IMPLEMENTATION.md
- Points system management: ../POINTS_SYSTEM_SUMMARY.md
- Delivery tracking flow: ../DELIVERY_TRACKING_SUMMARY.md
- Mobile app development: ../MOBILE_APP_SUMMARY.md
- Campus integration summary: ../CAMPUS_INTEGRATION_SUMMARY.md











