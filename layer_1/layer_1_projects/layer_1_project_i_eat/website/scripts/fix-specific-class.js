// resource_id: "59b66fbe-27be-42d4-bf39-8028f6ede9e3"
// resource_type: "document"
// resource_name: "fix-specific-class"
import { createClient } from '@supabase/supabase-js'
import dotenv from 'dotenv'

dotenv.config({ path: '.env.local' })

const supabaseUrl = process.env.VITE_SUPABASE_URL
const supabaseKey = process.env.VITE_SUPABASE_ANON_KEY

if (!supabaseUrl || !supabaseKey) {
  console.error('Supabase URL and Key must be set in .env.local')
  process.exit(1)
}

const supabase = createClient(supabaseUrl, supabaseKey)

async function fixSpecificClass() {
  console.log('🔧 Fixing Specific Class Students...')
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

    // Step 1: Get the specific class from browser logs
    const classId = '88d50621-92bf-4f02-b370-e88105922de8'
    console.log(`📋 Checking class: ${classId}`)

    const { data: classData, error: classError } = await supabase
      .from('classes')
      .select('id, name, code')
      .eq('id', classId)

    if (classError) {
      throw new Error(`Failed to fetch class: ${classError.message}`)
    }

    if (!classData || classData.length === 0) {
      console.log('❌ No class found with that ID')
      return
    }

    const currentClass = classData[0]
    console.log(`✅ Found class: ${currentClass.name} (${currentClass.code})`)

    // Step 2: Get students in this specific class
    console.log('👥 Fetching students in specific class...')
    const { data: students, error: studentsError } = await supabase
      .from('students')
      .select('id, student_id, user_credit_id, user_credit(points)')
      .eq('class_id', classId)

    if (studentsError) {
      throw new Error(`Failed to fetch students: ${studentsError.message}`)
    }

    if (!students || students.length === 0) {
      console.log('ℹ️  No students found in this class')
      return
    }

    console.log(`✅ Found ${students.length} students in class`)
    console.log('\n📋 Current Student Status:')
    students.forEach((student, index) => {
      console.log(`   ${index + 1}. ${student.student_id}: user_credit_id=${student.user_credit_id}, points=${student.user_credit?.points || 0}`)
    })

    // Step 3: Check if students are sharing user_credit records
    const userCreditIds = students.map(s => s.user_credit_id).filter(Boolean)
    const uniqueUserCreditIds = [...new Set(userCreditIds)]
    
    console.log(`\n🔍 Analysis:`)
    console.log(`   - Total students: ${students.length}`)
    console.log(`   - Unique user_credit_ids: ${uniqueUserCreditIds.length}`)
    console.log(`   - Students sharing records: ${userCreditIds.length - uniqueUserCreditIds.length}`)

    if (uniqueUserCreditIds.length === students.length) {
      console.log('✅ All students already have individual user_credit records!')
      return
    }

    // Step 4: Fix students that are sharing records
    console.log('\n🔄 Fixing shared user_credit records...')
    let fixedCount = 0
    const errors = []

    for (const student of students) {
      // Check if this student's user_credit_id is shared with others
      const studentsWithSameCredit = students.filter(s => s.user_credit_id === student.user_credit_id)
      
      if (studentsWithSameCredit.length > 1) {
        console.log(`   - Fixing ${student.student_id} (sharing user_credit_id ${student.user_credit_id} with ${studentsWithSameCredit.length - 1} others)`)
        
        try {
          // Create a new user_credit record for this student
          const { data: newCredit, error: creditError } = await supabase
            .from('user_credit')
            .insert({ points: student.user_credit?.points || 0 })
            .select('user_credit_id')
            .single()

          if (creditError) {
            throw new Error(`Failed to create user_credit: ${creditError.message}`)
          }

          // Update the student's user_credit_id
          const { error: updateError } = await supabase
            .from('students')
            .update({ user_credit_id: newCredit.user_credit_id })
            .eq('id', student.id)

          if (updateError) {
            throw new Error(`Failed to update user_credit_id: ${updateError.message}`)
          }

          console.log(`   ✅ Created new user_credit ${newCredit.user_credit_id} for ${student.student_id}`)
          fixedCount++

        } catch (error) {
          errors.push({ student: student.student_id, error: error.message })
          console.error(`   ❌ Failed to fix ${student.student_id}: ${error.message}`)
        }
      } else {
        console.log(`   ✅ ${student.student_id} already has unique user_credit_id: ${student.user_credit_id}`)
      }
    }

    // Step 5: Verify the fix
    console.log('\n🔍 Verifying fix...')
    const { data: finalStudents, error: verifyError } = await supabase
      .from('students')
      .select('id, student_id, user_credit_id, user_credit(points)')
      .eq('class_id', classId)

    if (verifyError) {
      console.error(`❌ Verification failed: ${verifyError.message}`)
    } else {
      console.log('✅ Verification successful!')
      console.log('\n📋 Final Student Status:')
      finalStudents.forEach((student, index) => {
        console.log(`   ${index + 1}. ${student.student_id}: user_credit_id=${student.user_credit_id}, points=${student.user_credit?.points || 0}`)
      })

      // Check if all students now have unique user_credit_ids
      const finalUserCreditIds = finalStudents.map(s => s.user_credit_id).filter(Boolean)
      const finalUniqueUserCreditIds = [...new Set(finalUserCreditIds)]
      
      if (finalUniqueUserCreditIds.length === finalStudents.length) {
        console.log('\n🎉 SUCCESS: All students now have individual user_credit records!')
      } else {
        console.log('\n⚠️  WARNING: Some students may still be sharing records')
      }
    }

    console.log('\n📊 Fix Results')
    console.log('================')
    console.log(`✅ Successfully fixed: ${fixedCount} students`)
    console.log(`❌ Errors: ${errors.length} students`)

    if (errors.length > 0) {
      console.log('Details:')
      errors.forEach(({ student, error }) => {
        console.log(`   - ${student}: ${error}`)
      })
    }

    // Sign out
    await supabase.auth.signOut()
    console.log('\n🔓 Signed out successfully')

  } catch (error) {
    console.error('💥 Fix failed:', error.message)
    console.error('Stack trace:', error.stack)
    process.exit(1)
  } finally {
    console.log('\n🎉 Fix completed!')
  }
}

fixSpecificClass()
