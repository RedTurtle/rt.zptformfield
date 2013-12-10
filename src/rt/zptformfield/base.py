# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView


class BaseMacroView(BrowserView):

    def __getitem__(self, key):
        return self.index.macros[key]
