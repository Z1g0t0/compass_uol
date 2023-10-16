create view fato_conta as
    select distinct idCliente, idVendedor, vlrDiaria, qtdDiaria, vlrDiaria * qtdDiaria as total 
    from tb_locacao