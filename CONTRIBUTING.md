# Contributing

## File encoding conventions

Repository configuration files (`.gitignore`, `.gitattributes`, etc.) must be UTF-8 without BOM. UTF-16 with BOM parses correctly with `git check-ignore` but silently breaks `git add -A` directory walks on Windows git, sweeping in supposedly-ignored files.

Before committing changes to config files, verify encoding:

```
python -c "import sys; b=open('.gitignore','rb').read()[:2]; print('UTF-16' if b in (b'\xff\xfe', b'\xfe\xff') else 'OK')"
```

Should print `OK`.
