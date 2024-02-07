from jinja2 import Environment, FileSystemLoader, meta

media_dir = 'media/'
jinja_environment = Environment(loader=FileSystemLoader(media_dir))


def get_tex_draft_variable_names(tex_draft_file) -> tuple:
    tex_draft_data = tex_draft_file.open('r').read()
    parsed_data = jinja_environment.parse(tex_draft_data)
    variables = tuple(meta.find_undeclared_variables(parsed_data))
    return variables


def text_is_tex_draft(text: str) -> bool:
    parsed_data = jinja_environment.parse(text)
    variables = tuple(meta.find_undeclared_variables(parsed_data))
    if variables:
        return True
    return False
