# Name: Joseph Steeb
# Collaborators: none

from os import openpty
from psItems import Value, ArrayValue, FunctionValue


class Operators:
    def __init__(self):
        # stack variables
        self.opstack = []  # assuming top of the stack is the end of the list
        self.dictstack = []  # assuming top of the stack is the end of the list

        # The builtin operators supported by our interpreter
        self.builtin_operators = {
            'add': self.add,
            'sub': self.sub,
            'mul': self.mul,
            'mod': self.mod,
            'eq': self.eq,
            'lt': self.lt,
            'gt': self.gt,
            'length': self.length,
            'getinterval': self.getinterval,
            'putinterval': self.putinterval,
            'aload': self.aload,
            'astore': self.astore,
            'if': self.psIf,
            'elseif': self.psIfelse,
            'ifelse': self.psIfelse,
            'repeat': self.repeat,
            'dup': self.dup,
            'copy': self.copy,
            'count': self.count,
            'pop': self.pop,
            'clear': self.clear,
            'exch': self.exch,
            'roll': self.roll,
            'stack': self.stack,
            'def': self.psDef,
            'dict': self.psDict,
            'begin': self.begin,
            'end': self.end,
            'forall': self.forall
            # TO-DO in part1
            # include the key value pairs where he keys are the PostScrip opertor names and the values are the function values that implement that operator.
            # Make sure **not to call the functions**
        }
    # -------  Operand Stack Operators --------------
    """
        Helper function. Pops the top value from opstack and returns it.
    """

    def opPop(self):
        if len(self.opstack) > 0:
            return self.opstack.pop(len(self.opstack)-1)
        else:
            print("ERROR, can't pop from empty opstack")
            return None

    """
       Helper function. Pushes the given value to the opstack.
    """

    def opPush(self, value):
        self.opstack.append(value)

    # ------- Dict Stack Operators --------------

    """
       Helper function. Pops the top dictionary from dictstack and returns it.
    """

    def dictPop(self):
        if len(self.dictstack) > 0:
            return self.dictstack.pop(len(self.dictstack) - 1)
        else:
            print("ERROR in, can't pop from empty dictstack")

    """
       Helper function. Pushes the given dictionary onto the dictstack. 
    """

    def dictPush(self, d):
        self.dictstack.append(d)

    """
       Helper function. Adds name:value pair to the top dictionary in the dictstack.
       (Note: If the dictstack is empty, first adds an empty dictionary to the dictstack then adds the name:value to that. 
    """

    def define(self, name, value):
        self.dictstack[len(self.dictstack) - 1][name] = value

    """
       Helper function. Searches the dictstack for a variable or function and returns its value. 
       (Starts searching at the top of the dictstack; if name is not found returns None and prints an error message.
        Make sure to add '/' to the begining of the name.)
    """

    def lookup(self, name):
        name = '/'+name
        for value in reversed(self.dictstack):
            if name in value.keys():
                return value[name]
        print("ERROR: key not found")

    # ------- Arithmetic Operators --------------

    """
       Pops 2 values from opstack; checks if they are numerical (int); adds them; then pushes the result back to opstack. 
    """

    def add(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op1 + op2)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)
        else:
            print("Error: add expects 2 operands")

    """
       Pop 2 values from opstack; checks if they are numerical (int); subtracts them; and pushes the result back to opstack. 
    """

    def sub(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op2 - op1)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)
        else:
            print("Error: add expects 2 operands")

    """
        Pops 2 values from opstack; checks if they are numerical (int); multiplies them; and pushes the result back to opstack. 
    """

    def mul(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op1 * op2)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)
        else:
            print("Error: add expects 2 operands")

    """
        Pops 2 values from stack; checks if they are int values; calculates the remainder of dividing the bottom value by the top one; 
        pushes the result back to opstack.
    """

    def mod(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op2 % op1)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)
        else:
            print("Error: add expects 2 operands")
    # ---------- Comparison Operators  -----------------
    """
       Pops the top two values from the opstack; pushes "True" is they are equal, otherwise pushes "False"
    """

    def eq(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                if op1 == op2:
                    self.opPush(True)
                else:
                    self.opPush(False)
            else:
                if op1 is op2:
                    self.opPush(True)
                else:
                    self.opPush(False)
        else:
            print("Error: add expects 2 operands")
    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is less than the top value, otherwise pushes "False"
    """

    def lt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                if op1 > op2:
                    self.opPush(True)
                else:
                    self.opPush(False)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)
        else:
            print("Error: add expects 2 operands")

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is greater than the top value, otherwise pushes "False"
    """

    def gt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                if op1 < op2:
                    self.opPush(True)
                else:
                    self.opPush(False)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)
        else:
            print("Error: add expects 2 operands")

    # ------- Array Operators --------------
    """ 
       Pops an array value from the operand opstack and calculates the length of it. Pushes the length back onto the opstack.
       The `length` method should support ArrayValue values.
    """

    def length(self):
        self.opPush(len(self.opPop().value))

    """ 
        Pops the `count` (int), an (zero-based) start `index`, and an array constant (ArrayValue) from the operand stack.  
        Pushes the slice of the array of length `count` starting at `index` onto the opstack.(i.e., from `index` to `index`+`count`) 
        If the end index of the slice goes beyond the array length, will give an error. 
    """

    def getinterval(self):
        count = self.opPop()
        index = self.opPop()
        array = self.opPop().value

        if(count + index <= len(array)):
            self.opPush(ArrayValue(array[index:(count + index)]))
        else:
            print("ERROR, index out of bounds")
    """ 
        Pops an array constant (ArrayValue), start `index` (int), and another array constant (ArrayValue) from the operand stack.  
        Replaces the slice in the bottom ArrayValue starting at `index` with the top ArrayValue (the one we popped first). 
        The result is not pushed onto the stack.
        The index is 0-based. If the end index of the slice goes beyond the array length, will give an error. 
    """

    def putinterval(self):
        # TODO this
        array1 = self.opPop()
        index = self.opPop()
        array2 = self.opPop()

        if index > len(array2.value):
            print("ERROR: index out of bounds")
        else:
            array2.value[index:index+len(array1.value)] = array1.value

    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pushes all values in the array constant to the opstack in order (the first value in the array should be pushed first). 
        Pushes the orginal array value back on to the stack. 
    """

    def aload(self):
        array = self.opPop()
        for val in array.value:
            self.opPush(val)
        self.opPush(array)

    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pops as many elements as the length of the array from the operand stack and stores them in the array constant. 
        The value which was on the top of the opstack will be the last element in the array. 
        Pushes the array value back onto the operand stack. 
    """

    def astore(self):
        array = self.opPop().value
        for i in reversed(range(len(array))):
            array[i] = self.opPop()
        self.opPush(ArrayValue(array))

    # ------- Stack Manipulation and Print Operators --------------

    """
       This function implements the Postscript "pop operator". Calls self.opPop() to pop the top value from the opstack and discards the value. 
    """

    def pop(self):
        self.opPop()

    """
       Prints the opstack. The end of the list is the top of the stack. 
    """

    def stack(self):
        for i in range(len(self.opstack), 0, -1):
            print(self.opstack[i])

    """
       Copies the top element in opstack.
    """

    def dup(self):
        temp = self.opPop()
        self.opPush(temp)
        self.opPush(temp)

    """
       Pops an integer count from opstack, copies count number of values in the opstack. 
    """

    def copy(self):
        count = self.opPop()
        length = len(self.opstack)
        if count < length:
            self.opstack += self.opstack[length-count:length]
        else:
            print("ERROR: copy count longer than stack")

    """
        Counts the number of elements in the opstack and pushes the count onto the top of the opstack.
    """

    def count(self):
        self.opPush(len(self.opstack))

    """
       Clears the opstack.
    """

    def clear(self):
        self.opstack = []

    """
       swaps the top two elements in opstack
    """

    def exch(self):
        one = self.opPop()
        two = self.opPop()
        self.opPush(one)
        self.opPush(two)

    """
        Implements roll operator.
        Pops two integer values (m, n) from opstack; 
        Rolls the top m values in opstack n times (if n is positive roll clockwise, otherwise roll counter-clockwise)
    """
    # TODO this

    def roll(self):
        n = self.opPop()
        m = self.opPop()
        arr = [None]*m

        if(n > 0):
            for i in range(n):
                arr[0] = self.opstack[len(self.opstack)-1]
                for j in range(m-1):
                    arr[len(arr) - 1 - j] = self.opstack[len(self.opstack) - 2 - j]
                self.opstack[len(self.opstack) - m:] = arr
        else:
            n = abs(n)
            for i in range(n):
                arr[m-1] = self.opstack[len(self.opstack)-m]
                for j in range(m-1):
                    arr[j] = self.opstack[len(self.opstack)-m+j+1]
                self.opstack[len(self.opstack) - m:] = arr

    """
       Pops an integer from the opstack (size argument) and pushes an  empty dictionary onto the opstack.
    """

    def psDict(self):
        self.opPop()
        self.opPush({})

    """
       Pops the dictionary at the top of the opstack; pushes it to the dictstack.
    """

    def begin(self):
        self.dictPush(self.opPop())

    """this
       Removes the top dictionary from dictstack.
    """

    def end(self):
        self.dictPop()

    """
       Pops a name and a value from opstack, adds the name:value pair to the top dictionary by calling define.  
    """

    def psDef(self):
        if len(self.dictstack) < 1:
            self.dictstack.append({})
        self.dictstack[len(self.dictstack) - 1][self.opPop()] = self.opPop()

    # ------- if/ifelse Operators --------------
    """
       Implements if operator. 
       Pops the `ifbody` and the `condition` from opstack. 
       If the condition is True, evaluates the `ifbody`.  
    """

    def psIf(self):
        body = self.opPop()
        condition = self.opPop()

        if condition:
            body.apply(self)
        # TO-DO in part2

    """
       Implements ifelse operator. 
       Pops the `elsebody`, `ifbody`, and the condition from opstack. 
       If the condition is True, evaluate `ifbody`, otherwise evaluate `elsebody`. 
    """

    def psIfelse(self):
        elsebody = self.opPop()
        ifbody = self.opPop()
        condition = self.opPop()

        if condition:
            ifbody.apply(self)
        else:
            elsebody.apply(self)
        # TO-DO in part2

    # ------- Loop Operators --------------
    """
       Implements repeat operator.   
       Pops the `loop_body` (FunctionValue) and loop `count` (int) arguments from opstack; 
       Evaluates (applies) the `loopbody` `count` times. 
       Will be completed in part-2. 
    """

    def repeat(self):
        loop_body = self.opPop()
        count = self.opPop()

        for i in range(count):
            loop_body.apply(self)
        # TO-DO in part2

    """
       Implements forall operator.   
       Pops a `codearray` (FunctionValue) and an `array` (ArrayValue) from opstack; 
       Evaluates (applies) the `codearray` on every value in the `array`.  
       Will be completed in part-2. 
    """

    def forall(self):
        codearray = self.opPop()
        array = self.opPop().value

        for element in array:
            self.opPush(element)
            codearray.apply(self)

        # TO-DO in part2

    # --- used in the setup of unittests
    def clearBoth(self):
        self.opstack[:] = []
        self.dictstack[:] = []
