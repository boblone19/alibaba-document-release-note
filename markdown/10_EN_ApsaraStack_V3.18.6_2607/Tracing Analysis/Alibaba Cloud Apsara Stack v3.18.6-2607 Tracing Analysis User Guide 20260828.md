---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Tracing Analysis User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 84
source_pdf: "1f7b565ae9cc7e9e_Alibaba Cloud Apsara Stack v3.18.6-2607 Tracing Analysis User Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%8F%AF%E8%A7%82%E6%B5%8B%E9%93%BE%E8%B7%AF%20OpenTelemetry%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Tracing%20Analysis%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Tracing Analysis User Guide 20260828

## Table of Contents

- 1 Getting started
  - 1.1 Log on to the Tracing Analysis console
  - 1.2 Get the endpoint
  - 1.3 OpenTelemetry integration guide
  - 1.4 Obtain OpenTelemetry Access Configuration
  - 1.5 Monitor Java applications
    - 1.5.1 Use Jaeger to report the trace data of Java applications
    - 1.5.2 Use Zipkin to report the trace data of Java applications
  - 1.6 Monitor PHP applications
    - 1.6.1 Use Zipkin to report the trace data of PHP applications
  - 1.7 Monitor Go applications
    - 1.7.1 Use Jaeger to report the trace data of Go applications
    - 1.7.2 Use Zipkin to report the trace data of a Go application
  - 1.8 Monitor Node.js applications
    - 1.8.1 Use Jaeger to report the trace data of Node.js applications
  - 1.9 Monitor .NET applications
    - 1.9.1 Use Jaeger to report the trace data of .NET applications
    - 1.9.2 Use Zipkin to report the trace data of .NET applications
  - 1.10 Monitor NGINX
    - 1.10.1 Use Zipkin to perform tracing analysis on NGINX
- 2 Tutorial
  - 2.1 View applications
  - 2.2 View the overall information about an application
  - 2.3 View application details
  - 2.4 View the details of span calls
  - 2.5 View database calls
  - 2.6 Perform diagnosis
  - 2.7 Configure application settings
  - 2.8 Run a multidimensional query
  - 2.9 Global topology
  - 2.10 Usage statistics

## 1 Getting started

### 1.1 Log on to the Tracing Analysis console

**console**

This topic describes how to log on to the Tracing Analysis console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineer. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language.
> The Authorized Login button is displayed only when a global identity provider (IdP) is configured in third-party authentication. You can specify a name for the Authorized Login button.

If you need to click Continue multiple times or cannot find the entry to the Apsara Uni-manager Management Console because the browser certificate has expired or HTTPS authentication is enabled in your environment, you must install a valid certificate. Click **Browser certificate installation** in the upper-right corner to open the browser certificate installation guide.
2. Enter your username and password.

> **Note:** Obtain the username and password from an operations administrator.
> The first time you log in to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**This is your first time logging in to the Apsara Uni-manager Management**

**Console after MFA is enabled by the administrator:**

a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the 6-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device:**

Enter the 6-digit MFA verification code and click **Authenticate**.

> **Note:** For more information about how to enable MFA and bind an MFA device, see the **Manage MFA** topic in Apsara Uni-manager Management Console User Guide.

5. In the top menu bar, choose **Products > Middleware > Cloud Native Observability >**
**Application Real-Time Monitoring Service (ARMS)**.
6. On the **Application Real-Time Monitoring Service** page, select an organization and a
region, and click **Administrative Access** to open the ARMS console.
7. In the navigation pane on the left, choose **Tracing Analysis** to open the Tracing Analysis
console.

### 1.2 Get the endpoint

Obtain an endpoint to connect your application. Connecting an application means reporting its trace data to Tracing Analysis through a client, enabling distributed tracing. You can report trace data from applications written in Java, PHP, Go, Python, JavaScript, .NET, C++, and other languages to Tracing Analysis.

**Procedure**

1. Log on to the Tracing Analysis console.
2. In the navigation pane on the left, choose **Tracing Analysis > Cluster Configuration**.
3. On the **Endpoint Information** tab, in the **Cluster Information** section, turn on the **Show**
**Token** switch.
4. In the **Client** section, click the **OpenTelemetry** tab.
In the table, the information next to **Endpoint** under the **Related Information** column is your endpoint.

### 1.3 OpenTelemetry integration guide

**guide**

Tracing Analysis now supports OpenTelemetry data ingestion. You can integrate the OpenTelemetry client into your application to report traces from applications in languages such as Java, PHP, Go, Python, and JavaScript to the Tracing Analysis console. This lets you visualize and analyze distributed call chains.

**Prerequisites**

Obtain an endpoint. For more information, see Obtain an endpoint.

**Data reporting**

The following figure shows how to report data using OpenTelemetry. Collector UI (Tracing Analysis) (Tracing Analysis) Host or container Application Linked Data OpenTelemetry Storage Report call chain data over an HTTP API Client with JSON serialization Query Log storage

**Recommended scenarios for ARMS and Tracing Analysis**

| Programming language | ARMS Application Monitoring (proprietary agent, SLA guaranteed) | Tracing Analysis (OpenTelemetry, open source client, self-managed) | Recommended connection type |
|---|---|---|---|
| Java | Automatic instrumentation | Automatic instrumentation | ARMS |
| Go | Not supported | Automatic instrumentation | OpenTelemetry |
| Python | Not supported | Automatic instrumentation | OpenTelemetry |
| Node.js | Not supported | Automatic instrumentation | OpenTelemetry |
| PHP | Not supported | Automatic instrumentation | OpenTelemetry |
| Erlang | Not supported | Automatic instrumentation | OpenTelemetry |
| C++ | Not supported | Manual instrumentation | OpenTelemetry |
| Ruby | Not supported | Manual instrumentation | OpenTelemetry |

| Rust | Not supported | Manual instrumentation | OpenTelemetry |
|---|---|---|---|
| .NET | Not supported | Automatic instrumentation | OpenTelemetry |

**Report data from Java applications using OpenTelemetry**

**Method 1: Use the OpenTelemetry Java Agent for automatic**

**instrumentation**

Sample code repository: Sample demo. The OpenTelemetry Java Agent provides a non-intrusive connection method. It supports automatic trace data reporting for hundreds of Java frameworks. To report data over HTTP, you can set the trace endpoint information.

```
java -javaagent:/path/to/opentelemetry-javaagent.jar\ # Replace the path with the act ual download path of your file. -Dotel.resource.attributes=service.name= \ # Application name -Dotel.exporter.otlp.protocol=http/protobuf \ -Dotel.exporter.otlp.traces.endpoint=<traces.endpoint> \ # Replace this with the trac e endpoint obtained in the Prerequisites section. -Dotel.logs.exporter=none \ -jar /path/to/your/app.jar # Replace this with the path to your actual JAR package.
```

Example:

```
 java -javaagent:/path/to/opentelemetry-javaagent.jar \
-Dotel.resource.attributes=service.name=test \ -Dotel.exporter.otlp.protocol=http/protobuf \ -Dotel.exporter.otlp.traces.endpoint=http://tracing-analysis-dc-hzinternal.aliyuncs.com/adapt_ggxw4l****@7323a5caae3****_ggxw4l****@53df7ad2afe****/api/otl traces \ -Dotel.logs.exporter=none \ -jar /path/to/your/app.jar
```

**Method 2: Use the OpenTelemetry Java SDK for manual**

**instrumentation**

The OpenTelemetry Java SDK is the foundation of the OpenTelemetry Java Agent and provides extensive customization capabilities. If the automatic instrumentation of the OpenTelemetry Java Agent does not meet your needs, or if you want to add custom business instrumentation, you can use the following method.
1. Import the Maven POM dependencies.

```xml
<dependencies>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-api</artifactId>
    </dependency>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-sdk-trace</artifactId>
    </dependency>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-exporter-otlp</artifactId>
    </dependency>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-sdk</artifactId>
    </dependency>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-semconv</artifactId>
        <version>1.30.0-alpha</version>
    </dependency>
</dependencies> <dependencyManagement> <dependencies>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-bom</artifactId>
        <version>1.30.0</version>
        <type>pom</type>
        <scope>import</scope>
    </dependency>
</dependencies> </dependencyManagement>
```

2. Obtain the OpenTelemetry Tracer.

```java
public class OpenTelemetrySupport {
    static {
        // Obtain the OpenTelemetry Tracer
        Resource resource = Resource.getDefault()
                .merge(Resource.create(Attributes.of(
                        ResourceAttributes.SERVICE_NAME, "",  // Application name.
                        ResourceAttributes.SERVICE_VERSION, "",  // Version number. Op
tional.
                        ResourceAttributes.DEPLOYMENT_ENVIRONMENT, "", // Deployment e
nvironment. Optional.
                        ResourceAttributes.HOST_NAME, "${host-name}" // Replace ${host
-name} with your hostname.
                )));
        SdkTracerProvider sdkTracerProvider = SdkTracerProvider.builder()
.addSpanProcessor(BatchSpanProcessor.builder(OtlpHttpSpanExporter.builder()
                        .setEndpoint("<endpoint>")  // Replace <endpoint> with the end
point information obtained in the Prerequisites section.
                        .build()).build())
                .setResource(resource)
                .build();
        OpenTelemetry openTelemetry = OpenTelemetrySdk.builder()
                .setTracerProvider(sdkTracerProvider)
.setPropagators(ContextPropagators.create(W3CTraceContextPropagator.getInstance()))
                .buildAndRegisterGlobal();
        tracer = openTelemetry.getTracer("OpenTelemetry Tracer", "1.0.0");
```

`}`

```java
    private static Tracer tracer;
    public static Tracer getTracer() {
        return tracer;
```

`}` `}`
3. Create a span.

```java
public class Main {
    public static void parentMethod() {
        Span span = OpenTelemetrySupport.getTracer().spanBuilder("parent
span").startSpan();
        try (Scope scope = span.makeCurrent()) {
            span.setAttribute("good", "job");
            childMethod();
        } catch (Throwable t) {
            span.setStatus(StatusCode.ERROR, "handle parent span error");
        } finally {
            span.end();
```

`}` `}`

```
    public static void childMethod() {
        Span span = OpenTelemetrySupport.getTracer().spanBuilder("child
span").startSpan();
        try (Scope scope = span.makeCurrent()) {
            span.setAttribute("hello", "world");
        } catch (Throwable t) {
            span.setStatus(StatusCode.ERROR, "handle child span error");
        } finally {
            span.end();
```

`}` `}`

```
    public static void main(String[] args) {
        parentMethod();
```

`}` `}`
4. Start the application.
In the application list on the Tracing Analysis page, you can select the target application to view its traces.

**Report data from Python applications using OpenTelemetry**

Python 3.8 or later. Sample code repository: python-opentelemetry-demo.

**Method 1: Use an agent for automatic instrumentation and**

**reporting**

1. Download the required packages.

```
pip install django pip install requests pip install opentelemetry-distro \
 opentelemetry-exporter-otlp
opentelemetry-bootstrap -a install
```

2. Create an AutoAndManualDemo project and a HelloWorld application.
i. Create the AutoAndManualDemo project.

```
django-admin startproject AutoAndManualDemo
```

ii. Create the HelloWorld application in the project.

```bash
cd AutoAndManualDemo
# Create the helloworld app in the project
python manage.py startapp helloworld
```

3. Modify the HelloWorld application code.
i. Add the following code to the `AutoAndManualDemo/helloworld/views.py` file.

```python
from django.http import HttpResponse from datetime import datetime
# Create your views here.
def hello_world_view(request):
    result = "Hello World! Current Time =" + str(get_time())
    return HttpResponse(result)
def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
```

ii. Create the `AutoAndManualDemo/helloworld/urls.py` file and add the following code to it.

```
from django.urls import path from . import views urlpatterns = [
    path('', views.hello_world_view, name='helloworld')
```

`]` iii. Modify the `AutoAndManualDemo/AutoAndManualDemo/urls.py` file to add the helloworld URL.

```
from django.contrib import admin from django.urls import path, include urlpatterns = [
 path('admin/', admin.site.urls),
 path('helloworld/', include('helloworld.urls')),
```

`]`
4. Run the project.
To report data over HTTP, replace `<your-service-name>` with your application name and `<http-endpoint>` with the HTTP endpoint.

```
opentelemetry-instrument \
    --traces_exporter console,otlp_proto_http \
    --metrics_exporter none \
    --service_name <your-service-name> \
    --exporter_otlp_traces_endpoint <http-endpoint> \
    python manage.py runserver --noreload
```

**Method 2: Manually instrument and report data**

1. Download the required packages.

```
pip install opentelemetry-api pip install opentelemetry-sdk pip install opentelemetry-exporter-otlp
```

2. In the manual.py file, set the OpenTelemetry initialization code.
Replace the `<endpoint>` and `<token>` placeholders in the code with the endpoint and authentication token from the Prerequisites section. You also need to replace `<service-` `name>` and `<host-name>` with your service name and hostname.

```python
from opentelemetry import trace, baggage from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter as OTLPSpanGrpcExporter from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter as OTLPSpanHttpExporter from opentelemetry.sdk.resources import SERVICE_NAME, Resource, HOST_NAME from opentelemetry.sdk.trace import TracerProvider from opentelemetry.sdk.trace.export import BatchSpanProcessor def init_opentelemetry():
    # Set the service name and hostname
    resource = Resource(attributes={
        SERVICE_NAME: "<service-name>",
        HOST_NAME: "<host-name>"
```

`})`

```bash
    # Report data over HTTP
     span_processor = BatchSpanProcessor(OTLPSpanHttpExporter(
         endpoint="<endpoint>",
```

`))`

```
    trace_provider = TracerProvider(resource=resource,
active_span_processor=span_processor)
    trace.set_tracer_provider(trace_provider)
```

3. Create a span.

```python
tracer = trace.get_tracer(__name__) # Get the tracer with tracer.start_as_current_span("child_span") as child_span: # Create a span named child_span
    print("hello world")
```

4. Retrieve the TraceID and SpanID.

```python
ctx = trace.get_current_span().get_span_context() trace_id = '{trace:032x}'.format(trace=ctx.trace_id) span_id = '{span:016x}'.format(span=ctx.span_id) print(trace_id) print(span_id)
```

