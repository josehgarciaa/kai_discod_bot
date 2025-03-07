from pathlib import Path
from typing import Dict, Any

from pathlib import Path
from typing import Dict, Any

def read_project(root_dir: str | Path) -> Dict[str, Any]:
    """
    Recursively reads a project's directory structure starting from `root_dir` and
    returns a nested dictionary representing the structure.
    
    Python files (.py) in each directory are read and stored as a dictionary under
    the "files" key, where each file name maps to its content.
    
    In each directory, if a ".crawler_ignore" file exists, any files or directories
    listed there (one per line, ignoring blank lines and comments starting with '#')
    are skipped from the scan.
    
    Args:
        root_dir (str or Path): The root directory of the project to scan.
    
    Returns:
        Dict[str, Any]: A nested dictionary representing the project structure.
    """
    # Convert to Path if necessary
    if not isinstance(root_dir, Path):
        root_dir = Path(root_dir)

    project_dict = {}

    # Build ignore set from .crawler_ignore if it exists
    ignore_set = set()
    ignore_file = root_dir / ".crawler_ignore"
    if ignore_file.is_file():
        for line in ignore_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                ignore_set.add(line)

    # Read Python files in the current directory
    files = {}
    for item in root_dir.iterdir():
        # Skip hidden items and those in the ignore list
        if item.name.startswith('.') or item.name in ignore_set:
            continue
        if item.is_file() and item.suffix == ".py":
            try:
                files[item.name] = item.read_text(encoding="utf-8")
            except Exception as e:
                files[item.name] = f"Error reading file: {e}"
    if files:
        project_dict["files"] = files

    # Recursively process subdirectories
    for item in root_dir.iterdir():
        if item.name.startswith('.') or item.name in ignore_set:
            continue
        if item.is_dir():
            sub_dict = read_project(item)
            if sub_dict:
                project_dict[item.name] = sub_dict

    return project_dict



def write_project(project_dict: Dict[str, Any], dest_dir: Path) -> None:
    """
    Recreates the project structure from `project_dict` into the destination directory
    `dest_dir`. The dictionary format should match that returned by `read_project`.
    
    Files (under the "files" key) are created with their corresponding content, and any
    subdirectories are recursively created.
    
    Args:
        project_dict (Dict[str, Any]): A nested dictionary representing the project structure.
        dest_dir (Path): The destination directory where the project should be recreated.
    
    Raises:
        Exception: If any file or directory cannot be created or written.
    """
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Write files in the current directory
    files = project_dict.get("files", {})
    for file_name, content in files.items():
        file_path = dest_dir / file_name
        try:
            file_path.write_text(content, encoding="utf-8")
        except Exception as e:
            print(f"Error writing file {file_path}: {e}")

    # Process subdirectories recursively
    for key, value in project_dict.items():
        if key == "files":
            continue
        sub_dir = dest_dir / key
        try:
            sub_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating directory {sub_dir}: {e}")
            continue
        if isinstance(value, dict):
            write_project(value, sub_dir)



