class HtmlNode:
    def __init__(
        self,
        tag: str | None = None ,
        value: str | None = None,
        children: list['HtmlNode'] | None = None,
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if not self.props:
            return ""

        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'

        return props_str

    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"
