
from models.Person import Person
from models.PDFOutput import PDFOutput
from models.TextOutput import TextOutput
from models.Context import Context
import sys
sys.stdout.flush()

if __name__ == "__main__":
    name = raw_input("Enter the name:")
    age = raw_input("Enter the age:")    
    mobile_number = raw_input("Enter the mobile number:")
    city = raw_input("Enter the mobile city:")
    export_type = raw_input("Enter the export type - pdf | text:")
    person = Person(name, age, city , mobile_number)
    
    if export_type == "text":
        output = TextOutput()
    elif export_type == "pdf":
        output = PDFOutput()
    else:
        print "Wrong choice"
        exit()
        
    context = Context(output)
    context.context_interface(person)
