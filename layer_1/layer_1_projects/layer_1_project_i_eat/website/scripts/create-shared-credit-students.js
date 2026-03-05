// resource_id: "7c81a1ed-4e33-4acd-acd4-c75082fcd523"
// resource_type: "document"
// resource_name: "create-shared-credit-students"
#!/usr/bin/env node

/**
 * Create Students with Shared User Credit Script
 * 
 * This script will create multiple students that share the same user_credit_id
 * to simulate the problem we need to fix
 */

import { createClient } from '@supabase/supabase-js'
import { fileURLToPath } from 'url'
import { dirname, join } from 'path'
import dotenv from 'dotenv'

// Get the directory of the current script
const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

// Load environment variables
dotenv.config({ path: join(__dirname, '..', '.env.local') })

// Initialize Supabase client
const supabaseUrl = process.env.VITE_SUPABASE_URL
const supabaseKey = process.env.VITE_SUPABASE_ANON_KEY

if (!supabaseUrl || !supabaseKey) {
  console.error('❌ Missing Supabase environment variables')
  process.exit(1)
}

const supabase = createClient(supabaseUrl, supabaseKey)

async function createSharedCreditStudents() {
  console.log('🚀 Creating Students with Shared User Credit...')
  console.log('==============================================')
  
  try {
    // Authenticate first
    console.log('🔐 Authenticating...')
    const { data: authData, error: authError } = await supabase.auth.signInWithPassword({
      email: 'testuser@byui.edu',
      password: 'password123'
    })

    if (authError) {
      throw new Error(`Authentication failed: ${authError.message}`)
    }

    console.log(`✅ Successfully authenticated as: ${authData.user.email}`)

    // Get a class
    const { data: classes, error: classesError } = await supabase
      .from('classes')
      .select('id, name, code')
      .limit(1)

    if (classesError || !classes || classes.length === 0) {
      throw new Error('No classes available')
    }

    const targetClass = classes[0]
    console.log(`Using class: ${targetClass.name} (${targetClass.code})`)

    // Create a shared user_credit record
    console.log('\n📝 Creating shared user_credit record...')
    const { data: sharedCredit, error: creditError } = await supabase
      .from('user_credit')
      .insert({
        points: 0
      })
      .select('user_credit_id')
      .single()

    if (creditError) {
      throw new Error(`Failed to create shared user_credit: ${creditError.message}`)
    }

    console.log(`✅ Created shared user_credit record: ${sharedCredit.user_credit_id}`)

    // Create 5 students that all share the same user_credit_id
    console.log('\n👥 Creating students with shared user_credit...')
    const students = []
    
    for (let i = 1; i <= 5; i++) {
      const studentId = `SHARED${String(i).padStart(3, '0')}`
      
      const { data: newStudent, error: studentError } = await supabase
        .from('students')
        .insert({
          user_id: authData.user.id, // Use the authenticated user's ID
          class_id: targetClass.id,
          student_id: studentId,
          user_credit_id: sharedCredit.user_credit_id // All students share the same credit
        })
        .select('id, student_id, user_credit_id')
        .single()

      if (studentError) {
        console.error(`❌ Failed to create student ${studentId}: ${studentError.message}`)
        continue
      }

      students.push(newStudent)
      console.log(`✅ Created student: ${studentId} with shared user_credit_id: ${sharedCredit.user_credit_id}`)
    }

    console.log(`\n🎉 Successfully created ${students.length} students with shared user_credit!`)
    
    // Verify the shared credit situation
    console.log('\n🔍 Verifying shared credit situation...')
    const { data: allStudents, error: verifyError } = await supabase
      .from('students')
      .select('id, student_id, user_credit_id, user_credit(points)')
      .eq('class_id', targetClass.id)

    if (verifyError) {
      console.error(`❌ Verification failed: ${verifyError.message}`)
    } else {
      console.log(`✅ Found ${allStudents.length} students in class`)
      
      // Group students by user_credit_id
      const creditGroups = {}
      allStudents.forEach(student => {
        const creditId = student.user_credit_id
        if (!creditGroups[creditId]) {
          creditGroups[creditId] = []
        }
        creditGroups[creditId].push(student)
      })

      console.log('\n📊 User Credit Distribution:')
      Object.keys(creditGroups).forEach(creditId => {
        const students = creditGroups[creditId]
        console.log(`   user_credit_id ${creditId}: ${students.length} students (${students.map(s => s.student_id).join(', ')})`)
      })
    }

    // Sign out
    await supabase.auth.signOut()
    console.log('\n🔓 Signed out successfully')

  } catch (error) {
    console.error('💥 Script failed:', error.message)
    console.error('Stack trace:', error.stack)
  }
}

// Run the script
createSharedCreditStudents()
  .then(() => {
    console.log('\n🎉 Script completed!')
    process.exit(0)
  })
  .catch((error) => {
    console.error('Script failed:', error)
    process.exit(1)
  })
