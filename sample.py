from marshmallow import Schema, fields, post_load

class Sample(object):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return '<Sample(name={self.name!r})>'.format(self=self)

class SampleSchema(Schema):
    name = fields.Str()

    @post_load
    def make_sample(self, data, **kwarge):
        return Sample(**data)
