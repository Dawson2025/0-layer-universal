---
resource_id: "2b5d6bdb-f1c5-43e5-857c-0a9200b55b6a"
resource_type: "readme
document"
resource_name: "README"
---
# Browser Automation Framework
*Universal Tool: Intelligent Browser Automation Strategy and Management*

<!-- section_id: "7c284462-07bf-48f4-a085-51f27c8b52e9" -->
## Overview

The Browser Automation Framework provides intelligent selection and management of browser automation tools based on task requirements, performance needs, and context. It supports multiple browser automation tools and automatically selects the optimal one for each specific task.

<!-- section_id: "7b827dd9-0004-4215-ad98-0fff29b00b11" -->
## Supported Tools

<!-- section_id: "aedf85f9-49b0-4daf-bb32-01cbc4d38595" -->
### 1. Browser Automation Tool
**MCP Server**: `browser`
**Purpose**: General-purpose browser automation
**Best For**: Simple navigation, form filling, basic interactions

<!-- section_id: "b949c47c-9f53-4d4f-b367-2cc3b5a6d167" -->
### 2. Chrome DevTools MCP
**MCP Server**: `chrome-devtools`
**Purpose**: Chrome-specific debugging and automation
**Best For**: Advanced debugging, performance analysis, Chrome-specific features

<!-- section_id: "f0dbf91b-a9cb-4102-ba89-8c9c8234ebf5" -->
### 3. Playwright MCP
**MCP Server**: `playwright`
**Purpose**: Cross-browser automation and testing
**Best For**: Cross-browser testing, complex interactions, reliable automation

<!-- section_id: "eccac81d-1ae3-43a6-ab14-3123979c6d49" -->
## Tool Selection Strategy

<!-- section_id: "5bafe9a9-df57-408a-9328-d9d3e2131d57" -->
### Selection Criteria

#### 1. Task Complexity
- **Simple Tasks**: Browser Automation Tool
- **Medium Tasks**: Chrome DevTools MCP
- **Complex Tasks**: Playwright MCP

#### 2. Browser Requirements
- **Chrome Only**: Chrome DevTools MCP
- **Cross-Browser**: Playwright MCP
- **Any Browser**: Browser Automation Tool

#### 3. Performance Requirements
- **High Performance**: Chrome DevTools MCP
- **Balanced**: Playwright MCP
- **Simple**: Browser Automation Tool

#### 4. Debugging Needs
- **Advanced Debugging**: Chrome DevTools MCP
- **Basic Debugging**: Playwright MCP
- **No Debugging**: Browser Automation Tool

<!-- section_id: "05070e1b-727a-4ec6-9dac-95951c9607c9" -->
### Selection Algorithm

```python
def select_browser_tool(task_requirements: Dict[str, Any]) -> str:
    complexity = task_requirements.get('complexity', 'simple')
    browser_requirement = task_requirements.get('browser', 'any')
    performance_requirement = task_requirements.get('performance', 'balanced')
    debugging_requirement = task_requirements.get('debugging', False)
    
    # Chrome-specific tasks
    if browser_requirement == 'chrome':
        if debugging_requirement or performance_requirement == 'high':
            return 'chrome-devtools'
        else:
            return 'playwright'
    
    # Cross-browser tasks
    if browser_requirement == 'cross-browser':
        return 'playwright'
    
    # Simple tasks
    if complexity == 'simple' and not debugging_requirement:
        return 'browser'
    
    # Default to Playwright for reliability
    return 'playwright'
```

<!-- section_id: "47b30a74-0b38-4502-a7a0-725a6ad8aae1" -->
## Usage

<!-- section_id: "17f456af-3207-4bf2-bc5b-cf90d1948ec2" -->
### Basic Tool Selection
```python
from features.meta_intelligent_orchestration.core.browser_automation_strategy import BrowserAutomationStrategy

# Create strategy
strategy = BrowserAutomationStrategy()

# Select tool for task
task_requirements = {
    'complexity': 'medium',
    'browser': 'cross-browser',
    'performance': 'balanced',
    'debugging': False
}

selected_tool = strategy.select_tool(task_requirements)
print(f"Selected tool: {selected_tool}")
```

<!-- section_id: "fa5e6f5e-b9d7-4e7a-8150-c82e06cb0f77" -->
### Tool Execution
```python
# Execute task with selected tool
result = await strategy.execute_task(
    tool=selected_tool,
    task="navigate_to_firebase_console",
    parameters={
        'url': 'https://console.firebase.google.com',
        'wait_for': 'Firebase Console'
    }
)
```

