# Instrumentation-Python
파이썬 언어의 계측기입니다.

### 데이터 형식
{
   "tracer":"omegi",
   "traceId":335595244538119375428299518720175183999,
   "error":{
      "exception.type":"<class 'ZeroDivisionError'>",
      "exception.message":"division by zero",
      "exception.flow":{
         "exception.flow":{
            "step.1":"starlette.errors.__call__",
            "step.3":"opentelemetry.__init__.__call__",
            "step.5":"starlette.exceptions.__call__",
            "step.7":"starlette._exception_handler.wrapped_app",
            "step.9":"starlette._exception_handler.wrapped_app",
            "step.11":"starlette.routing.__call__",
            "step.13":"starlette.routing.app",
            "step.15":"starlette.routing.handle",
            "step.17":"starlette.routing.app",
            "step.19":"starlette._exception_handler.wrapped_app",
            "step.21":"starlette._exception_handler.wrapped_app",
            "step.23":"starlette.routing.app",
            "step.25":"fastapi.routing.app",
            "step.27":"fastapi.routing.run_endpoint_function",
            "step.29":"main.throw_error",
            "step.31":"test_service.test_method2"
         }
      }
   },
   "spans":[
      {
         "name":"/app/service/test_service2.py.test_service2_method1",
         "spanId":9353669838611126179,
         "parent_span_id":11582500864749077008,
         "kind":"INTERNAL",
         "span enter-time":1715024079171327257,
         "span exit-time":1715024079171357632,
         "attributes":{
            "module":"/app/service/test_service2.py",
            "name":"test_service2_method1",
            "thread.name":"MainThread",
            "thread.id":"281473017053216",
            "arguments":"('num : 9999999',)"
         }
      },
      {
         "name":"/app/service/test_service.py.test_method3",
         "spanId":5629834827854166605,
         "parent_span_id":11582500864749077008,
         "kind":"INTERNAL",
         "span enter-time":1715024079171300382,
         "span exit-time":1715024079171382924,
         "attributes":{
            "module":"/app/service/test_service.py",
            "name":"test_method3",
            "thread.name":"MainThread",
            "thread.id":"281473017053216",
            "arguments":"()"
         }
      },
      {
         "name":"/app/service/test_service.py.test_method2",
         "spanId":2525535178842684496,
         "parent_span_id":11582500864749077008,
         "kind":"INTERNAL",
         "span enter-time":1715024079171268799,
         "span exit-time":1715024079171388174,
         "attributes":{
            "module":"/app/service/test_service.py",
            "name":"test_method2",
            "thread.name":"MainThread",
            "thread.id":"281473017053216",
            "arguments":"()"
         }
      },
      {
         "name":"/app/main.py.throw_error",
         "spanId":16131143732810558545,
         "parent_span_id":11582500864749077008,
         "kind":"INTERNAL",
         "span enter-time":1715024079171151257,
         "span exit-time":1715024079171390882,
         "attributes":{
            "module":"/app/main.py",
            "name":"throw_error",
            "thread.name":"MainThread",
            "thread.id":"281473017053216",
            "arguments":"()"
         }
      },
      {
         "name":"GET /error",
         "spanId":11582500864749077008,
         "parent_span_id":null,
         "kind":"SERVER",
         "span enter-time":1715024079170271632,
         "span exit-time":1715024079174058424,
         "attributes":{
            "http.scheme":"http",
            "http.host":"172.19.0.4:8083",
            "net.host.port":"8083",
            "http.flavor":"1.1",
            "http.target":"/error",
            "http.url":"http://172.19.0.4:8083/error",
            "http.method":"GET",
            "http.server_name":"localhost:8083",
            "http.user_agent":"PostmanRuntime/7.38.0",
            "net.peer.ip":"192.168.65.1",
            "net.peer.port":"48962",
            "http.route":"/error"
         }
      }
   ]
}
