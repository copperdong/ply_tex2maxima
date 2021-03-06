# tex2maxima_lexer.py   Author: Akira Hakuta, Date: 2017/07/19
# python.exe tex2maxima_lexer.py

from ply import lex

# List of token names.
tokens = ('EXPONENT', 'FACTORIAL', 'MULT', 'DIV', 'PLUS', 'MINUS',
        'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN','UB', 'LBRACKET','RBRACKET','COMMA',
        'LPIPE', 'RPIPE',
        'PI', 'IMAGINARY_UNIT', 'NAPIER_CONSTANT', 
        'NN_FLOAT', 'GREEK_CH', 'DGREEK_CH', 'DX', 'NN_INTEGER','ALPHABET',
        'LIM', 'INFTY', 'TO', 'DIFF',       
        'F_FRAC', 'F_SQRT',  'F_TRIG','F_TRIG_CAR', 'F_LOG','F_LOG_UB','F_SUM', 'F_INT', 'F_SEQ_TERM', 'F_GAMMA', 'F_ZETA',
        'COMBI_PERMU',
        'EQUAL', 'RELATION',
        'FUNCTION',)

# Define `t_ignore` to ignore unnecessary characters between tokens, such as whitespaces.
t_ignore = " \t"
  

# Define functions representing regular expression rules for each token.
# The name of functions must be like `t_<token_name>`.
# All tokens defined by functions are added in the same order as they appear in the lexer file.


def t_EXPONENT(t):
    r'\^'
    return t
    
 
def t_FACTORIAL(t):
    r'!'
    return t    


def t_MULT(t):
    r'\*|\\times|\\cdot'
    return t


def t_DIV(t):
    r'\\div'
    return t  
 
    
def t_PLUS(t):
    r'\+' 
    return t


def t_MINUS(t):
    r'\-'
    return t


def t_LBRACE(t):
    r'\{'
    return t


def t_RBRACE(t):
    r'\}'
    return t
   
    
def t_LPAREN(t):
    r'\(|\\left\('
    return t


def t_RPAREN(t):
    r'\)|\\right\)'
    return t

def t_LBRACKET(t):
    r'\['
    return t

def t_RBRACKET(t):
    r'\]'
    return t


def t_LPIPE(t):
    r'\\left\|'
    return t
    
def t_RPIPE(t):
    r'\\right\|'
    return t    
 
    
def t_COMMA(t):
    r','
    return t
    
def t_PI(t):
    r'\\ppi'
    return t
 
    
def t_IMAGINARY_UNIT(t):
    r'\\ii'
    return t
 
    
def t_NAPIER_CONSTANT(t):
    r'\\ee'
    return t  


def t_F_GAMMA(t):
    r'\\Gamma\(|\\Gamma\\left\('
    return t
 
    
def t_F_ZETA(t):
    r'\\zeta\(|\\zeta\\left\('
    return t
           
def t_GREEK_CH(t):
    r'%alpha|%beta|%gamma|%theta|%omega'
    return t


def t_DGREEK_CH(t):
    r'd%alpha|d%beta|d%Gamma|d%theta|d%omega'
    return t
    
    
def t_DX(t):
    r'd[a-z]'
    return t
  
    
def t_NN_FLOAT(t):
    r'\d*\.\d+'
    return t
  
    
def t_NN_INTEGER(t):
    r'\d+'
    return t  
 
      
def t_F_SEQ_TERM(t):
    r'[a-z]_'
    return t
    
def t_FUNCTION(t):
    r'f\(|g\('
    return t
 
        
def t_ALPHABET(t):
    r'[a-zA-Z]'
    return t


def t_DIFF(t):
    r'\\frac\{d|\\dfrac\{d'
    return t    
 
 
def t_F_FRAC(t):
    r'\\frac|\\dfrac'
    return t
 
         
def t_F_SQRT(t):
    r'\\sqrt'
    return t
 
        
def t_F_TRIG_CAR(t):
    r'\\sin\^|\\cos\^|\\tan\^'
    return t

    
def t_F_TRIG(t):
    r'\\sin|\\cos|\\tan'
    return t
 
    
def t_F_LOG_UB(t):
    r'\\log_'
    return t

    
def t_F_LOG(t):
    r'\\log'
    return t


def t_UB(t):
    r'_'
    return t   
 
    
def t_F_SUM(t):
    r'\\sum'
    return t

def t_LIM(t):
    r'\\lim'
    return t


def t_INFTY(t):
    r'\\infty'
    return t
 
    
def t_TO(t):
    r'\\to'
    return t 
    
def t_F_INT(t):
    r'\\int'
    return t
 
    
def t_COMBI_PERMU(t):
    r'\\C|\\P'
    return t
    
    


def t_EQUAL(t):
    r'='
    return t
 
    
def t_RELATION(t):
    r'>|<|\\geqq|\\leqq'
    return t
    



# To count correct line number
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    # return None, so this newlines will not be in the parsed token list.


# Special function for error handling
def t_error(t):
    print("illegal character '%s'" % (t.value[0]))
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

def test_lexer(input_string):
    lexer.input(input_string)
    result = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        result = result + [(tok.value,tok.type)]
    return result

if __name__ == '__main__':    
    print(test_lexer('2^3'))
    print(test_lexer('0.5 \\times 3 \\cdot 4 \\div 5'))
    print(test_lexer('2*a*b^2*c^3'))
    print(test_lexer('2ab^2c^3'))
    print(test_lexer('123.456'))
    print(test_lexer('%alpha%beta%gamma%theta%omega'))
    print(test_lexer('\\sqrt{3x}'))
    print(test_lexer('\\frac{2}{3}'))
    print(test_lexer('\\ee^{\\ppi\\ii}'))
    print(test_lexer('\\sin {x} \\cos {x} \\tan {x}'))
    print(test_lexer('\\sin {x} + \\cos {x} + \\tan {x}'))
    print(test_lexer('\\sin^{2}{x} \\cos^{2}{x} \\tan^{2}{x}'))#\\sin^k x, \\cos^{10} x bad 
    print(test_lexer('\\sin^{3}{x} + \\cos^{3}{x} + \\tan^{3}{x}'))  
    print(test_lexer('\\log{\\ee^3}'))#\\log \\ee^3 bad
    print(test_lexer('\\log_{2}{8}'))#\\log_2 8 bad 
    print(test_lexer('\\frac{d}{dx}{x^3}'))
    print(test_lexer('\\int{\\sin^{2}{x} dx}'))
    print(test_lexer('\\int_{1}^{3}{(x-1)(x-3)^2 dx}')) 
    print(test_lexer('\\sum_{k=1}^{n}{k^3}'))
    print(test_lexer('\\lim_{x \\to -\\infty}{(\\sqrt{x^2+3x}+x)}'))
    print(test_lexer('12a_{n+1}-35a_{n}'))
    print(test_lexer('2x^2+3x+4=0'))
    print(test_lexer('x^2-3x-4 \\leqq 0'))
    print(test_lexer('\\left| \\left| 3-\\ppi \\right|-1\\right|'))
    print(test_lexer('10!'))
    print(test_lexer('_{5}\\C_{2}'))
    print(test_lexer('_{5}\\P_{2}'))    
    print(test_lexer('2x+3y=4,3x-2y=5'))
    print(test_lexer('f(x)g(x)'))
    print(test_lexer('\\Gamma(x)'))
    print(test_lexer('\\zeta(x)'))
     
    
