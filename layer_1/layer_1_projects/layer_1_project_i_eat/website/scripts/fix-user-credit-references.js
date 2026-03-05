// resource_id: "333feed4-2523-41ec-9d9a-bf8019d0e65c"
// resource_type: "document"
// resource_name: "fix-user-credit-references"
#!/usr/bin/env node

/**
 * Migration Script: Fix Shared User Credit References
 * 
 * Problem: All students currently reference the same user_credit record (row 2),
 * causing them to share the same points balance.
 * 
 * Solution: Create individual user_credit records for each student and update
 * their user_credit_id references.
 */

import { createClient } from '@supabase/supabase-js'
import { fileURLToPath } from 'url'
import { dirname, join } from 'path'

// Get the directory of the current script
const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

// Load environment variables
import dotenv from 'dotenv'
dotenv.config({ path: join(__dirname, '..', '.env.local') })

// Initialize Supabase client
const supabaseUrl = process.env.VITE_SUPABASE_URL
const supabaseKey = process.env.VITE_SUPABASE_ANON_KEY

if (!supabaseUrl || !supabaseKey) {
  console.error('❌ Missing Supabase environment variables')
  console.error('Please ensure VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY are set in .env.local')
  process.exit(1)
}

const supabase = createClient(supabaseUrl, supabaseKey)

async function fixUserCreditReferences() {
  console.log('🚀 Starting user_credit migration...')
  console.log('=====================================')
  
  try {
    // Step 0: Authenticate first
    console.log('🔐 Authenticating...')
    const { data: authData, error: authError } = await supabase.auth.signInWithPassword({
      email: 'testuser@byui.edu',
      password: 'password123'
    })

    if (authError) {
      throw new Error(`Authentication failed: ${authError.message}`)
    }

    console.log(`✅ Successfully authenticated as: ${authData.user.email}`)

    // Step 1: Fetch all students
    console.log('📋 Fetching all students...')
    const { data: students, error: studentsError } = await supabase
      .from('students')
      .select('id, student_id, user_credit_id')

    if (studentsError) {
      throw new Error(`Failed to fetch students: ${studentsError.message}`)
    }

    if (!students || students.length === 0) {
      console.log('ℹ️  No students found in the database')
      return
    }

    console.log(`✅ Found ${students.length} students`)
    console.log('')

    // Step 2: Process each student
    let successCount = 0
    let errorCount = 0
    const errors = []

    for (let i = 0; i < students.length; i++) {
      const student = students[i]
      console.log(`🔄 Processing student ${i + 1}/${students.length}: ${student.student_id} (ID: ${student.id})`)
      
      try {
        // Check if student already has a unique user_credit_id
        const { data: existingCredits, error: checkError } = await supabase
          .from('user_credit')
          .select('user_credit_id')
          .eq('user_credit_id', student.user_credit_id)

        if (checkError) {
          throw new Error(`Failed to check existing credit: ${checkError.message}`)
        }

        // If this user_credit_id is only used by this student, skip
        const { data: otherStudents, error: otherStudentsError } = await supabase
          .from('students')
          .select('id')
          .eq('user_credit_id', student.user_credit_id)
          .neq('id', student.id)

        if (otherStudentsError) {
          throw new Error(`Failed to check other students: ${otherStudentsError.message}`)
        }

        if (otherStudents && otherStudents.length === 0) {
          console.log(`   ✅ Student already has unique user_credit_id: ${student.user_credit_id}`)
          successCount++
          continue
        }

        // Create new user_credit record
        console.log(`   📝 Creating new user_credit record...`)
        const { data: newCredit, error: creditError } = await supabase
          .from('user_credit')
          .insert({
            points: 0
          })
          .select('user_credit_id')
          .single()

        if (creditError) {
          throw new Error(`Failed to create user_credit: ${creditError.message}`)
        }

        console.log(`   ✅ Created user_credit record: ${newCredit.user_credit_id}`)

        // Update student's user_credit_id
        console.log(`   🔄 Updating student's user_credit_id...`)
        const { error: updateError } = await supabase
          .from('students')
          .update({ user_credit_id: newCredit.user_credit_id })
          .eq('id', student.id)

        if (updateError) {
          throw new Error(`Failed to update student: ${updateError.message}`)
        }

        console.log(`   ✅ Updated student to use user_credit_id: ${newCredit.user_credit_id}`)
        successCount++

      } catch (error) {
        console.error(`   ❌ Error processing student ${student.student_id}: ${error.message}`)
        errorCount++
        errors.push({
          student: student.student_id,
          error: error.message
        })
      }

      console.log('')
    }

    // Step 3: Report results
    console.log('📊 Migration Results')
    console.log('===================')
    console.log(`✅ Successfully processed: ${successCount} students`)
    console.log(`❌ Errors: ${errorCount} students`)
    
    if (errors.length > 0) {
      console.log('')
      console.log('❌ Error Details:')
      errors.forEach(({ student, error }) => {
        console.log(`   - ${student}: ${error}`)
      })
    }

    // Step 4: Verify the fix
    console.log('')
    console.log('🔍 Verifying migration...')
    const { data: verificationStudents, error: verifyError } = await supabase
      .from('students')
      .select('id, student_id, user_credit_id, user_credit(points)')

    if (verifyError) {
      console.error(`❌ Verification failed: ${verifyError.message}`)
    } else {
      console.log('✅ Verification successful!')
      console.log('')
      console.log('📋 Final Student Status:')
      verificationStudents.forEach((student, index) => {
        console.log(`   ${index + 1}. ${student.student_id}: user_credit_id=${student.user_credit_id}, points=${student.user_credit?.points || 0}`)
      })
    }

    console.log('')
    console.log('🎉 Migration completed!')
    
    if (errorCount === 0) {
      console.log('✅ All students now have individual user_credit records')
    } else {
      console.log(`⚠️  ${errorCount} students had errors - please review and fix manually`)
    }

    // Sign out
    await supabase.auth.signOut()
    console.log('🔓 Signed out successfully')

  } catch (error) {
    console.error('💥 Migration failed:', error.message)
    console.error('Stack trace:', error.stack)
    process.exit(1)
  }
}

// Run the migration
fixUserCreditReferences()
  .then(() => {
    console.log('Migration script completed')
    process.exit(0)
  })
  .catch((error) => {
    console.error('Migration script failed:', error)
    process.exit(1)
  })
