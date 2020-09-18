from todoist.api import TodoistAPI
import sys


class Title:
    def __init__(self):
        self.company_name = input("Enter in company name: ")
        self.isr = input("Enter in ISR name: ")
        self.products = self.validate_products()

    @staticmethod
    def validate_products():
        while True:
            try:
                prod = input("Enter in a product: ").split()
                for x in range(len(prod)):
                    if prod[x] == "CBD" or prod[x] == "CBLO" or prod[x] == "CBTH" \
                            or prod[x] == "CBR" or prod[x] == "CBP" or prod[x] == "CBC" \
                            or prod[x] == "CBS" or prod[x] == "CBA":
                        return prod
                print("Please enter in a valid product")
            except ValueError:
                print("Please enter in a valid product")

    def get_title(self):
        prods = ""
        for x in range(len(self.products)):
            prods = prods + self.products[x] + " "
        return str(self.company_name + " - " + self.isr + " - " + prods)

    def get_products(self):
        return self.products


def assign_company_name(api_object, project_id, template_name, title, company_name):
    parent_id = ""
    for y in range(len(api_object.state['items'])):
        if api_object.state['items'][y]['content'] == template_name and \
                api_object.state['items'][y]['project_id'] == project_id:
            parent_id = api_object.state['items'][y]['id']
            parent_item = api_object.items.get_by_id(parent_id)
            parent_item.update(content=title)
    for y in range(len(api_object.state['items'])):
        if api_object.state['items'][y]['parent_id'] == parent_id:
            original_content = api_object.state['items'][y]['content']
            item = api_object.items.get_by_id(api_object.state['items'][y]['id'])
            new_content = company_name + " - " + original_content
            item.update(content=new_content)
    api_object.commit()


def import_csv(api_object, project_id, csv):
    api_object.templates.import_into_project(project_id, csv)


def get_project_id(command):
    if command == "demo":
        # Demo Project ID
        return 2213838333
    else:
        # POC Project ID
        return 2215732027


def get_csv(data, product):
    if data == "demo":
        return 'templates/Demo_Checklist.csv'
    else:
        for x in range(len(product)):
            if product[x] == "CBD" or product[x] == "CBLO" or product[x] == "CBTH" or product[x] == "CBC" \
                    or product[x] == "CBS" or product[x] == "CBA":
                return 'templates/POC_CBC.csv'
            elif product[x] == "CBR":
                return 'templates/POC_CBR.csv'
            elif product[x] == "CBP":
                return 'templates/POC_CBP.csv'


def get_template_name(products, command):
    if command == "demo":
        return 'Demo Checklist Template:'
    else:
        for x in range(len(products)):
            if products[x] == "CBD" or products[x] == "CBLO" or products[x] == "CBTH" or products[x] == "CBC" \
                    or products[x] == "CBS" or products[x] == "CBA":
                return 'CBC POC Checklist Template:'
            elif products[x] == "CBR":
                return 'CBR POC Checklist Template:'
            elif products[x] == "CBP":
                return 'CBP POC Checklist Template:'


def validate_command():
    while True:
        try:
            com = input("Enter in a command: ")
            if com == "new demo":
                return "demo"
            elif com == "new poc":
                return "poc"
            else:
                print("Please enter in a valid command")
        except ValueError:
            print("Please enter in a valid command")


def main():
    api = TodoistAPI('1bfa68a130d0206b525c94f22e524f4564b4f0ad')
    api.sync()
    command = validate_command()
    title = Title()
    products = title.get_products()
    project_id = get_project_id(command)
    csv = get_csv(command, products)
    template_name = get_template_name(products, command)
    import_csv(api, project_id, csv)
    api.sync()
    assign_company_name(api, project_id, template_name, title.get_title(), title.company_name)
    api.sync()


if __name__ == "__main__":
    sys.exit(main())
