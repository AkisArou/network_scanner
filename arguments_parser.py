import argparse


class ArgumentsParser():
    def get_arguments(self):
        # Instantiate the parser
        parser = argparse.ArgumentParser(
            description='Network scanner with email notification functionality on networking devices change')

        # Optional argument
        parser.add_argument("--testing", action="store_true",
                            help="Set if is testing run")

        # Optional argument
        parser.add_argument("--email", type=str,
                            help="Your email")

        # Optional argument
        parser.add_argument("--pw", type=str,
                            help="Your email password")
        # Optional argument
        parser.add_argument("--interval", type=int,
                            help="Watch mode interval value in seconds")

        # Optional argument
        parser.add_argument("--watch", action="store_true",
                            help="Watch mode or single networking devices check")

        args = parser.parse_args()

        return args
