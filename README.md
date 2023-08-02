# deepl_pdf
A program that translates pdf files.

# Usage
First, you need to save your authentication key as auth_key.txt in the top directory of the repository. if you don't have one, you can get from [here](https://www.deepl.com/ja/pro/change-plan?utm_source=github&utm_medium=github-python-readme#developer)

then, run
```
python deepl_pdf input.pdf -o output.pdf -l JA
```
You can specify target language using `-l` option, you can checkout [Deepl API documentation](https://www.deepl.com/docs-api/translating-text/?utm_source=github&utm_medium=github-python-readme) to see your desired language code.

The default target language is japanese.

# Installation
you can use deepl_pdf without install by the command above, but ommit "`python`" part if you install via:
```
pip install -e .
```