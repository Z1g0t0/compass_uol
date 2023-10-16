create view fato_entrada as
    select distinct idCliente, idCarro, dataLocacao, horaLocacao
    from tb_locacao