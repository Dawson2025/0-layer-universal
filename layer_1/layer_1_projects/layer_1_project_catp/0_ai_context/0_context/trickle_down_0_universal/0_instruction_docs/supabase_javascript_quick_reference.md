---
resource_id: "4828e63d-fa7f-4800-b363-a3ee9996f3b9"
resource_type: "document"
resource_name: "supabase_javascript_quick_reference"
---
# SUPABASE JAVASCRIPT QUICK REFERENCE

<!-- section_id: "c7595b8d-3df3-412a-90f8-8582c07b6fcb" -->
## **🚨 MANDATORY RULE**

**ALL Supabase operations MUST use JavaScript client methods - NO direct SQL, NO UI operations, NO raw database access.**

<!-- section_id: "98f4c8c4-df50-4ada-af3e-5af3b9909f14" -->
## **✅ CORRECT PATTERNS**

<!-- section_id: "dd97b164-c63e-4262-b042-ac0e49b9dee7" -->
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

<!-- section_id: "764a0271-c1b2-4ea0-8202-c7d9f7b08bdc" -->
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

<!-- section_id: "954e9075-ff98-4d53-8ac3-a2bfafe421a3" -->
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

<!-- section_id: "2bfafd8a-0084-447a-84d0-41b3183dcb32" -->
## **❌ FORBIDDEN PATTERNS**

```javascript
// ❌ NO direct SQL
const { data, error } = await supabase.rpc('custom_function');

// ❌ NO raw SQL queries
const query = "SELECT * FROM table_name";

// ❌ NO direct database connections
import { Pool } from 'pg';
```

<!-- section_id: "951d3cf1-3569-4749-91e5-62660d8215d8" -->
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

<!-- section_id: "b9759140-a60d-4e42-b421-485339c3761c" -->
## **📁 REQUIRED FILE STRUCTURE**

```
website/src/services/
├── api.js          # Supabase client config
├── auth.js         # Authentication operations
├── database.js     # CRUD operations
├── points.js       # Points system
└── realtime.js     # Real-time subscriptions
```

<!-- section_id: "bc28fbb7-9b5d-424c-afbe-64649dab8472" -->
## **🎯 ENFORCEMENT**

- **Code Review**: Reject any direct SQL or UI operations
- **Build Checks**: Automated validation of Supabase patterns
- **Type Safety**: Use TypeScript interfaces for all data

---

**This rule is MANDATORY for ALL Supabase interactions in the I-eat project.**
