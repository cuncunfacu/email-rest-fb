from flask import Blueprint, jsonify, request, render_template
import os
from utils import send_email

emailing = Blueprint(name="emailing", import_name=__name__)


@emailing.route('/send', methods=['POST'])
def test():
    # TODO: add validation
    template = request.json['template']
    email_subject = request.json['subject']
    to = request.json['to']
    html_content = render_template(template, ctx=request.json['context'])

    context = request.json['context']
    send_email(to=to, subject=email_subject, plain_txt_content="hola", html_content=html_content)
    
    return jsonify(
        {
            "message": "email sent!",
            "ctx": context
        }
    )

