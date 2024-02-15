from flask import Flask, request, send_file
from jinja2 import TemplateSyntaxError

from engine import render_template, generate_pdf

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    json_data = request.json
    error_message = ''
    try:
        rendered_template = render_template(json_data.get('template'), **json_data.get('variables'))
        pdf_filename = generate_pdf(rendered_template)
        return send_file(pdf_filename, download_name='result.pdf')
    except TypeError:
        error_message = 'Expected keys: template, variables'
    except TemplateSyntaxError:
        error_message = 'Template has some syntax errors'
    except ValueError as error:
        error_message = str(error)
    except SyntaxError:
        error_message = 'Template has some syntax errors'
    return {'message': error_message, 'status': '400'}, 400
