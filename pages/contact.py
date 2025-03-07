from fasthtml.common import  Div, H1, H3, Form, Label, Input, Textarea, Button
from components.layout import layout

def form_content(subject: str = "", message: str = "", subject_error: bool = False, message_error: bool = False):
    custom_class_subject: str = "mysite__form--group"
    custom_class_message: str = "mysite__form--group"

    if subject_error : 
        custom_class_subject = "mysite__form--group mysite__form--group-error"

    if message_error : 
        custom_class_message = "mysite__form--group mysite__form--group-error"

    return Div(
        Form(
            Div(
                Label("Assunto"),
                Input(name="subject", value=subject, placeholder="Diga o assunto", cls="mysite__form--control"),
                cls=custom_class_subject,
            ),
            Div(
                Label("Mensagem"),
                Textarea(message, name="message", placeholder="Deixe sua mensagem", cls="mysite__form--control"),
                cls=custom_class_message
            ),
            Div(
                Button("Enviar", type="submit", cls="mysite__button--primary"),
                cls="mysite__form--group"
            ),
            method="post",
            action="/enviar-mensagem",
            hx_post="/enviar-mensagem",
            hx_target="#content",
            hx_swap="outerHTML",
            cls="mysite__form",
        ),
        id="content",
    )

def send_message_success():
    return Div(
        Div(
            H3("Mensagem foi enviada com sucesso!", cls="mysite_msg--success"),
            Button(
                "Enviar outra mensagem", 
                cls="mysite__button--secondary", 
                hx_post="/contato-form", 
                hx_target="#content",
                hx_swap="outerHTML"
            ),
            cls="mysite__form"
        ),
        id="content",
    )

def contact():
    return layout(
        "Contato | Meu Site",
        Div(
            H1("Contato", cls="mysite__title"),
            form_content()
        )
    )