from fasthtml.common import  Div, H1
from components.layout import layout

def about():
    return layout(
        "Sobre | Meu Site",
        Div(
            H1("Sobre", cls="mysite__title")
        )
    )