5. Use the OpenTelemetry Baggage API to pass custom business tags. When you create
baggage_parent_span, you can set properties by specifying the attributes parameter.

```python
def baggage_and_attribute_usage():
    tracer = trace.get_tracer(__name__)
    global_ctx = baggage.set_baggage("key", "value_from_global_ctx")  # Use the bagga
ge API to pass data between different spans
    with tracer.start_as_current_span(name='baggage_parent_span', attributes={'attrib
ute_key': 'value'}) as baggage_parent_span:
        parent_ctx = baggage.set_baggage("key", "value_from_parent_ctx")
        with tracer.start_as_current_span(name='baggage_child_span',
context=parent_ctx) as baggage_child_span:
            child_ctx = baggage.set_baggage("key", "value_from_child_ctx")
    # Get the value of the key in different contexts
    print(baggage.get_baggage("key", global_ctx))
    print(baggage.get_baggage("key", parent_ctx))
    print(baggage.get_baggage("key", child_ctx))
```

**Method 3: Add manual instrumentation on top of automatic**

**instrumentation**

To add custom business instrumentation while you use the automatic instrumentation capabilities of OpenTelemetry, complete the following steps based on Method 1: Use an agent for automatic instrumentation and reporting.
1. Download the required packages.

```
pip install django pip install requests pip install opentelemetry-sdk pip install opentelemetry-instrumentation-django pip install opentelemetry-exporter-otlp
```

2. Create an AutoAndManualDemo project and a HelloWorld application.
i. Create the AutoAndManualDemo project.

```
django-admin startproject AutoAndManualDemo
```

ii. Create the HelloWorld application in the project.

```bash
cd AutoAndManualDemo
# Create the helloworld app in the project
python manage.py startapp helloworld
```

3. Modify the code in the `helloworld/views.py` file to retrieve the tracer, manually create a
span, and set the span name.

```python
from django.http import HttpResponse from opentelemetry import trace from datetime import datetime
# Create your views here.
def hello_world_view(request):
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("hello_world_span") as hello_world_span:
        result = "Hello World! Current Time =" + str(get_time())
        return HttpResponse(result)
def get_time():
    now = datetime.now()
    tracer = trace.get_tracer(__name__)
    # Create a new span
    with tracer.start_as_current_span("time_span") as time_span:
        return now.strftime("%H:%M:%S")
```

4. Modify the urls.py file.
i. Create the `helloworld/urls.py` file and add the following code to it.

```
from django.urls import path from . import views urlpatterns = [
    path('', views.hello_world_view, name='helloworld')
```

`]` ii. Modify the `AutoAndManualDemo/AutoAndManualDemo/urls.py` file to add the helloworld URL.

```
from django.contrib import admin from django.urls import path, include urlpatterns = [
 path('admin/', admin.site.urls),
 path('helloworld/', include('helloworld.urls')),
```

`]`
5. Modify the code in the manage.py file. Add the following content to the application
initialization code.

```python
from opentelemetry import trace from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter # Connect over gRPC
# from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
# Connect over HTTP
from opentelemetry.sdk.resources import SERVICE_NAME, Resource, HOST_NAME from opentelemetry.sdk.trace import TracerProvider from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter resource = Resource(attributes={
        SERVICE_NAME: "<service-name>",
        HOST_NAME: "<host-name>"
```

`})`

```bash
trace.set_tracer_provider(TracerProvider(resource=resource)) trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter(
        endpoint="<endpoint>",
        headers="Authentication=<token>" # The headers parameter is required for gRPC
connections but not for HTTP connections ))) # Report traces using OTLPSpanExporter trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()
# Output traces to the console
```

Replace the following placeholders and modify the code based on your connection type (gRPC or HTTP): `<service-name>` : The name of the service to report. `<host-name>` : The hostname. `<endpoint>` : The endpoint for reporting data over HTTP/gRPC. `<token>` : The authentication token for reporting data over gRPC.

**Report data from Go applications using OpenTelemetry**

Sample code repository: oltp-exporter.
1. Add the OpenTelemetry Go dependencies.

```
go get go.opentelemetry.io/otel go get go.opentelemetry.io/otel/trace go get go.opentelemetry.io/otel/sdk go get go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp // otlp http
```

2. Initialize the OpenTelemetry Go SDK. Replace the Endpoint and URLPath with the endpoint
information that you obtained in the Prerequisites section. You can report data directly through the OpenTelemetry SDK or forward it through an open source OpenTelemetry Collector. To report data directly, replace the Endpoint and URLPath with the endpoint information that you obtained in the Prerequisites section. To forward data using an OpenTelemetry Collector, replace the Endpoint with your locally deployed service endpoint and delete the header information.

```
func initProvider() func() {
    ctx := context.Background()
    traceClientHttp := otlptracehttp.NewClient(
        otlptracehttp.WithEndpoint("127.0.XX.XX:8080"),      // Replace the Endpoint
with the endpoint information obtained in the Prerequisites section.
        otlptracehttp.WithURLPath("/adapt_xxxxx/api/otlp/traces"),   // Replace the U
RLPath with the endpoint information obtained in the Prerequisites section.
        otlptracehttp.WithInsecure())
    otlptracehttp.WithCompression(1)
    traceExp, err := otlptrace.New(ctx, traceClientHttp)
    handleErr(err, "Failed to create the collector trace exporter")
    res, err := resource.New(ctx,
        resource.WithFromEnv(),
        resource.WithProcess(),
        resource.WithTelemetrySDK(),
        resource.WithHost(),
        resource.WithAttributes(
            // The service name displayed in the Managed Service for OpenTelemetry
backend.
            semconv.ServiceNameKey.String(common.ClientServiceName),
            semconv.HostNameKey.String(common.ClientServiceHostName),
```

`),` `)`

```
    handleErr(err, "failed to create resource")
    bsp := sdktrace.NewBatchSpanProcessor(traceExp)
    tracerProvider := sdktrace.NewTracerProvider(
        sdktrace.WithSampler(sdktrace.AlwaysSample()),
        sdktrace.WithResource(res),
        sdktrace.WithSpanProcessor(bsp),
```

`)`

```
    // Set the global propagator to tracecontext (not set by default).
    otel.SetTextMapPropagator(propagation.TraceContext{})
    otel.SetTracerProvider(tracerProvider)
    log.Println("OTEL init success")
    return func() {
        cxt, cancel := context.WithTimeout(ctx, time.Second)
        defer cancel()
        if err := traceExp.Shutdown(cxt); err != nil {
            otel.Handle(err)
```

`}` `}` `}`
3. Add instrumentation.

```
tracer := otel.Tracer(common.TraceInstrumentationName)
    method, _ := baggage.NewMember("method", "repl")
    client, _ := baggage.NewMember("client", "cli")
    bag, _ := baggage.New(method, client)
    defaultCtx := baggage.ContextWithBaggage(context.Background(), bag)
    for {
        ctx, span := tracer.Start(defaultCtx, "ExecuteRequest")
        makeRequest(ctx)
        span.End()
        time.Sleep(time.Duration(1) * time.Second)
```

`}`
4. Start the application.

**Report data from C++ applications using OpenTelemetry**

Sample code repository: opentelemetry-cpp-demo. C++ 11 or later. For information about supported C++ versions and development platforms, see Supported C++ Versions and Development Platforms. Step 1: Prepare the environment
1. **(Optional)** Run the C++ image.

```bash
docker pull gcc # This image uses the Debian system docker run -it --name otel-cpp-demo gcc bash
```

2. Install the required dependencies.
protobuf grpc

```python
apt-get update apt-get install sudo sudo apt-get install git cmake g++ libcurl4-openssl-dev
# Install protobuf
sudo apt-get install protobuf-compiler libprotobuf-dev
# Install grpc
sudo apt-get install -y libgrpc++-dev libgrpc-dev protobuf-compiler-grpc
```

Step 2: Install the OpenTelemetry C++ library.

```bash
git clone --recurse-submodules https://github.com/open-telemetry/opentelemetry-cpp cd opentelemetry-cpp mkdir build && cd build cmake -DBUILD_TESTING=OFF -DWITH_OTLP_GRPC=ON -DWITH_OTLP_HTTP=ON .. cmake --build . --target all
# Install directly to /usr/local (recommended)
cmake --install .
# Or, install to a specified path
# cmake --install . --prefix /opentelemetry-cpp-lib
```

Step 3: Use the OpenTelemetry C++ library in your project. Report data over HTTP.
1. Create a project.

```
mkdir otel-http-export-demo cd otel-http-export-demo
```

2. Write the project's CMakeLists.txt file.

```
cmake_minimum_required(VERSION 3.25.1) # Set version to your cmake version. Use cmake --version to check. project(otel-http-export-demo) # Enter the project name in the parentheses add_executable(otel-http-export-demo http_exporter.cc) # Project name and main file find_package(opentelemetry-cpp CONFIG REQUIRED) find_package(protobuf) find_package(gRPC) find_package(CURL) find_package(nlohmann_json) include_directories("${OPENTELEMETRY_CPP_INCLUDE_DIRS}") target_link_libraries(
    opentelemetry_trace
    opentelemetry_common
    opentelemetry_http_client_curl
    opentelemetry_exporter_otlp_http
    opentelemetry_exporter_otlp_grpc
    opentelemetry_exporter_otlp_http_client
    opentelemetry_otlp_recordable
    opentelemetry_resources
```

`)`
3. Write the demo code.
The test code contains only one http_exporter.cc file. Replace ${ServiceName} with your application name and ${HostName} with your hostname.

```
// Copyright The OpenTelemetry Authors // SPDX-License-Identifier: Apache-2.0
#include "opentelemetry/exporters/otlp/otlp_http_exporter_factory.h"
#include "opentelemetry/exporters/otlp/otlp_http_exporter_options.h"
#include "opentelemetry/context/propagation/global_propagator.h"
#include "opentelemetry/context/propagation/text_map_propagator.h"
#include "opentelemetry/exporters/ostream/span_exporter_factory.h"
#include "opentelemetry/nostd/shared_ptr.h"
#include "opentelemetry/sdk/trace/simple_processor_factory.h"
#include "opentelemetry/sdk/trace/tracer_context.h"
#include "opentelemetry/sdk/trace/tracer_context_factory.h"
#include "opentelemetry/sdk/trace/tracer_provider_factory.h"
#include "opentelemetry/trace/propagation/http_trace_context.h"
#include "opentelemetry/trace/provider.h"
#include "opentelemetry/ext/http/client/http_client_factory.h"
#include "opentelemetry/sdk/resource/semantic_conventions.h"
#include "opentelemetry/sdk/common/global_log_handler.h"
```

```
#include <string>
namespace trace = opentelemetry::trace; namespace trace_sdk = opentelemetry::sdk::trace; namespace otlp = opentelemetry::exporter::otlp; namespace internal_log = opentelemetry::sdk::common::internal_log; namespace resource = opentelemetry::sdk::resource; namespace nostd = opentelemetry::nostd; namespace
```

`{`

```
    opentelemetry::exporter::otlp::OtlpHttpExporterOptions opts;
    void InitTracer()
```

`{`

```
        // Create an OTLP exporter
        auto exporter  = otlp::OtlpHttpExporterFactory::Create(opts);
        auto processor =
trace_sdk::SimpleSpanProcessorFactory::Create(std::move(exporter));
        resource::ResourceAttributes attributes = {
                {resource::SemanticConventions::kServiceName, "${ServiceName}"}, // Appl
ication name
                {resource::SemanticConventions::kHostName, "${HostName}"}
```

};

```
        auto resource = opentelemetry::sdk::resource::Resource::Create(attributes);
        std::shared_ptr<opentelemetry::trace::TracerProvider> provider =
                trace_sdk::TracerProviderFactory::Create(std::move(processor), std::move
(resource));
        // Set the Trace provider
        trace::Provider::SetTracerProvider(provider);
```

`}`

```
    void CleanupTracer()
```

`{`

```
        std::shared_ptr<opentelemetry::trace::TracerProvider> none;
        trace::Provider::SetTracerProvider(none);
```

`}`

```
    nostd::shared_ptr<trace::Tracer> get_tracer()
```

`{`

```
        auto provider = trace::Provider::GetTracerProvider();
        return provider->GetTracer("library name to trace", OPENTELEMETRY_SDK_VERSION);
```

`}`

```
    void f1()
```

`{`

```
        auto scoped_span = trace::Scope(get_tracer()->StartSpan("f1"));
```

`}`

```
    void f2()
```

`{`

```
        auto scoped_span = trace::Scope(get_tracer()->StartSpan("f2"));
        f1();
        f1();
```

`}`

```
    void foo_library()
```

`{`

```
        auto scopedspan = trace::Scope(gettracer()->StartSpan("library"));
```

`_` `_`

```
        f2();
```

`}`

```
} // namespace
```

`/*`

```xml
  Usage:
  - example_otlp_http
  - example_otlp_http <URL>
  - example_otlp_http <URL> <DEBUG>
  - example_otlp_http <URL> <DEBUG> <BIN>
  <DEBUG> = yes|no, to turn console debug on or off
  <BIN> = bin, to export in binary format
```

`*/`

```
int main(int argc, char *argv[])
```

`{`

```
    if (argc > 1)
```

`{`

```
        opts.url = argv[1];
        if (argc > 2)
```

`{`

```
            std::string debug  = argv[2];
            opts.console_debug = debug != "" && debug != "0" && debug != "no";
```

`}`

```
        if (argc > 3)
```

`{`

```
            std::string binary_mode = argv[3];
            if (binary_mode.size() >= 3 && binary_mode.substr(0, 3) == "bin")
```

`{`

```
                opts.content_type = otlp::HttpRequestContentType::kBinary;
```

`}` `}` `}`

```
    if (opts.console_debug)
```

`{`

```
        internal_log::GlobalLogHandler::SetLogLevel(internal_log::LogLevel::Debug);
```

`}`

```
    InitTracer();
    foo_library();
    CleanupTracer();
```

`}`
4. Compile the project.

```
mkdir build && cd build && cmake .. && make
```

5. Run the project.

```
./otel-http-export-demo ${http-endpoint}
```

### 1.4 Obtain OpenTelemetry Access Configuration

