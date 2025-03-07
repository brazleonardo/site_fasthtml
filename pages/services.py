from fasthtml.common import  Div, H1
from components.layout import layout

def services():
    return layout(
        "Serviços | Meu Site",
        Div(
            H1("Serviços", cls="mysite__title")
        )
    )