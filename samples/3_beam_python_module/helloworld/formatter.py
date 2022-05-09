import apache_beam as beam

class Formatter(beam.DoFn):
    def __init__(self, header):
        self.header = header

    def process(self, row):
        import emoji
        thumb = emoji.emojize(':thumbs_up:')
        result = '%s [%s] %s' % (thumb, self.header.get(), row)
        yield result
