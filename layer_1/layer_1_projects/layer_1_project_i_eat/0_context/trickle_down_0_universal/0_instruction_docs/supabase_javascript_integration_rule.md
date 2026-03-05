---
resource_id: "516f04cb-ed8a-4f60-b20c-a3690dacd5ab"
resource_type: "document"
resource_name: "supabase_javascript_integration_rule"
---
# SUPABASE JAVASCRIPT INTEGRATION RULE

<!-- section_id: "4b1a3516-824d-4226-bb28-c07b7a305b20" -->
## **MANDATORY REQUIREMENT**

**ALL Supabase database operations, field management, table interactions, and data manipulation MUST be performed using the JavaScript/TypeScript client library methods, NOT direct SQL queries or database UI operations.**

<!-- section_id: "f741a9c2-f63d-44c0-9b51-a00be96b7321" -->
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

<!-- section_id: "201eb712-bf0f-4e75-bca1-59ba90e2ba46" -->
## **REQUIRED JAVASCRIPT PATTERNS**

<!-- section_id: "9015438a-1a5e-4a67-932f-e9ad63e32c69" -->
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

<!-- section_id: "ca4063af-fd26-4b63-b097-368805a00ab5" -->
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

<!-- section_id: "0bfef3f0-a3e9-44a8-9516-52877ed0d501" -->
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

<!-- section_id: "590de5f1-2dd1-4253-b584-8b34b6455b76" -->
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

<!-- section_id: "f6256818-0c7d-40d8-a55f-b70e9c4449c8" -->
## **FORBIDDEN PATTERNS**

<!-- section_id: "3fe76961-0e06-4f62-a4ce-d5e38af307e4" -->
### **❌ NEVER USE: Direct SQL Queries**

```javascript
// ❌ FORBIDDEN: Direct SQL execution
const { data, error } = await supabase.rpc('custom_function', {
  param1: 'value1'
});

// ❌ FORBIDDEN: Raw SQL in client code
const query = "SELECT * FROM table_name WHERE field = 'value'";
```

<!-- section_id: "9702965a-1190-4b1d-9c49-335d84c4433e" -->
### **❌ NEVER USE: Database UI Operations**

- Creating tables through Supabase Dashboard
- Modifying schema through Table Editor
- Running SQL queries in SQL Editor
- Manual data insertion through UI

<!-- section_id: "6274be51-1cb4-4917-8b9b-1df0b36e7d95" -->
### **❌ NEVER USE: Direct Database Connections**

```javascript
// ❌ FORBIDDEN: Direct PostgreSQL connections
import { Pool } from 'pg';
const pool = new Pool({ connectionString: 'postgresql://...' });
```

<!-- section_id: "b83b4259-1db3-4868-810c-073b4d52479a" -->
## **REQUIRED IMPLEMENTATION PATTERNS**

<!-- section_id: "37f5ff28-6bc5-4397-8910-9bf3f02c5fc0" -->
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

<!-- section_id: "f01da566-09e4-4507-a0e6-9fae9d16c14d" -->
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

<!-- section_id: "38758d62-768d-412e-91b8-bb585b99dae4" -->
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

<!-- section_id: "c4e93408-1199-465d-8a4f-03916c9c3b2f" -->
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

<!-- section_id: "ba675935-0f2d-463e-9ad3-61a9f41f2614" -->
## **VALIDATION REQUIREMENTS**

<!-- section_id: "3944b0b9-7484-47ee-b4f3-c4c6af7cebe5" -->
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

<!-- section_id: "4f954ec1-7caf-42ce-b4c0-af188a00c11b" -->
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

<!-- section_id: "ff8c8b08-3ff1-4030-87c7-b9a679cceaae" -->
## **TESTING REQUIREMENTS**

<!-- section_id: "d0278f7a-d5df-4e18-92b6-0b1ad7986bcc" -->
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

<!-- section_id: "dd3750e4-1d19-49ac-b140-d7ede987df75" -->
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

<!-- section_id: "57d969ac-30dd-4a0f-b205-c6c951ac8086" -->
## **ENFORCEMENT**

<!-- section_id: "40aabb62-0ab4-466d-916d-3009d806fa5c" -->
### **Code Review Checklist**

- [ ] All database operations use Supabase client methods
- [ ] No direct SQL queries in client code
- [ ] Proper error handling for all Supabase operations
- [ ] Type safety with TypeScript interfaces
- [ ] Real-time subscriptions properly implemented
- [ ] Service layer architecture followed
- [ ] Data validation before database operations

<!-- section_id: "1d5eae5d-1e37-4908-b167-12b774017020" -->
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

<!-- section_id: "d364938b-0c99-43e3-a471-fa121e565225" -->
## **MIGRATION STRATEGY**

<!-- section_id: "c026ffeb-31a7-4216-9826-dc4493383b76" -->
### **Phase 1: Service Layer Implementation**
1. Create service layer files
2. Implement all CRUD operations using Supabase client
3. Add proper error handling and validation

<!-- section_id: "d8f2cf92-eff6-4512-974c-dea0c12b85cb" -->
### **Phase 2: Component Integration**
1. Update all components to use service layer
2. Remove any direct database UI operations
3. Implement real-time subscriptions

<!-- section_id: "3b6d2f46-0919-434c-9c65-be806fab50c2" -->
### **Phase 3: Testing and Validation**
1. Add comprehensive unit tests
2. Implement integration tests
3. Add end-to-end testing with Supabase operations

<!-- section_id: "90c94596-0533-404f-a5a1-66e86b0a515b" -->
## **BENEFITS**

1. **Consistency**: All database operations follow the same pattern
2. **Type Safety**: TypeScript integration provides compile-time checking
3. **Error Handling**: Centralized error handling and validation
4. **Real-time**: Built-in real-time capabilities
5. **Security**: Row Level Security (RLS) policies enforced
6. **Scalability**: Optimized for Supabase's architecture
7. **Maintainability**: Clear separation of concerns

<!-- section_id: "68b7a996-c9e8-411d-b0f3-b4bab5b7601e" -->
## **VIOLATION CONSEQUENCES**

- **Code Review Rejection**: Any code using direct SQL or UI operations will be rejected
- **Build Failure**: Automated checks will fail the build
- **Performance Issues**: Non-optimized operations will be flagged
- **Security Risks**: Bypassing RLS policies will be detected

---

**This rule is MANDATORY and must be followed for ALL Supabase interactions in the I-eat project.**