**Configuration**

This topic describes how to obtain OpenTelemetry access configurations.

**Operation Guide**

**Step 1: Obtain arms-pop Domain Name Information**

1. Log on to Apsara Infrastructure Management.
2. In the menu bar at the top of Apsara Uni-manager Operations Console, select **Platform**
**O&M > Apsara Infrastructure Management > Resource Management**.
3. In the navigation pane on the left, click **Resource Management >**
**Product & Cluster O&M**. In the search box for **Product | Cluster**, enter `ARMS` to
search.
4. In the product list, click **Cluster Details** to the right of the destination cluster.
5. On the Cluster Details page, click the **Resource Details** tab. Then, click
**Resource Application Result** for the resource named **arms-pop** to view the `domain`
information.

**Step 2: Invoke an API to Obtain the Endpoint**

Execute the following command:

```bash
curl -v http://<domain>:8099/pop/xtrace/XtraceGetToken.json? duserId="149666**********" -dagentType="OpenTelemetry" -dregionId="cn-*****"
```

Parameter description:

| Parameter | Description |
|---|---|
| domain | The domain information obtained from arms- pop. |
| userId | You can organize the userId information. |
| agentType | The value is OpenTelemetry. |

| regionId | The unique identity of a region. |
|---|---|

Example result:

**Step 3: Simulate Usage**

When using the Endpoint obtained from ARMS, add protocol information, such as HTTP or HTTPS.

**Step 4: View on Page**

1. Log on to the ARMS console.
2. In the navigation pane on the left, select **Tracing Analysis > Application List**.
3. If you find the configured application on the Application List page, the access is successful.

### 1.5 Monitor Java applications

#### 1.5.1 Use Jaeger to report the trace data of Java applications

**Java applications**

Before you can view the trace data of your application, you must use a client to report the trace data to the Application Real-Time Monitoring (ARMS) console. This topic describes how to use Jaeger to report the trace data of Java applications.

**Prerequisites**

The endpoint is obtained. For more information, see Get the endpoint.

**Background information**

Jaeger is an open source distributed tracing system. It is compatible with the OpenTracing API and has joined the Cloud Native Computing Foundation (CNCF). Jaeger aggregates real-time monitoring data that is collected from multiple heterogeneous systems. To use Jaeger to report the trace data of a Java application to the ARMS console, you must first instrument the application. You can instrument the application manually or by using existing components. You can use the following methods to instrument the application: Manually instrument a Java application Use Spring Cloud to instrument a Java application Use gRPC to instrument a Java application

**Report data**

The following figure shows how to report data without using the Jaeger agent.

**Manually instrument a Java application**

To use Jaeger to report the trace data of a Java application to the ARMS console, you must first instrument the application. In this example, the application is manually instrumented.
1. Download the demo project. Go to the **manualDemo** directory and run the program as
prompted in the README.md file.
2. Add the following dependency for Jaeger clients to the pom.xml file:

```xml
<dependency>
    <groupId>io.jaegertracing</groupId>
    <artifactId>jaeger-client</artifactId>
    <version>0.31.0</version>
</dependency>
```

3. Configure initialization parameters and create a tracer.
A tracer can be used to create spans to record distributed operation time, transmit data across servers in pass-through mode by using the Extract or Inject method, or specify the current span. The tracer also contains data such as the endpoint used for data reporting, local IP address, sample rate, and service name. You can adjust the sample rate to reduce the overhead that is caused by data reporting.

```
// Replace manualDemo with your application name. io.jaegertracing.Configuration config = new io.jaegertracing.Configuration("manualDemo"); io.jaegertracing.Configuration.SenderConfiguration sender = new io.jaegertracing.Configuration.SenderConfiguration(); // Replace <endpoint> with the endpoint that is displayed on the Access point informa tion tab of the Cluster Configurations page in the ARMS console. sender.withEndpoint("<endpoint>"); config.withSampler(new io.jaegertracing.Configuration.SamplerConfiguration().withType("const").withParam(1)); config.withReporter(new io.jaegertracing.Configuration.ReporterConfiguration().withSender(sender).withMaxQueueS e(10000)); GlobalTracer.register(config.getTracer());
```

4. Record the request data.

```
Tracer tracer = GlobalTracer.get(); // Create a span. Span span = tracer.buildSpan("parentSpan").withTag("myTag", "spanFirst").start(); tracer.scopeManager().activate(span, false); tracer.activeSpan().setTag("methodName", "testTracing"); // The business logic. secondBiz(); span.finish();
```

5. **Optional.** You can run the preceding code to create a root span to record the root
operation of a request. If you want to record the previous and subsequent operations of a request, specify the context information.

```
Tracer tracer = GlobalTracer.get(); Span parentspan = tracer.activeSpan(); Tracer.SpanBuilder spanBuilder = tracer.buildSpan("childSpan").withTag("myTag", "span Second"); if (parentspan !=null) {
    spanBuilder.asChildOf(parentspan).start();
```

`}`

```
Span childSpan = spanBuilder.start(); tracer.scopeManager().activate(childSpan, false); // The business logic. childSpan.finish(); tracer.activeSpan().setTag("methodName", "testCall");
```

6. **Optional.** To troubleshoot issues in an efficient manner, you can add custom tags to a
record. For example, you can add custom tags to a request to indicate whether an error occurs or describe the returned values of the request.

```
tracer.activeSpan().setTag("methodName", "testCall");
```

7. In a distributed system, remote procedure call (RPC) requests are sent together with trace
data. Trace data contains the values of the TraceId, ParentSpanId, SpanId, and Sampled parameters. You can call the Extract or Inject method to pass through trace data in HTTP request headers. The following figure shows the entire process.

```
   Client Span                                                Server Span
┌──────────────────┐ ┌──────────────────┐ │ │ │ │ │ TraceContext │ Http Request Headers │ TraceContext │ │ ┌──────────────┐ │ ┌───────────────────┐ │ ┌──────────────┐ │ │ │ TraceId │ │ │ X-B3-TraceId │ │ │ TraceId │ │ │ │ │ │ │ │ │ │ │ │ │ │ ParentSpanId │ │ Inject │ X-B3-ParentSpanId │Extract │ │ ParentSpanId │ │ │ │ ├─┼─────────>│ ├────────┼>│ │ │ │ │ SpanId │ │ │ X-B3-SpanId │ │ │ SpanId │ │ │ │ │ │ │ │ │ │ │ │ │ │ Sampled │ │ │ X-B3-Sampled │ │ │ Sampled │ │ │ └──────────────┘ │ └───────────────────┘ │ └──────────────┘ │ │ │ │ │ └──────────────────┘ └──────────────────┘
```

i. Call the Inject method on the client to specify the context information.

```java
private void attachTraceInfo(Tracer tracer, Span span, final Request request) {
        tracer.inject(span.context(), Format.Builtin.TEXT_MAP, new TextMap() {
            @Override
            public void put(String key, String value) {
                request.setHeader(key, value);
```

`}`

```java
            @Override
            public Iterator<Map.Entry<String, String>> iterator() {
                throw new UnsupportedOperationException("TextMapInjectAdapter should
only be used with Tracer.inject()");
```

`}`

```
        });
```

`}` ii. Call the Extract method on the server to extract the context information.

```java
protected Span extractTraceInfo(Request request, Tracer tracer) {
    Tracer.SpanBuilder spanBuilder = tracer.buildSpan("/api/xtrace/test03");
    try {
        SpanContext spanContext = tracer.extract(Format.Builtin.TEXT_MAP, new TextM
apExtractAdapter(request.getAttachments()));
        if (spanContext != null) {
            spanBuilder.asChildOf(spanContext);
```

`}`

```
    } catch (Exception e) {
        spanBuilder.withTag("Error", "extract from request fail, error msg:" +
e.getMessage());
```

`}`

```
    return spanBuilder.start();
```

`}`

**Use Spring Cloud to instrument a Java application**

To use Jaeger to report the trace data of a Java application to the ARMS console, you must first instrument the application. In this example, the application is instrumented by using Spring Cloud. You can use Spring Cloud to instrument the following applications: @Async, @Scheduled, Executors Feign, HystrixFeign Hystrix JDBC JMS Mongo RabbitMQ Redis RxJava Spring Messaging: Trace messages are sent by using message channels. Spring Web (RestControllers, RestTemplates, WebAsyncTask) Standard Logging: Logs are added to the current span. WebSocket STOMP Zuul Perform the following steps to use Spring Cloud to instrument an application:
1. Download the demo project. Go to the **springMvcDemo/webmvc4-boot** directory and run
the program as instructed in the README.md file.
2. Open the pom.xml file and add JAR dependencies.

```xml
<dependency>
   <groupId>io.opentracing.contrib</groupId>
  <artifactId>opentracing-spring-cloud-starter</artifactId>
  <version>0.2.0</version>
</dependency> <dependency>
  <groupId>io.jaegertracing</groupId>
  <artifactId>jaeger-client</artifactId>
  <version>0.31.0</version>
</dependency>
```

3. Add an OpenTracing Tracer bean.

```
@Bean public io.opentracing.Tracer tracer() {
    io.jaegertracing.Configuration config = new
io.jaegertracing.Configuration("springFrontend");
    io.jaegertracing.Configuration.SenderConfiguration sender = new
io.jaegertracing.Configuration.SenderConfiguration();
    sender.withEndpoint("<endpoint>");
    config.withSampler(new
io.jaegertracing.Configuration.SamplerConfiguration().withType("const").withParam(1));
    config.withReporter(new
io.jaegertracing.Configuration.ReporterConfiguration().withSender(sender).withMaxQueueS e(10000));
    return config.getTracer();
```

`}`

**Use gRPC to instrument a Java application**

To use Jaeger to report the trace data of a Java application to the ARMS console, you must first instrument the application. In this example, an application is instrumented by using Google Remote Procedure Call (gRPC). Use gRPC to instrument an application by performing the following steps:
1. Download the demo project. Go to the **grpcDemo** directory and run the program as
instructed in the README.md file.
2. Open the pom.xml file and add JAR dependencies.

```xml
<dependency>
    <groupId>io.opentracing.contrib</groupId>
    <artifactId>opentracing-grpc</artifactId>
    <version>0.0.7</version>
</dependency>
```

3. Initialize the Tracer object on the server, create the ServerTracingInterceptor class, and
then add an interceptor to the server.

```java
import io.opentracing.Tracer;
    public class YourServer {
        private int port;
        private Server server;
        private final Tracer tracer;
        private void start() throws IOException {
            ServerTracingInterceptor tracingInterceptor = new
ServerTracingInterceptor(this.tracer);
            // If GlobalTracer is used:
            // ServerTracingInterceptor tracingInterceptor = new
ServerTracingInterceptor();
            server = ServerBuilder.forPort(port)
                .addService(tracingInterceptor.intercept(someServiceDef))
                .build()
                .start();
```

`}` `}`
4. Initialize the Tracer object on the client, create the ClientTracingInterceptor class, and then
add an interceptor to the client.

```java
import io.opentracing.Tracer;
    public class YourClient {
        private final ManagedChannel channel;
        private final GreeterGrpc.GreeterBlockingStub blockingStub;
        private final Tracer tracer;
        public YourClient(String host, int port) {
            channel = ManagedChannelBuilder.forAddress(host, port)
                .usePlaintext(true)
                .build();
            ClientTracingInterceptor tracingInterceptor = new
ClientTracingInterceptor(this.tracer);
            // If GlobalTracer is used:
            // ClientTracingInterceptor tracingInterceptor = new
ClientTracingInterceptor();
            blockingStub =
GreeterGrpc.newBlockingStub(tracingInterceptor.intercept(channel));
```

`}` `}`

**FAQ**

Q: What do I do if no data is reported to the console after I run the demo program? A: Debug the io.jaegertracing.thrift.internal.senders.HttpSender.send(Process process, List<Span> spans) method and check the return value of data reporting. If an HTTP 403 error is returned, you have specified an invalid endpoint. Change the endpoint to a valid one.

**References**

Jaeger official website Jaeger client for Java Component library of OpenTracing OpenTracing Spring Cloud

#### 1.5.2 Use Zipkin to report the trace data of Java applications

**Java applications**

Before you can view the trace data of your application, you must use a client to report the trace data to Tracing Analysis. This topic describes how to use Zipkin to report the trace data of Java applications.

**Prerequisites**

The endpoint is obtained. For more information, see Get the endpoint.

**Background information**

After years of development, Zipkin boasts comprehensive support for various Java frameworks. For more information, visit GitHub. To use Zipkin to report the trace data of a Java application to Tracing Analysis, you must first instrument the application. You can instrument the application manually or by using existing components. Zipkin supports the following instrumentation methods: Manually instrument a Java application Use Spring 2.5 MVC or Spring 3.0 MVC to instrument a Java application Use Spring 4.0 MVC or Spring Boot to instrument a Java application Use Dubbo to instrument a Java application Use Spring Sleuth to instrument a Java application

**Report data**

The following figure shows how to report data by using Zipkin.

**Manually instrument a Java application**

If you want to manually instrument a Java application, you must write instrumentation code.

> **Note:** Click to download the demo project. Then, go to the **manualDemo** directory and follow the instructions in the README.md file to run the program.

1. Add a JAR package as a dependency.

```xml
<dependency>
            <groupId>io.zipkin.brave</groupId>
            <artifactId>brave</artifactId>
            <version>5.4.2</version>
        </dependency>
        <dependency>
            <groupId>io.zipkin.reporter2</groupId>
            <artifactId>zipkin-sender-okhttp3</artifactId>
            <version>2.7.9</version>
        </dependency>
```

2. Create a Tracer object.

```java
private static final String zipkinEndPoint = "<endpoint>";
  ...
  // Create an object that is used to send data.
  OkHttpSender sender = OkHttpSender.newBuilder().endpoint(zipkinEndPoint).build();
  // Create an object that is used to report data.
  Reporter<Span> reporter = AsyncReporter.builder(sender).build();
  tracing =
Tracing.newBuilder().localServiceName(localServiceName).spanReporter(reporter).build();
```

3. Create a span and a child span.

