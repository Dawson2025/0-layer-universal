---
resource_id: "3f5f195c-ab93-4386-bae9-3e6202e0c436"
resource_type: "document"
resource_name: "supabase_javascript_integration_rule"
---
# SUPABASE JAVASCRIPT INTEGRATION RULE

<!-- section_id: "b9383990-3983-494a-985a-c312f0ec4eaf" -->
## **MANDATORY REQUIREMENT**

**ALL Supabase database operations, field management, table interactions, and data manipulation MUST be performed using the JavaScript/TypeScript client library methods, NOT direct SQL queries or database UI operations.**

<!-- section_id: "3915d68b-04e4-4033-b626-ca87174ad448" -->
## **RULE SCOPE**

This rule applies to:
- Database operations (CRUD)
- Field creation and modification
- Table schema changes
- Data validation and constraints
- Authentication and authorization
- Real-time subscriptions
- Storage operations
- Edge functions integration

<!-- section_id: "d2a369a1-4f8b-402a-b4cb-f31be1114ef9" -->
## **REQUIRED JAVASCRIPT PATTERNS**

<!-- section_id: "1f24380b-a1e1-433e-988d-92193956f4e3" -->
### **1. Database Operations**

```javascript
// ✅ CORRECT: Use Supabase client methods
import { supabase } from './services/api.js';

// Insert data
const { data, error } = await supabase
  .from('table_name')
  .insert([{ field1: 'value1', field2: 'value2' }]);

// Select data
const { data, error } = await supabase
  .from('table_name')
  .select('*')
  .eq('field', 'value');

// Update data
const { data, error } = await supabase
  .from('table_name')
  .update({ field: 'new_value' })
  .eq('id', recordId);

// Delete data
const { data, error } = await supabase
  .from('table_name')
  .delete()
  .eq('id', recordId);
```

<!-- section_id: "68bf488f-02e3-462f-b10b-14b17bb63cf1" -->
### **2. Authentication Operations**

```javascript
// ✅ CORRECT: Use Supabase auth methods
import { supabase } from './services/api.js';

// Sign up
const { data, error } = await supabase.auth.signUp({
  email: 'user@example.com',
  password: 'password123'
});

// Sign in
const { data, error } = await supabase.auth.signInWithPassword({
  email: 'user@example.com',
  password: 'password123'
});

// Sign out
const { error } = await supabase.auth.signOut();

// Get current user
const { data: { user } } = await supabase.auth.getUser();
```

<!-- section_id: "2f2b016b-f4f4-4498-adaf-8e284de73829" -->
### **3. Real-time Subscriptions**

```javascript
// ✅ CORRECT: Use Supabase real-time subscriptions
import { supabase } from './services/api.js';

const subscription = supabase
  .channel('table_changes')
  .on('postgres_changes', 
    { event: '*', schema: 'public', table: 'table_name' },
    (payload) => {
      console.log('Change received!', payload);
    }
  )
  .subscribe();
```

<!-- section_id: "c9544f8f-52f3-4ba5-a5d2-ea9f115ca8d5" -->
### **4. Storage Operations**

```javascript
// ✅ CORRECT: Use Supabase storage methods
import { supabase } from './services/api.js';

// Upload file
const { data, error } = await supabase.storage
  .from('bucket_name')
  .upload('file_path', file);

// Download file
const { data, error } = await supabase.storage
  .from('bucket_name')
  .download('file_path');
```

<!-- section_id: "2b4f132e-db27-4e6b-b785-b4838f459f18" -->
## **FORBIDDEN PATTERNS**

<!-- section_id: "84bc270e-3985-4bd0-8e87-4cdf7a8fd5f2" -->
### **❌ NEVER USE: Direct SQL Queries**

```javascript
// ❌ FORBIDDEN: Direct SQL execution
const { data, error } = await supabase.rpc('custom_function', {
  param1: 'value1'
});

// ❌ FORBIDDEN: Raw SQL in client code
const query = "SELECT * FROM table_name WHERE field = 'value'";
```

<!-- section_id: "184ca7f2-abe2-47b0-b1e5-f2110b9d40a2" -->
### **❌ NEVER USE: Database UI Operations**

- Creating tables through Supabase Dashboard
- Modifying schema through Table Editor
- Running SQL queries in SQL Editor
- Manual data insertion through UI

<!-- section_id: "b80986bf-e8eb-4fd5-b4d2-e26fee497041" -->
### **❌ NEVER USE: Direct Database Connections**

