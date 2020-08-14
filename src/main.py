from arguments_parser import ArgumentsParser
from email_sender import EmailSender
from network_scanner import NetworkScanner
import time

class Application():
    argumentsParser = ArgumentsParser()
    emailSender = EmailSender()
    network_scanner = NetworkScanner()
    arguments = None
    final_interval = None
        

    def initialize(self):
        self.arguments = self.argumentsParser.get_arguments()
        self.final_interval = self.arguments.interval or 5
        self.start_scanning()

    def start_scanning(self):
        output = self.network_scanner.get_network_devices_output()
        print(output)

        if self.arguments.testing == True or self.arguments.email != None and self.arguments.pw != None:
            self.emailSender.send_email(self.arguments.testing, self.arguments.email, self.arguments.pw, output)

        if self.arguments.watch:
            for x in range(1, self.final_interval):
                b = f"  Next scan in: {self.final_interval - x} seconds"  + "." * x
                print (b, end="\r")
                time.sleep(1)
            self.start_scanning()        


def main():
    app = Application()
    app.initialize()


main()