```java
private void firstBiz() {
        // Create a root span.
        tracing.tracer().startScopedSpan("parentSpan");
        Span span =  tracing.tracer().currentSpan();
        span.tag("key", "firstBiz");
        secondBiz();
        span.finish();
```

`}`

```java
    private void secondBiz() {
        tracing.tracer().startScopedSpanWithParent("childSpan",
tracing.tracer().currentSpan().context());
        Span chindSpan =  tracing.tracer().currentSpan();
        chindSpan.tag("key", "secondBiz");
        chindSpan.finish();
        System.out.println("end tracing,id:" + chindSpan.context().traceIdString());
```

`}`
4. Optional. Add custom tags to a span for quick troubleshooting. For example, you can add a
custom tag to record the return value of a request or check whether an error occurs.

```
tracer.activeSpan().setTag("http.status_code", "500");
```

5. In a distributed system, remote procedure call (RPC) requests are sent together with trace
data. Trace data contains the values of the TraceId, ParentSpanId, SpanId, and Sampled parameters. You can call the Extract or Inject method to pass through trace data in HTTP request headers. The following figure shows the entire process.

```
   Client Span                                                Server Span
┌──────────────────┐ ┌──────────────────┐ │ │ │ │ │ TraceContext │ Http Request Headers │ TraceContext │ │ ┌──────────────┐ │ ┌───────────────────┐ │ ┌──────────────┐ │ │ │ TraceId │ │ │ X-B3-TraceId │ │ │ TraceId │ │ │ │ │ │ │ │ │ │ │ │ │ │ ParentSpanId │ │ Inject │ X-B3-ParentSpanId │Extract │ │ ParentSpanId │ │ │ │ ├─┼─────────>│ ├────────┼>│ │ │ │ │ SpanId │ │ │ X-B3-SpanId │ │ │ SpanId │ │ │ │ │ │ │ │ │ │ │ │ │ │ Sampled │ │ │ X-B3-Sampled │ │ │ Sampled │ │ │ └──────────────┘ │ └───────────────────┘ │ └──────────────┘ │ │ │ │ │ └──────────────────┘ └──────────────────┘
```

i. Call the Inject method on the client to specify the context information.

```
// start a new span representing a client request
    oneWaySend = tracer.nextSpan().name(service + "/" + method).kind(CLIENT);
    --snip--
    // Add the trace context to the request, so it can bepropagated in-band
    tracing.propagation().injector(Request::addHeader)
                     .inject(oneWaySend.context(), request);
   // fire off the request asynchronously, totally dropping any response
   request.execute();
   // start the client side and flush instead of finish
   oneWaySend.start().flush();
```

ii. Call the Extract method on the server to extract the context information.

```
// pull the context out of the incoming request extractor = tracing.propagation().extractor(Request::getHeader); // convert that context to a span which you can name and add tags to oneWayReceive = nextSpan(tracer, extractor.extract(request))
    .name("process-request")
    .kind(SERVER)
    ... add tags etc.
// start the server side and flush instead of finish oneWayReceive.start().flush(); // you should not modify this span anymore as it is complete. However, // you can create children to represent follow-up work. next = tracer.newSpan(oneWayReceive.context()).name("step2").start();
```

**Use Spring 2.5 MVC or Spring 3.0 MVC to instrument a Java**

**application**

You can use Spring 2.5 MVC or Spring 3.0 MVC to instrument a Java application.

> **Note:** Click to download the demo project. Then, go to the **springMvcDemo\webmvc3|webmvc25** directory and follow the instructions in the README.md file to run the program.

1. Configure the tracing object in the **applicationContext.xml** file.

```xml
<bean class="zipkin2.reporter.beans.OkHttpSenderFactoryBean">
  <property name="endpoint" value="<endpoint>"/>
</bean> <!-- allows us to read the service name from spring config --> <context:property-placeholder/> <bean class="brave.spring.beans.TracingFactoryBean">
  <property name="localServiceName" value="brave-webmvc3-example"/>
  <property name="spanReporter">
    <bean class="zipkin2.reporter.beans.AsyncReporterFactoryBean">
      <property name="encoder" value="JSON_V2"/>
      <property name="sender" ref="sender"/>
      <!-- wait up to half a second for any in-flight spans on close -->
      <property name="closeTimeout" value="500"/>
    </bean>
  </property>
  <property name="propagationFactory">
    <bean class="brave.propagation.ExtraFieldPropagation" factory-
method="newFactory">
      <constructor-arg index="0">
        <util:constant static-field="brave.propagation.B3Propagation.FACTORY"/>
      </constructor-arg>
      <constructor-arg index="1">
        <list>
          <value>user-name</value>
        </list>
      </constructor-arg>
    </bean>
  </property>
  <property name="currentTraceContext">
    <bean class="brave.spring.beans.CurrentTraceContextFactoryBean">
      <property name="scopeDecorators">
        <bean class="brave.context.log4j12.MDCScopeDecorator" factory-
method="create"/>
      </property>
    </bean>
  </property>
</bean> <bean class="brave.spring.beans.HttpTracingFactoryBean">
  <property name="tracing" ref="tracing"/>
</bean>
```

2. Add an interceptors object.

```xml
<bean class="brave.httpclient.TracingHttpClientBuilder"
      factory-method="create">
    <constructor-arg type="brave.http.HttpTracing" ref="httpTracing"/>
  </bean>
  <bean factory-bean="httpClientBuilder" factory-method="build"/>
  <bean
class="org.springframework.web.servlet.mvc.annotation.DefaultAnnotationHandlerMapping">
    <property name="interceptors">
      <list>
        <bean class="brave.spring.webmvc.SpanCustomizingHandlerInterceptor"/>
      </list>
    </property>
  </bean>
  <!-- Loads the controller -->
  <context:component-scan base-package="brave.webmvc"/>
```

3. Add a filter object.

```xml
<!-- Add the delegate to the standard tracing filter and map it to all paths --> <filter>
  <filter-name>tracingFilter</filter-name>
  <filter-class>brave.spring.webmvc.DelegatingTracingFilter</filter-class>
</filter> <filter-mapping>
  <filter-name>tracingFilter</filter-name>
  <url-pattern>/*</url-pattern>
</filter-mapping>
```

**Use Spring 4.0 MVC or Spring Boot to instrument a Java**

**application**

You can use Spring 4.0 MVC or Spring Boot to instrument a Java application.

> **Note:** Click to download the demo project. Then, go to the **springMvcDemo\webmvc4-** **boot|webmv4** directory and follow the instructions in the README.md file to run the program.

1. Configure the tracing and filter objects.

```
/** Configuration for how to send spans to Zipkin */
  @Bean Sender sender() {
    return OkHttpSender.create("<endpoint>");
```

`}`

```
  /** Configuration for how to buffer spans into messages for Zipkin */
  @Bean AsyncReporter<Span> spanReporter() {
    return AsyncReporter.create(sender());
```

`}`

```
  /** Controls aspects of tracing such as the name that shows up in the UI */
  @Bean Tracing tracing(@Value("${spring.application.name}") String serviceName) {
    return Tracing.newBuilder()
        .localServiceName(serviceName)
        .propagationFactory(ExtraFieldPropagation.newFactory(B3Propagation.FACTORY, "
user-name"))
        .currentTraceContext(ThreadLocalCurrentTraceContext.newBuilder()
            .addScopeDecorator(MDCScopeDecorator.create()) // puts trace IDs into
logs
            .build()
```

`)`

```
        .spanReporter(spanReporter()).build();
```

`}`

```
  /** decides how to name and tag spans. By default they are named the same as the ht
tp method. */
  @Bean HttpTracing httpTracing(Tracing tracing) {
    return HttpTracing.create(tracing);
```

`}`

```java
  /** Creates client spans for http requests */
  // We are using a BPP as the Frontend supplies a RestTemplate bean prior to this co
nfiguration
  @Bean BeanPostProcessor connectionFactoryDecorator(final BeanFactory beanFactory) {
    return new BeanPostProcessor() {
      @Override public Object postProcessBeforeInitialization(Object bean, String bea
nName) {
        return bean;
```

`}`

```java
      @Override public Object postProcessAfterInitialization(Object bean, String bean
Name) {
        if (!(bean instanceof RestTemplate)) return bean;
        RestTemplate restTemplate = (RestTemplate) bean;
        List<ClientHttpRequestInterceptor> interceptors =
            new ArrayList<>(restTemplate.getInterceptors());
        interceptors.add(0, getTracingInterceptor());
        restTemplate.setInterceptors(interceptors);
        return bean;
```

`}`

```
      // Lazy lookup so that the BPP doesn't end up needing to proxy anything.
      ClientHttpRequestInterceptor getTracingInterceptor() {
        return
TracingClientHttpRequestInterceptor.create(beanFactory.getBean(HttpTracing.class));
```

`}` }; `}`

```
  /** Creates server spans for http requests */
  @Bean Filter tracingFilter(HttpTracing httpTracing) {
    return TracingFilter.create(httpTracing);
```

`}`

```java
  @Autowired SpanCustomizingAsyncHandlerInterceptor webMvcTracingCustomizer;
  /** Decorates server spans with application-defined web tags */
  @Override public void addInterceptors(InterceptorRegistry registry) {
    registry.addInterceptor(webMvcTracingCustomizer);
```

`}`
2. Configure auto-configuration in the spring.factories file.

```
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\ brave.webmvc.TracingConfiguration
```

**Use Dubbo to instrument a Java application**

You can use Dubbo to instrument a Java application.

> **Note:** Click to download the demo project. Then, go to the **dubboDem** directory and follow the instructions in the README.md file to run the program.

1. Add a JAR package as a dependency.

```xml
<dependency>
            <groupId>io.zipkin.brave</groupId>
            <artifactId>brave-instrumentation-dubbo-rpc</artifactId>
            <version>5.4.2</version>
        </dependency>
        <dependency>
            <groupId>io.zipkin.brave</groupId>
            <artifactId>brave-spring-beans</artifactId>
            <version>5.4.2</version>
        </dependency>
        <dependency>
            <groupId>io.zipkin.brave</groupId>
            <artifactId>brave-context-slf4j</artifactId>
            <version>5.4.2</version>
        </dependency>
        <dependency>
            <groupId>io.zipkin.reporter2</groupId>
            <artifactId>zipkin-sender-okhttp3</artifactId>
            <version>2.7.9</version>
        </dependency>
        <dependency>
            <groupId>io.zipkin.brave</groupId>
            <artifactId>brave</artifactId>
            <version>5.4.2</version>
        </dependency>
        <dependency>
            <groupId>io.zipkin.reporter2</groupId>
            <artifactId>zipkin-sender-okhttp3</artifactId>
            <version>2.7.9</version>
        </dependency>
```

2. Configure the tracing object.

```
<bean class="zipkin2.reporter.beans.OkHttpSenderFactoryBean">
        <property name="endpoint" value="<endpoint>"/>
    </bean>
    <bean class="brave.spring.beans.TracingFactoryBean">
        <property name="localServiceName" value="double-provider"/>
        <property name="spanReporter">
            <bean class="zipkin2.reporter.beans.AsyncReporterFactoryBean">
                <property name="sender" ref="sender"/>
                <!-- wait up to half a second for any in-flight spans on close -->
                <property name="closeTimeout" value="500"/>
            </bean>
        </property>
        <property name="currentTraceContext">
            <bean class="brave.spring.beans.CurrentTraceContextFactoryBean">
                <property name="scopeDecorators">
                    <bean class="brave.context.slf4j.MDCScopeDecorator" factory-method
="create"/>
                </property>
            </bean>
        </property>
    </bean>
```

3. Configure the filter object.

```
// The configurations on the server. <dubbo:provider filter="tracing" /> // The configurations on the client. <dubbo:consumer filter="tracing" />
```

**Use Spring Sleuth to instrument a Java application**

You can use Spring Sleuth to instrument a Java application.

> **Note:** Click to download the demo project. Then, go to the **sleuthDemo** directory and follow the instructions in the README.md file to run the program.

1. Add a JAR package as a dependency.

```xml
<dependency>
            <groupId>io.zipkin.brave</groupId>
            <artifactId>brave</artifactId>
            <version>5.4.2</version>
        </dependency>
        <dependency>
            <groupId>io.zipkin.reporter2</groupId>
            <artifactId>zipkin-sender-okhttp3</artifactId>
            <version>2.7.9</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>2.0.1.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-sleuth-core</artifactId>
            <version>2.0.1.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-sleuth-zipkin</artifactId>
            <version>2.0.1.RELEASE</version>
        </dependency>
```

2. Configure the application.yml file.

> **Note:** You must replace `<endpoint_short>` with the endpoint for your client and region. You can log on to the Application Real-Time Monitoring Service (ARMS) console and obtain the public endpoint that ends with api/v2/spans on the Access point information tab of the **Cluster Configurations** page.

```bash
spring:
   application:
     # This ends up as the service name in zipkin
     name: sleuthDemo
   zipkin:
     # Uncomment to send to zipkin, replacing 192.168.99.100 with your zipkin IP addr
ess
     baseUrl: <endpoint_short>
   sleuth:
     sampler:
       probability: 1.0
 sample:
   zipkin:
     # When enabled=false, traces log to the console. Comment to send to zipkin
     enabled: true
```

**FAQ**

Q: Why am I unable to find any data on specific websites after the demo program is run? A: Insert a breakpoint to debug the **parseResponse** method in
**zipkin2.reporter.okhttp3.HttpCall** and view the return value of the request for reporting
data. If a 403 error is returned, the username configuration is invalid. You must check the endpoint configuration.

**References**

brave-webmvc-example brave-instrumentation spring-cloud-zipkin-sleuth-tutorial

### 1.6 Monitor PHP applications

#### 1.6.1 Use Zipkin to report the trace data of PHP applications

**PHP applications**

Before you can view the trace data of your application, you must use a client to report the trace data to Tracing Analysis. This topic describes how to use Zipkin to report the trace data of PHP applications.

**Prerequisites**

The endpoint is obtained. For more information, see Get the endpoint.

**Report data**

The following figure shows how to report data by using Zipkin.

**Instrument an application**

To use Zipkin to report the data of an PHP application to Tracing Analysis, you must first instrument the application.
1. Install Zipkin PHP.

```
composer require openzipkin/zipkin
```

