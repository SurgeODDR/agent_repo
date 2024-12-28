# Agent Tools Briefing

## Execution Environment

### 1. Local Environment Access
The agent has access to:
- **Workspace Path**: `/Users/olivierdebeufderijcker/Documents/GitHub/agent_repo`
- **Shell**: Uses `/bin/zsh` as the default shell
- **OS**: Runs on darwin 23.5.0 (macOS)

## Available Tools Overview

### 1. File System Operations
The agent can perform various file system operations:

#### File Reading and Search:
- **Semantic Code Search**: Find relevant code snippets using semantic search
- **File Content Reading**: Read file contents with line number precision
- **Directory Listing**: Explore directory contents and structure
- **Fuzzy File Search**: Find files using fuzzy matching against file paths
- **Pattern Search**: Fast text-based regex search using ripgrep

#### File Modifications:
- **File Editing**: Make precise edits to existing files
- **File Creation**: Create new files with specified content
- **File Deletion**: Remove files from the workspace
- **Parallel Editing**: Apply similar edits across multiple files

### 2. Command Execution
The agent can:
- **Run Commands**: Execute terminal commands with user approval
- **Background Tasks**: Run long-running commands in the background
- **Command Safety**: All commands require explicit user approval unless marked as safe

### 3. Code Analysis and Modification
The agent provides:
- **Code Understanding**: Semantic search to find relevant code
- **Code Editing**: Make precise, contextual code changes
- **Batch Operations**: Apply similar edits across multiple files
- **Error Recovery**: Smart reapplication of edits if needed

## Tool Details

### 1. Search and Navigation
- **Semantic Search**: Find code based on meaning rather than exact matches
- **Grep Search**: Find exact text or regex patterns (max 50 matches)
- **File Search**: Fuzzy file path matching (max 10 results)
- **Directory Listing**: Explore codebase structure

### 2. File Operations
- **Read Files**: View file contents with line precision (max 250 lines per view)
- **Edit Files**: Make precise code changes with context
- **Delete Files**: Remove files with safety checks
- **Parallel Edits**: Apply similar changes across multiple files (max 50 files)

### 3. Command Execution
- **Command Running**: Execute shell commands with approval
- **Background Processing**: Long-running task support
- **Safety Controls**: User approval required for most commands

## Best Practices

1. **File Operations**
   - Provide sufficient context when reading files
   - Use semantic search for understanding code
   - Utilize parallel edits for consistent changes
   - Verify file contents before modifications

2. **Command Execution**
   - Always explain command purpose
   - Use background processing for long tasks
   - Append `| cat` for pager commands
   - Respect user approval requirements

3. **Search Operations**
   - Use semantic search for concept finding
   - Use grep for exact pattern matching
   - Combine search tools for better results
   - Target specific directories when possible

## Limitations

1. **Technical Constraints**
   - 250 lines maximum per file read
   - 50 matches maximum for grep search
   - 10 results maximum for file search
   - 50 files maximum for parallel edits

2. **Safety Considerations**
   - Most commands require user approval
   - File deletions have safety checks
   - Limited to workspace directory
   - No direct system file access

## Security Considerations
The agent operates with:
- Controlled file system access
- Command execution safeguards
- User approval requirements
- Workspace isolation