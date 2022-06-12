# Adding an external library as git submodule to the project

```
git submodule add git@github.com:dparniewicz-pa/libproj.git
git submodule init
git commit -a -m "Adding libproj as submodule"
git push
```
A new file `.gitmodules` is created.

# Commit changes to the submodule project
After making code changes in `rootproj/libproj/libproj/greeting.py`
commit changes to subproject:
```
cd libproj
git remote get-url origin
git status
git commit -a -m "libproject update"
git push
```
However, the main `rootproj` repository still points to old version of the `libproj`. 
`rootproj` need to be updated to point a newest version of `libproj`:
```
cd ..
git status
git remote get-url origin
git commit -a -m "Update to newest libproj"
git push
```

# Investigate which submodules were changed and need be commited

One of difficulties working with submodules is proper management of changes in each of submodules (especially if there is more of them).
We can detect changes in submodule using: 
```
git status
```
In order to get more detailed info about changes:
```
git submodule foreach --recursive git status
```
When it is required to go manually to each submodule and commit changes or create a script doint that.

# Update to the latest version of the submodule project

If someone made change in `libproj` then it is nice to update the submodule:
```
cd libproj
git pull
git log
```
and we have latest version of `libproj` available locally in `rootproj`.

Alternatively, use `git submodule` commands to update all submodules:
```
git submodule update --remote --merge
```

To update that in the remote `rootproj` repository: 
```
cd ..
git commit -a -m "Update to newest libproj"
git push
```

Check to which commit a submodule is pointing:
```
git submodule status
```

# Update to a specific version of the submodule project
To use in the `rootproj` the another version of `libproj` apply any proper git command within the `libproj`.
In example to use older version:
```
cd libproj
git checkout 86553932d12fc98559c988f7b7daefc41e3c6c78
git commit -a -m "Use older libproj version"
git push
```

# Cloning repository with submodules
Optionally can provide how many parallel submodule downloading jobs should be created:
```
git clone --recurse-submodules --jobs 1 git@github.com:dparniewicz-pa/rootproj.git
```

# Update all submodules

Pull changes in `rootproj` togather with changes in all submodules:
```
git pull --recurse-submodules
```
Pull changes only for all submodules:
```
git submodule update --remote
```

# Submodule detached

When updating submodules using:
```
git submodule update --remote
```
then submodule becomes detached from head of the submodule repository.

To correct that
```
cd libproj
git checkout main
```
and use `--merge` or `--rebase` options for `git submodule update`.
More on this problem:
https://stackoverflow.com/questions/18770545/why-is-my-git-submodule-head-detached-from-master


# Git submodule with poetry
Poetry can disover and install dependencies of git submodule `libproj`. All required libraries will be installed in `rootproj`:
```
[tool.poetry.dependencies]
libproj = { path = "./libproj", develop = true }
```
