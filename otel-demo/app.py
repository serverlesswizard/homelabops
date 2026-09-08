from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
import time

app = Flask(__name__)

# OpenTelemetry configuration
resource = Resource.create({
    "service.name": "otel-demo"
})

provider = TracerProvider(resource=resource)

otlp_exporter = OTLPSpanExporter(
    endpoint="http://192.168.0.122:4318/v1/traces"
)

provider.add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)


@app.route("/")
def home():
    with tracer.start_as_current_span("home-request"):

        with tracer.start_as_current_span("database-operation"):
            time.sleep(0.2)

        with tracer.start_as_current_span("business-logic"):
            time.sleep(0.1)

        return "OTel Demo Application is running!"


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
