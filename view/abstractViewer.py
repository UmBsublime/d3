#!/usr/bin/env python3

from abc import ABCMeta


class AbstractViewer(metaclass=ABCMeta):

    def _set_header(self, title, border='*'):

        border80 = border * 80
        title = '{border}{title:^78}{border}'.format(border=border, title=title)

        self.header = '{border80}\n{title}\n{border80}'.format(border80=border80, title=title)

    def _print_80(self, border='*'):
        print(border*80)