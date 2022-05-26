from apache_beam.options.pipeline_options import PipelineOptions

__all__ = ["AppOptions"]


class AppOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_value_provider_argument("--header")
        parser.add_value_provider_argument("--output")
