# import Locacoes.crud_locacoes as lc

# lc.cadastrar()
# lc.atualizar_locacoes()
# lc.apagar_locacoes()
# lc.listar_locacoes()


# import Manutencoes.crud_manuntecoes as mt

# mt.cadastrar()
# mt.atualizar_manutencoes()
# mt.apagar_manutencoes()
# mt.listar_manutencoes()


#import Veiculos.crud_veiculos as vc

# vc.cadastrar()
# vc.atualizar_veiculos()
# vc.apagar_veiculos()
# vc.listar_veiculos()


# import Funcionarios.crud_funcionarios as fu

# fu.cadastrar()
# fu.atualizar_funcionarios()
# fu.apagar_funcionarios()
# fu.listar_funcionarios()


import Locadora.Clientes.crud_clientes as cli

cli.cadastrar("Maria Aparecida Da Conceição","123.456.789-00","Rua Qualquer,10","11-98765-4321","1956-06-15","01234567890")
#cli.atualizar_clientes(1,"Maria Ap. Conceicao","123.456.789-01","Rua Qualquer,09","11-98765-4320","1956-03-15","01234567891")
#cli.apagar_clientes(1)
cli.listar_clientes()