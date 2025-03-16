import subprocess

process = subprocess.Popen(
    ['ddgs', 'chat'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True 
)

process.stdin.write("1\n")
process.stdin.write("Что нового?\n")
process.stdin.write("Как называется столица Франции?\n")
process.stdin.flush()

# Прочитай ответ
output, errors = process.communicate() 
print("Ответ AI:", output)

input()
