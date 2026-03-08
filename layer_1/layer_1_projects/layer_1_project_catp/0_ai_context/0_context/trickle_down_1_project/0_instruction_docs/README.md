---
resource_id: "21beda8a-a550-4e83-bf80-9c4b34a88e7f"
resource_type: "readme_document"
resource_name: "README"
---
# I-Eat University Food Delivery Platform Documentation

Welcome to the documentation for the I-Eat University Food Delivery Platform.

<!-- section_id: "b0ad02d9-40fd-4740-b1e2-46692a4a6d99" -->
## Table of Contents

<!-- section_id: "0f579d29-bbce-46f2-bb8a-2af207545dc3" -->
### Core Project Documentation
- **[Environments and Integrations](./ENVIRONMENTS_AND_INTEGRATIONS.md)** - Complete guide to dev, testing, staging, and production environments
- [Quickstart](./QUICK_START.md)
- [Project Constitution](./trickle-down-1-project/constitution.md)
- [Project Instructions](./trickle-down-1-project/project_instructions.md)

<!-- section_id: "cb4b6ed9-0b32-425d-823a-d527e6f9ab26" -->
### Testing
- [Testing Guide (Root)](../../../README_TESTING.md) - Quick start guide
- [Realistic Navigation Testing](./REALISTIC_NAVIGATION_TASKS.md)
- [Realistic vs Direct Navigation](./REALISTIC_vs_DIRECT_NAVIGATION.md)
- [Navigation Testing Guide](./NAVIGATION_TESTING_GUIDE.md)

<!-- section_id: "0d9af053-d375-4091-87e5-82d6394564d8" -->
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

<!-- section_id: "cfe66740-717a-44de-8f83-3cf8a7cd962c" -->
## About
I-Eat is a university-focused food delivery platform that connects students with food delivery services on campus. The platform features:

- **Student Users**: Order food, earn points from teachers, track deliveries
- **Delivery Drivers**: Accept orders, navigate campus locations, complete deliveries  
- **Points System**: Teachers award points to students for academic performance
- **Campus Integration**: Specialized for university dorms, classrooms, and campus locations

<!-- section_id: "35cabfde-c5f0-4997-99fa-cf25946cf532" -->
### Technology Stack
- **Frontend**: React 19.1.1 + Vite 7.1.7
- **Backend**: Supabase (Authentication, Database, Real-time)
- **Mobile**: React Native (planned)
- **Deployment**: Vercel/Netlify (web), App Store/Google Play (mobile)

<!-- section_id: "00b0e244-924d-4bc0-a543-f5d7317f7bd9" -->
### Previewing the Web App
Launch the development server:

```bash
cd website
npm install
npm run dev
```

Then open your browser to http://localhost:5173 (Vite default port).

<!-- section_id: "80985031-ff32-4e4b-be97-4b6bbbb294e3" -->
## Key Features

<!-- section_id: "02de956e-e70d-4a50-b024-83fd03930f55" -->
### For Students
- Browse campus food vendors and menus
- Place food orders with campus-specific delivery locations
- Earn and redeem points from teachers
- Track order status in real-time
- Rate and review food and delivery experience

<!-- section_id: "f6594137-77e4-464a-aced-0afc0b62a0f2" -->
### For Delivery Drivers
- Register and verify driver status
- Accept available delivery orders
- Navigate to campus locations (dorms, classrooms, etc.)
- Update delivery status and communicate with students
- Track earnings and delivery history

<!-- section_id: "d6bc49c8-da15-429f-809c-8bad8b76c617" -->
### For Teachers/Administrators
- Award points to students for academic performance
- Monitor platform usage and student engagement
- Manage campus location database
- View analytics and reporting

<!-- section_id: "8843b1a7-fd0e-47bb-922e-31c987f15a56" -->
## Related Summaries
- Authentication implementation: ../AUTHENTICATION_IMPLEMENTATION.md
- Points system management: ../POINTS_SYSTEM_SUMMARY.md
- Delivery tracking flow: ../DELIVERY_TRACKING_SUMMARY.md
- Mobile app development: ../MOBILE_APP_SUMMARY.md
- Campus integration summary: ../CAMPUS_INTEGRATION_SUMMARY.md











