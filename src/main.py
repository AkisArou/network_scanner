from arguments_parser import ArgumentsParser
from email_sender import EmailSender
from network_scanner import NetworkScanner
import time

class Application():
    argumentsParser = ArgumentsParser()
    emailSender = EmailSender()
    network_scanner = NetworkScanner()
    arguments = None


    def initialize(self):
        self.arguments = self.argumentsParser.get_arguments()
        self.start_scanning(self.arguments.interval or 5)

    def start_scanning(self, interval: int):
        output = self.network_scanner.get_network_devices_output()
        print(output)

        if self.arguments.testing == True or self.arguments.email != None and self.arguments.pw != None:
            self.emailSender.send_email(self.arguments.testing, self.arguments.email, self.arguments.pw, output)

        if self.arguments.watch:
            for x in range(1, interval):
                b = f"  Next scan in: {interval - x} seconds"  + "." * x
                print (b, end="\r")
                time.sleep(1)
            self.start_scanning(interval)


def main():
    app = Application()
    app.initialize()


main()
