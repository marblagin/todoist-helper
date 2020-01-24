from todoist import TodoistAPI


def print_projects(api_object, verbose=False):
    if verbose:
        print(api_object.state['projects'])
    else:
        for x in range(len(api_object.state['projects'])):
            print(api_object.state['projects'][x]['name'])


def print_items(api_object, project_id, verbose=False):
    if verbose:
        for y in range(len(api_object.state['items'])):
            if api_object.state['items'][y]['project_id'] == project_id:
                print(api_object.state['items'][y])
    else:
        for y in range(len(api_object.state['items'])):
            if api_object.state['items'][y]['project_id'] == project_id:
                print(api_object.state['items'][y]['content'])


def export_to_url(api_object, project_id):
    return api_object.templates.export_as_url(project_id)


def main():
    api = TodoistAPI('1bfa68a130d0206b525c94f22e524f4564b4f0ad')
    api.sync()
    # print_projects(api, verbose=True)
    # print_items(api, project ID, verbose=True)
    # print(export_to_url(api, project ID))


if __name__ == "__main__":
    main()
