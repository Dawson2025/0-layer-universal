#!/usr/bin/env python3
# resource_id: "3b1418ca-6b07-4e5c-993b-2e247aeeb077"
# resource_type: "document"
# resource_name: "test_user_story_traceability"
"""
User Story Traceability Validator

This test ensures that all user stories have corresponding test coverage
and that all referenced test files and MCP scripts actually exist.
"""

import json
import os
import sys
from pathlib import Path
import pytest

# Get project root
PROJECT_ROOT = Path(__file__).parent.parent
MATRIX_PATH = PROJECT_ROOT / "layer_1_group/layer_1_99_stages/stage_1_07_testing/.0agnostic/05_handoff_documents/01_incoming/01_from_above/user_story_test_matrix.json"
USER_STORIES_PATH = PROJECT_ROOT / "layer_1_group/layer_1_99_stages/stage_1_06_development/.0agnostic/01_knowledge/legacy_status_progress/1_status_progress_docs/for_ai/requirements/USER_STORIES.md"


def load_matrix():
    """Load the user story test matrix."""
    if not MATRIX_PATH.exists():
        pytest.fail(f"User story test matrix not found at {MATRIX_PATH}")
    
    with open(MATRIX_PATH) as f:
        return json.load(f)


def extract_user_stories_from_doc():
    """Extract all user story IDs from USER_STORIES.md"""
    if not USER_STORIES_PATH.exists():
        pytest.fail(f"USER_STORIES.md not found at {USER_STORIES_PATH}")
    
    story_ids = []
    with open(USER_STORIES_PATH) as f:
        for line in f:
            # Match "### US-XXX:" or "### CLOUD-XXX:"
            if line.startswith("### US-") or line.startswith("### CLOUD-"):
                # Extract story ID (e.g., "US-001" from "### US-001: Title")
                story_id = line.split(":")[0].replace("### ", "").strip()
                story_ids.append(story_id)
    
    return story_ids


def test_matrix_file_exists():
    """Verify the user story test matrix file exists."""
    assert MATRIX_PATH.exists(), f"User story test matrix not found at {MATRIX_PATH}"


def test_all_mcp_scripts_exist():
    """Verify all MCP scripts referenced in the matrix actually exist."""
    matrix = load_matrix()
    missing_scripts = []
    
    for category in matrix["categories"]:
        mcp_scripts = category.get("mcp_scripts")
        if mcp_scripts is None:
            continue
        
        if isinstance(mcp_scripts, dict):
            for mode, script_path in mcp_scripts.items():
                full_path = PROJECT_ROOT / script_path
                if not full_path.exists():
                    missing_scripts.append({
                        "category": category["id"],
                        "mode": mode,
                        "path": script_path
                    })
        elif isinstance(mcp_scripts, str):
            full_path = PROJECT_ROOT / mcp_scripts
            if not full_path.exists():
                missing_scripts.append({
                    "category": category["id"],
                    "path": mcp_scripts
                })
    
    if missing_scripts:
        error_msg = "Missing MCP scripts:\n"
        for item in missing_scripts:
            error_msg += f"  - {item['category']}: {item['path']}\n"
        pytest.fail(error_msg)


def test_all_pytest_tests_exist():
    """Verify all pytest test files referenced in the matrix actually exist."""
    matrix = load_matrix()
    missing_tests = []
    
    for category in matrix["categories"]:
        pytest_tests = category.get("pytest_tests", [])
        
        for test_path in pytest_tests:
            full_path = PROJECT_ROOT / test_path
            if not full_path.exists():
                missing_tests.append({
                    "category": category["id"],
                    "path": test_path
                })
    
    if missing_tests:
        error_msg = "Missing pytest test files:\n"
        for item in missing_tests:
            error_msg += f"  - {item['category']}: {item['path']}\n"
        pytest.fail(error_msg)


def test_all_user_stories_have_category():
    """Verify all user stories from USER_STORIES.md are mapped to at least one category."""
    matrix = load_matrix()
    doc_stories = set(extract_user_stories_from_doc())
    
    # Build set of all stories mentioned in matrix
    mapped_stories = set()
    for category in matrix["categories"]:
        for story_id in category.get("user_stories", []):
            mapped_stories.add(story_id)
    
    # Find unmapped stories
    unmapped = doc_stories - mapped_stories
    
    if unmapped:
        error_msg = f"User stories without test mapping ({len(unmapped)}):\n"
        for story_id in sorted(unmapped):
            error_msg += f"  - {story_id}\n"
        pytest.fail(error_msg)


