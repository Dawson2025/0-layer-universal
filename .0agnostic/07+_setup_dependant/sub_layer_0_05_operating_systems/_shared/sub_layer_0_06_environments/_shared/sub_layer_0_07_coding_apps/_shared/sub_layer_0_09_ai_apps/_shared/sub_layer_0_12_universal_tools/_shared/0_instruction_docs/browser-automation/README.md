---
resource_id: "31a565e9-b40f-4f5c-84a8-a200fe8faa3f"
resource_type: "readme_document"
resource_name: "README"
---
# Browser Automation Framework
*Universal Tool: Intelligent Browser Automation Strategy and Management*

<!-- section_id: "efae591d-81a2-4a5b-8075-538cf6542e0a" -->
## Overview

The Browser Automation Framework provides intelligent selection and management of browser automation tools based on task requirements, performance needs, and context. It supports multiple browser automation tools and automatically selects the optimal one for each specific task.

<!-- section_id: "c445caa1-b654-45c7-aaa3-9bf1836255b3" -->
## Supported Tools

<!-- section_id: "e991767c-49cb-449d-ab77-82ca4a7359f6" -->
### 1. Browser Automation Tool
**MCP Server**: `browser`
**Purpose**: General-purpose browser automation
**Best For**: Simple navigation, form filling, basic interactions

<!-- section_id: "e6ece831-3c11-4075-9a53-e95c58ba50da" -->
### 2. Chrome DevTools MCP
**MCP Server**: `chrome-devtools`
**Purpose**: Chrome-specific debugging and automation
**Best For**: Advanced debugging, performance analysis, Chrome-specific features

<!-- section_id: "65c12125-eec9-4cb1-bb00-6871642351bb" -->
### 3. Playwright MCP
**MCP Server**: `playwright`
**Purpose**: Cross-browser automation and testing
**Best For**: Cross-browser testing, complex interactions, reliable automation

<!-- section_id: "84d88a5a-c8b9-4fc0-afdf-8674f7d866ea" -->
## Tool Selection Strategy

<!-- section_id: "681f51fa-1084-4a0b-8922-9a32481e6f1b" -->
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

<!-- section_id: "87402c55-808d-49d1-b85d-a913b751b32a" -->
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

<!-- section_id: "1bee2451-e219-4248-ac9c-6ae766b1ee53" -->
## Usage

<!-- section_id: "825f720d-7d56-4f23-9d84-9cae2e42ff31" -->
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

<!-- section_id: "e121b81e-ae5a-4c0e-a3f0-fd9bc7611280" -->
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

<!-- section_id: "25652f86-b391-4ed9-a771-95818b1010a4" -->
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

<!-- section_id: "3d1e05dd-b53c-43fb-b2f5-5cba74119ea0" -->
## Tool-Specific Features

<!-- section_id: "bcaefab6-6aab-41cc-a0ec-036c0e4392ce" -->
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

<!-- section_id: "2574e804-f0e9-41fe-aded-54ff7563ea5e" -->
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

<!-- section_id: "1affd766-c17a-4f6d-bd3e-4358ce669c7b" -->
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

<!-- section_id: "b7790f71-b495-4a26-8b61-e3fadbf4c5b9" -->
## Performance Optimization

<!-- section_id: "032c146f-b8f0-4838-ab3c-929f8d514a37" -->
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

<!-- section_id: "0da9e7b9-6250-4d43-afb3-92ad5f07c900" -->
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

<!-- section_id: "f7a3d8e3-7fe4-4490-8371-01ddb0ec134f" -->
## Error Handling and Recovery

<!-- section_id: "3f8759ff-b415-4959-9e11-4f88ed9156cf" -->
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

<!-- section_id: "59a3509d-239d-4070-9434-6d028f042c77" -->
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

<!-- section_id: "a0855010-9327-4970-af6d-a9946d8178ce" -->
## Testing

<!-- section_id: "a19d945c-d487-4bca-8172-f0dd4f7e585f" -->
### Test Suite
```bash
# Run browser automation tests
python3 features/meta-intelligent-orchestration/core/tests/test_browser_automation_strategy.py

# Run tool-specific tests
python3 features/meta-intelligent-orchestration/core/tests/test_playwright_integration.py
python3 features/meta-intelligent-orchestration/core/tests/test_chrome_devtools_integration.py
```

<!-- section_id: "41d0cfc1-5788-405f-8a40-e7b63dd697db" -->
### Test Coverage
- **Unit Tests**: Individual tool testing
- **Integration Tests**: Tool interaction testing
- **Performance Tests**: Tool performance validation
- **Error Handling Tests**: Error recovery testing

<!-- section_id: "8ed5af8d-a1f3-4fec-ac03-694ba7d4d40a" -->
## Integration with Project

<!-- section_id: "702bc8d3-ece7-448d-a5fb-c8bcb8d1d767" -->
### Trickle-Down Integration
- **Level 0**: Universal instructions inform tool design
- **Level 0.75**: Universal tools provide browser automation framework
- **Level 1.5**: Project tools use browser automation for specific tasks
- **Level 2**: Features integrate browser automation for user interactions

<!-- section_id: "89183ba2-7ef8-4277-a39d-285426e44b75" -->
### Project Constitution Compliance
- **Type Safety**: Python type hints throughout
- **Component Reusability**: Modular, reusable browser automation components
- **Clean Architecture**: Clear separation between tool selection and execution
- **Documentation**: Comprehensive documentation for all browser automation features

<!-- section_id: "a1bc1e78-c3c6-4b8e-9088-3991a03c6597" -->
## Future Enhancements

<!-- section_id: "18d15778-ad09-4ce2-ae72-e13109f7b45d" -->
### Planned Features
- **Advanced Tool Selection**: ML-powered tool selection
- **Performance Monitoring**: Real-time performance tracking
- **Custom Tool Support**: Support for custom browser automation tools
- **Cloud Integration**: Cloud-based browser automation

<!-- section_id: "0eccc68c-100d-4915-ba97-cbac1a41c7ee" -->
### Extensibility
- **Plugin Architecture**: Support for custom tool plugins
- **API Integration**: RESTful API for browser automation
- **SDK Development**: Software development kits for tool integration
- **Community Contributions**: Open source tool contributions

<!-- section_id: "cc52eb41-685d-4162-a3ab-c44cff866a33" -->
## Documentation

- [Meta-Intelligent Orchestration Framework](./meta-intelligent-orchestration/README.md)
- [Visual Orchestration Framework](./visual-orchestration/README.md)
- [Project Analysis Framework](./project-analysis/README.md)
- [Efficiency Tips](./EFFICIENCY_TIPS.md) - Learned patterns and best practices for efficient browser automation

---

<!-- section_id: "a648e3de-a80d-4b22-8647-489e3939f499" -->
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
