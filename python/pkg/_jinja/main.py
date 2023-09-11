from typing import Union

from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader


class FilmsInfoSchema(BaseModel):
    id: str
    title: str
    imdb_rating: float
    description: str
    preview: str


class ConfirmationUrlSchema(BaseModel):
    url: str


ContentListSchema = Union[list[FilmsInfoSchema], list[ConfirmationUrlSchema], None]
content = [ConfirmationUrlSchema(url="hello")]

# Load the template from file
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader, autoescape=True)
template = env.get_template('my_template.html')

# Define a macro
rendered_template = template.render({"content": content})

print(rendered_template)

# wrapper = env.get_template('my_wrapper.html')

# text = wrapper.render(content=rendered_template)
# print(text)