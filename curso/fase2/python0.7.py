class MeuError(Exception):
    ...
    
class OutroError(Exception):
    ...
def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('olha a nota1')
    exception_.add_note('vc errou isso')
    raise exception_

try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('vamos lançar de outro jeito')
    exception_.__notes__ += error.__notes__.copy()
    exception_.add_note('mais uma nota')
    raise exception_ from error