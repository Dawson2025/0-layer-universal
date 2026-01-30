# SUPABASE JAVASCRIPT QUICK REFERENCE

## **🚨 MANDATORY RULE**

**ALL Supabase operations MUST use JavaScript client methods - NO direct SQL, NO UI operations, NO raw database access.**

## **✅ CORRECT PATTERNS**

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

## **❌ FORBIDDEN PATTERNS**

```javascript
// ❌ NO direct SQL
const { data, error } = await supabase.rpc('custom_function');

// ❌ NO raw SQL queries
const query = "SELECT * FROM table_name";

// ❌ NO direct database connections
import { Pool } from 'pg';
```

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

## **📁 REQUIRED FILE STRUCTURE**

```
website/src/services/
├── api.js          # Supabase client config
├── auth.js         # Authentication operations
├── database.js     # CRUD operations
├── points.js       # Points system
└── realtime.js     # Real-time subscriptions
```

## **🎯 ENFORCEMENT**

- **Code Review**: Reject any direct SQL or UI operations
- **Build Checks**: Automated validation of Supabase patterns
- **Type Safety**: Use TypeScript interfaces for all data

---

**This rule is MANDATORY for ALL Supabase interactions in the I-eat project.**
