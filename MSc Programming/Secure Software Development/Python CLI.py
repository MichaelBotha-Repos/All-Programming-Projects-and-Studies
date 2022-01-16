'''
In this session, you will create a command shell in Python, and then run it and answer questions about it.
Review the blogs at Praka (2018) and Szabo (n.d.) and then create a CLI/ shell that implements the following:

When you enter the command LIST it lists the contents of the current directory
The ADD command will add the following two numbers together and provide the result
The HELP command provides a list of commands available
The EXIT command exits the shell
Add suitable comments to your code and add the program to your e-portfolio.
Be prepared to demonstrate it in the seminar session next week.

Run the shell you have created, try a few commands and then answer the questions below:

What are the two main security vulnerabilities with your shell?
**Injection and Errors

What is one recommendation you would make to increase the security of the shell? **
Input sanitation

Add a section to your e-portfolio that provides a (pseudo)code example of
changes you would make to the shell to improve its security.
***
# Test for only numeric characters   
count = 0
for char in code:
    count += 1
    if (ord(char) < 48 and ord(char) > 57):
        print("Incorrect character used at character", count, "from left side")
        break


'''

""" This program is a command shell with only four commands """

from cmd import Cmd
import os 

class Cli(Cmd):
    """ Cli facilitates the addition of new commands to the Cmd class """

    prompt = 'cmd > '

    def do_add(self, inp):
        """ adds two numbers entered after the command """

        nums = inp.split()
        answer = 0
        for i in nums:
            answer += float(i)
        print(answer)

    def do_exit(self, inp):
        """ Ends program """
        
        print("Session ended")
        return True

    def do_list(self, inp):
        print(os.listdir())
    
        
Cli().cmdloop()
