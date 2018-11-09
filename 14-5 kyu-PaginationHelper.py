#https://www.codewars.com/kata/paginationhelper/train/python

class PaginationHelper:

  def __init__(self, collection, items_per_page):
    self.collection = collection
    self.items_per_page = items_per_page

  def item_count(self):
  	return len(self.collection)

  def page_count(self):
  	return (self.item_count() / self.items_per_page) if (self.item_count() % self.items_per_page == 0) else (self.item_count() / self.items_per_page + 1)
   
  def page_item_count(self,page_index):
  	pageCount = self.page_count() - 1
  	if (page_index > pageCount):
  		return -1
  	elif (page_index == pageCount and self.page_count * self.items_per_page > self.item_count()):
  		return self.item_count() % self.items_per_page
  	else:
  		return self.items_per_page

  def page_index(self,item_index):
     if item_index < 0 or item_index >= self.item_count():
     	return -1
     return item_index % self.items_per_page - 1