---
resource_id: "77c65325-a4e2-4306-ab32-fadcb733e135"
resource_type: "document"
resource_name: "supabase_javascript_quick_reference"
---
# SUPABASE JAVASCRIPT QUICK REFERENCE

<!-- section_id: "e4dabbc6-b613-4445-88a3-06ad92bd8baa" -->
## **🚨 MANDATORY RULE**

**ALL Supabase operations MUST use JavaScript client methods - NO direct SQL, NO UI operations, NO raw database access.**

<!-- section_id: "4f219c78-8d4d-49c2-b0e0-e87c3b6d1505" -->
## **✅ CORRECT PATTERNS**

<!-- section_id: "8784ae7f-e623-49a3-94a6-d040aef51fc7" -->
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

<!-- section_id: "db7bd628-d21d-4ebe-bd6e-22d8c373654c" -->
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

<!-- section_id: "44024a68-dde7-420d-9efa-792ed1d0e14b" -->
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

<!-- section_id: "a09e1cb4-3029-40e5-a39b-9aa32266311f" -->
## **❌ FORBIDDEN PATTERNS**

```javascript
// ❌ NO direct SQL
const { data, error } = await supabase.rpc('custom_function');

// ❌ NO raw SQL queries
const query = "SELECT * FROM table_name";

// ❌ NO direct database connections
import { Pool } from 'pg';
```

<!-- section_id: "c23862d5-3d9c-44f0-a6b4-c9e7fe707d60" -->
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

<!-- section_id: "6ecbcb9f-948c-4475-b07a-9db185988b0e" -->
## **📁 REQUIRED FILE STRUCTURE**

```
website/src/services/
├── api.js          # Supabase client config
├── auth.js         # Authentication operations
├── database.js     # CRUD operations
├── points.js       # Points system
└── realtime.js     # Real-time subscriptions
```

<!-- section_id: "0ae4b3b9-2ecd-4d8d-a19f-bee0246c0f74" -->
## **🎯 ENFORCEMENT**

- **Code Review**: Reject any direct SQL or UI operations
- **Build Checks**: Automated validation of Supabase patterns
- **Type Safety**: Use TypeScript interfaces for all data

---

**This rule is MANDATORY for ALL Supabase interactions in the I-eat project.**
