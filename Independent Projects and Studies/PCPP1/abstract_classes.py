"""
Scenario
You are about to create a multifunction device (MFD) that can scan and print documents;
the system consists of a scanner and a printer;
your task is to create blueprints for it and deliver the implementations;

create an abstract class representing a scanner that enforces the following methods:
scan_document – returns a string indicating that the document has been scanned;
get_scanner_status – returns information about the scanner (max. resolution, serial number)

Create an abstract class representing a printer that enforces the following methods:
print_document – returns a string indicating that the document has been printed;
get_printer_status – returns information about the printer (max. resolution, serial number)

Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
MFD2 – should be a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device;
MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.

Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.

"""

import abc

class Scanner(abc.ABC):

    @abc.abstractmethod
    def __init__(self, sres, ssn):
        self.sres = sres
        self.ssn = ssn

    @abc.abstractmethod
    def scan_document(self):
        return "document scanned"

    @abc.abstractmethod
    def get_scanner_status(self):
        return [self.sres, self.ssn]

class Printer(abc.ABC):

    @abc.abstractmethod
    def __init__(self, pres, psn):
        self.pres = pres
        self.psn = psn

    @abc.abstractmethod
    def print_document(self):
        return "document printed"

    @abc.abstractmethod
    def get_printer_status(self):
        return [self.pres, self.psn]

class MFD1(Scanner, Printer):
    def __init__(self, sres, pres, sn):
        self.sres = sres
        self.pres = pres
        self.sn = sn

    def scan_document(self):
        return "document scanned"

    def get_scanner_status(self):
        return [self.sres, self.ssn]

    def print_document(self):
        return "document printed"

    def get_printer_status(self):
        return [self.pres, self.sn]



one = MFD1(1000, 500, 'thasg')
print(one.get_printer_status())