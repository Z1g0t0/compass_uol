create view fato_saida as
    select distinct idCliente, idCarro, dataEntrega, horaEntrega
    from tb_locacao