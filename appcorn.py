import app as bbs

app = bbs.configured_app()


# gunicorn -b '0.0.0.0:80' redischat:app
# guincorn appcorn:app

# 在服务器上运行的命令的最终版本
# nohup gunicorn -b '0.0.0.0:80' appcorn:app &