# -*- coding: utf-8 -*-

import json
from Products.Five.browser import BrowserView

class OutputView(BrowserView):
    
    def __call__(self, *args, **kwargs):
        form = self.request.form
        self.request.response.setHeader('Content-Type', 'text/plain')
        return form.items()

class VocabView(BrowserView):
    
    def __call__(self, *args, **kwargs):
        response = self.request.response
        response.setHeader("Content-type", "application/json")
        response.write(json.dumps([
                                   {'value': 'aaa',
                                    'label': 'Aaa',
                                   },
                                   {'value': 'bbb',
                                    'label': 'Bbb',
                                   },
                                   {'value': 'ccc',
                                    'label': 'Ccc',
                                   },                                   
                                   ]))
