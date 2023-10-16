create view fato_duracao as
    select distinct idCarro, dataLocacao, horaLocacao, qtdDiaria, dataEntrega, horaEntrega 
    from tb_locacao