def test_all_categories_have_coverage():
    """Verify all categories have either MCP scripts or pytest tests (or both)."""
    matrix = load_matrix()
    categories_without_coverage = []
    
    for category in matrix["categories"]:
        mcp_scripts = category.get("mcp_scripts")
        pytest_tests = category.get("pytest_tests", [])
        
        has_mcp = mcp_scripts is not None and (
            (isinstance(mcp_scripts, dict) and len(mcp_scripts) > 0) or
            (isinstance(mcp_scripts, str) and len(mcp_scripts) > 0)
        )
        has_pytest = len(pytest_tests) > 0
        
        if not has_mcp and not has_pytest:
            categories_without_coverage.append(category["id"])
    
    if categories_without_coverage:
        error_msg = "Categories without any test coverage:\n"
        for cat_id in categories_without_coverage:
            error_msg += f"  - {cat_id}\n"
        pytest.fail(error_msg)


def test_matrix_schema_valid():
    """Verify the matrix has required schema fields."""
    matrix = load_matrix()
    
    assert "$schema" in matrix, "Matrix missing $schema field"
    assert "description" in matrix, "Matrix missing description field"
    assert "categories" in matrix, "Matrix missing categories field"
    assert isinstance(matrix["categories"], list), "categories must be a list"
    
    # Check each category has required fields
    for i, category in enumerate(matrix["categories"]):
        assert "id" in category, f"Category {i} missing 'id' field"
        assert "name" in category, f"Category {i} missing 'name' field"
        assert "user_stories" in category, f"Category {i} missing 'user_stories' field"
        assert isinstance(category["user_stories"], list), f"Category {i} 'user_stories' must be a list"


def test_no_duplicate_story_mappings():
    """Verify no user story is mapped to multiple categories."""
    matrix = load_matrix()
    story_to_categories = {}
    
    for category in matrix["categories"]:
        for story_id in category.get("user_stories", []):
            if story_id not in story_to_categories:
                story_to_categories[story_id] = []
            story_to_categories[story_id].append(category["id"])
    
    duplicates = {story: cats for story, cats in story_to_categories.items() if len(cats) > 1}
    
    if duplicates:
        error_msg = "User stories mapped to multiple categories:\n"
        for story_id, categories in duplicates.items():
            error_msg += f"  - {story_id}: {', '.join(categories)}\n"
        pytest.fail(error_msg)


def test_report_coverage_summary():
    """Generate a summary report of test coverage (informational, doesn't fail)."""
    matrix = load_matrix()
    doc_stories = set(extract_user_stories_from_doc())
    
    # Count mapped stories
    mapped_stories = set()
    for category in matrix["categories"]:
        for story_id in category.get("user_stories", []):
            mapped_stories.add(story_id)
    
    # Count coverage types
    categories_with_mcp = 0
    categories_with_pytest = 0
    categories_with_both = 0
    
    for category in matrix["categories"]:
        mcp_scripts = category.get("mcp_scripts")
        pytest_tests = category.get("pytest_tests", [])
        
        has_mcp = mcp_scripts is not None and (
            (isinstance(mcp_scripts, dict) and len(mcp_scripts) > 0) or
            (isinstance(mcp_scripts, str) and len(mcp_scripts) > 0)
        )
        has_pytest = len(pytest_tests) > 0
        
        if has_mcp:
            categories_with_mcp += 1
        if has_pytest:
            categories_with_pytest += 1
        if has_mcp and has_pytest:
            categories_with_both += 1
    
    # Print summary
    print("\n" + "="*60)
    print("USER STORY TEST COVERAGE SUMMARY")
    print("="*60)
    print(f"Total user stories documented: {len(doc_stories)}")
    print(f"User stories mapped: {len(mapped_stories)} ({len(mapped_stories)*100//len(doc_stories)}%)")
    print(f"User stories unmapped: {len(doc_stories) - len(mapped_stories)}")
    print(f"\nTotal test categories: {len(matrix['categories'])}")
    print(f"Categories with MCP E2E tests: {categories_with_mcp}")
    print(f"Categories with pytest tests: {categories_with_pytest}")
    print(f"Categories with both: {categories_with_both}")
    print("="*60 + "\n")
    
    # This test always passes - it's just informational
    assert True


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v", "--tb=short"])

