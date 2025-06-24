# ia_walk

## Overview

The `ia_walk` module provides an asynchronous implementation of the directory traversal functionality similar to Python's built-in `os.walk()`. This module leverages the `aiofiles` library to perform non-blocking file system operations, making it suitable for applications that require efficient I/O operations without blocking the event loop.

### Key Features

- **Asynchronous Directory Traversal**: Walks through a directory tree asynchronously, yielding tuples containing the current directory, subdirectories, and files.
- **Separation of Concerns**: Provides dedicated functions to walk through files and directories separately, enhancing usability and clarity.
- **Error Handling**: Includes basic error handling for directory access issues, ensuring that the traversal process can continue even if some directories are inaccessible.

### Functions

#### `walk(directory: Union[str, Path]) -> AsyncGenerator[Tuple[str, List[str], List[str]], None]`

Asynchronously walks a directory tree, yielding tuples of the current directory, its subdirectories, and files.

- **Args**:
  - `directory`: The root directory to walk, specified as a string or `Path` object.
  
- **Yields**:
  - A tuple containing:
    - `root`: The name of the current directory.
    - `dirs`: A list of names of subdirectories in the current directory.
    - `files`: A list of names of non-directory entries in the current directory.

#### `walk_files(directory: Union[str, Path]) -> AsyncGenerator[Tuple[str, str], None]`

Asynchronously walks through the specified directory and yields tuples of the current directory and each file within it.

#### `walk_dirs(directory: Union[str, Path]) -> AsyncGenerator[Tuple[str, str], None]`

Asynchronously walks through the specified directory and yields tuples of the current directory and each subdirectory within it.

### Usage

To use the `ia_walk` module, you can run the following example:

```python
import asyncio
from ia_walk import walk_files

async def main():
    async for root, file in walk_files('/path/to/directory'):
        print(f'Directory: {root}, File: {file}')

if name == 'main':
    asyncio.run(main())
```

### Installation

To use this module, ensure you have the `aiofiles` library installed. You can install it using pip:

```bash
pip install aiofiles
```

## Author

This module is developed by InnovAnon, Inc.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

-- you.com
