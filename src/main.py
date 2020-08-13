from arguments_parser import ArgumentsParser
from email_sender import EmailSender
from network_scanner import NetworkScanner
from thread_job import ThreadJob


class Application():
    argumentsParser = ArgumentsParser()
    emailSender = EmailSender()
    network_scanner = NetworkScanner()
    thread_job = None
    arguments = None

    def initialize(self):
        self.arguments = self.argumentsParser.get_arguments()

        if self.arguments.watch:
            self.make_watch_mode()
        else:
            self.make_single_mode()

    def make_watch_mode(self):
        self.thread_job = ThreadJob(self.make_single_mode, self.arguments.interval)
        self.thread_job.run()

    def make_single_mode(self):
        output = self.network_scanner.get_network_devices_output()
        print(output)
        if self.arguments.testing == True or self.arguments.email != None and self.arguments.pw != None:
            self.emailSender.send_email(self.arguments.testing, self.arguments.email, self.arguments.pw, output)


def main():
    application = Application()
    application.initialize()


main()