```javascript
// ❌ FORBIDDEN: Direct PostgreSQL connections
import { Pool } from 'pg';
const pool = new Pool({ connectionString: 'postgresql://...' });
```

<!-- section_id: "44889e7a-1cf9-4712-a2bc-16ed4a6e0975" -->
## **REQUIRED IMPLEMENTATION PATTERNS**

<!-- section_id: "a0bc1ceb-0850-4515-a8bf-4594e84cb068" -->
### **1. Service Layer Architecture**

```javascript
// services/database.js
import { supabase } from './api.js';

export const databaseService = {
  // User operations
  async createUser(userData) {
    const { data, error } = await supabase
      .from('users')
      .insert([userData])
      .select();
    
    if (error) throw new Error(error.message);
    return data[0];
  },

  // Class operations
  async createClass(classData) {
    const { data, error } = await supabase
      .from('classes')
      .insert([classData])
      .select();
    
    if (error) throw new Error(error.message);
    return data[0];
  },

  // Student operations
  async addStudent(studentData) {
    const { data, error } = await supabase
      .from('students')
      .insert([studentData])
      .select();
    
    if (error) throw new Error(error.message);
    return data[0];
  }
};
```

<!-- section_id: "0be9201f-ad53-4c2b-9f62-c00c0bb8205b" -->
### **2. Error Handling Pattern**

```javascript
// ✅ CORRECT: Comprehensive error handling
export const pointsService = {
  async givePoints(studentId, amount, reason) {
    try {
      // Get current student data
      const { data: student, error: fetchError } = await supabase
        .from('students')
        .select('*')
        .eq('id', studentId)
        .single();

      if (fetchError) throw new Error(fetchError.message);

      // Update points
      const { data, error } = await supabase
        .from('students')
        .update({ 
          points_balance: student.points_balance + amount,
          updated_at: new Date().toISOString()
        })
        .eq('id', studentId)
        .select();

      if (error) throw new Error(error.message);
      return data[0];

    } catch (error) {
      console.error('Error giving points:', error);
      throw error;
    }
  }
};
```

<!-- section_id: "a1a9ce14-104b-445b-89c2-753889e91a1a" -->
### **3. Real-time Integration Pattern**

```javascript
// ✅ CORRECT: Real-time data synchronization
export const realtimeService = {
  subscribeToStudentUpdates(callback) {
    return supabase
      .channel('student_updates')
      .on('postgres_changes', 
        { 
          event: 'UPDATE', 
          schema: 'public', 
          table: 'students' 
        },
        callback
      )
      .subscribe();
  },

  subscribeToClassUpdates(callback) {
    return supabase
      .channel('class_updates')
      .on('postgres_changes', 
        { 
          event: '*', 
          schema: 'public', 
          table: 'classes' 
        },
        callback
      )
      .subscribe();
  }
};
```

<!-- section_id: "d7b96af9-8d57-446f-8691-629754c98dfe" -->
## **REQUIRED FILE STRUCTURE**

```
website/src/
├── services/
│   ├── api.js              # Supabase client configuration
│   ├── auth.js             # Authentication operations
│   ├── database.js         # Database CRUD operations
│   ├── points.js           # Points system operations
│   ├── realtime.js         # Real-time subscriptions
│   └── storage.js          # File storage operations
├── components/
│   ├── auth/               # Authentication components
│   ├── teacher/            # Teacher-specific components
│   └── student/            # Student-specific components
└── utils/
    ├── validation.js       # Data validation helpers
    └── constants.js        # Application constants
```

<!-- section_id: "8ad25230-b0b8-43f5-9073-5245d547100a" -->
## **VALIDATION REQUIREMENTS**

<!-- section_id: "e10c20ae-987c-4efc-939b-a5175dd41d28" -->
### **1. Data Validation**

```javascript
// ✅ CORRECT: Client-side validation before Supabase operations
export const validateClassData = (classData) => {
  const errors = [];
  
  if (!classData.name || classData.name.length < 3) {
    errors.push('Class name must be at least 3 characters');
  }
  
  if (classData.code && classData.code.length > 20) {
    errors.push('Class code must be 20 characters or less');
  }
  
  if (classData.total_points && classData.total_points < 0) {
    errors.push('Total points must be non-negative');
  }
  
  return errors;
};
```

<!-- section_id: "cf760c03-0e83-4b63-84a9-fc16e3d68a5c" -->
### **2. Type Safety**