<!-- section_id: "7a05e550-b4db-4701-ab2c-48a8b569528e" -->
### Fallback Strategy
```python
# Execute with fallback
result = await strategy.execute_with_fallback(
    primary_tool='playwright',
    fallback_tool='chrome-devtools',
    task="configure_firebase_auth",
    parameters={'project_id': 'my-project'}
)
```

<!-- section_id: "9cce6d49-04a5-4b26-a540-8373b4aa8ea7" -->
## Tool-Specific Features

<!-- section_id: "b0adf4b8-3b5d-4a9e-8d7c-e595b5c20f11" -->
### Browser Automation Tool
```python
# Simple navigation
await browser.navigate('https://example.com')

# Form filling
await browser.fill_form([
    {'selector': '#email', 'value': 'user@example.com'},
    {'selector': '#password', 'value': 'password123'}
])

# Clicking
await browser.click('#submit-button')
```

<!-- section_id: "4d3ea71e-71f5-48f3-a1b5-aab5a041452e" -->
### Chrome DevTools MCP
```python
# Advanced debugging
await chrome_devtools.take_snapshot(verbose=True)
await chrome_devtools.evaluate_script("console.log('Debug info')")

# Performance analysis
await chrome_devtools.performance_start_trace(reload=True, autoStop=True)
await chrome_devtools.performance_stop_trace()

# Network monitoring
requests = await chrome_devtools.list_network_requests()
```

<!-- section_id: "d9932ce0-d7cc-4d59-af9c-394da7cc8dfa" -->
### Playwright MCP
```python
# Cross-browser testing
await playwright.navigate('https://example.com')
await playwright.take_screenshot(filename='page.png')

# Complex interactions
await playwright.click('button[data-testid="submit"]')
await playwright.fill_form([
    {'name': 'email', 'value': 'user@example.com'},
    {'name': 'password', 'value': 'password123'}
])

# Wait for elements
await playwright.wait_for('text=Success')
```

<!-- section_id: "e4c03c3a-c515-458d-bb37-2f47be2bd286" -->
## Performance Optimization

<!-- section_id: "7e853e3b-1ee8-4f06-be72-e3e8daa6ccd6" -->
### Tool Performance Characteristics

#### Browser Automation Tool
- **Speed**: Fast
- **Memory Usage**: Low
- **Reliability**: Medium
- **Features**: Basic

#### Chrome DevTools MCP
- **Speed**: Very Fast
- **Memory Usage**: Medium
- **Reliability**: High
- **Features**: Advanced

#### Playwright MCP
- **Speed**: Medium
- **Memory Usage**: Medium
- **Reliability**: Very High
- **Features**: Comprehensive

<!-- section_id: "4bb740df-1f85-4da3-9450-73e72ba02ea0" -->
### Optimization Strategies

#### 1. Tool Selection Optimization
```python
def optimize_tool_selection(task_requirements: Dict[str, Any]) -> str:
    # Consider task frequency
    if task_requirements.get('frequency') == 'high':
        return 'chrome-devtools'  # Fastest for repeated tasks
    
    # Consider task complexity
    if task_requirements.get('complexity') == 'high':
        return 'playwright'  # Most reliable for complex tasks
    
    # Consider resource constraints
    if task_requirements.get('memory_limit') == 'low':
        return 'browser'  # Lowest memory usage
    
    return 'playwright'  # Default to most reliable
```

#### 2. Task Batching
```python
# Batch similar tasks for efficiency
async def batch_tasks(tasks: List[Dict[str, Any]]) -> List[Any]:
    # Group tasks by tool
    tool_groups = group_tasks_by_tool(tasks)
    
    results = []
    for tool, tool_tasks in tool_groups.items():
        # Execute tasks in batch
        tool_results = await execute_tool_batch(tool, tool_tasks)
        results.extend(tool_results)
    
    return results
```

#### 3. Caching and Reuse
```python
# Cache browser instances
browser_cache = {}

async def get_browser_instance(tool: str) -> Any:
    if tool not in browser_cache:
        browser_cache[tool] = await create_browser_instance(tool)
    return browser_cache[tool]
```

<!-- section_id: "3d2d7766-ac9b-4e06-afb1-9f1514fa2401" -->
## Error Handling and Recovery

<!-- section_id: "a138976f-5c07-4568-b7c1-2b22e5e8575e" -->
### Error Types

#### 1. Tool Unavailable
```python
try:
    result = await execute_with_tool('playwright', task)
except ToolUnavailableError:
    # Fallback to alternative tool
    result = await execute_with_tool('chrome-devtools', task)
```

#### 2. Task Failure
```python
try:
    result = await execute_task(tool, task)
except TaskFailureError as e:
    # Retry with different strategy
    result = await retry_with_different_strategy(task, e)
```

