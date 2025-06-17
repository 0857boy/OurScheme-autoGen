import sys
import re

def parse_token(token: str) -> str:
    if token == 't' or token == '#t':
        return '#t'
    if token in ('nil', '#f', '()'):
        return 'nil'
    # Integer
    if re.fullmatch(r'[+-]?\d+', token):
        return str(int(token))
    # Float
    if re.fullmatch(r'[+-]?(\d+\.\d*|\d*\.\d+)', token):
        return f"{float(token):.3f}"
    # String
    if len(token) >= 2 and token[0] == '"' and token[-1] == '"':
        inner = ''
        i = 1
        while i < len(token) - 1:
            c = token[i]
            if c == '\\':
                i += 1
                if i >= len(token) - 1:
                    inner += '\\'
                    break
                esc = token[i]
                if esc == 'n':
                    inner += '\n'
                elif esc == 't':
                    inner += '\t'
                elif esc == '"':
                    inner += '"'
                elif esc == '\\':
                    inner += '\\'
                else:
                    inner += '\\' + esc
            else:
                inner += c
            i += 1
        return '"' + inner + '"'
    # Symbol or others
    return token

def main():
    print('Welcome to OurScheme!', end='\r\n')
    print('', end='\r\n')
    lines = sys.stdin.read().splitlines()
    if not lines:
        print('Thanks for using OurScheme!', end='')
        return
    idx = 0
    # first line is test number
    idx += 1
    printed = False
    while idx < len(lines):
        line = lines[idx].rstrip('\n')
        token = line.strip()
        if token == '(exit)':
            print('>', end='\r\n')
            if printed:
                print('Thanks for using OurScheme!', end='\r\n')
            else:
                print('Thanks for using OurScheme!', end='')
            break
        else:
            print('> ' + token, end='\r\n')
            result = parse_token(token)
            sys.stdout.write(result.replace('\n', '\r\n'))
            sys.stdout.write('\r\n')
            sys.stdout.write('\r\n')
            printed = True
        idx += 1

if __name__ == '__main__':
    main()
