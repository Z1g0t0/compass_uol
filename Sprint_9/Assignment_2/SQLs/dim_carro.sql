create view dim_carro as
    select distinct idCarro, kmCarro, classiCarro as chassiCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel
    from tb_locacao