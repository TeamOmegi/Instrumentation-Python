import os
from typing import Collection

from opentelemetry import trace
from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.instrumentation.utils import unwrap
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from .exporter.OmegiSpanExporter import OmegiKafkaSpanExporter
from .util.OmegiDependencyInstrument import instrument_dependencies
from .util.OmegiTracingSetup import wrap_functions


class OmegiInstrumentor(BaseInstrumentor):

    def instrumentation_dependencies(self) -> Collection[str]:
        return []

    def instrument(self, app=None):
        self._instrument(app=app)

    def _instrument(self, app=None):
        """
        SETTING UP INSTRUMENTATION
        1. Figure Custom TraceExporter and SpanProcessor
        TraceExporter exports spans to Kafka.
        Kafka server urls can be figured through environment variables
        2. Figure Other Instrumentations
        By installed libraries this library detects fast api, django, flask, elasticsearch
        detected library's instrumentation is enabled automatically
        3. Set Function tracing
        detect module's functions and wrap it in decorator to enable tracing
        """
        # Setup Custom Exporter, SpanProcessor
        custom_exporter = OmegiKafkaSpanExporter()
        span_processor = BatchSpanProcessor(custom_exporter)
        trace.set_tracer_provider(TracerProvider(
            resource=Resource.create({"service.name": os.getenv("OMEGI_SERVICE_NAME")}),
        ))
        trace.get_tracer_provider().add_span_processor(span_processor)
        tracer = trace.get_tracer(__name__)
        # Setup Instrumentations
        if app is not None:
            self._start_depending_instumentation(app=app)
        # Setup Tracing Functions
        wrap_functions(tracer)

    def _uninstrument(self, **kwargs):
        return unwrap(kwargs)

    def _start_depending_instumentation(self, app):
        instrument_dependencies(app)