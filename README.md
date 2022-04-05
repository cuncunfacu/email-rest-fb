# Flask REST API for emailing

Send email (GMAIL SMPT) via REST API.

HTML files using Jinja2 syntax can be used to define email templates.

## Example:
Gmail access credentials where be provided as environment variables and a `test.html` template was stored in the `html_templates` directory.

### POSTMAN REQUEST:
By making a POST REQUEST to the `/send` endpoint, an email is sent according to the request’s body.
In the image below, you can see the request and response made by the instance of the service running
![Postman request example](https://firebasestorage.googleapis.com/v0/b/portfolio22-38a55.appspot.com/o/postman1.png?alt=media&token=89f05a3a-0af5-4e02-bac7-bc6c16a45544)

### EMAIL RECEPTION
Here you can see the email sent. Notice how the html template was rendered according to the context variables passed in the request.
![Gmail email reception example](https://firebasestorage.googleapis.com/v0/b/portfolio22-38a55.appspot.com/o/email1.png?alt=media&token=104856b3-7122-43fb-8ad8-34e339162516)

## Stacks Used
+ Flask
+ Docker
+ Python's smtplib module
