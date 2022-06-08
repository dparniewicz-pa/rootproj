# Adding an external library as git submodule to the project

```
git submodule add git@github.com:dparniewicz-pa/libproj.git
git submodule init
git commit -a -m "Adding libproj as submodule"
git push
```


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