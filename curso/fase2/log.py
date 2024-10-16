class Log:
    def _log(self, msg):
        raise NotImplementedError(
            'Implemente o método log'
        )
        
    def log_error(self, msg):
        self.log(f'ERRO: {msg}')
        
        
class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)
       
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')
  
        
if __name__ == '__main__':
    l = LogFileMixin()
    l.log_error('qualquer coisa')