2. Create a tracer. You can use tracers to create spans that record the time of distributed
operations. Tracers contain information such as the endpoint from which data is reported, the IP address of the on-premises machine, and the sampling rate. You can adjust the sampling rate to reduce the cost of reporting data.

```
function create_tracing($endpointName, $ipv4)
```

`{`

```
    $endpoint = Endpoint::create($endpointName, $ipv4, null, 2555);
    /* Do not copy this logger into production.
     * Read https://github.com/Seldaek/monolog/blob/master/doc/01-usage.md#log-levels
```

`*/`

```
    $logger = new \Monolog\Logger('log');
    $logger->pushHandler(new \Monolog\Handler\ErrorLogHandler());
    $reporter = new
Zipkin\Reporters\Http(\Zipkin\Reporters\Http\CurlFactory::create());
    $sampler = BinarySampler::createAsAlwaysSample();
    $tracing = TracingBuilder::create()
        ->havingLocalEndpoint($endpoint)
        ->havingSampler($sampler)
        ->havingReporter($reporter)
        ->build();
    return $tracing;
```

`}`
3. Record the request data.

```
$rootSpan = $tracer->newTrace(); $rootSpan->setName('encode') $rootSpan->start(); try {
  doSomethingExpensive();
} finally {
  $rootSpan->finish();
```

`}`

> **Note:** You can run the preceding code to create a root span that records the root operation of a request. If you want to record the previous and next operations of a request, specify the context information. Example:

```
$span = $tracer->newChild($parentSpan->getContext()); $span->setName('encode'); $span->start(); try {
  doSomethingExpensive();
} finally {
  $span->finish();
```

> `}`

4. **Optional.** To troubleshoot issues in an efficient manner, you can add custom tags to a
record. For example, you can add custom tags to a request to indicate whether an error occurs or describe the returned values of the request.

```
$span->tag('http.status_code', $resultCode);
```

5. **Optional.** The sampling rate for a request is determined by the root operation. Generally,
a sampling policy is created when you create a Tracer object. You can locally override the sampling policy. Example:

```java
private function newTrace(Request $request) {
  $flags = SamplingFlags::createAsEmpty();
  if (strpos($request->getUri(), '/experimental') === 0) {
    $flags = DefaultSamplingFlags::createAsSampled();
  } else if (strpos($request->getUri(), '/static') === 0) {
    $flags = DefaultSamplingFlags::createAsSampled();
```

`}`

```
  return $tracer->newTrace($flags);
```

`}`
6. In a distributed system, remote procedure call (RPC) requests are sent together with trace
data. Trace data contains the values of the TraceId, ParentSpanId, SpanId, and Sampled parameters. You can call the Extract or Inject method to pass through trace data in HTTP request headers. The following figure shows the entire process.

```
   Client Span                                                Server Span
┌──────────────────┐ ┌──────────────────┐ │ │ │ │ │ TraceContext │ Http Request Headers │ TraceContext │ │ ┌──────────────┐ │ ┌───────────────────┐ │ ┌──────────────┐ │ │ │ TraceId │ │ │ X-B3-TraceId │ │ │ TraceId │ │ │ │ │ │ │ │ │ │ │ │ │ │ ParentSpanId │ │ Inject │ X-B3-ParentSpanId │Extract │ │ ParentSpanId │ │ │ │ ├─┼─────────>│ ├────────┼>│ │ │ │ │ SpanId │ │ │ X-B3-SpanId │ │ │ SpanId │ │ │ │ │ │ │ │ │ │ │ │ │ │ Sampled │ │ │ X-B3-Sampled │ │ │ Sampled │ │ │ └──────────────┘ │ └───────────────────┘ │ └──────────────┘ │ │ │ │ │ └──────────────────┘ └──────────────────┘
```

i. Call the Inject method on the client to specify the context information.

```
// configure a function that injects a trace context into a request $injector = $tracing->getPropagation()->getInjector(new RequestHeaders); // before a request is sent, add the current span's context to it $injector->inject($span->getContext(), $request);
```

ii. Call the Extract method to extract the context information.

```
// configure a function that extracts the trace context from a request $extracted = $tracing->getPropagation()->extractor(new RequestHeaders); $span = $tracer->newChild($extracted) $span->setKind(Kind\SERVER);
```

**Getting started**

The following official Zipkin PHP example shows how to use Zipkin to report the trace data of a PHP application.
1. Download the Demo file.
2. Change the endpoint for data reporting in the functions.php file. Replace $reporter = new
Zipkin\Reporters\Http(\Zipkin\Reporters\Http\CurlFactory::create()); with the following code:

```json
reporter = new Zipkin\Reporters\Http(\Zipkin\Reporters\Http\CurlFactory::create(), ['endpoint_url' => '<endpoint> ',]);
```

3. Install the required dependency.

```
// As of zipkin php is still in 1.0.0-betaX rm composer.lock && composer install
```

4. Start the Dubbo service.

```bash
# Run the composer run-frontend command on Terminal 1.
# Run the composer run-backend command on Terminal 2.
```

5. Report trace data on the fronted page.

```bash
curl http://localhost:8081
```

6. View the reported data in the Application Real-Time Monitoring Service (ARMS) console.

**FAQ**

Q: Why is no data reported after I perform the preceding operations? A: Check whether the endpoint is valid.

**References**

Zipkin official website Zipkin source code for PHP zipkin-php-example

### 1.7 Monitor Go applications

#### 1.7.1 Use Jaeger to report the trace data of Go applications

**Go applications**

Before you can view the trace data of your application, you must use a client to report the trace data to Tracing Analysis. This topic describes how to use Jaeger to report the trace data of Go applications.

**Prerequisites**

The endpoint is obtained. For more information, see Get the endpoint.

**Report data**

The following figure shows how to report data without using the Jaeger agent.

**Getting started**

1. Run the following command to download the Demo file to the GOPATH/src directory:

```
wget http://arms-apm.oss-cn-hangzhou.aliyuncs.com/tools/tracingtest.zip && unzip trac ingtest.zip
```

2. Modify configuration items.

```
sender := transport.NewHTTPTransport(
        // Specify the endpoint. The endpoint varies based on regions.
        "<endpoint>",
```

`)`
3. Run the following command to upload data:

```
go run main.go http done grpc done
```

> **Note:** The following errors indicate that the specified account and password are invalid. Specify a valid account and password and try again.

```
go run main.go http done 2018/09/17 21:11:54 ERROR: error when flushing the buffer: error from collector:
```

4. View the reported data in the Application Real-Time Monitoring Service (ARMS) console.

**Directly report data**

1. Import **jaeger-client-go**.
Package path: github.com/uber/jaeger-client-go Version: 2.11.0 or later For example, if you use Glide, you must add the following code to the glide.yaml file:

```java
package: github.com/uber/jaeger-client-go version: ^2.11.0 subpackages: transport
```

2. Create a Tracer object.

```
func NewJaegerTracer(service string) (opentracing.Tracer, io.Closer) {
    sender := transport.NewHTTPTransport(
       // Specify the endpoint. The endpoint varies based on regions.
        "<endpoint>",
```

`)`

```
   tracer, closer:= jaeger.NewTracer(service,
        jaeger.NewConstSampler(true),
   jaeger.NewRemoteReporter(sender))
   return tracer, closer
```

`}`
3. Create a span and pass data.
If no parent span is available, use the following code:

```
// Create a span. span := tracer.StartSpan("myspan") // Configure a tag. clientSpan.SetTag("mytag", "123") // Pass the ID of the trace. tracer.Inject(span.Context(), opentracing.HTTPHeaders, opentracing.HTTPHeadersCarrier(req.Header)) ... defer span.Finish()
```

If a parent span is available, use the following code:

```
// Extract a SpanContext from an HTTP request or an RPC request. spanCtx, _ := tracer.Extract(opentracing.HTTPHeaders, opentracing.HTTPHeadersCarrier(r.Header)) span := tracer.StartSpan("myspan", opentracing.ChildOf(spanCtx)) ... defer span.Finish()
```

#### 1.7.2 Use Zipkin to report the trace data of a Go application

**Go application**

Before you can view the trace data of your application, you must use a client to report the trace data to the Application Real-Time Monitoring (ARMS) console. This topic describes how to use Zipkin to report the trace data of Go applications.

**Prerequisites**

The endpoint is obtained. For more information, see Get the endpoint.

**Report data**

The following figure shows how to report data by using Zipkin.

**Instrument an application**

To use Zipkin to report the trace data of a Go application to the ARMS console, you must first instrument the application.
1. Add dependencies.

```
[[constraint]]
  name = "github.com/openzipkin/zipkin-go"
  version = "0.1.1"
[[constraint]]
  name = "github.com/gorilla/mux"
  version = "1.6.2"
```

2. Create a tracer. You can use tracers to create spans that record the time of distributed
operations. Tracers contain information such as the endpoint from which data is reported, the IP address of the on-premises machine, and the sampling rate. You can adjust the sampling rate to reduce the cost of reporting data.

```
func getTracer(serviceName string, ip string) *zipkin.Tracer {
  // create a reporter to be used by the tracer
  reporter := httpreporter.NewReporter("http://tracing-analysis-dc-
hz.aliyuncs.com/adapt_aokcdqnxyz@123456ff_abcdef123@abcdef123/api/v2/spans")
  // set-up the local endpoint for our service
  endpoint, _ := zipkin.NewEndpoint(serviceName, ip)
  // set-up our sampling strategy
  sampler := zipkin.NewModuloSampler(1)
  // initialize the tracer
  tracer, _ := zipkin.NewTracer(
    reporter,
    zipkin.WithLocalEndpoint(endpoint),
    zipkin.WithSampler(sampler),
```

`)`

```
  return tracer;
```

`}`
3. Record the request data.

```
// tracer can now be used to create spans. span := tracer.StartSpan("some_operation") // ... do some work ... span.Finish() // Output:
```

> **Note:** You can run the preceding code to create a root span that records the root operation of a request. If you want to record the previous and next operations of a request, specify the context information. Sample code:

```
childSpan := tracer.StartSpan("some_operation2", zipkin.Parent(span.Context()))
    // ... do some work ...
childSpan.Finish()
```

4. **Optional.** To troubleshoot issues in an efficient manner, you can add custom tags to a
record. For example, you can add custom tags to a request to indicate whether an error occurs or describe the returned values of the request.

```
childSpan.Tag("http.status_code", statusCode)
```

5. In a distributed system, remote procedure call (RPC) requests are sent together with trace
data. Trace data contains the values of the TraceId, ParentSpanId, SpanId, and Sampled parameters. You can call the Extract or Inject method to pass through trace data in HTTP request headers. The following figure shows the entire process.

```
   Client Span                                                Server Span
┌──────────────────┐ ┌──────────────────┐ │ │ │ │ │ TraceContext │ Http Request Headers │ TraceContext │ │ ┌──────────────┐ │ ┌───────────────────┐ │ ┌──────────────┐ │ │ │ TraceId │ │ │ X-B3-TraceId │ │ │ TraceId │ │ │ │ │ │ │ │ │ │ │ │ │ │ ParentSpanId │ │ Inject │ X-B3-ParentSpanId │Extract │ │ ParentSpanId │ │ │ │ ├─┼─────────>│ ├────────┼>│ │ │ │ │ SpanId │ │ │ X-B3-SpanId │ │ │ SpanId │ │ │ │ │ │ │ │ │ │ │ │ │ │ Sampled │ │ │ X-B3-Sampled │ │ │ Sampled │ │ │ └──────────────┘ │ └───────────────────┘ │ └──────────────┘ │ │ │ │ │ └──────────────────┘ └──────────────────┘
```

> **Note:** Zipkin allows you to pass through context information over HTTP or Google Remote Procedure Call (gRPC).

i. Call the Inject method on the client to specify the context information.

```
req, _ := http.NewRequest("GET", "/", nil) // configure a function that injects a trace context into a reques injector := b3.InjectHTTP(req) injector(sp.Context())
```

ii. Call the Extract method on the server to extract the context information.

```
req, _ := http.NewRequest("GET", "/", nil)
        b3.InjectHTTP(req)(sp.Context())
        b.ResetTimer()
        _ = b3.ExtractHTTP(copyRequest(req))
```

**Getting started with Zipkin**

The following example shows how to use Zipkin to report the trace data of a Go application.
1. Download the Demo file.
2. Modify the endpoint for data reporting in the utils.go file.
3. Install the required dependency.

```
dep ensure
```

4. Run the test application.

```
go run main.go
```

5. View the reported data in the ARMS console.

**FAQ**

Q: Why is no data reported after I perform the preceding steps? A: You can check the error message that is returned when the application is running and check whether the value of the **endpoint_url** parameter is valid. For example, if the `failed` `the request with status code 403` message is returned, the username or password is invalid.

**References**

Zipkin official website Zipkin Library for Go

### 1.8 Monitor Node.js applications

#### 1.8.1 Use Jaeger to report the trace data of Node.js applications

**Node.js applications**

Before you can view the trace data of your application, you must use a client to report the trace data to Tracing Analysis. This topic describes how to use Jaeger to report the trace data of Node.js applications.

**Prerequisites**

Dependencies on the jaeger-client library are added to the package of the Node.js project.

```json
"dependencies": {
    "jaeger-client": "^3.12.0"
```

`}` The endpoint is obtained. For more information, see Get the endpoint.

**Report data**

The following figure shows how to report data without using the Jaeger agent.

**Procedure**

1. Configure parameters for initialization.

```
const initTracer = require("jaeger-client").initTracer; const config = {
    serviceName: 'node-service',
    sampler: {
        type: "const",
        param: 1
```

`},`

```
    reporter: {
        collectorEndpoint: "<endpoint>"
```

`},` };
2. Create a Tracer object.

```
const tracer = initTracer(config);
```

3. Create a span.

```
const span = tracer.startSpan("say-hello"); // Optional. Configure one or more tags. span.setTag("tagKey-01", "tagValue-01"); // Optional. Log one or more events. span.log({event: "timestamp", value: Date.now()}); // Finish the span. span.finish();
```

4. Log on to the Application Real-Time Monitoring Service (ARMS) console and view the trace.

**Complete sample code based on Express**

