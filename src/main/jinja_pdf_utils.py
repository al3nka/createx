import os

from jinja2 import Environment, FileSystemLoader, meta

tex_draft_dir = 'media/'
jinja_environment = Environment(loader=FileSystemLoader(tex_draft_dir))


def get_tex_draft_variable_names(tex_draft_filename: str) -> tuple:
    template_location = tex_draft_dir + tex_draft_filename
    with open(template_location, 'r') as file:
        tex_draft_data = file.read()
    parsed_data = jinja_environment.parse(tex_draft_data)
    variables = tuple(meta.find_undeclared_variables(parsed_data))
    return variables


def text_is_tex_draft(text: str) -> bool:
    parsed_data = jinja_environment.parse(text)
    variables = tuple(meta.find_undeclared_variables(parsed_data))
    if variables:
        return True
    return False
