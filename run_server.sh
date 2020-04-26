#!/bin/bash
mod_wsgi-express start-server --port 3838 --document-root /home/ubuntu/web/ --python-path /home/ubuntu/web/python/ /home/ubuntu/web/python/handler.wsgi
