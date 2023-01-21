#this is actually for make the list for wpfunc
def list_html_list(any_list):
    start = '<!-- wp:list --><ul>'
    for element in any_list:
        start += f'<!-- wp:list-item --><li>{element}</li><!-- /wp:list-item -->'
    ends = '</ul><!-- /wp:list -->'
    code = start+ends
    return code

def dict_list(dicts):
    start = '<!-- wp:list --><ul>'
    for key, value in dicts.items():
        start += f'<!-- wp:list-item --><li><strong>{key.title()}</strong>: {value.title()}</li><!-- /wp:list-item -->'
    ends = '</ul><!-- /wp:list -->'
    code = start + ends
    return code



def headers(username, password):
    import base64
    credential = f'{username}:{password}'
    token = base64.bs4encode(credential.encode())
    code = {'Authentication': f'Basic {token.decode("utf-8")}'}
    return code

print(dict_list({'name': 'omor', 'age': '33'}))