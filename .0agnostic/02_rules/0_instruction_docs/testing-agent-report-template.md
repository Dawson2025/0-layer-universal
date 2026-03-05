---
resource_id: "c697a56b-1b3c-4bfa-a473-9e142319ff56"
resource_type: "rule"
resource_name: "testing-agent-report-template"
---
# Testing Report Template
*Standard Template for Testing Agent Reports*

**Purpose**: Use this template to report testing results to Development Agents.

---

## 📋 **Testing Report Template**

```markdown
# Testing Report - [FEATURE/FIX NAME]

**Date**: [YYYY-MM-DD]
**Testing Agent**: [Your ID/Name]
**Development Agent**: [Their ID/Name]
**Handoff Document**: [Link to handoff document]

---

## 📊 **Executive Summary**

**Status**: ✅ APPROVED / ⚠️ NEEDS REVIEW / ❌ REQUIRES FIXES

**Key Metrics**:
- Tests Created: [X] tests
- Tests Passing: [X]/[Y] ([Z]%)
- Code Coverage: [X]% (Min: 80%, Target: 95%)
- Execution Time: [X] seconds
- Issues Found: [X] critical, [Y] warnings

**Recommendation**: [Ready for merge / Needs fixes / Blocked]

---

## ✅ **Test Results**

### Overall Test Status
| Category | Total | Passing | Failing | Coverage |
|----------|-------|---------|---------|----------|
| Unit Tests | X | X | 0 | XX% |
| Integration Tests | Y | Y | 0 | XX% |
| E2E Tests | Z | Z | 0 | XX% |
| **TOTAL** | **XX** | **XX** | **0** | **XX%** |

### Test Execution Summary
```
✅ All tests passing: XX/XX (100%)
✅ Code coverage: XX% (exceeds minimum 80%)
✅ No warnings or errors
✅ Execution time: X.X seconds (under 60s limit)
```

---

## 🧪 **Tests Created**

### Unit Tests (X tests created)

#### Happy Path Tests
1. ✅ `test_function_with_valid_input_returns_expected`
   - **Purpose**: Verify function handles valid input correctly
   - **Coverage**: Lines 10-25 in module.py
   - **Status**: PASS

2. ✅ `test_function_with_different_scenarios_works`
   - **Purpose**: Test various valid input scenarios
   - **Coverage**: Lines 26-40 in module.py
   - **Status**: PASS

#### Error Handling Tests
3. ✅ `test_function_with_invalid_input_raises_error`
   - **Purpose**: Verify proper error handling
   - **Coverage**: Lines 41-50 in module.py
   - **Status**: PASS

4. ✅ `test_function_with_missing_data_returns_error`
   - **Purpose**: Test missing data scenarios
   - **Coverage**: Lines 51-60 in module.py
   - **Status**: PASS

#### Edge Case Tests
5. ✅ `test_function_with_empty_input_handles_gracefully`
   - **Purpose**: Test edge case handling
   - **Coverage**: Lines 61-70 in module.py
   - **Status**: PASS

[... list all unit tests ...]

### Integration Tests (Y tests created)

1. ✅ `test_api_endpoint_creates_resource_successfully`
   - **Purpose**: Test API endpoint integration
   - **Coverage**: API route + database interaction
   - **Status**: PASS

2. ✅ `test_api_endpoint_validates_input_correctly`
   - **Purpose**: Test input validation in API
   - **Coverage**: Validation layer + API route
   - **Status**: PASS

[... list all integration tests ...]

### E2E Tests (Z tests created)

1. ✅ `test_complete_user_workflow_end_to_end`
   - **Purpose**: Test complete user journey
   - **Coverage**: Full workflow from login to completion
   - **Status**: PASS

[... list all E2E tests ...]

---

## 📈 **Coverage Analysis**

### Coverage by Module
| Module | Lines | Covered | Coverage | Status |
|--------|-------|---------|----------|--------|
| services/feature.py | 150 | 145 | 97% | ✅ Excellent |
| utils/helpers.py | 80 | 72 | 90% | ✅ Good |
| models/data.py | 60 | 50 | 83% | ⚠️ Acceptable |
| **TOTAL** | **290** | **267** | **92%** | **✅ Good** |

### Uncovered Code Analysis

**Lines Not Covered**:
- `services/feature.py:145-150` - Rare error handling edge case
  - **Reason**: Extremely unlikely scenario (< 0.01% probability)
  - **Risk**: Low - logging only, no business logic
  - **Recommendation**: Optional - add if time permits

- `models/data.py:55-60` - Legacy fallback code
  - **Reason**: Deprecated code path for backwards compatibility
  - **Risk**: Medium - will be removed in next major version
  - **Recommendation**: Consider adding test before removal

### Coverage Trends
```
Previous Coverage: 85%
Current Coverage:  92%
Change:           +7% ✅ Improvement
```

---

## 🐛 **Issues Found**

### Critical Issues (Must Fix Before Merge)
None found ✅

### Medium Priority Issues (Should Fix Soon)
None found ✅

### Low Priority Issues / Warnings
None found ✅

### Code Quality Observations
1. **Observation**: All functions have proper error handling
2. **Observation**: Input validation is comprehensive
3. **Observation**: Code is well-structured and testable

---

## 🎯 **Test Quality Assessment**

### Test Quality Metrics
- ✅ All tests follow AAA pattern
- ✅ All tests have descriptive names
- ✅ All assertions include clear error messages
- ✅ Tests are independent and repeatable
- ✅ No hard-coded values
- ✅ Proper use of fixtures and mocking

### Test Performance
- Average unit test execution: X.XX ms
- Average integration test execution: XX.X ms
- Average E2E test execution: X.XX seconds
- Total suite execution: X.X seconds ✅ (under 60s limit)

---

## 💡 **Recommendations**

### For Immediate Action
1. ✅ All tests pass - ready for merge
2. ✅ Coverage exceeds minimum - no action needed
3. ✅ No critical issues - safe to deploy

### For Future Consideration
1. Consider adding performance tests for large datasets
2. Consider adding concurrency tests for multi-user scenarios
3. Consider adding security tests for authentication endpoints

### Technical Debt
- None identified ✅

---

## 📚 **Test Documentation**

### Test Files Created
```
tests/unit/test_feature_module.py (X tests)
tests/integration/test_feature_api.py (Y tests)
tests/e2e/test_feature_workflow.py (Z tests)
```

### Test Data / Fixtures Added
```
tests/fixtures/feature_data.py
tests/conftest.py (updated)
```

### Configuration Changes
```
pytest.ini (updated markers)
.coveragerc (no changes)
```

---

## ✅ **Approval Decision**

### Approval Criteria Checklist
- [X] All tests pass (100% pass rate)
- [X] Coverage ≥ 80% (achieved: XX%)
- [X] No critical issues found
- [X] Test quality meets standards
- [X] Execution time acceptable
- [X] Documentation complete

### Final Decision

**STATUS**: ✅ **APPROVED FOR MERGE**

**Rationale**:
All tests pass successfully with XX% coverage (exceeds minimum 80% requirement). No critical issues found. Test quality is excellent. Ready for merge and deployment.

**Conditions**:
None - unconditional approval ✅

---

## 📝 **Additional Notes**

[Any additional observations, context, or information for the Development Agent]

---

## 🔗 **References**

- Handoff Document: [Link]
- Test Files: [Links to test files]
- Coverage Report: [Link to HTML coverage report]
- CI/CD Build: [Link if applicable]

---

**Testing Complete**: [Date and Time]
**Report Generated By**: Testing Agent
**Next Steps**: Development Agent can merge changes

---

*This report confirms that comprehensive testing has been completed and all quality standards have been met.*
```

