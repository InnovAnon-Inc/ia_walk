#! /usr/bin/env python
# cython: language_level=3
# distutils: language=c++

"""Async os.walk()"""

import asyncio
from pathlib           import Path
from typing            import List, Tuple, Union

import aiofiles
import aiofiles.os
import aioshutil
from structlog         import get_logger
from typing_extensions import AsyncGenerator

logger = get_logger()

async def walk(directory:Union[str,Path])->AsyncGenerator[Tuple[str,List[str],List[str]],None]:
    """
    Asynchronously walks a directory tree, similar to os.walk.

    Args:
        directory (str or Path): The root directory to walk.

    Yields:
        tuple: A tuple containing (root, dirs, files) for each directory
               in the tree.
               - root (str): The name of the current directory.
               - dirs (list): A list of names of subdirectories in root.
               - files (list): A list of names of non-directory entries
                               in root.
    """
    await logger.adebug('walk(directory=%s)', directory, )
    async def _walk(current_dir:Path)->AsyncGenerator[Tuple[str,List[str],List[str]],None]:
        try:
            entries:List[str]  = await aiofiles.os.listdir(str(current_dir))

            dirs   :List[str]  = []
            files  :List[str]  = []
            for entry in entries:
                entry_path :Path = current_dir / entry
                # Check if entry is a directory asynchronously
                if await aiofiles.os.path.isdir(str(entry_path)):
                    dirs.append(entry)
                else:
                    files.append(entry)

            # Yield the results for the current directory
            yield str(current_dir), dirs, files

            # Recursively traverse subdirectories
            for dir_name in dirs:
                subdir_path:Path = current_dir / dir_name
                async for root, subdirs, subfiles in _walk(subdir_path):
                    yield root, subdirs, subfiles

        except OSError as e:
            print(f"Error accessing directory {current_dir}: {e}")

    async for result in _walk(Path(directory)):
        yield result

async def walk_files(directory:Union[str,Path])->AsyncGenerator[Tuple[str,str],None]:
    async for root, dirs, files in walk(directory):
        for file in files:
            yield root, file

async def walk_dirs(directory:Union[str,Path])->AsyncGenerator[Tuple[str,str],None]:
    async for root, dirs, files in walk(directory):
        for dir in dirs:
            yield root, dir

__author__:str = 'InnovAnon, Inc.' # NOQA
