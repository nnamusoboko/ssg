from typing import override


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


class LeafNode(HtmlNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    @override
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
