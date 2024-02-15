from jinja2 import Environment, TemplateSyntaxError, meta
import subprocess

environment = Environment()

def render_template(template: str, **variables):
    template_variable_names = get_template_variable_names(template)
    if set(variables.keys()) != set(template_variable_names):
        raise ValueError(f'Expected variable keys: {", ".join(template_variable_names)}')
    template = environment.from_string(template)
    return template.render(**variables)


def get_template_variable_names(template: str) -> tuple:
    jinja_environment = Environment()
    parsed_data = jinja_environment.parse(template)
    variables = tuple(meta.find_undeclared_variables(parsed_data))
    return variables


def generate_pdf(template_string: str) -> str:
    template_filename = 'template.tex'
    pdf_filename = 'template.pdf'
    with open(template_filename, 'w') as file:
        file.write(template_string)
    exit_code = subprocess.run(['pdflatex', '-halt-on-error', template_filename]).returncode
    if exit_code != 0:
        raise SyntaxError
    return pdf_filename
