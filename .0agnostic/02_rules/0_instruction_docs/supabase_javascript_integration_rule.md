---
resource_id: "c6411bcd-7a6a-4834-a052-8202615ad359"
resource_type: "rule"
resource_name: "supabase_javascript_integration_rule"
---
# SUPABASE JAVASCRIPT INTEGRATION RULE

<!-- section_id: "f5a3fc7a-71d2-4eda-8e74-133621bce6d3" -->
## **MANDATORY REQUIREMENT**

**ALL Supabase database operations, field management, table interactions, and data manipulation MUST be performed using the JavaScript/TypeScript client library methods, NOT direct SQL queries or database UI operations.**

<!-- section_id: "65d20bc0-9470-4bcc-b5c9-01da1f82fbdf" -->
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

<!-- section_id: "0fdef9c1-dd23-4f1a-bff5-5adecb851d67" -->
## **REQUIRED JAVASCRIPT PATTERNS**

<!-- section_id: "ad7a7914-a783-4dfb-8b23-60c09298236c" -->
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

<!-- section_id: "deba66c7-1fa4-4f64-8acc-db86ba046f0e" -->
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

<!-- section_id: "95c81cfb-e8c9-427d-8698-7e61ce8f79ec" -->
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

<!-- section_id: "3d6757df-d6f7-4e3e-b566-fc3770e88f91" -->
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

<!-- section_id: "6e633135-70d3-41ef-b1ae-3bd684018cd6" -->
## **FORBIDDEN PATTERNS**

<!-- section_id: "8fdc7cd8-2951-4744-8b90-7b7a8c03db3f" -->
### **❌ NEVER USE: Direct SQL Queries**

```javascript
// ❌ FORBIDDEN: Direct SQL execution
const { data, error } = await supabase.rpc('custom_function', {
  param1: 'value1'
});

// ❌ FORBIDDEN: Raw SQL in client code
const query = "SELECT * FROM table_name WHERE field = 'value'";
```

<!-- section_id: "55253bbd-0580-4fd8-8c8f-507541fced7c" -->
### **❌ NEVER USE: Database UI Operations**

- Creating tables through Supabase Dashboard
- Modifying schema through Table Editor
- Running SQL queries in SQL Editor
- Manual data insertion through UI

<!-- section_id: "2578f3c6-a468-444b-9482-fcf5a572ac4c" -->
### **❌ NEVER USE: Direct Database Connections**

```javascript
// ❌ FORBIDDEN: Direct PostgreSQL connections
import { Pool } from 'pg';
const pool = new Pool({ connectionString: 'postgresql://...' });
```

<!-- section_id: "a20b5171-e755-4298-96e9-05ef219bf8e9" -->
## **REQUIRED IMPLEMENTATION PATTERNS**

<!-- section_id: "33941080-fd2f-43d9-ba13-9a880ea327fe" -->
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

<!-- section_id: "a5a940b5-3b6c-4423-a55c-41064f095981" -->
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

<!-- section_id: "efbb6443-c822-4cc9-9ba8-48bacd133b1b" -->
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

<!-- section_id: "5e5a4115-29dc-4682-a29e-7b625026017b" -->
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

<!-- section_id: "1693d6b0-6501-435a-b44f-4d3bc65ed4cf" -->
## **VALIDATION REQUIREMENTS**

<!-- section_id: "32ae877d-bbf5-491d-9256-e252b2dcd25e" -->
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

<!-- section_id: "90bf48a1-ddd1-4552-abf7-db76440675bd" -->
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

<!-- section_id: "5e68ccd1-bc26-4132-9ee3-c927e5ddb5cd" -->
## **TESTING REQUIREMENTS**

<!-- section_id: "0fbe9db7-acc7-4fba-a1f2-5ddc8c9f2eb7" -->
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

<!-- section_id: "5b465b38-854e-453a-9eee-614ae339f5f6" -->
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

<!-- section_id: "a54810a2-7c4f-437d-89f1-4bf7bbb4c7a0" -->
## **ENFORCEMENT**

<!-- section_id: "f48de6c5-aba6-4d06-a2bb-65c10c45a4fa" -->
### **Code Review Checklist**

- [ ] All database operations use Supabase client methods
- [ ] No direct SQL queries in client code
- [ ] Proper error handling for all Supabase operations
- [ ] Type safety with TypeScript interfaces
- [ ] Real-time subscriptions properly implemented
- [ ] Service layer architecture followed
- [ ] Data validation before database operations

<!-- section_id: "dad586ba-09c4-4d7d-94e8-64c7bbf01bef" -->
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

<!-- section_id: "9f25b766-223c-45e9-8fbb-d8f5490b309b" -->
## **MIGRATION STRATEGY**

<!-- section_id: "f7cf5c0f-811d-4443-ac2c-3ad7a0bd5215" -->
### **Phase 1: Service Layer Implementation**
1. Create service layer files
2. Implement all CRUD operations using Supabase client
3. Add proper error handling and validation

<!-- section_id: "3127aab2-9550-43ba-a986-4a9262cb7959" -->
### **Phase 2: Component Integration**
1. Update all components to use service layer
2. Remove any direct database UI operations
3. Implement real-time subscriptions

<!-- section_id: "45f25878-2f95-44b4-8678-2f525416d1c7" -->
### **Phase 3: Testing and Validation**
1. Add comprehensive unit tests
2. Implement integration tests
3. Add end-to-end testing with Supabase operations

<!-- section_id: "4689790e-fd8a-4c56-9abc-aa7b0d2fe0c1" -->
## **BENEFITS**

1. **Consistency**: All database operations follow the same pattern
2. **Type Safety**: TypeScript integration provides compile-time checking
3. **Error Handling**: Centralized error handling and validation
4. **Real-time**: Built-in real-time capabilities
5. **Security**: Row Level Security (RLS) policies enforced
6. **Scalability**: Optimized for Supabase's architecture
7. **Maintainability**: Clear separation of concerns

<!-- section_id: "e2670389-8325-4085-9ac9-19b4c590f97c" -->
## **VIOLATION CONSEQUENCES**

- **Code Review Rejection**: Any code using direct SQL or UI operations will be rejected
- **Build Failure**: Automated checks will fail the build
- **Performance Issues**: Non-optimized operations will be flagged
- **Security Risks**: Bypassing RLS policies will be detected

---

**This rule is MANDATORY and must be followed for ALL Supabase interactions in the I-eat project.**
