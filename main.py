from fasthtml.common import fast_app, serve
from pages.home import home
from pages.about import about
from pages.services import services
from pages.contact import contact, form_content, send_message_success

app, routes = fast_app()

@routes("/")
def home_page():
    return home()

@routes("/sobre")
def about_page():
    return about()

@routes("/servicos")
def services_page():
    return services()

@routes("/contato")
def contact_page():
    return contact()

@routes("/contato-form", methods=["post"])
def contact_form():
    return form_content()

@routes("/enviar-mensagem", methods=["post"])
def contact_page_send(subject: str, message: str):
    print({subject, message})
    subject_error: bool = False
    message_error: bool = False

    if len(subject) < 4:
       subject_error = True
    
    if len(message) < 6:
        message_error = True

    if len(subject) < 4 or len(message) < 6:
        return form_content(subject, message, subject_error, message_error)

    return send_message_success()

serve()