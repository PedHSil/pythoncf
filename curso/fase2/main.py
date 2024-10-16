from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log('qualquer coisa')
lp.log.success('Que legal')
lf = LogFileMixin()
lf.log('qualquer coisa')
lf.log.success('Que legal')