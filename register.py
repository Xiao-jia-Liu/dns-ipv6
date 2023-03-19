#自定义的网页路径或者site key，通过redns.site/${custom_site} 或者 redns.site?site=${custom_site}即可访问
#如自定义site key 为 my_site ，通过 redns.site/my_site 或者 redns.site?site=my_site就可以访问
SITE_KEY = "custom_site"

#指定端口，默认80端口，其他可能不是http服务的，可以自定义端口，,redns.site默认监听8080端口，同时会将80端口重定向到8080端口
#代码中使用接口调建议直接使用8080端口
PORT = 80

import requests


def getIpV6Address():
    return requests.get("http://v6.ident.me/").text

def register_site_and_ip_to_re_dns_site():
    ip = getIpV6Address()
    print(requests.post("http://redns.site:8080", params={'site': SITE_KEY,"ip": ip,"port": PORT}).text)

def main():
    register_site_and_ip_to_re_dns_site()

if __name__ == "__main__":
    main()