#check to see if assigned value to variable is the correct

import sys
import pdb

tokenList = []
variableDict = {}
nextTok = None
index = -1
#swap these two below
#edit: swapped
VAL = 0
TYPE = 1


def prog():
    let_in_end()
    
def let_in_end():
    while(index < len(tokenList) - 2):
        if(nextTok=="let"):
            match(nextTok)
            dec_list()
            print variableDict
        elif(nextTok=="in"):
            match(nextTok)
            varType = type()
            progTup = expr(varType)
            if(progTup[TYPE] == 'int'):
                final = (int(progTup[VAL]), progTup[TYPE])
            elif(progTup[TYPE] == 'real'):
                final = (float(progTup[VAL]), progTup[TYPE])
            else:
                sys.exit('ERROR1')
            print final[VAL]
        else:
            lex()

def dec_list():
    while(nextTok != 'in'):
        dec()
    return

#
def dec():
    global variableDict
    varType,varVal = None,None
    varName = nextTok

    lex()

    #read through declerations and insert them into variableDict with VAL and varType
    while(nextTok != ';'):
        if(nextTok==':'):
            match(nextTok)
            varType = type()
        elif(nextTok=='='):
            match(nextTok)
            varVal = expr(varType)


    #Check to see if assigned type is cast right
    '''
    if(varType == 'int'):
        if(isinstance(int(varVal, int) == True):
            variableDict[varName] = (varVal[VAL], varType)
        else:
            sys.exit('ERROR INT')
    elif(varType == 'real'):
        if(isinstance(varType,float) == True):
            variableDict[varName] = (varVal[VAL], varType)
        else:
            sys.exit('ERROR REAL')
    '''
  
   
    variableDict[varName] = (varVal[VAL], varType)
    lex() 
    return

#type check method, return type if 'int' or 'real', return error ifelse 
def type():
    if(nextTok == 'int' or 'real'):
        returnVal = nextTok
        match(nextTok)
        return returnVal
    else:
        sys.exit('ERROR2')

def expr(varType):
    #initialize leftTerm
    total = None
    while(True):
        #CREATE A TOTAL AND A LEFT TERM
        #check to see if there is a rightTerm and compute
        if(nextTok=='+'):
            match(nextTok)
            rightTerm = term(varType)
            if(leftTerm[TYPE] == rightTerm[TYPE]):
                total += rightTerm[VAL]
                varType = leftTerm[TYPE]
            else:
                sys.exit('ERROR3')
        elif(nextTok=='-'):
            match(nextTok)
            rightTerm = term(varType)
            if(leftTerm[TYPE] == rightTerm[TYPE]):
                total -= rightTerm[VAL]
                varType = leftTerm[TYPE]
            else:
                sys.exit('ERROR4')
        else:
            leftTerm = term(varType)
            total = leftTerm[VAL]
        if(nextTok == ')' or nextTok == ';'):
            break

    finalTup = (total, varType)
    return finalTup

def term(varType):
    #initialize leftFact
    leftFact = factor(varType)
    #check to see if there is a rightFact and compute
    if(nextTok=='*'):
        match(nextTok)
        rightFact = factor(varType)
        if(leftFact[TYPE] == rightFact[TYPE]):
            print variableDict
            finalFact = ((leftFact[VAL] * rightFact[VAL]), leftFact[TYPE])
            return finalFact
        else:
            sys.exit('ERROR5')

    elif(nextTok=='/'):
        match(nextTok)
        rightFact = factor(varType)
        if(leftFact[TYPE] == rightFact[TYPE]):
            finalFact = ((leftFact[VAL] / rightFact[VAL]), leftFact[TYPE])
            return finalFact
        else:
            sys.exit('ERROR6')
    return leftFact

def factor(varType):
    
    #initialize retTup 
    retTup = ()

    #check to see if nextTok is paranthesis or variable type
    if(nextTok=='('):
        match(nextTok)
        #this is causing problems with variable type
        exprCheck = expr(varType)
        retTup = (exprCheck[VAL], varType)
        match(')')
   
        
    elif(nextTok=='int' or nextTok=='real'):
        varType=type()
        if(nextTok=='('):
            match(nextTok)
            exprCheck = expr(varType) 
            retTup = (exprCheck[VAL], varType)
    else:
        retTup = (nextTok, varType)
    lex()

    #if factor has a stored value, convert value and return value and varType
    '''old:
    if(retTup[TYPE]=='int'):
        if(retTup[VAL] in variableDict):
            finalTup = (varType, int(variableDict[retTup[VAL]][VAL]))
            print finalTup
            return finalTup
    elif(retTup[TYPE]=='real'):
        if(retTup[VAL] in variableDict):
            finalTup = (varType, float(variableDict[retTup[VAL]][VAL]))
            return finalTup

    return retTup
    '''
    
    #New:
    if(retTup[VAL] in variableDict):    
        if(retTup[TYPE]=='int'):
            #Fix this
            finalTup = (int(variableDict[retTup[VAL]][VAL]), variableDict[retTup[VAL]][TYPE])
            return finalTup
        elif(retTup[TYPE]=='real'):
            finalTup = (float(variableDict[retTup[VAL]][VAL]), variableDict[retTup[VAL]][TYPE])
            return finalTup
    
    return retTup
#match to see if nextTok is correct, if not print error
def match(token):
    if(token==nextTok):
        lex()
    else:
        print token
        sys.exit('ERROR7')
         

#update nextTok and index counter
def lex():
    global index, nextTok

    index += 1
    nextTok = tokenList[index]

#initialze program
def main():
    global tokenList
    file = open('test.txt','r')
    tokenList = file.read().split()
    lex()
    prog()


if __name__=="__main__":
    main()