---

## 🎨 **Report Variations**

### **Variation 1: Tests Failing**

```markdown
## ✅ **Approval Decision**

**STATUS**: ❌ **REQUIRES FIXES**

**Issues Found**: 3 tests failing

**Details**:
1. `test_function_with_edge_case_fails` - AssertionError
   - **Expected**: Empty list
   - **Actual**: None
   - **Fix**: Add null check before processing

2. `test_api_endpoint_validation_fails` - ValidationError
   - **Expected**: 400 Bad Request
   - **Actual**: 500 Internal Server Error
   - **Fix**: Improve error handling in validation layer

3. `test_integration_database_fails` - DatabaseError
   - **Expected**: Record created
   - **Actual**: Connection timeout
   - **Fix**: Check database connection pooling

**Required Actions**:
1. Fix the 3 failing tests
2. Re-run test suite
3. Request new testing review

**Estimated Fix Time**: 2-4 hours
```

### **Variation 2: Low Coverage**

```markdown
## ✅ **Approval Decision**

**STATUS**: ⚠️ **NEEDS REVIEW - LOW COVERAGE**

**Coverage**: 65% (below minimum 80%)

**Uncovered Code**:
- `services/feature.py:50-80` - Main business logic (30 lines)
- `utils/validation.py:20-35` - Input validation (15 lines)

**Required Actions**:
1. Add unit tests for uncovered business logic
2. Add integration tests for validation layer
3. Aim for 80%+ coverage before merge

**Recommended Tests to Add**:
1. `test_main_business_logic_with_various_inputs`
2. `test_validation_handles_all_input_types`
3. `test_edge_cases_in_processing_logic`

**Estimated Time**: 3-5 hours to reach 80% coverage
```

---

## 📊 **Quick Status Indicators**

Use these emoji status indicators for quick scanning:

**Overall Status**:
- ✅ **APPROVED** - All green, ready to merge
- ⚠️ **NEEDS REVIEW** - Some issues, but not blocking
- ❌ **REQUIRES FIXES** - Critical issues, must fix before merge

**Metric Status**:
- ✅ **Excellent** - Exceeds target (> 95%)
- ✅ **Good** - Meets target (80-95%)
- ⚠️ **Acceptable** - Meets minimum (70-80%)
- ❌ **Insufficient** - Below minimum (< 70%)

---

**Template Version**: 1.0
**Last Updated**: January 24, 2025
**Maintained By**: Universal Documentation Team
