---
resource_id: "ff6c21ef-8849-44e6-a467-84e8f1f971a4"
resource_type: "rule"
resource_name: "supabase_javascript_quick_reference"
---
# SUPABASE JAVASCRIPT QUICK REFERENCE

<!-- section_id: "f623591d-0747-41a5-8987-b9ec0c3d8433" -->
## **🚨 MANDATORY RULE**

**ALL Supabase operations MUST use JavaScript client methods - NO direct SQL, NO UI operations, NO raw database access.**

<!-- section_id: "81d50756-44eb-4f0c-86db-b945b25fb249" -->
## **✅ CORRECT PATTERNS**

<!-- section_id: "2032e757-6705-433d-b04f-062ad1b3b9b7" -->
### **Database Operations**
```javascript
// ✅ Insert
const { data, error } = await supabase
  .from('table_name')
  .insert([{ field: 'value' }]);

// ✅ Select
const { data, error } = await supabase
  .from('table_name')
  .select('*')
  .eq('field', 'value');

// ✅ Update
const { data, error } = await supabase
  .from('table_name')
  .update({ field: 'new_value' })
  .eq('id', recordId);

// ✅ Delete
const { data, error } = await supabase
  .from('table_name')
  .delete()
  .eq('id', recordId);
```

<!-- section_id: "85ebeaa4-30e9-4018-94dd-1eae9d8bee1a" -->
### **Authentication**
```javascript
// ✅ Sign up
const { data, error } = await supabase.auth.signUp({
  email: 'user@example.com',
  password: 'password123'
});

// ✅ Sign in
const { data, error } = await supabase.auth.signInWithPassword({
  email: 'user@example.com',
  password: 'password123'
});

// ✅ Sign out
const { error } = await supabase.auth.signOut();
```

<!-- section_id: "b1dbfd5b-1794-4d5e-b5af-0e73490325a8" -->
### **Real-time Subscriptions**
```javascript
// ✅ Real-time updates
const subscription = supabase
  .channel('table_changes')
  .on('postgres_changes', 
    { event: '*', schema: 'public', table: 'table_name' },
    (payload) => console.log('Change:', payload)
  )
  .subscribe();
```

<!-- section_id: "d78ff6ef-52e5-4f08-a772-1d6653e3e396" -->
## **❌ FORBIDDEN PATTERNS**

```javascript
// ❌ NO direct SQL
const { data, error } = await supabase.rpc('custom_function');

// ❌ NO raw SQL queries
const query = "SELECT * FROM table_name";

// ❌ NO direct database connections
import { Pool } from 'pg';
```

<!-- section_id: "26600b78-0edc-4a79-93b8-66b83606f8dd" -->
## **🔧 REQUIRED SERVICE LAYER**

```javascript
// services/database.js
export const databaseService = {
  async createUser(userData) {
    const { data, error } = await supabase
      .from('users')
      .insert([userData])
      .select();
    
    if (error) throw new Error(error.message);
    return data[0];
  }
};
```

<!-- section_id: "5adb98cf-0de0-471d-aa7a-fbb409912a1a" -->
## **📁 REQUIRED FILE STRUCTURE**

```
website/src/services/
├── api.js          # Supabase client config
├── auth.js         # Authentication operations
├── database.js     # CRUD operations
├── points.js       # Points system
└── realtime.js     # Real-time subscriptions
```

<!-- section_id: "ab18ea56-88bd-4cc6-a37a-c6564a585780" -->
## **🎯 ENFORCEMENT**

- **Code Review**: Reject any direct SQL or UI operations
- **Build Checks**: Automated validation of Supabase patterns
- **Type Safety**: Use TypeScript interfaces for all data

---

**This rule is MANDATORY for ALL Supabase interactions in the I-eat project.**