```
const express = require("express"); const initTracer = require("jaeger-client").initTracer; const app = express(); const config = {
    serviceName: 'node-service',
    sampler: {
        type: "const",
        param: 1
```

`},`

```
    reporter: {
        collectorEndpoint: "<endpoint>"
```

`},` };

```
const tracer = initTracer(config); app.all('*', function (req, res, next) {
    req.span = tracer.startSpan("say-hello");
    next();
}); app.get("/api", function (req, res) {
    const span = req.span;
    span.log({event: "timestamp", value: Date.now()});
    req.span.finish();
    res.send({code: 200, msg: "success"});
}); app.listen(3000, '127.0.0.1', function () {
    console.log('start');
});
```

**References**

jaeger-client-node opentracing-javascript

### 1.9 Monitor .NET applications

#### 1.9.1 Use Jaeger to report the trace data of .NET applications

**.NET applications**

Before you can view the trace data of your application, you must use a client to report the trace data to the Application Real-Time Monitoring (ARMS) console. This topic describes how to use Jaeger to report the trace data of .NET applications. The methods also apply to C# applications.

**Prerequisites**

The endpoint is obtained. For more information, see Get the endpoint.

**Background information**

Jaeger is an open source distributed tracing system, which is created and used by Uber. Jaeger is compatible with the OpenTracing API and is a member of the Cloud Native Computing Foundation (CNCF). Jaeger aggregates real-time monitoring data that is collected from multiple heterogeneous systems. The OpenTracing community provides multiple components that support the following .NET frameworks: ASP.NET Core Entity Framework Core .NET Core BCL types (HttpClient) gRPC

**Report data**

The following figure shows how to report data without using the Jaeger agent.

**Use ASP.NET Core to automatically instrument a .NET**

**application**

Use ASP.NET Core to instrument an application by performing the following steps:

> **Note:** You can click here to download the demo project. Then, you can go to the webapi.dotnetcore directory and perform the steps in the README.md file to run the demo program.

1. Install the NuGet packages.

```
// Add the following components: // OpenTracing.Contrib.NetCore: the ASP.NET Core middleware. // Jaeger: an implementation component of OpenTracing. // Microsoft.Extensions.Logging.Console: a log component. dotnet add package OpenTracing.Contrib.NetCore dotnet add package Jaeger dotnet add package Microsoft.Extensions.Logging.Console
```

2. Use the Configure method in the Startup.cs file of the project to register the middleware.

```
// Register OpenTracing.Contrib.NetCore to instrument the application. services.AddOpenTracing(); // Filter requests that are collected by HttpClient to obtain requests for using Jaeg er to report data. var httpOption = new HttpHandlerDiagnosticOptions(); httpOption.IgnorePatterns.Add(req => req.RequestUri.AbsolutePath.Contains("/api/traces")); services.AddSingleton(Options.Create(httpOption));
```

3. Initialize and register Jaeger.

```
// Add a Jaeger tracer. services.AddSingleton<ITracer>(serviceProvider =>
```

`{`

```
    string serviceName = serviceProvider.GetRequiredService<IHostingEnvironment>().Ap
plicationName;
    ILoggerFactory loggerFactory = serviceProvider.GetRequiredService<ILoggerFactory>
();
     Configuration.SenderConfiguration senderConfiguration = new
Configuration.SenderConfiguration(loggerFactory)
     // Obtain the Jaeger endpoint in the ARMS console.
          .WithEndpoint("http://tracing-analysis-dc-
sz.aliyuncs.com/adapt_your_token/api/traces");
      // This will log to a default localhost installation of Jaeger.
      var tracer = new Tracer.Builder(serviceName)
          .WithSampler(new ConstSampler(true))
          .WithReporter(new
RemoteReporter.Builder().WithSender(senderConfiguration.GetSender()).Build())
           .Build();
      // Allows code that can't use DI to also access the tracer.
      GlobalTracer.Register(tracer);
      return tracer;
});
```

**Use gRPC to automatically instrument a .NET application**

Use gRPC to instrument an application by performing the following steps:

> **Note:** You can click here to download the demo project. Then, you can perform the steps in the README.md file to run the demo program.

1. Install the NuGet packages.

```
// Add the following components: // OpenTracing.Contrib.Grpc: the gRPC middleware. // Jaeger: an implementation component of OpenTracing. // Microsoft.Extensions.Logging.Console: a log component. dotnet add package OpenTracing.Contrib.grpc dotnet add package Jaeger
```

2. Initialize the ITracer object.

```
public static Tracer InitTracer(string serviceName, ILoggerFactory loggerFactory)
```

`{`

```
            Configuration.SamplerConfiguration samplerConfiguration = new
Configuration.SamplerConfiguration(loggerFactory)
                .WithType(ConstSampler.Type)
                .WithParam(1);
            Configuration.SenderConfiguration senderConfiguration = new
Configuration.SenderConfiguration(loggerFactory)
                    // Obtain the Jaeger endpoint in the ARMS console.
                   .WithEndpoint("http://tracing-analysis-dc-
sz.aliyuncs.com/adapt_your_token/api/traces");
            Configuration.ReporterConfiguration reporterConfiguration = new
Configuration.ReporterConfiguration(loggerFactory)
                .WithSender(senderConfiguration);
            return (Tracer)new Configuration(serviceName, loggerFactory)
                .WithSampler(samplerConfiguration)
                .WithReporter(reporterConfiguration)
                .GetTracer();
```

`}`
3. Add instrumentation on the server. Build the ServerTracingInterceptor object and bind the
object to the application.

```
ILoggerFactory loggerFactory = new LoggerFactory().AddConsole(); ITracer tracer = TracingHelper.InitTracer("dotnetGrpcServer", loggerFactory); ServerTracingInterceptor tracingInterceptor = new ServerTracingInterceptor(tracer); Server server = new Server
```

`{`

```
    Services = { Greeter.BindService(new GreeterImpl()).Intercept(tracingInterceptor)
```

`},`

```
     Ports = { new ServerPort("localhost", Port, ServerCredentials.Insecure) }
```

};
4. Add instrumentation on the client. Build the ServerTracingInterceptor object and bind the
object to the specified channel.

```
ILoggerFactory loggerFactory = new LoggerFactory().AddConsole(); ITracer tracer = TracingHelper.InitTracer("dotnetGrpcClient", loggerFactory); ClientTracingInterceptor tracingInterceptor = new ClientTracingInterceptor(tracer); Channel channel = new Channel("127.0.0.1:50051", ChannelCredentials.Insecure); var client = new Greeter.GreeterClient(channel.Intercept(tracingInterceptor));
```

**Manually instrument a .NET application**

The preceding sections describe how to use existing components to instrument .NET applications. You can also manually instrument .NET applications. In this case, you can use Jaeger to report the trace data of the applications to the ARMS console.

> **Note:** You can click here to download the demo project. Then, you can go to the ManualDemo directory and perform the steps in the README.md file to run the demo program.

1. Install the NuGet packages.

```
// Jaeger: an implementation component of OpenTracing. // Microsoft.Extensions.Logging.Console: a log component. dotnet add package Microsoft.Extensions.Logging.Console dotnet add package Jaeger
```

2. Build an ITracer object. The ITracer object is an object defined by OpenTracing. You can use
Jaeger to build this object. When you build this object, you can configure the object to specify the Jaeger endpoint and sample rate.

```
public static ITracer InitTracer(string serviceName, ILoggerFactory loggerFactory)
```

`{`

```
    Configuration.SamplerConfiguration samplerConfiguration = new
Configuration.SamplerConfiguration(loggerFactory)
          .WithType(ConstSampler.Type)
          .WithParam(1);
    Configuration.SenderConfiguration senderConfiguration = new
Configuration.SenderConfiguration(loggerFactory)
           // Obtain the Jaeger endpoint in the ARMS console.
          .WithEndpoint("http://tracing-analysis-dc-
sz.aliyuncs.com/adapt_your_token/api/traces");
   Configuration.ReporterConfiguration reporterConfiguration = new
Configuration.ReporterConfiguration(loggerFactory)
          .WithSender(senderConfiguration);
   return (Tracer)new Configuration(serviceName, loggerFactory)
          .WithSampler(samplerConfiguration)
          .WithReporter(reporterConfiguration)
        .GetTracer();
```

`}`
3. Register the ITracer object with GlobalTracer to facilitate code calling.

```
GlobalTracer.Register(InitTracer("dotnetManualDemo", loggerFactory ));
```

4. Record the request data.

```
ITracer tracer = GlobalTracer.Instance; ISpan span = tracer.BuildSpan("parentSpan").WithTag("mytag","parentSapn").Start(); tracer.ScopeManager.Activate(span, false); // ... do something span.Finish();
```

> **Note:** You can run the preceding code to record the root operation of a request. If you want to record the previous and next operations of the request, call the AsChildOf method.

Sample code:

```
ITracer tracer = GlobalTracer.Instance; ISpan parentSpan = tracer.ActiveSpan; ISpan childSpan =tracer.BuildSpan("childSpan").AsChildOf(parentSpan).WithTag("mytag", "spanSecond").Start(); tracer.ScopeManager.Activate(childSpan, false); // ... do something childSpan.Finish();
```

5. Optional. Add custom tags to a span for quick troubleshooting. For example, you can add a
custom tag to record the return value of a request or check whether an error occurs.

```
tracer.activeSpan().setTag("http.status_code", "200");
```

6. In a distributed system, remote procedure call (RPC) requests are sent together with trace
data. Trace data contains the values of the TraceId, ParentSpanId, SpanId, and Sampled parameters. You can call the Extract or Inject method to pass through trace data in HTTP request headers. The following figure shows the entire process.

```
   Client Span                                                Server Span
┌──────────────────┐ ┌──────────────────┐ │ │ │ │ │ TraceContext │ Http Request Headers │ TraceContext │ │ ┌──────────────┐ │ ┌───────────────────┐ │ ┌──────────────┐ │ │ │ TraceId │ │ │ X-B3-TraceId │ │ │ TraceId │ │ │ │ │ │ │ │ │ │ │ │ │ │ ParentSpanId │ │ Inject │ X-B3-ParentSpanId │Extract │ │ ParentSpanId │ │ │ │ ├─┼─────────>│ ├────────┼>│ │ │ │ │ SpanId │ │ │ X-B3-SpanId │ │ │ SpanId │ │ │ │ │ │ │ │ │ │ │ │ │ │ Sampled │ │ │ X-B3-Sampled │ │ │ Sampled │ │ │ └──────────────┘ │ └───────────────────┘ │ └──────────────┘ │ │ │ │ │ └──────────────────┘ └──────────────────┘
```

i. Call the Inject method on the client to specify the context information.

```
Tracer.Inject(span.Context, BuiltinFormats.HttpHeaders, new HttpHeadersInjectAdapter(request.Headers));
```

ii. Call the Extract method on the server to extract the context information.

```
ISpanContext extractedSpanContext = _tracer.Extract(BuiltinFormats.HttpHeaders, new RequestHeadersExtractAdapter(request.Headers)); ISpan childSpan = _tracer.BuildSpan(operationName).AsChildOf(extractedSpanContext);
```

**FAQ**

Q: What do I do if no data is reported to the console after I run the demo program? A: Check whether the endpoint in senderConfiguration is valid.

```
Configuration.SenderConfiguration senderConfiguration = new Configuration.SenderConfiguration(loggerFactory)
           // Obtain the Jaeger endpoint in the ARMS console.
          .WithEndpoint("http://tracing-analysis-dc-
sz.aliyuncs.com/adapt_your_token/api/traces");
```

**References**

Jaeger official website jaeger-client-csharp csharp-netcore csharp-grpc

#### 1.9.2 Use Zipkin to report the trace data of .NET applications

**.NET applications**

Before you can view the trace data of your application, you must use a client to report the trace data to the Application Real-Time Monitoring (ARMS) console. This topic describes how to use Zipkin to report the trace data of .NET applications. The methods also apply to C# applications.

**Prerequisites**

The endpoint is obtained. For more information, see Get the endpoint.

**Report data**

The following figure shows how to report data by using Zipkin.

**Use ASP.NET Core to automatically instrument a .NET**

**application**

Perform the following steps to use ASP.NET Core to instrument an application:

> **Note:** You can click here to download the demo project. Then, you can perform the steps in the README.md file to run the demo program.

1. Install the NuGet packages.

```
// Add the following components: // zipkin4net.middleware.aspnetcore: the ASP.NET Core middleware. // zipkin4net: a tracer. dotnet add package zipkin4net.middleware.aspnetcore dotnet add package zipkin4nete
```

2. Register and start Zipkin.

```
lifetime.ApplicationStarted.Register(() => {
    TraceManager.SamplingRate = 1.0f;
    var logger = new TracingLogger(loggerFactory, "zipkin4net");
    // Obtain the Zipkin endpoint in the ARMS console. Take note that the endpoint do
es not contain /api/v2/spans.
    var httpSender = new HttpZipkinSender("http://tracing-analysis-dc-
hz.aliyuncs.com/adapt_your_token", "application/json");
    var tracer = new ZipkinTracer(httpSender, new JSONSpanSerializer());
    TraceManager.RegisterTracer(tracer);
    TraceManager.Start(logger);
 });
lifetime.ApplicationStopped.Register(() => TraceManager.Stop()); app.UseTracing(applicationName);
```

3. Add TracingHandler to HttpClient that sends GET or POST requests.

```
public override void ConfigureServices(IServiceCollection services)
```

`{`

```
    services.AddHttpClient("Tracer").AddHttpMessageHandler(provider =>
        TracingHandler.WithoutInnerHandler(provider.GetService<IConfiguration>()["app
licationName"]));
```

`}`

**Use OWIN to automatically instrument a .NET application**

Use Open Web Interface for .NET (OWIN) to instrument an application by performing the following steps:

> **Note:** You can click here to download the demo project. Then, you can perform the steps in the README.md file to run the demo program.

1. Install the NuGet packages.

```
// Add the following components: // zipkin4net.middleware.aspnetcore: the ASP.NET Core middleware. // zipkin4net: a tracer. dotnet add package zipkin4net.middleware.aspnetcore dotnet add package zipkin4nete
```

2. Register and start Zipkin.