```javascript
// ✅ CORRECT: TypeScript interfaces for Supabase data
interface Student {
  id: string;
  user_id: string;
  class_id: string;
  student_id: string;
  points_balance: number;
  created_at: string;
  updated_at: string;
}

interface Class {
  id: string;
  teacher_id: string;
  name: string;
  code: string;
  description?: string;
  total_points: number;
  created_at: string;
  updated_at: string;
}
```

<!-- section_id: "bca74295-a22c-4cd0-9b9e-15818c17292d" -->
## **TESTING REQUIREMENTS**

<!-- section_id: "62f579f3-da9f-4aab-a6ad-9b0080156781" -->
### **1. Unit Tests for Services**

```javascript
// tests/services/database.test.js
import { databaseService } from '../src/services/database.js';
import { supabase } from '../src/services/api.js';

describe('Database Service', () => {
  test('should create user with valid data', async () => {
    const userData = {
      email: 'test@example.com',
      name: 'Test User'
    };
    
    const result = await databaseService.createUser(userData);
    expect(result).toBeDefined();
    expect(result.email).toBe(userData.email);
  });
});
```

<!-- section_id: "b95b6279-932c-423e-a184-d75e64e165d0" -->
### **2. Integration Tests**

```javascript
// tests/integration/supabase.test.js
import { supabase } from '../src/services/api.js';

describe('Supabase Integration', () => {
  test('should connect to database', async () => {
    const { data, error } = await supabase
      .from('users')
      .select('count')
      .limit(1);
    
    expect(error).toBeNull();
    expect(data).toBeDefined();
  });
});
```

<!-- section_id: "a96af13e-3cad-4873-b8e1-85fa4546fdc0" -->
## **ENFORCEMENT**

<!-- section_id: "19b0066c-3025-464a-8754-c2514d8b712b" -->
### **Code Review Checklist**

- [ ] All database operations use Supabase client methods
- [ ] No direct SQL queries in client code
- [ ] Proper error handling for all Supabase operations
- [ ] Type safety with TypeScript interfaces
- [ ] Real-time subscriptions properly implemented
- [ ] Service layer architecture followed
- [ ] Data validation before database operations

<!-- section_id: "1138d9cc-995f-487e-9236-c10cd3de3837" -->
### **Automated Checks**

```javascript
// eslint rules for Supabase usage
module.exports = {
  rules: {
    'no-supabase-sql': 'error',
    'require-supabase-client': 'error',
    'no-direct-db-access': 'error'
  }
};
```

<!-- section_id: "30a2a5b3-2861-4c1c-8649-a3b725cd6a83" -->
## **MIGRATION STRATEGY**

<!-- section_id: "f1628356-e361-4e53-80e2-0dc30b24e895" -->
### **Phase 1: Service Layer Implementation**
1. Create service layer files
2. Implement all CRUD operations using Supabase client
3. Add proper error handling and validation

<!-- section_id: "7912086f-7f69-4046-ac08-586973cdffe3" -->
### **Phase 2: Component Integration**
1. Update all components to use service layer
2. Remove any direct database UI operations
3. Implement real-time subscriptions

<!-- section_id: "9f214944-2204-4b86-a42a-96927b231bce" -->
### **Phase 3: Testing and Validation**
1. Add comprehensive unit tests
2. Implement integration tests
3. Add end-to-end testing with Supabase operations

<!-- section_id: "d9552c88-7dab-45c2-8571-aa6022e93257" -->
## **BENEFITS**

1. **Consistency**: All database operations follow the same pattern
2. **Type Safety**: TypeScript integration provides compile-time checking
3. **Error Handling**: Centralized error handling and validation
4. **Real-time**: Built-in real-time capabilities
5. **Security**: Row Level Security (RLS) policies enforced
6. **Scalability**: Optimized for Supabase's architecture
7. **Maintainability**: Clear separation of concerns

<!-- section_id: "7ed61f25-9b4c-4264-aa69-a728d0d93e38" -->
## **VIOLATION CONSEQUENCES**

- **Code Review Rejection**: Any code using direct SQL or UI operations will be rejected
- **Build Failure**: Automated checks will fail the build
- **Performance Issues**: Non-optimized operations will be flagged
- **Security Risks**: Bypassing RLS policies will be detected

---

**This rule is MANDATORY and must be followed for ALL Supabase interactions in the I-eat project.**
