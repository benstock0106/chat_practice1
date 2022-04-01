
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding ='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None #假如開頭不是人名 person先設定為虛"無"才不會無法執行
    for line in lines:
        if line == 'Lan Lan':
            person = 'Lan Lan'
            continue
        elif line == '你':
            person = '你'
            continue
        if person:
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('lan.txt')
    lines = convert(lines)
    write_file('lan_output.txt', lines)


main() #進入點