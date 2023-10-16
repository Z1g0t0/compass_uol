create view dim_cliente as
    select distinct idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente 
    from tb_locacao