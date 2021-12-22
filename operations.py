import math as m

class Calculator:

    @classmethod
    def checking(cls, args):
        special_char = ['\u00F7', 'x', '\u221A']
        data = ''
        for simb in args:
            if simb in special_char:
                match simb:
                    case 'x':
                        simb = simb.replace('x', '*')
                    case '\u00F7':
                        simb = simb.replace('\u00F7', '/')
                    case '\u221A':
                        args = args.split("\u221A")
                        return (args, True)
            data += simb
        return data

    @classmethod
    def operaciones(cls, operation):
        sty = type(operation)
        if sty == str:
            return eval(operation)
        elif sty == tuple:
            return m.sqrt(int(operation[0][1]))

if __name__ == '__main__':
    data = ('\u221A8')
    raiz = Calculator.checking(data)
    print(Calculator.operaciones(raiz))
