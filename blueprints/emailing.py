from flask import Blueprint, jsonify, request, render_template
from utils import send_email

emailing = Blueprint(name="emailing", import_name=__name__)


@emailing.route('/send', methods=['POST'])
def test():
    # TODO: add validation
    try:
        template = request.json['template']
        email_subject = request.json['subject']
        to = request.json['to']
        context = request.json['context']
    except:
        return jsonify({"message": "Bad Request"}), 400

    
    try:
        html_content = render_template(template, ctx=request.json['context'])
    except Exception as e:
        return jsonify({"Error": e.__str__()})


    try:
        send_email(to=to, subject=email_subject, plain_txt_content="hola", html_content=html_content)
    except Exception as e:
        return jsonify({"Error": e.__str__()})
    
    return jsonify(
        {
            "message": "email sent!",
            "ctx": context
        }
    )

