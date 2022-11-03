import re
import io
def patternChecker(expression, content, list_file):

    with io.open(list_file, 'w', encoding='utf-8') as f:
        for k in range(0, len(expression)):
            for (i, j) in enumerate(re.finditer(expression[k], content,
                                    re.M)):
                pattern = j.group(0)
                f.write(pattern + '\n')
                
def dollarGenerator(basePath, content):
    expression = []
    expression.append("(\$[\s]?(\d+(\,\d{3})*(\.\d+)?)[\s]?(thousand|million|billion|trillion)?)")
    expression.append("((\d+(\,\d{3})*(\.\d+)?)[\s]?(thousand|million|billion|trillion)?[\s]?(dollars|dollar|cents|cent))")
    expression.append("((\d+(\,\d{3})*(\.\d+)?)[\s]?(thousand|million|billion|trillion)?[\s]?(dollars|dollar)[\s]?(and)[\s]?(\d+)[\s]?(thousand|million|billion|trillion)?(cents|cent))")
    expression.append("((one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand)[\s])+(million|billion|trillion)?[\s]?(dollars|dollar|cents|cent)")
    
    patternChecker(expression, content, basePath + "dollar_output.txt")

    
if __name__ == "__main__":
    basePath = "/Users/arunimamitra/Downloads/hw2/"
    fileName = "test_dollar_phone_corpus.txt"
    with io.open(basePath+fileName,encoding='utf-8') as f:
        content = f.read()
        dollarGenerator(basePath,content)