#### 3. Browser Crash
```python
try:
    result = await execute_task(tool, task)
except BrowserCrashError:
    # Restart browser and retry
    await restart_browser(tool)
    result = await execute_task(tool, task)
```

<!-- section_id: "de7c1b5b-3c33-465b-b47c-c57963b13624" -->
### Recovery Strategies

#### 1. Automatic Fallback
```python
async def execute_with_automatic_fallback(task: str) -> Any:
    tools = ['playwright', 'chrome-devtools', 'browser']
    
    for tool in tools:
        try:
            return await execute_task(tool, task)
        except Exception as e:
            logger.warning(f"Tool {tool} failed: {e}")
            continue
    
    raise AllToolsFailedError("All browser automation tools failed")
```

#### 2. Retry with Backoff
```python
async def execute_with_retry(task: str, max_retries: int = 3) -> Any:
    for attempt in range(max_retries):
        try:
            return await execute_task(tool, task)
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)  # Exponential backoff
```

<!-- section_id: "748773ad-b564-4e33-ac41-06f7d2c6f1eb" -->
## Testing

<!-- section_id: "5f142d24-1b54-4742-a98f-21f1a24510d6" -->
### Test Suite
```bash
# Run browser automation tests
python3 features/meta-intelligent-orchestration/core/tests/test_browser_automation_strategy.py

# Run tool-specific tests
python3 features/meta-intelligent-orchestration/core/tests/test_playwright_integration.py
python3 features/meta-intelligent-orchestration/core/tests/test_chrome_devtools_integration.py
```

<!-- section_id: "780cd8c7-5cd5-4ec9-a3d9-8489a07c239e" -->
### Test Coverage
- **Unit Tests**: Individual tool testing
- **Integration Tests**: Tool interaction testing
- **Performance Tests**: Tool performance validation
- **Error Handling Tests**: Error recovery testing

<!-- section_id: "4d85c08d-d435-40e6-83a5-0de81298262b" -->
## Integration with Project

<!-- section_id: "084479af-37d2-49d4-96d3-f7645f4d2560" -->
### Trickle-Down Integration
- **Level 0**: Universal instructions inform tool design
- **Level 0.75**: Universal tools provide browser automation framework
- **Level 1.5**: Project tools use browser automation for specific tasks
- **Level 2**: Features integrate browser automation for user interactions

<!-- section_id: "69c4ac59-6ac3-4b68-8529-fac69df811f5" -->
### Project Constitution Compliance
- **Type Safety**: Python type hints throughout
- **Component Reusability**: Modular, reusable browser automation components
- **Clean Architecture**: Clear separation between tool selection and execution
- **Documentation**: Comprehensive documentation for all browser automation features

<!-- section_id: "4b19422e-2e08-4f51-be58-298a60fb3382" -->
## Future Enhancements

<!-- section_id: "7bd08ada-849e-4399-8500-629c6988176a" -->
### Planned Features
- **Advanced Tool Selection**: ML-powered tool selection
- **Performance Monitoring**: Real-time performance tracking
- **Custom Tool Support**: Support for custom browser automation tools
- **Cloud Integration**: Cloud-based browser automation

<!-- section_id: "879fc1ee-9374-4af2-a4c1-acd22b16c3e6" -->
### Extensibility
- **Plugin Architecture**: Support for custom tool plugins
- **API Integration**: RESTful API for browser automation
- **SDK Development**: Software development kits for tool integration
- **Community Contributions**: Open source tool contributions

<!-- section_id: "869d6386-3c85-49ff-be9f-cfe2b62a9bbb" -->
## Documentation

- [Meta-Intelligent Orchestration Framework](./meta-intelligent-orchestration/README.md)
- [Visual Orchestration Framework](./visual-orchestration/README.md)
- [Project Analysis Framework](./project-analysis/README.md)
- [Efficiency Tips](./EFFICIENCY_TIPS.md) - Learned patterns and best practices for efficient browser automation

---

<!-- section_id: "607eb6cc-226c-4b89-a3b5-f3edb66cde5f" -->
## Efficiency Tips

For learned patterns, best practices, and efficiency tips discovered during browser automation work, see:

**[EFFICIENCY_TIPS.md](./EFFICIENCY_TIPS.md)**

This document includes:
- Element reference management patterns
- Negative number input handling
- Dialog state management
- Concurrent work strategies
- Session expiration handling
- Input field navigation patterns
- Error recovery patterns
- Tab management best practices
- Performance optimization techniques

---
*This tool is part of the Universal Tools section and can be applied to any project.*
