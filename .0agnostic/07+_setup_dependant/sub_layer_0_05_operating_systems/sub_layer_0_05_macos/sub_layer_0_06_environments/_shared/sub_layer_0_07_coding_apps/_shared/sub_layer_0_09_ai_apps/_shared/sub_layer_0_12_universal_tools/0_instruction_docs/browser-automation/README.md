---
resource_id: "6792b120-337b-48e0-99f8-9f9924d1b1d4"
resource_type: "readme
document"
resource_name: "README"
---
# Browser Automation Framework
*Universal Tool: Intelligent Browser Automation Strategy and Management*

<!-- section_id: "6e73c14f-4ca4-4e87-8c9a-276c3437e350" -->
## Overview

The Browser Automation Framework provides intelligent selection and management of browser automation tools based on task requirements, performance needs, and context. It supports multiple browser automation tools and automatically selects the optimal one for each specific task.

<!-- section_id: "99de8316-4dfb-44b5-b504-aa8a742c7205" -->
## Supported Tools

<!-- section_id: "afec1d49-3740-48b3-9124-1a9b50421243" -->
### 1. Browser Automation Tool
**MCP Server**: `browser`
**Purpose**: General-purpose browser automation
**Best For**: Simple navigation, form filling, basic interactions

<!-- section_id: "5d5762a5-d4e6-43c8-8fd2-c37c87d10151" -->
### 2. Chrome DevTools MCP
**MCP Server**: `chrome-devtools`
**Purpose**: Chrome-specific debugging and automation
**Best For**: Advanced debugging, performance analysis, Chrome-specific features

<!-- section_id: "312c7079-1155-47cb-bb54-cc2623ff5c58" -->
### 3. Playwright MCP
**MCP Server**: `playwright`
**Purpose**: Cross-browser automation and testing
**Best For**: Cross-browser testing, complex interactions, reliable automation

<!-- section_id: "80ec02b9-8e23-4c28-94f9-2355f719a610" -->
## Tool Selection Strategy

<!-- section_id: "47902927-0268-45c9-b429-f365dce5ddcb" -->
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

<!-- section_id: "743567b3-e766-4a49-a8d8-93ff79cd404c" -->
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

<!-- section_id: "46e1e003-0e19-4009-9310-3cb1ebf829f2" -->
## Usage

<!-- section_id: "ea4aa445-256f-4333-9b33-e25c962586ed" -->
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

<!-- section_id: "ecd95914-77cd-45e1-aea6-8348a561d843" -->
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

<!-- section_id: "9c821fa5-8528-4c5a-8cfc-42798e46d8c3" -->
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

<!-- section_id: "61e85ad8-3994-40af-baaa-a25e18183f76" -->
## Tool-Specific Features

<!-- section_id: "7867fe46-71b1-49d8-9462-63d886dd5cc2" -->
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

<!-- section_id: "35c66e9b-5c06-40b8-bd87-130e09f178b7" -->
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

<!-- section_id: "62ea594a-69db-435c-b60a-fe49c1413b05" -->
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

<!-- section_id: "99ad598e-2dda-4968-b332-fb9c572b734a" -->
## Performance Optimization

<!-- section_id: "4eeab4a3-f917-4146-98bb-2162c00b64c3" -->
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

<!-- section_id: "8d00f7e8-251d-43d7-a871-be61afbf1c8f" -->
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

<!-- section_id: "ff550cfb-e6a5-46a6-8b3f-af7061a6e776" -->
## Error Handling and Recovery

<!-- section_id: "28688a7f-d1ec-4fe0-9f26-0b5813138318" -->
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

<!-- section_id: "227c9569-a633-4da8-9211-6313a8e474b4" -->
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

<!-- section_id: "de9bb4b6-6648-4ade-aaae-a005473c9a9d" -->
## Testing

<!-- section_id: "ffdf8b62-ce92-4ad7-ae92-4870805c8509" -->
### Test Suite
```bash
# Run browser automation tests
python3 features/meta-intelligent-orchestration/core/tests/test_browser_automation_strategy.py

# Run tool-specific tests
python3 features/meta-intelligent-orchestration/core/tests/test_playwright_integration.py
python3 features/meta-intelligent-orchestration/core/tests/test_chrome_devtools_integration.py
```

<!-- section_id: "9833475f-cde5-4c38-8538-894bac30616d" -->
### Test Coverage
- **Unit Tests**: Individual tool testing
- **Integration Tests**: Tool interaction testing
- **Performance Tests**: Tool performance validation
- **Error Handling Tests**: Error recovery testing

<!-- section_id: "11d7485b-c099-441f-8da3-af4972a554ca" -->
## Integration with Project

<!-- section_id: "26089d11-6a5f-477b-ad67-ce446c872dd5" -->
### Trickle-Down Integration
- **Level 0**: Universal instructions inform tool design
- **Level 0.75**: Universal tools provide browser automation framework
- **Level 1.5**: Project tools use browser automation for specific tasks
- **Level 2**: Features integrate browser automation for user interactions

<!-- section_id: "18e4130f-4ae0-42a5-b563-8abc66d1c15a" -->
### Project Constitution Compliance
- **Type Safety**: Python type hints throughout
- **Component Reusability**: Modular, reusable browser automation components
- **Clean Architecture**: Clear separation between tool selection and execution
- **Documentation**: Comprehensive documentation for all browser automation features

<!-- section_id: "a8250f8e-0474-4c76-96e7-7880e3488411" -->
## Future Enhancements

<!-- section_id: "f9300dc1-35ed-4b0d-bac1-11469ccedb7e" -->
### Planned Features
- **Advanced Tool Selection**: ML-powered tool selection
- **Performance Monitoring**: Real-time performance tracking
- **Custom Tool Support**: Support for custom browser automation tools
- **Cloud Integration**: Cloud-based browser automation

<!-- section_id: "841ab681-b09a-4482-8b62-f82a6669ece1" -->
### Extensibility
- **Plugin Architecture**: Support for custom tool plugins
- **API Integration**: RESTful API for browser automation
- **SDK Development**: Software development kits for tool integration
- **Community Contributions**: Open source tool contributions

<!-- section_id: "ec07554f-746e-4165-a50e-4aba17222cf3" -->
## Documentation

- [Meta-Intelligent Orchestration Framework](./meta-intelligent-orchestration/README.md)
- [Visual Orchestration Framework](./visual-orchestration/README.md)
- [Project Analysis Framework](./project-analysis/README.md)
- [Efficiency Tips](./EFFICIENCY_TIPS.md) - Learned patterns and best practices for efficient browser automation

---

<!-- section_id: "4af7950b-7847-4ea6-8fe5-3812ea5bf517" -->
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
