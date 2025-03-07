from fasthtml.common import Html, Head, Meta, Title, Script, Link, Body, Main, Div
from components.header import header

def layout(title, page, haslinkhome: bool = True):
    return Html(
        Head(
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale-0.1"),
            Title(title),
            Script(src="/assets/js/htmx.min.js"),
            Link(href="/assets/images/favicon.ico", rel="icon"),
            Link(href="assets/css/main.css", rel="stylesheet")
        ),
        Body(
            Main(
                header(haslinkhome),
                Div(page(), cls="mysite__container", id="main-container"),
                cls="mysite__main"
            )
        ),
        lang="pt-BR",
    )