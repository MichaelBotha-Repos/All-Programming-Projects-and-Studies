"""
Scenario
Your task is to build a multifunction device (MFD) class consisting of methods responsible for document scanning, printing, and sending via fax.
The methods are delivered by the following classes:
scan(), delivered by the Scanner class;
print(), delivered by the Printer class;
send() and print(), delivered by the Fax class.
Each method should print a message indicating its purpose and origin, like:
'print() method from Printer class'
'send() method from Fax class'
create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
on each object call the methods: scan(), print(), send();
observe the output differences. Was the Printer class utilized each time?

"""

class Scanner:
    def scan(self):
        print("scan() from Scanner")

class Printer:
    def print2(self):
        print("print() from printer")

class Fax:
    def send(self):
        print("send() from Fax")
    def print2(self):
        print("print() from Fax")

class MFD_SPF(Scanner, Printer, Fax):
    pass
class MFD_SFP(Scanner, Fax, Printer):
    pass

mfd1 = MFD_SPF()
mfd2 = MFD_SFP()

mfd1.scan()
mfd1.print2()
mfd1.send()

mfd2.scan()
mfd2.print2()
mfd2.send()