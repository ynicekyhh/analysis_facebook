from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

PORT = 8000

# handler class 만들어주고, httpserver 객체를 만들어 serve_forever()를 실행시키면 서버가 됨

# django나 flask는 아래처럼 mapping을 시켜준다. -> 장고나 플라스크 공부해서 처리할 것
# REQUEST_MAPPING = {'/graph', 'controller.ex1'}


class TestHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        index = self.path.find('?')
        req_url = self.path if index == -1 else self.path[:self.path.index('?')]
        # 에러처리
        if req_url != '/graph':
            self.send_error(404, 'File Not Found:' + req_url)
            return
        print(req_url)

        # 우선, 심벌 테이블 확인해보자 -> 우리가 만든 function들이 들어가 있음을 확인함
        # print(TestHTTPRequestHandler.__dict__)

        handler_name = 'ex' + self.get_params('ex')
        if handler_name not in TestHTTPRequestHandler.__dict__:
            self.send_error(404, 'File Not Found:' + req_url)
            return
        # 아래와 같이 처리하면 동적으로 ex()함수를 실행시킬 수 있으나, self는 bound_instance_method이고, 아래는 unbound_class_method이니까 self를 넣어줘야함(python-ch2.8 project의 paint.py 참고)
        TestHTTPRequestHandler.__dict__[handler_name](self)

    def get_params(self, name):
        index = self.path.find('?')
        if index == -1:
            return

        qs = self.path[self.path.index('?') + 1:]
        # parse_qs는 dictionary type으로 오니까 작업이 필요함
        params = parse_qs(qs)
        values = params.get(name)

        return None if values is None else values.pop()

    def ex1(self):
        # 응답코드 200은 ok
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        # wfile에서 바로 write를 해 줄 때, 한글이니까 인코딩
        self.wfile.write("<h1>안녕하세요</h1>".encode('utf-8'))

    def ex2(self):
        arr = np.random.normal(5, 3, 500)

        fig, subplots = plt.subplots(2, 1)
        subplots[0].plot(arr, color='red', linestyle='solid')
        subplots[1].hist(arr, bins=20, edgecolor='black', linewidth=1)

        buffer = BytesIO()
        plt.savefig(buffer, dpi=100, bbox_inches='tight')

        # 응답코드 200은 ok
        self.send_response(200)
        self.send_header('Content-Type', 'image/png')
        self.end_headers()
        # wfile에서 바로 write를 해 줄 때, 한글이니까 인코딩
        self.wfile.write(buffer.getvalue())


httpd = HTTPServer(('', PORT), TestHTTPRequestHandler)
print('Server running on port', PORT)
httpd.serve_forever()