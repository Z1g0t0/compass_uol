create table tb_combustivel(
    idCombustivel   integer primary key,
    tipoCombustivel text
);

insert into tb_combustivel( 
    idCombustivel   ,
    tipoCombustivel 
)
    select distinct 
        idcombustivel   ,
        tipoCombustivel 
    from tb_locacao;