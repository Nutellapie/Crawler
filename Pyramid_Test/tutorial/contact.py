from deform.exception import ValidationFailure
from pyramid.response import Response
from pyramid.view import view_config
import colander
import deform
import deform.widget


class Person (colander.Schema):
    name = colander.SchemaNode(colander.String(),
                               validator=colander.Length(50))
    email = colander.SchemaNode(colander.String(),
                                validator=colander.Length(40))
    message = colander.SchemaNode(colander.String(),
                                  widget=deform.widget.RichTextWidget())
    security_q = colander.SchemaNode(colander.Int(), validator=2)


@view_config(renderer='templates/test.pt', route_name='test')
def test(context, request):
    schema = person
    form = deform.form.Form(schema(), buttons=('submit',))
    appstruct = {}
    captured = None
    controls = request.POST.items()

    try:
        appstruct = form.validate(controls)
    except ValidationFailure as e:
        return {'form': e.render()}

    return {'form': None, 'appstruct': appstruct, 'name': 'DeformTest'}


def includeme(config):
    config.scan(__name__)
