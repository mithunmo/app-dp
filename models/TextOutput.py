from Strategy import Strategy

class TextOutput(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """
    def output_interface(self, person):
        with open("out.txt", 'w') as outfile:
            for key,val in person.__dict__.items():
                outfile.write(val+"\n")