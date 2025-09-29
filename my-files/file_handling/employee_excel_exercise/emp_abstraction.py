from abc import ABC, abstractmethod

class FileOperation:
    @abstractmethod
    def generate(self):
        pass
    
    @abstractmethod
    def write_headers(self):
        pass
    
    @abstractmethod
    def insert_records(self):
        pass

    @abstractmethod
    def read_records(self):
        pass