```
// Configure tracing. TraceManager.SamplingRate = 1.0f; var logger = new ConsoleLogger(); // Obtain the Zipkin endpoint in the ARMS console. Take note that the endpoint does not contain /api/v2/spans. var httpSender = new HttpZipkinSender("http://tracing-analysis-dchz.aliyuncs.com/adapt_your_token", "application/json"); var tracer = new ZipkinTracer(httpSender, new JSONSpanSerializer()); TraceManager.RegisterTracer(tracer); TraceManager.Start(logger); //Stop TraceManager on app dispose var properties = new AppProperties(appBuilder.Properties); var token = properties.OnAppDisposing; if (token != CancellationToken.None)
```

`{`

```
token.Register(() =>
```

`{`

```
TraceManager.Stop(); });
```

`}` `//`

```
// Setup Owin Middleware appBuilder.UseZipkinTracer(System.Configuration.ConfigurationManager.AppSettings["appli tionName"]);
```

3. Add TracingHandler to HttpClient that sends GET or POST requests.

```
using (var httpClient = new HttpClient(new TracingHandler(applicationName)))
```

`{`

```
       var response = await httpClient.GetAsync(callServiceUrl);
       var content = await response.Content.ReadAsStringAsync();
       await context.Response.WriteAsync(content);
```

`}`

**Manually instrument a .NET application**

The preceding sections describe how to use existing components to instrument .NET applications. You can also manually instrument .NET applications. In this case, you can use Zipkin to report the trace data of the applications to the ARMS console.

> **Note:** You can click here to download the demo project. Then, you can perform the steps in the README.md file to run the demo program.

1. Install the NuGet packages.

```
// Add zipkin4net as a tracer. dotnet add package zipkin4nete
```

2. Register and start Zipkin.

```
TraceManager.SamplingRate = 1.0f; var logger = new ConsoleLogger(); // Obtain the Zipkin endpoint in the ARMS console. Take note that the endpoint does not contain /api/v2/spans. var httpSender = new HttpZipkinSender("http://tracing-analysis-dchz.aliyuncs.com/adapt_your_token", "application/json"); var tracer = new ZipkinTracer(httpSender, new JSONSpanSerializer()); TraceManager.RegisterTracer(tracer); TraceManager.Start(logger);
```

3. Record the request data.

```
var trace = Trace.Create(); Trace.Current = trace; trace.Record(Annotations.ClientSend()); trace.Record(Annotations.Rpc("client")); trace.Record(Annotations.Tag("mytag", "spanFrist")); trace.Record(Annotations.ServiceName("dotnetManual")); // ...do something testCall(); trace.Record(Annotations.ClientRecv());
```

> **Note:** You can run the preceding code to record the root operation of a request. If you want to record the previous and next operations of the request, call the ChildOf method. Sample code:

```
var trace = Trace.Current.Child(); Trace.Current = trace; trace.Record(Annotations.ServerRecv()); trace.Record(Annotations.Rpc("server")); trace.Record(Annotations.Tag("mytag", "spanSecond")); trace.Record(Annotations.ServiceName("dotnetManual")); // ...do something trace.Record(Annotations.ServerSend());
```

4. **Optional.** To troubleshoot issues in an efficient manner, you can add custom tags to a
record. For example, you can add custom tags to a request to indicate whether an error occurs or describe the returned values of the request.

```
tracer.activeSpan().setTag("http.status_code", "200");
```

5. In a distributed system, remote procedure call (RPC) requests are sent together with trace
data. Trace data contains the values of the TraceId, ParentSpanId, SpanId, and Sampled parameters. You can call the Extract or Inject method to pass through trace data in HTTP request headers. The following figure shows the entire process.

```
   Client Span                                                Server Span
┌──────────────────┐ ┌──────────────────┐ │ │ │ │ │ TraceContext │ Http Request Headers │ TraceContext │ │ ┌──────────────┐ │ ┌───────────────────┐ │ ┌──────────────┐ │ │ │ TraceId │ │ │ X-B3-TraceId │ │ │ TraceId │ │ │ │ │ │ │ │ │ │ │ │ │ │ ParentSpanId │ │ Inject │ X-B3-ParentSpanId │Extract │ │ ParentSpanId │ │ │ │ ├─┼─────────>│ ├────────┼>│ │ │ │ │ SpanId │ │ │ X-B3-SpanId │ │ │ SpanId │ │ │ │ │ │ │ │ │ │ │ │ │ │ Sampled │ │ │ X-B3-Sampled │ │ │ Sampled │ │ │ └──────────────┘ │ └───────────────────┘ │ └──────────────┘ │ │ │ │ │ └──────────────────┘ └──────────────────┘
```

i. Call the Inject method on the client to specify the context information.

```
_injector.Inject(clientTrace.Trace.CurrentSpan, request.Headers);
```

ii. Call the Extract method on the server to extract the context information.

```
Ivar traceContext = traceExtractor.Extract(context.Request.Headers); var trace = traceContext == null ? Trace.Create() : Trace.CreateFromId(traceContext);
```

**FAQ**

Q: What do I do if no data is reported to the console after I run the demo program? A: Check whether the endpoint in senderConfiguration is valid.

```
// Obtain the Zipkin endpoint in the ARMS console. Take note that the endpoint does not contain /api/v2/spans. var httpSender = new HttpZipkinSender("http://tracing-analysis-dchz.aliyuncs.com/adapt_your_token", "application/json");
```

**References**

Zipkin official website .NET client for Zipkin

### 1.10 Monitor NGINX

#### 1.10.1 Use Zipkin to perform tracing analysis on NGINX

**on NGINX**

NGINX is a free, open source, and high-performance server that serves as an HTTP server and a reverse proxy. You can perform tracing analysis on NGINX to monitor the status of your applications. This topic describes how to perform tracing analysis on NGINX.

**Prerequisites**

The endpoint is obtained. For more information, see Get the endpoint.

**Report data**

The following figure shows how to report data by using Zipkin.

**Overview**

If a slow response occurs in a microservice that uses NGINX as a proxy, you cannot estimate the impact of the slow response because no data is collected. In this case, you can use Tracing Analysis to trace NGINX requests for the microservice and calculate the number of page views that are affected by the slow response.

**Procedure**

1. Pull an image from the registry.

```python
sudo docker pull registry.cn-hangzhou.aliyuncs.com/public-community/nginx-zipkin:0.1
```

2. Run theNGINX Docker image.

```bash
docker run --rm -p 80:80 -e "COLLECTOR_HOST=${ZIPKIN_ENDPOINT}?" -d registry.cn-hang zhou.aliyuncs.com/public-community/nginx-zipkin:0.1
```

Set the ${ZIPKIN_ENDPOINT} variable to the V1 endpoint of Zipkin that you obtain, but remove http:// and add a question mark (?) to the value as the suffix. Sample code:

```bash
docker run --rm -p 80:80 -e "COLLECTOR_HOST=tracing-analysis-dchz.aliyuncs.com/adapt_******_******/api/v1/spans?" -d registry.cnhangzhou.aliyuncs.com/public-community/nginx-zipkin:0.1
```

3. Go to the NGINX page by using a browser.
Enter localhost/nginx.conf in the address bar of a browser or run the curl "localhost/nginx.conf" command to access the nginx.conf file.
4. View the data of the nginx-jaeger application in the Application Real-Time Monitoring
Service (ARMS) console.

**Deploy and trace NGINX in a Docker container**

1. Download, build, and then deploy a Dockerfile:

```bash
wget https://arms-apm.oss-cn-hangzhou.aliyuncs.com/demo/nginx-zipkin-docker.tgz tar -xzvf nginx-zipkin-docker.tgz cd nginx-zipkin // Build the Dockerfile. docker build --rm --tag nginx-jaeger:0.1 .
```

2. Run Docker:

```bash
docker run --rm -p 80:80 -e "COLLECTOR_HOST=${ZIPKIN_ENDPOINT}?" -d nginx-zipkin:0.1
```

Set the ${ZIPKIN_ENDPOINT} variable to the V1 endpoint of Zipkin that you obtain, but remove http:// and add a question mark (?) to the value as the suffix. Sample code:

```bash
docker run --rm -p 80:80 -e "COLLECTOR_HOST=tracing-analysis-dchz.aliyuncs.com/adapt_123@abc_456@efg/api/v1/spans?" -d nginx-zipkin:0.1
```

**Deploy and trace NGINX on an ECS instanceNginx**

1. Run the following command to install NGINX:
i. Download the NGINX source code package and decompress it.

```
wget http://nginx.org/download/nginx-1.14.2.tar.gz tar -xzvf nginx-1.14.2.tar.gz
```

ii. Compile the NGINX source code.

```python
cd nginx-1.14.2 ./configure --with-compat make sudo make install
```

2. Install OpenTracing.
i. Download the OpenTracing package and decompress it.

```
wget https://github.com/opentracing-contrib/nginxopentracing/releases/download/v0.7.0/linux-amd64-nginx-1.14.0ngx_http_module.so.tgz tar -xzvf linux-amd64-nginx-1.14.0-ngx_http_module.so.tgz
```

ii. Copy the .so file to the modules folder of NGINX. If the folder does not exist, create one.

```python
sudo mkdir /usr/local/nginx/modules sudo cp ngx_http_opentracing_module.so /usr/local/nginx/modules/ngx_http_opentracing_module.so
```

3. Use Zipkin to perform tracing analysis.
i. Download Zipkin to a working directory.

```python
wget https://github.com/rnburn/zipkin-cppopentracing/releases/download/v0.5.2/linux-amd64-libzipkin_opentracing_plugin.so.gz gunzip linux-amd64-libzipkin_opentracing_plugin.so.gz sudo cp linux-amd64-libzipkin_opentracing_plugin.so /usr/local/lib/libzipkin_opentracing_plugin.so
```

ii. Configure the /usr/local/nginx/conf/nginx.conf file.

```bash
load_module modules/ngx_http_opentracing_module.so; events {} http {
  opentracing on;
  opentracing_load_tracer /usr/local/lib/libzipkin_opentracing.so /etc/zipkin-confi
g.json;
  server {
    error_log /var/log/nginx/debug.log debug;
    listen 80;
    location  ~ {
      opentracing_operation_name $uri;
      opentracing_trace_locations off;
      # The service that you use to navigate to the proxy. Specify the parameter ba
sed on your business requirements.
      proxy_pass http://127.0.0.1:8081;
      opentracing_propagate_context;
```

`}` `}` `}`

> **Note:** For more information, see the configuration in opentracing-contrib.

iii. Configure the Zipkin parameters in the /etc/zipkin-config.json file. `{`

```json
  "service_name": "nginx",
  "collector_host": "zipkin"
```

`}` If you use the Zipkin service that is managed by Alibaba Cloud, set thecollector_hostparameter to an endpoint of Zipkin.

> **Note:** Enter the V1 endpoint of Zipkin that you obtain, but remove http:// and add a question mark (?) to the value as the suffix.

```json
"collector_host": "tracing-analysis-dchz.aliyuncs.com/adapt_abc123@abc456_abc123@abc356/api/v1/spans?"
```

iv. Configure thesample_rateparameter to specify the sampling rate.

```json
// Set the sampling_rate parameter to 0.1. "sample_rate":0.1
```

v. Run NGINX and access the NGINX service:

```python
sudo /usr/local/nginx/sbin/nginx curl "http://localhost"
```

**Check the result**

Wait for a moment. Then, log on to the ARMS console. If monitoring data appears, the tracing is successful.

**Related information**

nginx-opentracing project jaeger-client-cpp project zipkin-cpp-opentracing Jaeger Example Zipkin Example

## 2 Tutorial

### 2.1 View applications

On the Applications page, you can view the key metrics of all monitored applications, including the number of requests and errors in the current day and the response time. You can also add custom tags to applications and filter applications by tag.

**Procedure**

1. Log on to the Application Real-Time Monitoring Service (ARMS) console.
2. In the left-side navigation pane, choose **Tracing > Applications**.

**Sort applications**

You can click the up or down arrow next to one of the following columns to sort applications in ascending or descending order based on the column:

**Requests Today**

**Errors Today**

**Response Time**

**Add tags to an application**

You can add custom tags to applications and filter applications by tag.
1. Move the pointer over the application to which you want to add tags, click the
icon in the **Labels** column, and then select **Manage Labels**.
2. On the **Labels** tab, click **Manage Application Labels**.
3. In the **Manage Application Labels** dialog box, click the
icon and enter a custom tag. Then, click **Determine**. In the **Success** message, click **Determine**.

> **Important:** If you delete a tag in the **Manage Application Labels** dialog box, the tag is removed from all applications to which the tag is previously added.

4. Return to the **Applications** page. Find the application to which you want to add a tag, click
the icon in the **Labels** column, and then select the tag that you specify.

**Filter applications by tag**

On the Applications page, you can click one or more tags in the **Select Label** section to search for all applications that have at least one of the selected tags.

### 2.2 View the overall information about an application

**about an application**

On the Application Overview page of an application, you can view the key performance metrics and topology of an application.

**Background information**

After the data of an application is reported to the Application Real-Time Monitoring Service (ARMS) console, Tracing Analysis starts to monitor the application in an all-around manner. On the **Application Overview** page, you can view the key performance metrics of the application. You can also view the topology to check the upstream and downstream services of your application and their dependencies.

**View the key performance metrics of the application**

On the **Overall Analysis** tab, you can view the key performance metrics of an application.
1. Log on to the Tracing Analysis console.
2. In the left-side navigation pane, choose **Tracing > Applications**.
3. On the **Applications** page, click the name of your application.
4. On the **Overall Analysis** tab of the **Application Overview** page, view the following key
performance metrics: The total number of requests, average response time, number of errors, and number of spans in the specified time range, along with the percentage changes compared to the same day last week and the previous day. The line chart of how many times your application is called by upstream services and the response time, and how many times your application calls downstream services and the response time. The 10 spans that require the most time and their line charts of average response time.

**View the topology of the application**

