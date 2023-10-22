from textual.widgets import Label


def Title(text: str):
    label = Label(text)
    label.styles.text_style = "bold"
    label.styles.color = "cyan"

    return label