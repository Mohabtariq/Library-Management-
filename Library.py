#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Library:
    def __init__(self,booksList=[],libraryname='',lendedbooks={}):
        self.booksList=booksList
        self.libraryname=libraryname
        self.lendedbooks=lendedbooks

    def displaybooks(self):
        print(f'The available books:')
        for book in self.booksList:
            if not any(book in books for books in self.lendedbooks.values()):
                print(book)

