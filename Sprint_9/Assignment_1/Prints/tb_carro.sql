create table tb_carro(
    idCarro         integer primary key,
    chassiCarro     text,
    marcaCarro      text,
    modeloCarro     text,
    anoCarro        integer,
    idCombustivel   integer
);

insert into tb_carro( 
    idCarro        , 
    chassiCarro    , 
    marcaCarro     , 
    modeloCarro    , 
    anoCarro       , 
    idCombustivel   
)
    select distinct 
        idCarro       , 
        classiCarro   , 
        marcaCarro    , 
        modeloCarro   , 
        anoCarro      , 
        idcombustivel  
    from tb_locacao;