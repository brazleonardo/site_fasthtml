from fasthtml.common import Header, Div, Img, Ul, Li, A, Span

url_logo = "/assets/images/logo.png"

def header(linkhomepage = True):
    logo = Img(src=url_logo)
    link_home = Span("Home", cls="mysite__home")

    if linkhomepage :
        logo = A(Img(src=url_logo), href="/", cls="mysite__header--logo")
        link_home = A(Span("Home"), href="/")

    return Header(
        Div(
            logo,
            Ul(
                Li(link_home),
                Li(A(Span("Sobre"), href="/sobre")),
                Li(A(Span("Serviços"), href="/servicos")),
                Li(A(Span("Contato"), href="/contato")),
            ),
            cls="mysite__header--container"
        ),
        cls="mysite__header"
    )