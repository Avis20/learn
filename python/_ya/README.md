

```
python/_ya$ find . -type f | egrep '*.py$' | egrep -v 'template|main|tmp' | wc -l
28
```

```
leetcode$ find . -type f | egrep '*.py$' | egrep -v 'template|main|tmp' | wc -l
11
```
