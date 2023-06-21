## This is why you should not use pip freeze

Imagine that you are working on a project that requires 5 dependencies: dep1, dep2, dep3, dep4, and dep5.

The reaction that most people will have when generating the dependencies file is to use the following magic command:

```bash
pip freeze > requirements.txt
```

### But how can this be an issue?

pip freeze is only for ```pip install```:

It is only aware of the packages installed using the pip install command.

This means that any packages installed using a different approach such as peotry, setuptools, condaetc. won’t be
included in the final requirements.txt file.

### Pipreqs — a better alternative

**pipreqs** starts by scanning all the python files (.py) in your project, then generates the requirements.txt file
based on the import statements in each python file of the project.

Also, it tackles all the issues faced when using pip freeze.

```bash
pip install pipreqs
```

Once you have installed the library, you just need to provide the root location of your project and run this command to
generate the **requirements.txt** file of the project.

```bash
pipreqs
```

Sometimes you might want to update the requirement file.

In this case, you need to use the ```--force``` option to force the regeneration of the file.
