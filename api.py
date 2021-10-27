import justpy as jp
import definition
import json

class Api:
    """Handles requests at /?w=word
    """

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        # Using a Div is unnecessary because it serves a full Webpage!
        # jp.Div(a=wp, text=word.title())

        defined = definition.Definition(word).get()

        response = {
            "word":word,
            "definition":defined
        }

        wp.html = json.dumps(response)
        return wp


