import sys
from todoist.api import TodoistAPI


def print_projects(api_object):
    return api_object.state['projects']


def import_csv(api_object, project_id, csv):
    api_object.templates.import_into_project(project_id, csv)


def export_to_url(api_object, project_id):
    return api_object.templates.export_as_url(project_id)


def get_project_id(data):
    if data == "new demo":
        return 2213838333
    else:
        return 2215732027


def get_csv(data, product):
    if data == "new demo":
        return 'templates/Demo_Checklist.csv'
    elif product == "cbd":
        print("Returning CBD")
        return 'templates/POC_CBC.csv'
    elif product == "cbr":
        return 'templates/POC_CBR.csv'
    elif product == "cbp":
        return 'templates/POC_CBP.csv'


def validate_command():
    while True:
        try:
            com = input("Enter in a command: ")
            if com == "new demo" or com == "new poc":
                break
            else:
                print("Please enter in a valid command")
        except ValueError:
            print("Please enter in a valid command")
    return com


def validate_product():
    while True:
        try:
            prod = input("Enter in a product: ")
            if prod == "cbd" or prod == "cbr" or prod == "cbp":
                break
            else:
                print("Please enter in a valid product")
        except ValueError:
            print("Please enter in a valid product")
    return prod


def main():
    api = TodoistAPI('1bfa68a130d0206b525c94f22e524f4564b4f0ad')
    api.sync()
    command = validate_command()
    product = validate_product()
    project_id = get_project_id(command)
    csv = get_csv(command, product)
    import_csv(api, project_id, csv)


if __name__ == "__main__":
    sys.exit(main())
