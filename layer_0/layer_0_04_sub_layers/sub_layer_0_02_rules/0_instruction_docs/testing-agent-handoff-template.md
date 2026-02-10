# Testing Agent Handoff Template
*Standard Template for Development-to-Testing Handoffs*

**Purpose**: This template ensures consistent, complete handoffs from Development Agents to Testing Agents.

---

## 📋 **Handoff Document**

Copy this template when handing off to a Testing Agent:

```markdown
# Testing Request - [FEATURE/FIX NAME]

**Date**: [YYYY-MM-DD]
**Development Agent**: [Your Name/ID]
**Change Type**: [ ] New Feature  [ ] Bug Fix  [ ] Refactoring  [ ] API Change  [ ] Other

---

## 1️⃣ **What Changed**

### Files Modified
```
[List all modified files with line numbers if applicable]
- file1.py (lines 10-50)
- file2.py (new file)
- file3.html (lines 20-30)
```

### Description of Changes
[Detailed description of what was changed and why]

**Before**:
[Brief description of previous behavior]

**After**:
[Brief description of new behavior]

### Dependencies Changed
- [ ] New dependencies added: [list]
- [ ] Existing dependencies updated: [list]
- [ ] Database schema changed: [describe]
- [ ] API contracts changed: [describe]

---

## 2️⃣ **Testing Scope Required**

### Test Types Needed
- [ ] **Unit Tests** - Test individual functions/methods
  - Priority: High/Medium/Low
  - Estimated tests needed: [number]

- [ ] **Integration Tests** - Test component interactions
  - Priority: High/Medium/Low
  - Estimated tests needed: [number]

- [ ] **E2E Tests** - Test complete user workflows
  - Priority: High/Medium/Low
  - Estimated tests needed: [number]

- [ ] **Regression Tests** - Prevent bug recurrence
  - Priority: High/Medium/Low
  - Estimated tests needed: [number]

### Specific Test Requirements
[List specific scenarios that must be tested]
1. Test scenario 1
2. Test scenario 2
3. Test scenario 3

---

## 3️⃣ **Critical User Paths**

### Primary User Workflow
```
1. User does X
2. System responds with Y
3. User does Z
4. Expected outcome: [describe]
```

### Alternative Workflows
```
1. Alternative path 1: [describe]
2. Alternative path 2: [describe]
```

### Edge Cases to Consider
- Edge case 1: [describe]
- Edge case 2: [describe]
- Edge case 3: [describe]

---

## 4️⃣ **Acceptance Criteria**

Tests must verify:
- [ ] Criterion 1: [specific measurable criterion]
- [ ] Criterion 2: [specific measurable criterion]
- [ ] Criterion 3: [specific measurable criterion]
- [ ] Criterion 4: [specific measurable criterion]

### Performance Requirements
- Response time: < [X] ms
- Throughput: > [Y] requests/second
- Memory usage: < [Z] MB

### Security Requirements
- [ ] Input validation
- [ ] Authentication/Authorization
- [ ] Data encryption
- [ ] SQL injection prevention
- [ ] XSS prevention

---

## 5️⃣ **Known Risks and Concerns**

### Potential Issues
1. **Risk 1**: [Description]
   - Likelihood: High/Medium/Low
   - Impact: High/Medium/Low
   - Mitigation: [How to handle]

2. **Risk 2**: [Description]
   - Likelihood: High/Medium/Low
   - Impact: High/Medium/Low
   - Mitigation: [How to handle]

### Areas of Uncertainty
- Uncertainty 1: [describe what's unclear]
- Uncertainty 2: [describe what's unclear]

### Technical Debt
- [ ] This change introduces technical debt: [describe]
- [ ] This change reduces technical debt: [describe]

---

## 6️⃣ **Testing Environment Requirements**

### Environment Setup
- [ ] Database: [SQLite/Firebase/Other]
- [ ] External Services: [list any external dependencies]
- [ ] Test Data: [describe required test data]
- [ ] Configuration: [special configuration needed]

### Prerequisites
```bash
# Commands to set up test environment
pip install -r requirements-test.txt
pytest tests/ --setup-show
```

---

## 7️⃣ **Documentation and References**

### Related Documentation
- User story: [link or reference]
- Design document: [link or reference]
- API specification: [link or reference]

### Related Code
- Similar implementation: [file:line]
- Existing tests to reference: [test file]

### External Resources
- Stack Overflow: [links if relevant]
- Library documentation: [links if relevant]

---

## 8️⃣ **Manual Testing Performed**

### What I Tested
- [ ] Happy path: [describe results]
- [ ] Error handling: [describe results]
- [ ] Edge cases: [describe results]

### What I Didn't Test
- [ ] Scenario 1: [reason not tested]
- [ ] Scenario 2: [reason not tested]

---

## 9️⃣ **Success Criteria for Testing Agent**

Testing Agent should:
1. ✅ Create comprehensive test plan
2. ✅ Implement all required tests
3. ✅ Achieve minimum 80% code coverage (target: 95%)
4. ✅ All tests pass successfully
5. ✅ No warnings or errors in test output
6. ✅ Test execution time < 60 seconds
7. ✅ Provide detailed testing report

---

## 🔟 **Questions for Testing Agent**

[Any specific questions or concerns you want the Testing Agent to address]

1. Question 1?
2. Question 2?
3. Question 3?

---

## 📝 **Additional Notes**

[Any other information the Testing Agent should know]

---

## ✅ **Handoff Checklist**

Before handing off to Testing Agent, verify:
- [ ] All sections above are completed
- [ ] Code is committed to version control
- [ ] Manual testing has been performed
- [ ] Documentation is updated
- [ ] No obvious bugs or issues remain
- [ ] Change is ready for comprehensive testing

---

**Handoff Complete**: [YES/NO]
**Ready for Testing Agent**: [YES/NO]

---

*This handoff ensures the Testing Agent has all information needed to create comprehensive, effective tests.*
```