On the **Topology Graph** tab, you can obtain a better view of the upstream and downstream services of your application and the call relationships between the services and the application. Then, you can identify the performance bottlenecks of your application.
1. Log on to the Tracing Analysis console.
2. In the left-side navigation pane, choose **Tracing > Applications**.
3. On the **Applications** page, click the name of your application.
4. On the **Application Overview** page, click the **Topology Graph** tab. On the **Topology**
**Graph** tab, view the following information:
The topology of service calls for the application in the specified time range. The number of calls on databases, calls on the client, calls on the server, and internal calls, average response time, and error rate in the specified time range. The line charts of the number of requests, response time, and error rate in each minute of the specified time range.

**Specify a time range**

You can select a predefined time range or specify a custom time range. In the upper-right corner of the page, click the date and time picker and select a predefined time range, such as **Last 30 Minutes**, **Today**, or **This Week**. If no predefined time ranges meet your business requirements, select **Custom**. Select a start time and an end time in the calendar or enter a start time and an end time, and then click **OK**.

> **Note:** The date is in the `YYYY-MM-DD` format and the time is in the `HH:MM` format.

Figure 1 Date and time picker

### 2.3 View application details

On the Application Details page of an application, you can view the key metrics, call topology, and traces of an application on each server where it is deployed.

**View key metrics and call topology**

On the **Application Details** page of an application, the **Overview** tab displays all servers where the application is deployed. You can sort the applications by response time, number of requests, or number of exceptions. After you select a server from the server list, you can view the detailed call topology of the application on the **Overview** tab. You can also view the time series curves of the response time, number of requests, and number of exceptions.
1. Log on to the Application Real-Time Monitoring Service (ARMS) console.
2. In the left-side navigation pane, choose **Tracing > Applications**.
3. On the **Applications** page, click the name of your application.
4. In the left-side navigation pane, click **Application Details**. Then, click **All** or select a
server from the server list on the left. Then, you can view the call topology and key metrics on the **Overview** tab.

> **Note:** To sort the servers where the application is deployed, you can click the **Response** **Time**, **Requests**, or **Exceptions** tab, and then click the upward or downward arrow next to the name of the tab. To filter the servers, you can enter a keyword in the search box and click the search icon.

> **Note:** If you want to switch to a different application, select the new application from the Application Name drop-down list in the upper-left corner of the page.

**View traces**

The **Traces** tab displays up to 100 traces that consume the most amount of time on the specified host within the specified period of time. Figure 1 Traces tab

> **Note:** In the **Status** column, the green icon indicates that the time consumed is less than 500 milliseconds. The yellow icon indicates that the time consumed ranges from 500 milliseconds to 1,000 milliseconds. The red icon indicates that the time consumed is greater than 1,000 milliseconds or that one of the tag keys of the trace is set to `error` .

On the **Traces** tab, you can perform one of the following operations based on your business requirements: Enter a value that is accurate to milliseconds in the **Takes Longer Than (ms)** field and click **Query**. Then, the traces whose time consumed is greater than the specified value are displayed on the Traces tab. Select **Exceptions** and click **Query**. Then, abnormal traces are displayed on the Traces tab. Click the up or down arrow next to **Generation Time** or **Status** to sort the traces in descending or ascending order. Click the ID of a trace to go to the **Traces** page. The page displays the waterfall chart of the trace.

**View the waterfall chart of a trace**

The **Traces** tab displays the following information about a trace: start time, duration, number of applications, depth, number of spans, span name, timeline chart, and application name. Move the pointer over the name of a span to view the information about the span, including the duration, start time, tags, and log events.

**Specify a time range**

You can select a predefined time range or specify a custom time range. In the upper-right corner of the page, click the date and time picker and select a predefined time range, such as **Last 30 Minutes**, **Today**, or **This Week**. If no predefined time ranges meet your business requirements, select **Custom**. Select a start time and an end time in the calendar or enter a start time and an end time, and then click **OK**.

> **Note:** The date is in the `YYYY-MM-DD` format and the time is in the `HH:MM` format.

Figure 2 Date and time picker

### 2.4 View the details of span calls

On the Interface Calls page of an application, you can view the performance metrics of the span calls on the client, span calls on the server, and internal span calls of an application. You can also view the details of span calls for the upstream services that call the application and the downstream services that are called by the application.

**View the performance metrics of span calls**

On the **Interface Calls** page of an application, you can view all the spans that are involved in application calls. You can sort the spans by response time, number of requests, or number of exceptions. After you click a span in the span list, the **Overview** tab displays the topology of the span and the line charts for the performance metrics of span calls. The performance metrics include the number of requests, response time, and number of errors.
1. Log on to the Application Real-Time Monitoring Service (ARMS) console.
2. In the left-side navigation pane, choose **Tracing > Applications**.
3. On the **Applications** page, click the name of your application.
4. In the left-side navigation pane, click **Interface Calls**. In the left-side span list, click the
span that you want to view. Then, view the topology of the span and the performance metrics of span calls on the **Overview** tab. You can click the **Response Time**, **Requests**, or **Exceptions** tab and click the upward or downward arrow next to the tab name to sort spans in ascending or descending order based on the conditions. You can set the **Call Type** parameter to **All**, **Client**, **Server**, or **Local Calls** to list all spans of the specified call type. To filter the spans, you can enter a keyword in the search box and click the search icon.

**View the details of span calls for upstream and downstream**

**services**

This feature is not supported by the current version.

**View traces**

The **Traces** tab displays up to 100 traces that consume the most amount of time on the specified host within the specified period of time. Figure 1 Traces page

> **Note:** In the **Status** column, the green icon indicates that the time consumed is less than 500 milliseconds. The yellow icon indicates that the time consumed ranges from 500 milliseconds to 1,000 milliseconds. The red icon indicates that the time consumed is greater than 1,000 milliseconds or that one of the tag keys of the trace is set to `error` .

On the **Traces** tab, you can perform one of the following operations based on your business requirements: Enter a value that is accurate to milliseconds in the **Takes Longer Than (ms)** field and click **Query**. Then, the traces whose time consumed is greater than the specified value are displayed on the Traces tab. Select **Exceptions** and click **Query**. Then, abnormal traces are displayed on the Traces tab. Click the up or down arrow next to **Consumed Time** or **Status** to sort the traces in ascending or descending order. Click the ID of a trace to go to the **Traces** page. The page displays the waterfall chart of the trace.

**View the waterfall chart of a trace**

The **Traces** tab displays the following information about a trace: start time, duration, number of applications, depth, number of spans, span name, timeline chart, and application name. Move the pointer over the name of a span to view the information about the span, including the duration, start time, tags, and log events.

**Specify a time range**

You can select a predefined time range or specify a custom time range. In the upper-right corner of the page, click the date and time picker and select a predefined time range, such as **Last 30 Minutes**, **Today**, or **This Week**. If no predefined time ranges meet your business requirements, select **Custom**. Select a start time and an end time in the calendar or enter a start time and an end time, and then click **OK**.

> **Note:** The date is in the `YYYY-MM-DD` format and the time is in the `HH:MM` format.

Figure 2 Date and time picker

### 2.5 View database calls

On the **Database Calls** page of an application, you can analyze SQL statements or query traces.

**View SQL analysis results**

You can query and analyze the number of SQL calls, the average time consumption, and related traces for each SQL statement to locate SQL performance issues.
1. Log on to the Application Real-time Monitoring Service (ARMS) console.
2. In the left-side navigation pane, choose **Tracing > Applications**.
3. On the **Applications** page, click the name of your application.
4. In the left-side navigation pane, click **Database Calls**. On the **SQL Analysis** tab, view the
following metrics: The number of times that SQL statements are called per minute and the chart of the average response time for the calls within the specified period of time The number of times that a specific SQL statement is called and the average response time for the calls within the specified period of time
5. On the **SQL Analysis** tab, perform the following steps as required:
Click **Call Statistics** in the **Actions** column. The number of times that the SQL statement is called per minute and the chart of the average response time for the calls within the specified period of time are displayed. Click **Trace Query** in the **Actions** column. All the traces that are related to the SQL statement are displayed on the **Traces** tab.

**Specify a time range**

You can select a predefined time range or specify a custom time range. In the upper-right corner of the page, click the date and time picker and select a predefined time range, such as **Last 30 Minutes**, **Today**, or **This Week**. If no predefined time ranges meet your business requirements, select **Custom**. Select a start time and an end time in the calendar or enter a start time and an end time, and then click **OK**.

> **Note:** The date is in the `YYYY-MM-DD` format and the time is in the `HH:MM` format.

Figure 1 Date and time picker

### 2.6 Perform diagnosis

This topic describes how to perform diagnosis on exceptions.

**View exceptions**

1. Log on to the Application Real-time Monitoring Service (ARMS) console.
2. In the left-side navigation pane, choose **Tracing > Applications**.
3. On the **Applications** page, click the name of your application.
4. In the left-side navigation pane, click **Exception Diagnosis**.

**View the details of exceptions**

1. On the **Exception Name** tab, click the exception that you want to view.
The **Exception Details** tab displays the name of the exception, the span in which the exception occurs, the summary of the exception, and the number of occurrences. The
**Error Messages** tab displays specific errors.
2. Click **Invocation Trace Query** in the Actions column if you want to view the associated
traces of the exception.

**Specify a time range**

You can select a predefined time range or specify a custom time range. In the upper-right corner of the page, click the date and time picker and select a predefined time range, such as **Last 30 Minutes**, **Today**, or **This Week**. If no predefined time ranges meet your business requirements, select **Custom**. Select a start time and an end time in the calendar or enter a start time and an end time, and then click **OK**.

> **Note:** The date is in the `YYYY-MM-DD` format and the time is in the `HH:MM` format.

Figure 1 Date and time picker

### 2.7 Configure application settings

This topic describes how to enable and manage tags and delete applications.

**Enable tags**

1. Log on to the Application Real-Time Monitoring Service (ARMS) console.
2. In the left-side navigation pane, choose **Tracing > Applications**.
3. On the **Applications** page, find your application and click **Settings** in the **Actions** column.
Alternatively, click the name of your application and click **Application Settings** in the leftside navigation pane.
4. On the **Application Settings** page, click the **Labels** tab.
5. In the **Manage Application Labels** section, select the tags next to **Linked Labels** that
you want to enable for the application and click **Save**.

**Manage tags**

1. Log on to the Tracing Analysis console.
2. In the left-side navigation pane, choose **Tracing Analysis > Applications**.
3. On the **Applications** page, find your application and click **Settings** in the **Actions** column.
Alternatively, click the name of your application and click **Application Settings** in the leftside navigation pane.
4. On the **Application Settings** page, click the **Labels** tab.
5. In the **Manage Application Labels** section, click **Manage Application Labels**.
6. In the **Manage Application Labels** dialog box, perform the following operations based on
your business requirements and click **Determine**. To create a tag, click the Plus icon and enter a tag in the field. To delete a tag, move the pointer over the tag and click the X icon on the left.

> **Important:** If you delete a tag in the **Manage Application Labels** dialog box, the tag is removed from all applications to which the tag is previously added.

**Delete an application**

1. Log on to the Tracing Analysis console.
2. In the left-side navigation pane, choose **Tracing Analysis > Applications**.
3. On the **Applications** page, find your application and click **Settings** in the **Actions** column.
Alternatively, click the name of your application and click **Application Settings** in the leftside navigation pane.
4. On the **Application Settings** page, click the **Delete** tab.
5. In the **Delete Application** section, click **Delete**.
6. In the **Delete an application** dialog box, click **Delete**.

> **Important:** After an application is deleted, all monitoring data of the application is cleared. The deleted data cannot be restored.

### 2.8 Run a multidimensional query

This topic describes how to use the multidimensional query feature to query traces.

**Query traces**

1. Log on to the Application Real-Time Monitoring Service (ARMS) console.
2. In the left-side navigation pane, choose **Tracing > Multidimensional Query**.
3. On the **Advanced Query** page, configure the following parameters based on your business
requirements and click **Search**: Required query parameters TraceID Takes Longer Than (ms) Application Name Span Name Date Optional query parameter: Tag Key Enter a value in the **Tag Key** field and then enter a value in the **Tag Value** field. To add more tag keys and tag values as query conditions, click the blue plus sign to the right of the Tag Value field.

> **Note:** In the search results, click the ID of a trace to go to the **Traces** tab and view the trace details.

4. To save the current configuration of query parameters, click **Favorite** and specify an alias.
5. To delete the favorite configuration of query parameters, click the Delete icon to the right
of the configuration alias.

**Specify a time range**

You can select a predefined time range or specify a custom time range. In the upper-right corner of the page, click the date and time picker and select a predefined time range, such as **Last 30 Minutes**, **Today**, or **This Week**. If no predefined time ranges meet your business requirements, select **Custom**. Select a start time and an end time in the calendar or enter a start time and an end time, and then click **OK**.

> **Note:** The date is in the `YYYY-MM-DD` format and the time is in the `HH:MM` format.

Figure 1 Date and time picker

### 2.9 Global topology

The global topology map in Tracing Analysis displays the upstream and downstream dependencies of your applications.

**View global topology**

1. Log on to the Tracing Analysis console.
2. In the navigation pane on the left, choose **Tracing Analysis > Global topology**.
3. On the **Global topology** page, select a time range in the upper-right corner.
On the Global topology page, you can: Click the plus (+) icon or scroll up with your mouse wheel to zoom in on the topology map. Click the minus (-) icon or scroll down with your mouse wheel to zoom out of the topology map. Click the RESET icon to restore the topology map to its default size. Click a node to highlight its associated paths. Right-click an application node to copy application information, view only its downstream information, or view the application's details. For more information, see View application details. Click the dot on a connection line between nodes to view metrics such as QPS (number of requests), RT (response time), and ERROR (number of errors), and their corresponding time-series curves.

### 2.10 Usage statistics

On the Usage statistics page, you can view the statistics on resource consumption. You can also specify filter conditions to view the resource consumption details of an application within the specified time range.
1. Log on to the Application Real-Time Monitoring Service (ARMS) console.
2. In the left-side navigation pane, choose **Tracing > Usage statistics**
3. In the upper-right corner of the **Usage statistics** page, specify the time range to query.
4. On the **Self-developed probe report** or **Self-developed probe report (global)** tab,
view the number of online applications, number of application performance monitoring (APM) instances, and corresponding usage trends. The Self-developed probe report tab displays the usage data of the current user. The **Self-developed probe report (global)** tab displays the usage data of all users. Only the administrator can view the information on this tab.
