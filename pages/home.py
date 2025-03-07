from fasthtml.common import  Div, H1
from components.layout import layout

def home():
    return layout(
        "Meu Site",
        Div(
            H1("Início", cls="mysite__title")
        ),  
        False,
    )