---

## 🎯 **Quick Start Examples**

### **Example 1: New Feature Handoff**

```markdown
# Testing Request - User Authentication System

**Date**: 2025-01-24
**Development Agent**: Development Agent Alpha
**Change Type**: [X] New Feature

## 1️⃣ What Changed

### Files Modified
- services/auth.py (new file, 250 lines)
- app.py (lines 45-80, added auth routes)
- templates/login.html (new file)
- templates/register.html (new file)

### Description of Changes
Implemented complete user authentication system with:
- User registration with email validation
- Login with session management
- Password hashing using bcrypt
- JWT token generation
- Logout functionality

**Before**: No authentication, all pages publicly accessible
**After**: Protected routes require authentication, secure session management

### Dependencies Changed
- [X] New dependencies added: flask-login, bcrypt, pyjwt
- [ ] Database schema changed: Added users table

## 2️⃣ Testing Scope Required

### Test Types Needed
- [X] Unit Tests - Priority: High, ~15 tests
  - Password hashing/verification
  - Token generation/validation
  - Session management logic

- [X] Integration Tests - Priority: High, ~10 tests
  - Login API endpoint
  - Register API endpoint
  - Protected route access

- [X] E2E Tests - Priority: Medium, ~5 tests
  - Complete registration workflow
  - Complete login workflow
  - Access protected page after login

## 3️⃣ Critical User Paths

### Primary User Workflow
1. User visits /register
2. Fills out registration form (email, password)
3. Submits form
4. System creates account and redirects to login
5. User logs in with credentials
6. System creates session and redirects to dashboard

### Edge Cases
- Duplicate email registration attempt
- Invalid email format
- Weak password
- Wrong login credentials
- Session expiration

## 4️⃣ Acceptance Criteria

- [ ] Passwords are hashed (never stored in plaintext)
- [ ] Sessions expire after 24 hours
- [ ] Invalid login attempts are logged
- [ ] Email validation prevents invalid formats
- [ ] Protected routes redirect to login when unauthenticated

## ✅ Handoff Checklist
- [X] All sections completed
- [X] Code committed
- [X] Manual testing done
- [X] Ready for Testing Agent
```

### **Example 2: Bug Fix Handoff**

```markdown
# Testing Request - Fix Word Deletion Bug

**Date**: 2025-01-24
**Development Agent**: Development Agent Beta
**Change Type**: [X] Bug Fix

## 1️⃣ What Changed

### Files Modified
- services/word_manager.py (lines 120-135)

### Description of Changes
Fixed bug where deleting a word didn't remove associated phonemes from the database, causing orphaned data.

**Before**: Word deleted but phonemes remained in database
**After**: Word deletion cascades to remove all associated phonemes

### Bug Details
- **Bug ID**: #423
- **Severity**: Medium
- **Impact**: Database bloat from orphaned records

## 2️⃣ Testing Scope Required

### Test Types Needed
- [X] Unit Tests - Priority: High, ~3 tests
  - Test delete_word() function

- [X] Integration Tests - Priority: High, ~2 tests
  - Test database cascade deletion

- [X] Regression Tests - Priority: Critical, ~2 tests
  - Ensure bug doesn't recur

## 3️⃣ Critical User Paths

### Primary Workflow
1. User creates word with phonemes
2. User deletes word
3. System removes word AND all associated phonemes

### Edge Cases
- Delete word with no phonemes
- Delete word with many phonemes
- Delete non-existent word

## 4️⃣ Acceptance Criteria

- [ ] Word deletion removes all associated phonemes
- [ ] Database integrity maintained after deletion
- [ ] No orphaned records in database
- [ ] Error handling for non-existent words

## ✅ Handoff Complete: YES
```

---

## 📊 **Handoff Quality Checklist**

Use this to evaluate handoff quality:

| Criterion | Met? | Notes |
|-----------|------|-------|
| **Completeness**: All sections filled | ☐ | |
| **Clarity**: Changes clearly described | ☐ | |
| **Specificity**: Specific test requirements listed | ☐ | |
| **Context**: Sufficient context provided | ☐ | |
| **Edge Cases**: Edge cases identified | ☐ | |
| **Acceptance Criteria**: Measurable criteria defined | ☐ | |
| **Risks**: Known risks documented | ☐ | |

**Overall Quality**: ☐ Excellent  ☐ Good  ☐ Needs Improvement

---

**Template Version**: 1.0
**Last Updated**: January 24, 2025
**Maintained By**: Universal Documentation Team
