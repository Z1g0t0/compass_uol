create view dim_vendedor as
    select distinct idVendedor, nomeVendedor, sexoVendedor, estadoVendedor 
    from tb_locacao