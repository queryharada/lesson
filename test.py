def index():
    with open("./templates/index.html", mode='r', encoding='utf-8') as f:
        try:
            linesIndex = f.readlines()
        except:
            import traceback
            traceback.print_exc()

    with open("./templates/javascriptTest.js", mode='r', encoding='utf-8') as f:
        linesScript = '<script>' + f.read() + '</script>'

    lines = ''
    for line in linesIndex:
        if 'javascriptTest.js' in line:
            lines += linesScript
        else:
            lines += line

    return lines


if __name__ == "__main__":
    print(index())
