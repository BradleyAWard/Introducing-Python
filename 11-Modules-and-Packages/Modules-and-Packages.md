## 11) Modules and Packages

In this notebook we will write our own modules and learn how to use others from Python's standard library and other sources. To allow Python applications to scale larger, you can organize modules into file and module hierarchies called packages. A package is a subdirectory that contains `.py` files.

Consider we have a local module with the same name as a standard one; how do we choose the correct one? Python supports absolute or relative import. If you typed `import [name]` for each directory in the search path (found at `sys.path`), Python will look for a file named `name.py` (a module) or a directory named `name` (a package).

- If `name.py` is in the same directory as your calling problem, you can import it relative to your location with `from . import name`.
- If it is in the directory above you use `from .. import name`.
- If it is under a sibling directory called `name_sub` use `from .. name_sub import name`.

The `.` and `..` notation is burrowed from Unix's shorthand for current directory and parent directory.

You can also split a package across directories with namespace packages. Say we want to create a package called `animals` that will contain a Python module for each animal. This might get large over time and you would like to subdivide these by location. One option is to add location subpackages under `animals` and move the existing `.py` module files under them. However, this would break things for other modules that import them. Instead, we can go up a subdirectory and do the following:

- Make new location directories above `animals`.
- Make cousin `animals` under these new parents.
- Move existing modules to their respective directories.

Say we started with the following file layout:

- `animals`
    - `cat.py`
    - `dog.py`
    - `fish.py`

Normal imports of these modules would look like: `from animals import cat, dog, fish`.

Now if we used locations, the files and directories would look like:

- `land`
    - `animals`
        - `cat.py`
        - `dog.py`

- `water`
    - `animals`
        - `fish.py`

You can import the modules as though they were still cohabiting a single directory using `from animals import cat, dog, fish`.