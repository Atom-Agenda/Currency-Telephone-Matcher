import re
import io

def patternChecker(expression, content, list_file):
    with io.open(list_file, 'w', encoding='utf-8') as f:
        for k in range(0, len(expression)):
            for (i, j) in enumerate(re.finditer(expression[k], content,
                                    re.M)):
                pattern = j.group(0)
                f.write(pattern + '\n')
    

def phoneGenerator(basePath, content):
    expression = "(\d{3})(-\.\s)?(\d{3})[-\.\s]?(\d{4})|(\(\d{3}\))\s*((\d{3})[-\.\s]?(\d{4})|(\d{3})[-\.\s]?(\d{4}))"
    patternChecker(expression, content, basePath + "telephone_output.txt")

if __name__ == "__main__":
    basePath = "/Users/arunimamitra/Downloads/hw2/"
    fileName = "test_dollar_phone_corpus.txt"
    with io.open(basePath+fileName,encoding='utf-8') as f:
        content = f.read()
        phoneGenerator(basePath, content)
