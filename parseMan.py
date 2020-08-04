# coding: utf-8

"""
parseMan 用于解析Burp抓取到的http数据包
"""


class parseMan(object):
    """
    :param file_name    指定数据包文件名
    """
    def __init__(self, file_name):
        self._file_name = file_name
        self._packet_list = self.get_content()
        self._packet_len = len(self._packet_list)
        self._request_method = self.get_request_method()
        self._request_url = None
        self._http_version = None
        self._header = dict()
        self._get_data = dict()
        self._post_data = dict()
        self.parse_http_header()
        self.parse_args()

    def get_content(self):
        with open(self._file_name, 'r', encoding='utf-8') as f:
            content = [line.strip() for line in f.readlines()]
        return content

    def get_request_method(self):
        return self._packet_list[0].split(' ')[0]

    def parse_http_header(self):
        first_line_list = self._packet_list[0].split(' ')
        self._request_url = first_line_list[1]
        self._http_version = first_line_list[2]
        for i in list(range(1, len(self._packet_list)-1)):
            if self._packet_list[i] != '':
                item = self._packet_list[i].split(':')
                self._header[item[0]] = item[1].strip()

    def parse_args(self):
        # 解析get参数
        if '?' in self._request_url:
            index = self._request_url.find('?') + 1
            args_line = self._request_url[index::]
            try:
                if args_line.find('&') == -1:
                    item = args_line.split('=')
                    self._get_data[item[0]] = item[1]
                else:
                    item_list = args_line.split('&')
                    for item in item_list:
                        args = item.split('=')
                        self._get_data[args[0]] = args[1]
            except Exception as e:
                print(e)

        # 解析post参数
        if (self._packet_list[self._packet_len-2] == '') and (self._packet_list[self._packet_len-1] != ''):
            args_line = self._packet_list[self._packet_len-1]
            if args_line.find('&') == -1:
                item = args_line.split('=')
                self._post_data[item[0]] = item[1]
            else:
                item_list = args_line.split('&')
                for item in item_list:
                    args = item.split('=')
                    self._post_data[args[0]] = args[1]


# pb = parseMan('sql.txt')
# print(pb._post_data)
